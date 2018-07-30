import pgit
import unittest
import shutil, tempfile, os

class PGitTest(unittest.TestCase):
    def test_init(self):
        pgit.init(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "HEAD")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "refs")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "objects")))

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)


if __name__ == '__main__':
    unittest.main()
