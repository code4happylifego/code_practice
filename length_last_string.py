class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_array = s.split(' ')
        arr_len = len(word_array)
        for i in range(-1, -arr_len - 1, -1):
            if len(word_array[i]) != 0:
                res = len(word_array[i])
                return res


def main():
    solution = Solution()
    s = "hello world"
    res = solution.lengthOfLastWord(s)
    print(res)


if __name__ == '__main__':
    main()
