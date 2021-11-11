class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x=str(x)
        self.rev=self.x[::-1]
        for i,j in enumerate(self.x):
            if self.rev[i]!=j:
                return False
        return True
sol=Solution()
flag=sol.isPalindrome(121)
print(flag)
        
