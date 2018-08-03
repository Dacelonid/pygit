import pgit
import unittest
import shutil, tempfile, os

class PGitTest(unittest.TestCase):
    def test_init(self):
        pgit.init(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git")), ".git")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "HEAD")), ".git/HEAD")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "branches")), ".git/branches")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "config")), ".git/config")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "description")), ".git/description")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "hooks")), ".git/hooks")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "info")), ".git/info")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "objects")), "/git/objects")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "refs")), ".git/refs")

        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "info", "exclude")), ".git/info/exclude")

        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "objects", "info")), ".git/objects/info")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "objects", "pack")), ".git/objects/pack")

        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "refs", "heads")), ".git/refs/heads")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, ".git", "refs", "tags")), ".git/refs/tags")
        
        head_file = open(os.path.join(self.test_dir, ".git", "HEAD"))
        head_file_contents = head_file.read()
        head_file.close()
        self.assertEqual("ref: refs/heads/master", head_file_contents, "Ensuring HEAD points to master")
        
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)


if __name__ == '__main__':
    unittest.main()
