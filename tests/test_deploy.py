"""Verify that local deployment copies an intact, runnable application."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from deploy import deploy


class TestDeploy(unittest.TestCase):
    def test_release_is_intact_and_runnable(self):
        with TemporaryDirectory() as directory:
            destination = deploy(Path(directory) / "release")
            source = Path(__file__).resolve().parents[1] / "app.py"
            self.assertEqual(destination.read_bytes(), source.read_bytes())
            manifest = json.loads(
                (destination.parent / "manifest.json").read_text()
            )
            self.assertEqual(manifest["sha256"], hashlib.sha256(
                destination.read_bytes()).hexdigest())
            result = subprocess.run(
                [sys.executable, str(destination)], check=True,
                capture_output=True, text=True,
            )
            self.assertEqual(result.stdout.strip(),
                             "Hello, World from Nathalio Hassoun!")
