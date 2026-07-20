class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = [0]* 2 
        kelven = celsius + 273.15
        farhan = celsius*1.80 + 32.0

        ans[0] = kelven
        ans[1] = farhan 

        return ans