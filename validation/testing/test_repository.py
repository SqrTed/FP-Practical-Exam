from unittest import TestCase

from entities.exception import ScrambleException
from repository.repository import Repository


class TestRepository(TestCase):
    def setUp(self):
        self.repo = Repository("test.txt")

    def test_get_scramble(self):
        self.assertEqual(self.repo.get_scramble().id, "Arthur")

    def test_IOError(self):
        with self.assertRaises(ScrambleException):
            repo = Repository("no.txt")
