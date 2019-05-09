"""
@author: Tanmay Bhoir
@date: February 25, 2019

"""

import requests, json

def getRepoCommits(userId):
    try:
        gitURL = f'https://api.github.com/users/{userId}/repos'
    except requests.exceptions.InvalidURL:
        print('invalid URL!')
    except requests.exceptions.ConnectionError:
        print('Invalid Request!')
    except requests.exceptions.InvalidSchema:
        print('Invalid Request!')
    else:
        response = requests.get(gitURL)
        responseCode = response.status_code
        if  responseCode == 200:
            repositories = json.loads(response.content)
            repoData = list()

            for repo in repositories: 
                repoName = repo['name']
                repoURL = f'https://api.github.com/repos/{userId}/{repoName}/commits'
                commits = requests.get(repoURL)
                commits = json.loads(commits.content) 
                numCommits = len(commits)
                repoData.append(f'Repo: {repoName}, Number of commits: {numCommits}')

            return repoData


userId = 'tanmaybhoir09'
res = getRepoCommits(userId)

if res != None:
    for i in res:
        print(i)
else:
    print('Invalid Request!')