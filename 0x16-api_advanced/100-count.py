#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests


def words_count(subreddit, word_list, after=None, count_word=None):
    """Defines words count"""
    if count_word is None:
        count_word = {word: 0 for word in word_list}

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10&after={after}",
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )

    if response.status_code != 200:
        return 'None'

    data = response.json()
    posts = [child.get("data").get("title") for child in data.get("data").get("children")]

    for title in posts:
        split_words = title.lower().split()  # Convert to lowercase for case-insensitive matching
        for word in word_list:
            if word.lower() in split_words:
                count_word[word] += split_words.count(word.lower())

    if data.get("data").get("after"):
        return words_count(subreddit, word_list, data.get("data").get("after"), count_word)
    
    counts_sorted = sorted(count_word.items(), key=lambda kv: (-kv[1], kv[0]))
    for word, count in counts_sorted:
        if count > 0:
            print(f"{word}: {count}")