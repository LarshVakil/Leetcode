class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(filter(str.isalnum, s))
        text  = text.lower()
        left , right = 0 , len(text) - 1
        while right > left:
            if text[left] == text[right]:
                left += 1 
                right -= 1

            else :
                return False
        return True


