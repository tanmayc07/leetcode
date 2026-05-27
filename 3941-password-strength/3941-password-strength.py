class Solution:
    def passwordStrength(self, password: str) -> int:
        p = set(password)
        st = 0
        for c in p:
            if c.isalpha():
                if c.islower(): st += 1
                if c.isupper(): st += 2
            if c.isdigit(): st += 3
            if c in ['!', '@', '#', '$']: st += 5
        return st