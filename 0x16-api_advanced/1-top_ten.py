#!/usr/bin/python3
"""Queries Reddit and prints titles"""
import requests


def top_ten(subreddit):
    """Define the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        'User-Agent': 'MyRedditBot/1.0'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            for get_data in data.get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
            
        else:
                print(None)
