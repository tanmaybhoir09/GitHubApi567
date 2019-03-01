'''

Created on Feb 19, 2019

@author: Tanmay Bhoir

'''
import unittest
from gitHubApi import repoNames, commitNum

class TestGithub(unittest.TestCase):
    
    def testRepo1(self):
        allRepos = repoNames('richkempinski')
        self.assertGreaterEqual(len(allRepos), 1)
        self.assertIn('hellogitworld',allRepos)

    def testRepo2(self):
        allRepos = repoNames('richkempinski')
        self.assertGreaterEqual(len(allRepos), 2)
        self.assertIn('Mocks',allRepos)
        self.assertIn('Project1',allRepos)
    
    def testRepo3(self):
        allRepos = repoNames('richkempinski')
        self.assertGreaterEqual(len(allRepos), 5)
        self.assertIn('hellogitworld',allRepos)
        self.assertIn('helloworld',allRepos)
        self.assertIn('Mocks',allRepos)
        self.assertIn('Project1',allRepos)
        self.assertIn('threads-of-life',allRepos)
            
    def testNumCommits1(self):
        self.assertGreaterEqual(commitNum('richkempinski','hellogitworld'),30)
        
    def testNumCommits2(self):
        self.assertGreaterEqual(commitNum('richkempinski','Mocks'),9)
        
    def testNumCommits3(self):
        self.assertGreaterEqual(commitNum('richkempinski','hellogitworld'),30)
        self.assertGreaterEqual(commitNum('richkempinski','helloworld'),6)
        self.assertGreaterEqual(commitNum('richkempinski','Mocks'),9)
        self.assertGreaterEqual(commitNum('richkempinski','Project1'),2)
        self.assertGreaterEqual(commitNum('richkempinski','threads-of-life'),1)

    def testInvalidInfo(self):
        allRepos = repoNames('richkempenski')
        self.assertEqual(len(allRepos), 0)

    if __name__=="__main__":
        unittest.main(exit=False, verbosity=2) 