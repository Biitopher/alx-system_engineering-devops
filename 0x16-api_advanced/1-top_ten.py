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
            data = response.json()

            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for i, post in enumerate(posts, 1):
                    print(f"{i}. {post['data']['title']}")
            else:
                print("No posts found in this subreddit.")
        elif response.status_code == 302:
            return None

        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
