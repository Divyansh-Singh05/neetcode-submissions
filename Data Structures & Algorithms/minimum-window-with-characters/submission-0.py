class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = {}
        for char in t:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        window = {}
        have = 0
        required = len(need)

        l = 0
        min_len = float("inf")
        min_s = ""

        for r, char in enumerate(s):
            if char in window:
                window[char] += 1
            else:
                window[char] = 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_s = s[l:r + 1]

                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                l += 1

        return min_s