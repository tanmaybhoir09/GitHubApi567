import unittest
import json
from gitHubApi import repoNames, commitNum
from unittest.mock import Mock, patch

class TestGithub(unittest.TestCase):
    @patch('TestGitHubApi.repoNames')
    def testRepo1(self,mock_repo_names):
        mock_repo_names.return_value = Mock(['SSW'])
        
        allRepos = repoNames('tanmaybhoir09')
        
        self.assertGreaterEqual(len(allRepos), 1)
        self.assertIn('SSW',allRepos)

    @patch('TestGitHubApi.repoNames')
    def testRepo2(self, mock_repo_names):
        fake_json = ['Triangle567',
                     'GitHubApi567',
                     'UniversityDatabase',
                     'SSW567-HW02']
        mock_repo_names.return_value = Mock(fake_json)
        
        allRepos = repoNames('tanmaybhoir09')
        #self.assertTrue(mock_repo_names.called)
        self.assertGreaterEqual(len(allRepos), 2)
        self.assertIn('Triangle567',allRepos)
        self.assertIn('GitHubApi567',allRepos)

    @patch('TestGitHubApi.repoNames')
    def testRepo3(self, mock_repo_names):
        fake_json = ['ssw555CKMM2018Spring',
                     'CS-546-Web-Programming',
                     'karuaan.github.io',
                     'Android-Projects',
                     'Systems-Programming-',
                     'MusicMeld',
                     'Ratemycourse.com']
        mock_repo_names.return_value = Mock(fake_json)
        
        allRepos = repoNames('karuaan')

        #self.assertTrue(mock_repo_names.called)
        self.assertGreaterEqual(len(allRepos), 7)
        self.assertIn('ssw555CKMM2018Spring',allRepos)
        self.assertIn('CS-546-Web-Programming',allRepos)
        self.assertIn('karuaan.github.io',allRepos)
        self.assertIn('Android-Projects',allRepos)
        self.assertIn('Systems-Programming-',allRepos)
        self.assertIn('MusicMeld',allRepos)
        self.assertIn('Ratemycourse.com',allRepos)

    @patch('TestGitHubApi.commitNum')
    def testNumCommits1(self, mock_commit_num):
        mock_commit_num.return_value = Mock(30)
        self.assertGreaterEqual(commitNum('tanmaybhoir09','Triangle567'), 11)
        #self.assertTrue(mock_commit_num.called)

    @patch('TestGitHubApi.repoNames')
    def testNumCommits2(self, mock_commit_num):
        mock_commit_num.return_value = Mock(50)
        self.assertGreaterEqual(commitNum('tanmaybhoir09','GitHubApi567'),9)
        #self.assertTrue(mock_commit_num.called)

    @patch('TestGitHubApi.commitNum')
    def testNumCommits3(self, mock_commit_num):
        mock_commit_num.return_value = Mock(30)
        self.assertGreaterEqual(commitNum('karuaan','ssw555CKMM2018Spring'),23)
        self.assertGreaterEqual(commitNum('karuaan','CS-546-Web-Programming'),1)
        self.assertGreaterEqual(commitNum('karuaan','karuaan.github.io'),2)
        self.assertGreaterEqual(commitNum('karuaan','Android-Projects'),2)
        self.assertGreaterEqual(commitNum('karuaan','Systems-Programming-'),18)
        self.assertGreaterEqual(commitNum('karuaan','MusicMeld'),6)
        self.assertGreaterEqual(commitNum('karuaan','Ratemycourse.com'),6)
        #self.assertTrue(mock_commit_num.called)

    @patch('TestGitHubApi.repoNames')
    def testInvalidInfo(self, mock_repo_name):
        mock_repo_name.return_value = Mock(0)
        allRepos = repoNames('tanmaybhoir09')
        self.assertEqual(len(allRepos), 0)
        #self.assertTrue(mock_repo_name.called)

if __name__ == '__main__':
    print("Running unit test")
    unittest.main()        