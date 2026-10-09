"""Check cross-page vault invariants; Obsidian Linter handles Markdown formatting."""

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[[^]\n]+\]\(([^)]+)\)")
BASE_PATH = re.compile(r'file\.(folder|path)\s*(?:==|!=)\s*["\']([^"\']+)["\']|file\.inFolder\(["\']([^"\']+)["\']\)')
INTENSITIES = {"on", "ongoing", "simmering", "sleeping"}
STATUSES = {"proposed", "planning", "ready", "active", "complete", "paused"}


def markdown_links(text):
    """Yield link destinations outside fenced code blocks."""
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker and fence is None:
            fence = marker.group(1)[0]
        elif marker and marker.group(1)[0] == fence:
            fence = None
        elif fence is None:
            for match in LINK.finditer(line):
                yield match.group(1)


def local_target(root, source, link):
    link = link.strip().strip("<>")
    parsed = urlsplit(link)
    if parsed.scheme or parsed.netloc or link.startswith(("#", "//")):
        return None
    return (source.parent / unquote(parsed.path)).resolve()


def frontmatter(text):
    if not text.startswith("---\n"):
        return ""
    parts = text.split("\n---\n", 1)
    return parts[0][4:] if len(parts) == 2 else ""


def check(root):
    root = root.resolve()
    errors = []
    index = root / "index.md"
    if not index.is_file():
        return ["index.md: missing"]
    indexed = {local_target(root, index, link) for link in markdown_links(index.read_text(encoding="utf-8"))}
    for page in sorted(root.rglob("*.md")):
        if any(part in {".git", ".obsidian", ".agents", "_assets", "tests"} for part in page.relative_to(root).parts):
            continue
        if page.is_symlink():
            continue
        name = page.relative_to(root).as_posix()
        text = page.read_text(encoding="utf-8")
        for link in markdown_links(text):
            target = local_target(root, page, link)
            if target is not None and not target.is_relative_to(root):
                errors.append(f"{name}: link outside vault: {link}")
            elif target is not None and not target.exists():
                errors.append(f"{name}: broken link: {link}")
        parts = page.relative_to(root).parts
        if parts[0] in {"Atlas", "Projects", "+"} and name != "+/_inbox.md" and page.resolve() not in indexed:
            errors.append(f"{name}: missing from index.md")
        if parts[0] == "Projects" and page.name.startswith("Project - "):
            if len(parts) != 3 or parts[1] not in INTENSITIES:
                errors.append(f"{name}: unsupported intensity folder")
            status = re.search(r"(?m)^status:\s*(\S+)\s*$", frontmatter(text))
            if not status or status.group(1) not in STATUSES:
                errors.append(f"{name}: invalid status")
        if parts[0] == "+" and page.name != "_inbox.md":
            meta = frontmatter(text)
            if not re.search(r"(?m)^\s*-\s*type/clip\s*$", meta):
                errors.append(f"{name}: missing type/clip tag")
            if not re.search(r"(?i)\bunreviewed\b", text[len(meta):]):
                errors.append(f"{name}: missing unreviewed notice")
            if not re.search(r"(?m)^\s*-\s*[\"']?https?://\S+", meta):
                errors.append(f"{name}: missing source URL in frontmatter")
    for base in sorted(root.rglob("*.base")):
        name = base.relative_to(root).as_posix()
        for match in BASE_PATH.finditer(base.read_text(encoding="utf-8")):
            kind, path = ("folder", match.group(3)) if match.group(3) else (match.group(1), match.group(2))
            target = root / path
            if not (target.is_file() if kind == "path" else target.is_dir()):
                errors.append(f"{name}: stale {kind} filter: {path}")
    return sorted(errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if not args.vault.is_dir():
        parser.error(f"not a directory: {args.vault}")
    errors = check(args.vault)
    print("\n".join(errors) if errors else "Vault checks passed")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
