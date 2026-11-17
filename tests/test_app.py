"""Exercise both the function and the application's entry point."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
import unittest

from app import greet


class TestApp(unittest.TestCase):
    def test_world(self):
        self.assertEqual(
            greet("World"), "Hello, World from Nathalio Hassoun!"
        )

    def test_another_name(self):
        self.assertEqual(greet("Jenkins"),
                         "Hello, Jenkins from Nathalio Hassoun!")

    def test_entry_point(self):
        output = StringIO()
        with redirect_stdout(output):
            runpy.run_path(
                str(Path(__file__).resolve().parents[1] / "app.py"),
                run_name="__main__",
            )
        self.assertEqual(output.getvalue().strip(), greet("World"))
