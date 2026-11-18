class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s=len(s)
        len_t=len(t)
        if len_s != len_t:
            return False
        else:
            sorted_s=''.join(sorted(s))
            sorted_t=''.join(sorted(t))
            if sorted_s==sorted_t:
                return True
            else:
                return False