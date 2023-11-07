#!/usr/bin/python3
"""Queries Reddit and prints titles"""
import requests


def top_ten(subreddit):
    """Define the Reddit API"""
    response = requests.get(
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers = {"User-Agent": "Custom"},
        parameter={"limit": 10},
    )

    if response.status_code == 200:
        for list_data in response.json().get("data").get("children"):
            dat = list_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print()
        return None