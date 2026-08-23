class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx - 1])
        while minHeap and len(out) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            out.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx - 1])
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
