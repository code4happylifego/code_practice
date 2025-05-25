class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = s.lower()
        res = []
        for str in temp:
            if str not in "abcdefghijklmnopqrstuvwxyz0123456789":
                continue
            else:
                res.append(str)
        result_str = ''.join(res)
        if result_str == result_str[::-1]:
            return True
        else:
            return False


def main():
    solution = Solution()
    test_str = "HELLO"
    res = solution.isPalindrome(test_str)
    print(res)


if __name__ == '__main__':
    main()
