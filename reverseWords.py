class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.split()
        result = " ".join(reversed(temp))
        return result


def main():
    solution = Solution()
    test_str = "hello world"
    res = solution.reverseWords(test_str)
    print(res)


if __name__ == '__main__':
    main()
