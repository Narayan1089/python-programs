class Solution:
    def fizzBuzz(self, n: int):
        l = []
        for i in range(1, n):
            if (i % 3) and (i % 5) == 0:
                ['FizzBuzz'] == l[i]
                # l[i] == ['FizzBuzz']
            elif (i % 3) == 0:
                l[i] == ['Fizz']
            elif (i % 5) == 0:
                l[i] == ['Buzz']
            else:
                return l
        return l


s = Solution()
print(s.fizzBuzz(5))
