from plotly.graph_objs import Bar
from plotly import offline
from operator import itemgetter

import requests

# Make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    if (
        'title' in response_dict
        and "descendants" in response_dict
    ):

        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    else:
        print(f"We do not have a title or descendants/comments for the news source with the id {submission_id}.")

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, discussion_links, comments = [], [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    discussion_link = f"<a href='{submission_dict['hn_link']}'>{title}</a>"
    comment = submission_dict['comments']
    titles.append(title)
    discussion_links.append(discussion_link)
    comments.append(comment)

data = [{
    'type': 'bar',
    'x': discussion_links,
    'y': comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most Discussed on Hacker news sources',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'News Source',
        'titlefont': {"size": 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="htmls/hacker_news_sources.html")
