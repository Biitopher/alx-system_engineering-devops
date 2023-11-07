#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests


def words_count(subreddit, word_list, after=None, word_count={}):
    """Defines words count"""
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10&after={after}",
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)

    if response.status_code != 200:
        return 'None'

    data = response.json()
    posts = [child.get("data").get("title")
     for child in data.get("data").get("children")]
    if not posts:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in posts:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not data.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           data.get("data").get("after"))