import os

from unittest import TestCase

from listcourses import parse_html


class TestProcessHTML(TestCase):
    def test(self):
        example_file_name = os.path.join(os.path.dirname(__file__), "example.html")
        with open(example_file_name) as f:
            html = f.read()

        courses = parse_html(html)
        self.assertIn("Zaawansowane programowanie funkcyjne", courses)
