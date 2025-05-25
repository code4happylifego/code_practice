class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


def main():
    solution = Solution()
    haystack = "HELLO"
    needle = "LL"
    res = solution.strStr(haystack, needle)
    print(res)


if __name__ == '__main__':
    main()
