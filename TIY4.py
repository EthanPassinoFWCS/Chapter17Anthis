import requests

from plotly.graph_objs import Bar
import plotly.graph_objects as go
from plotly import offline

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels, issues = [], [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"Owner: {owner}<br />Description: {description}"
    labels.append(label)
    issues.append(repo_dict["open_issues_count"])

# Make visualization.

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars/Issues',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}


fig = go.Figure(data=[
    go.Bar(name='Stars', x=repo_links, y=stars),
    go.Bar(name='Issues', x=repo_links, y=issues)
])

# Change barmode
fig.update_layout(barmode='group')

offline.plot(fig, filename='htmls/python_repos2.html')
