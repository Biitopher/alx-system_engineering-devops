#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import sys
import requests


def recurse(subreddit, hot_list=[], after=""):
    """defines Reddit API"""
   if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': '2-recurse'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()['data']['children'][:10]
            for post in data:
                title = post['data']['title']
                hot_list.append(title)
            after = response.json()['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except (KeyError, ValueError):
            return None
    elif response.status_code == 302:
        return None
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) > 2:
        subreddit = sys.argv[2]
        recurse(subreddit)