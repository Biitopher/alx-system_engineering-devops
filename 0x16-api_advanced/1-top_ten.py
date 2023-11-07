#!/usr/bin/python3
"""Queries Reddit and prints titles"""
import requests
import sys
import json


def top_ten(subreddit):
    """Define the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        'User-Agent': 'MyRedditBot/1.0'
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            for get_data in response.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)