#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests

def words_count(subreddit, word_list, after=None, counts=None):
    """Define the Reddit API word count"""
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)

    if response.status_code != 200:
        return('None')
    
     data = response.json()

    posts = [child.get("data").get("title")
             for child in data
             .get("data")
             .get("children")]
    if not posts:
        return None

    word_list = list(dict.fromkeys(word_list))

    if count_word == {}:
        count_word = {word: 0 for word in word_list}

    for title in posts:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    count_word[word] += 1

    if not data.get("data").get("after"):
        counts_sorted = sorted(count_word.items(), key=lambda kv: kv[0])
        counts_sorted = sorted(count_word.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in counts_sorted if v != 0]
    else:
        return words_count(subreddit, word_list, count_word,
                           data.get("data").get("after"))