#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests
import sys
import re


def count_words(subreddit, word_list, after=None, word_counts=None):
    """ Defines words count"""
    if word_counts is None:
        word_counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': '100-count'
    }
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            post_data = response.json()['data']['children']
            for post in post_data:
                title = post['data']['title']

                normalized_title = re.sub(r'[^a-zA-Z0-9 ]', '',
                                          title.lower())
                words = normalized_title.split()

                for word in words:
                    if word in word_list:
                        if word in word_counts:
                            word_counts[word] += 1
                        else:
                            word_counts[word] = 1

            after = response.json()['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, word_counts, after)
            else:
                sorted_word_counts = sorted(word_counts.items(),
                                            key=lambda item:
                                            (-item[1], item[0]))
                for keyword, count in sorted_word_counts:
                    print(f"{keyword}: {count}")
        except (KeyError, ValueError):
            return None
    elif response.status_code == 302:
        return None
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) > 2:
        subreddit = sys.argv[2]
        word_list = sys.argv[3]
        count_words(subreddit, word_list)
