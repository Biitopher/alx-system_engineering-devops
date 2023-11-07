#!/usr/bin/python3
"""Exports cvs files"""

import requests
import sys


def number_of_subscribers(subreddit):
    """defines reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        'User-Agent': '0-subs'
    }
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()

            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0


if __name__ == "__main__":
    if len(sys.argv) > 2:
        subreddit = sys.argv[2]
        number_of_subscribers(subreddit)
