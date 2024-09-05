class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        #concept : PigeonHole
        # n = number of  slots the dice will role apart from the rolls array
        
        m = len(rolls)
        total_sum = mean * (m+n)
        missing_sum = total_sum - sum(rolls)

        #  This validation is crucial because we cant have a dice with values 0 
        #  or eg 19//3 = 6 6 or 7 as dice cant be of value 7
        if missing_sum > 6 *n or missing_sum < n:
            return []
        
        res = []

        while n:
            dice = min(6, missing_sum - n + 1)
            res.append(dice)
            missing_sum -= dice
            n -=1 
        
        return res
