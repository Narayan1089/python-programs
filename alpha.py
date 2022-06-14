st = input("Enter the string : ")
alpha = num = special = 0

for i in range(len(st)):
    if((st[i] >= 'a' and st[i] <= 'z') or (st[i] >= 'A' and st[i] <= 'Z')):
        alpha = alpha + 1
    elif(st[i] >= '0' and st[i] <= '9'):
        num = num + 1
    else:
        special = special + 1
print("Number of alphabets:", alpha)
print("Number of numbers :", num)
print("Number of special characters:", special)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         al = ''
#         n = s.lower()
#         for i in range(len(n)):
#             if (n[i] >= 'a' and n[i] <= 'z') or (n[i] >= '0' and n[i] <= '9'):

#                 al = n[i] + al
#         ol = al
#         # if len(al) ==1:
#         #     return False
#         if al[::-1] == ol:
#             return True
#         else:
#             return False


# s = Solution()
# s.isPalindrome("0P")
