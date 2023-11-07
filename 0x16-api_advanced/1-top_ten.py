#!/usr/bin/python3
"""Queries Reddit and prints titles"""
import requests


def top_ten(subreddit):
    """Define the Reddit API"""
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)

    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]