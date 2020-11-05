import requests

language = input("What language would you like to view? ")

def api_call(lg):
    # Make an API call and store the response
    url = f'https://api.github.com/search/repositories?q=language:{lg}&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    # Store api response in a variable
    response_dict = r.json()

    if 'message' in response_dict:
        print(f"Invalid language, {lg}")
        return None

    print(f"Total repositories: {response_dict['total_count']}")

    # Explore information about the repos
    repo_dicts = response_dict['items']
    print(f"Repos returned: {len(repo_dicts)}")

    # Examine the first repo
    for repo_dict in repo_dicts:
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")


api_call(language)
