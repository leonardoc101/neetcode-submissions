class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_set = set()
        freq_list = []
        out = []
        for num in nums:
            if num not in num_set:
                freq_list.append([num, 1])
                num_set.add(num)
            else:
                for sub_list in freq_list:
                    if sub_list[0] == num:
                        sub_list[1] += 1
                        break
        sorted_list = sorted(freq_list, key = lambda sublist: sublist[1], reverse = True)
        for i in range(k):
            out.append(sorted_list[i][0])
        return out