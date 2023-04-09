# https://leetcode.com/problems/design-twitter/description/

from typing import DefaultDict, Dict, List
from collections import defaultdict


class Twitter:
    tweet_order = 1

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.tweet_order])
        self.tweet_order += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees_feeds = list()
        for followee_id in self.followers[userId]:
            followees_feeds.extend(self.tweets[followee_id])
        news_feed = sorted(
            self.tweets[userId] + followees_feeds, key=lambda tweet: -tweet[-1])

        return list(map(lambda x: x[0], news_feed))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 3)
twitter.postTweet(1, 101)
twitter.postTweet(1, 13)
twitter.postTweet(1, 10)
twitter.postTweet(1, 2)
twitter.postTweet(1, 94)
twitter.postTweet(1, 505)
twitter.postTweet(1, 333)
twitter.postTweet(1, 22)
twitter.postTweet(1, 11)
print(twitter.getNewsFeed(1))

# ???????
