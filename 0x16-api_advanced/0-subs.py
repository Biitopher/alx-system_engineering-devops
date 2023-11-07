#!/usr/bin/python3
"""Exports cvs files"""

import requests
import sys
import json


def number_of_subscribers(subreddit):
    """defines reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        'User-Agent': '0-subs'
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 302:
            return 0
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
