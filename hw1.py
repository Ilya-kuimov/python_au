import requests
import json


PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'REQUESTS']
GROUP = '1013'
ACTION = ['Added', 'Deleted', 'Updated']
TOKEN = ''


headers = {'Authorization': 'token ' + TOKEN}

def get_all_user_pr(userName = 'Ilya-kuimov', repos = 'python_au', state = 'open'):
    all_prs = requests.get("https://api.github.com/repos/{}/{}/pulls?state={}".format(userName, repos, state), headers = headers).json()
    return all_prs

def get_all_pr_commits(pr):
    list_of_commits = requests.get(pr['commits_url'], headers = headers).json()
    return list_of_commits

def get_title(dictionary):
    return dictionary['commit']['message']

def check_prefixes(title):
    title = title.replace('-', ' ')
    parsed_title = title.split(' ')
    errors = list()
    if len(parsed_title) < 4:
        return ('неверный формат')
    if parsed_title[0] not in PREFIX:
        errors.append('Эта домашка не из {}.'.format(parsed_title[0], PREFIX))
    if parsed_title[1] not in GROUP:
        errors.append('Снова не из {}.'.format(parsed_title[1], GROUP))
    if parsed_title[2] not in ACTION:
        errors.append('Она не из {}.'.format(parsed_title[2], ACTION))
    if len(errors) == 0:
      return 'Всё в порядке'
    else:
      title_errors = '\n'.join(errors)
    return title_errors

def create_pr_comment(title, title_errors):
    return('Hello! \n I am here to help you with making your pr title looks better. Now it is: \n {} \n Mistakes: \n {} '.format(title, title_errors))

def send_pr_comment(pr, comment):
    data = {'body': comment,
            'path': requests.get(pr['url']+'/files', headers=headers).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}
    r = requests.post(pr['url']+'/comments', headers=headers, json=data)
    print(r.json())

def bully_your_pull_request(pr):
    commits = get_all_pr_commits(pr)
    for commit in commits:
        title = get_title(commit)
        title_errors = check_prefixes(title)
        comment = create_pr_comment(title, title_errors)
        send_pr_comment(pr, comment)

def main():
    for pr in get_all_user_pr(userName = 'Ilya-kuimov'):
      bully_your_pull_request(pr)

if __name__ == '__main__':
    main()