class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        #For getting max x we will decrese x and increase nums as aslo mentioned in hint 
        return (num + 2*t)