from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for index, word in enumerate(words):
            if x in word:
                res.append(index)
        return res


def main():
    solution = Solution()
    words = ["leet", "code"]
    x = "e"
    res = solution.findWordsContaining(words, x)
    print(res)


if __name__ == '__main__':
    main()
