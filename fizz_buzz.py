class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i == 1 or i == 2:
                ans.append(str(i))
                continue
            if (i % 3 == 0) and (i % 5 == 0):
                ans.append("FizzBuzz")
                continue
            if (i % 3 == 0) and not (i % 5 == 0):
                ans.append("Fizz")
                continue
            if not (i % 3 == 0) and (i % 5 == 0):
                ans.append("Buzz")
                continue
            if not (i % 3 == 0) and not (i % 5 == 0):
                ans.append(str(i))
                continue
        return ans