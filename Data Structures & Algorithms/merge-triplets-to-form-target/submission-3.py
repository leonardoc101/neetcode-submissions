class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        can_reach = [False, False, False]
        for i in range(len(triplets)):
            if (triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]):
                continue
            for j in range(3):
                if ((triplets[i][j] == target[j]) 
                and (triplets[i][(j + 1) % 3] <= target[(j + 1) % 3])
                and (triplets[i][(j + 2) % 3] <= target[(j + 2) % 3])):
                    can_reach[j] = True
                if (can_reach[0] and can_reach[1] and can_reach[2]):
                    return True
        return can_reach[0] and can_reach[1] and can_reach[2]
