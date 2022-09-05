class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        # list alphabet
        la = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        # panjang s
        ps = len(s)
        # temp iterate s
        tis = ''
        # distance in s
        dis = 0
        for i in range(ps):
            
            if tis != s[i] or tis == '':
                tis = s[i]
                
            if tis == s[i]:
                continue
                
            if i == ps:
                pass
            
            for j in range(i + 1, ps):
                
                if tis != s[j]:
                    dis += 1
                    continue
                    
                if this == s[j]:
                    if distance[la.index(tis)] != dis:
                        pass
                    
                    if distance[la.index(tis)] == dis:
                        dis = 0
                        tis = ''
                        break


if __name__ == "__main__":
    solution = Solution()
    s = input()
    distance = list(map(int, input().rstrip().split(",")))
    result = solution.checkDistances(s, distance)
    print(result)