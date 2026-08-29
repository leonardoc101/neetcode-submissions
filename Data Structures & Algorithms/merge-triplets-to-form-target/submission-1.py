class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        can_reach = [False, False, False]
        for i in range(len(triplets)):
            for j in range(3):
                if ((triplets[i][j] == target[j]) 
                and (triplets[i][(j + 1) % 3] <= target[(j + 1) % 3])
                and (triplets[i][(j + 2) % 3] <= target[(j + 2) % 3])):
                    can_reach[j] = True
        return can_reach[0] and can_reach[1] and can_reach[2]
