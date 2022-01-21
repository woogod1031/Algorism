class Solution(object):
    def numJewelsInStones(self,jewels, stones):

        freq = {}
        count = 0
        for char in stones: #freq에 값 넣어주기
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        for jew in jewels:
            if jew not in freq:
                continue
            else:
                count += freq[jew]

        return count
    
        