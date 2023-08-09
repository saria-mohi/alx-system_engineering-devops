#!/usr/bin/python3
"""Function to query a list of all hot posts"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Returns a list of titles of all hot posts"""

    baseurl = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 10}
    response = requests.get(baseurl, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return None

    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for i in res.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
