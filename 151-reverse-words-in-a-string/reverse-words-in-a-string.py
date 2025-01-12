class Solution:
    def reverseWords(self, s: str) -> str:
        # simple two pointer
        s = s.rstrip().lstrip()
        s = s.split()
        start = 0
        end = len(s) - 1

        while(start < end):
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp

            start = start + 1
            end = end - 1

        return " ".join(s)