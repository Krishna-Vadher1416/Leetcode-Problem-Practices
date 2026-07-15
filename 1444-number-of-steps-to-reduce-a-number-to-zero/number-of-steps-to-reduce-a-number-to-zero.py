class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num <= 0 :
            return 0
        i = 0

        while num != 0:
            if num%2 == 0:
                num = num/ 2
            else :
                num -= 1

            i += 1

        return i

        




        