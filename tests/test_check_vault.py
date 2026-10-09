import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_vault.py"


class VaultCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.put("index.md", "- [Map](Atlas/Maps/Map.md)\n- [Project](Projects/on/Project%20-%20One.md)\n- [Clip](+/Clip.md)\n")
        self.put("Atlas/Maps/Map.md", "# Map\n[Project](../../Projects/on/Project%20-%20One.md)\n")
        self.put("Projects/on/Project - One.md", "---\nstatus: active\n---\n# Project - One\n")
        self.put("+/Clip.md", "---\ntags:\n  - type/clip\nurls:\n  - https://example.org/article\n---\n# Clip\nClip — unreviewed.\n")
        self.put('Projects/_projects.base', 'filters:\n  and:\n    - file.inFolder("Projects")\n')

    def put(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def check(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root)],
            capture_output=True, text=True, check=False,
        )

    def test_valid_vault_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_broken_link_and_missing_index_entry_fail(self):
        self.put("Atlas/Maps/Extra.md", "[Missing](../../gone.md)\n")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gone.md", result.stdout)
        self.assertIn("Atlas/Maps/Extra.md: missing from index.md", result.stdout)

    def test_invalid_project_folder_and_status_fail(self):
        self.put("Projects/other/Project - Two.md", "---\nstatus: unknown\n---\n# Project - Two\n")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsupported intensity", result.stdout)
        self.assertIn("invalid status", result.stdout)

    def test_stale_base_filter_and_unreviewed_clip_fail(self):
        self.put("Projects/_projects.base", 'filters:\n  and:\n    - file.folder == "OldProjects"\n')
        self.put("+/Clip.md", "---\ntags: []\nurls: []\n---\n# Clip\n")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("OldProjects", result.stdout)
        self.assertIn("type/clip", result.stdout)
        self.assertIn("unreviewed", result.stdout)


if __name__ == "__main__":
    unittest.main()
