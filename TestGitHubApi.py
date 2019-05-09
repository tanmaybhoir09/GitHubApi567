"""
@author: Tanmay Bhoir
@date: February 25, 2019

"""

import unittest
from GitHubApi import getRepoCommits, res

class TestGitHub(unittest.TestCase):
    def testgetRepoCommits_Blank(self):
        self.assertIsNone(getRepoCommits(''))

    def testgetRepoCommits_InvalidValue(self):
        self.assertIsNotNone(getRepoCommits('ABC'))

    def testgetRepoCommits_ValidValue(self):
        self.assertEqual(getRepoCommits('tanmaybhoir09'), ['Repo: Triangle567, Number of commits: 11',
                                                    'Repo: SSW567-HW02, Number of commits: 5',
                                                    'Repo: GitHubApi567, Number of commits: 4',
                                                    'Repo: UniversityDatabase, Number of commits: 2'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()