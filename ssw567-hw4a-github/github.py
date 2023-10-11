import requests, json, unittest


class Github():

    def __init__(self, username:str) -> None:
        if not type(username) == str:
            username = str(username)
        self.username = username

    def get_user(self):
        print(len(self.username))
        if len(self.username) == 0 or self.username == '':
            return -2
        
        url = 'https://api.github.com/users/%s/repos' % self.username
        print(url)
        data = requests.get(url)
        # print(data.status_code)
        if data.status_code == 200:
            self.repos = json.loads(data.text)
            if 'message' in self.repos and self.repos['message'] == 'Not Found':
                print('User Not Found')
                return -1
            else:
                # print(self.repos)
                # return len(self.repos)
                for r in self.repos:
                    repo = requests.get(r['url'])
                    if repo.status_code == 200:
                        repo_data = json.loads(repo.text)
                        commit_count = self.get_commits_of_repo(repo_data['name'])
                        print('Repo: %s Number of commits: %s' % (repo_data['name'], commit_count))
        elif data.status_code == 404:
            print('User Not Found')
            return -1
    
    def get_all_repos(self):
        print(len(self.username))
        if len(self.username) == 0 or self.username == '':
            return -2
        
        url = 'https://api.github.com/users/%s/repos' % self.username
        # print(url)
        data = requests.get(url)
        # print(data.status_code)
        if data.status_code == 200:
            self.repos = json.loads(data.text)
            if 'message' in self.repos and self.repos['message'] == 'Not Found':
                print('User Not Found')
                return -1
            else:
                # print(self.repos)
                return len(self.repos)
        elif data.status_code == 404:
            print('User Not Found')
            return -1

    def get_commits_of_repo(self, repo):
        if repo == '' or len(repo) == 0:
            raise Exception("repo cant be empty")
        
        url = 'https://api.github.com/repos/%s/%s/commits' % (self.username, repo)
        print(url)
        data = requests.get(url)
        print(data.status_code)
        if data.status_code == 200:
            # self.repos = json.loads(data.text)
            commits = json.loads(data.text)
            print('Len: %d' % len(commits))
            if commits == None:
                return -1
            return len(commits)
        elif data.status_code == 404:
            print('Repo: %s Not Found' % repo)
            return -1

    def __repr__(self) -> str:
        return self.username
    

class GithubTest(unittest.TestCase):

    def setUp(self) -> None:
        self.TESTCASES = [
            {'username':'ishangarg', 'repo':'bor', 'asset_repo':14, 'assert_commits':30, 'type':'normal'}, #everything in order
            {'username':'hufsdhsadfkjhfsfsasaf', 'repo':'bor', 'asset_repo':-1, 'assert_commits':-1, 'type':'normal'}, #user does not exist  = -1
            {'username':123, 'repo':'bor', 'asset_repo':1, 'assert_commits':-1, 'type':'normal'}, #taking number input, code will work byt might throw an error due to assetion fail 
            {'username':'ishangarg', 'repo':'boris', 'asset_repo':14, 'assert_commits':-1, 'type':'normal'}, #repo does not exist = -1 
            {'username':'', 'repo':'boris', 'asset_repo':-2, 'assert_commits':-1, 'type':'error'}, #throws error 
            {'username':'ishangarg', 'repo':'', 'asset_repo':100, 'assert_commits':-1, 'type':'error'}, #throws error 
            
        ]

    def test_get_all_repos(self):
        #onverting testing to monolithic as parallely becomcing confusing
        print('Starting Tesf For Get All Repos')
        for t in self.TESTCASES:
            g = Github(t['username'])
            if t['type'] == 'normal':
                print('Testing: ' + str(t))
                self.assertEqual(g.get_all_repos(), t['asset_repo'])
                self.assertEqual(g.get_commits_of_repo(t['repo']), t['assert_commits'])


    # def test_commit_of_repo(self):
    #     print('Starting Tesf For Get All Commits of Repos')
    #     for t in self.TESTCASES:
    #         g = Github(t['username'])
    #         if t['type'] == 'normal':
    #             print('Testing: ' + str(t))
    #             self.assertEqual(g.get_commits_of_repo(t['repo']), t['assert_commits'])
    #         else:
    #             with self.assertRaises(Exception) as context:
    #                 g.get_all_repos()
    #             self.assertTrue('username cant be empty', str(context.exception))


if __name__ == '__main__':
    unittest.main()
    # g = Github('ishangarg')
    # g.get_user()
