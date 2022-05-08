class Solution:
    def hammingWeight(self, n: str) -> int:
        count = 0
        a = str(n)
        count = a.count('1')
        # for i in range(len(a)):
        #     if a[i] == '1':
        #         count = count+1
        return count


s = Solution()
print(s.hammingWeight('00000000000000000000000000001011'))
