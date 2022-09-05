class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        r = {}
        for letter in magazine:
            m[letter] = 1 if m.get(letter) == None else (m.get(letter) + 1) 
        
        for letter in ransomNote:
            r[letter] = 1 if r.get(letter) == None else (r.get(letter) + 1)
            
        for letter in r:
            if m.get(letter) == None:
                return False
            if letter in r:
                if m[letter] < r[letter]:
                    return False
        
        return True