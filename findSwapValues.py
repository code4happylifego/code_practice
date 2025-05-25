class Solution(object):
    def findSwapValues(self, array1, array2):
        """
        :type array1: List[int]
        :type array2: List[int]
        :rtype: List[int]
        """
        sum1 = sum(array1)
        sum2 = sum(array2)
        diff = sum1 - sum2
        target_diff = diff // 2
        set2 = set(array2)
        if diff % 2 != 0:
            return []
        else:
            for x in array1:
                y = x - target_diff
                if y in set2:
                    return [x, y]
        return []

def main():
    solution = Solution()
    arr1 = [4, 1, 2, 1, 1, 2]
    arr2 = [3, 6, 3, 3]
    res = solution.findSwapValues(arr1, arr2)
    print(res)


if __name__ == '__main__':
    main()