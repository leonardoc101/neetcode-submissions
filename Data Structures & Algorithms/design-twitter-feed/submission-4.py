class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush_max(maxHeap, [time, tweetId, followeeId, idx - 1])
        while maxHeap and len(out) < 10:
            time, tweetId, followeeId, idx = heapq.heappop_max(maxHeap)
            out.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush_max(maxHeap, [time, tweetId, followeeId, idx - 1])
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)