# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# F.e. 121 is a palidrom, (-777) is not (turns into 777-)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        # as '-' goes from the first to the last position, all negative numbers are NOT palindroms
        if x < 0:
            return False

        x = str(x)        
        for i in range(0, len(x)//2):
            if x[i] != x[len(x)-1-i]: # compare 1st digit with the last, 2nd with (last-1) and so on until come to the middle      
                return False        
        return True            