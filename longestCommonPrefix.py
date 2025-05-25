class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max_str = max(strs)
        min_str = min(strs)
        length_min = len(min_str)
        temp = []
        if "" in strs:
            return ""
        for index, s_test in enumerate(max_str):
            if index <= (length_min - 1) and s_test == min_str[index]:
                temp.append(s_test)
            else:
                break
        return ''.join(temp)


def main():
    solution = Solution()
    s = ["abc", "abcd", "abce"]
    res = solution.longestCommonPrefix(s)
    print(res)


if __name__ == '__main__':
    main()
