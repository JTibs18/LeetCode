# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
# Implement the Twitter class:
#   Twitter() Initializes your twitter object.
#   void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
#   List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
#   void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
#   void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 
class Twitter:
    def __init__(self):
        self.followers = dict()
        self.tweets = dict()
        self.recency = 0

    def postTweet(self, userId: int, tweetId: int):
        if userId not in self.tweets:
            self.tweets[userId] = [(tweetId, self.recency)]
        else:
            self.tweets[userId].append((tweetId, self.recency))

        self.recency += 1 
        
    def getNewsFeed(self, userId: int):
        if userId in self.tweets:
            recentTweets = self.tweets[userId][:]
        else:
            recentTweets = []

        if userId in self.followers:
            for i in self.followers[userId]:
                if i in self.tweets:
                    recentTweets.extend(self.tweets[i])

        recentTweets.sort(key=lambda x:x[1], reverse=True)

        return [i[0] for i in recentTweets][:10]
        
    def follow(self, followerId: int, followeeId: int):
        if followerId not in self.followers:
            self.followers[followerId] = set([followeeId])
        else:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)

# Test case
twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))