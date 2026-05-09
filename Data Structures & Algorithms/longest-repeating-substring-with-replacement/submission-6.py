class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        L = 0
        count = {}
        maxF = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            maxF = max(maxF, count[s[i]])

            while i - L + 1 - maxF > k:
                count[s[L]] -= 1
                L += 1
            length = max(length, i - L + 1)
        return length