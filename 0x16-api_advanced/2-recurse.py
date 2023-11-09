#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """defines Reddit API"""
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = response.json().get("data").get("after")

        if after is None:
            return (OK)
        else:
            return (recurse(subreddit, hot_list, after))
        else:
            return (OK)
    else:
        return (None)