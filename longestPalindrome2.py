from collections import Counter


def longestPalindrome(words):
    word_count = Counter(words)  # 统计每个单词出现的次数
    result = 0  # 记录回文串的总长度
    center = 0  # 记录中间部分是否能添加一个对称单词
    processed = set()  # 记录已处理过的单词，避免重复计算

    for word in word_count:
        if word in processed:
            continue  # 如果单词已处理，跳过
        reversed_word = word[::-1]  # 获取当前单词的反转形式

        if word == reversed_word:
            # 处理对称单词（如"aa"）
            count = word_count[word]
            pairs = count // 2  # 计算可以成对的数量
            result += pairs * 4  # 每对贡献4个字符（两个单词，每个两个字符）
            if count % 2 == 1:
                center = 2  # 如果存在奇数次数的对称单词，中间可以加一个
            processed.add(word)  # 标记为已处理
        else:
            # 处理非对称单词（如"ab"和"ba"）
            if reversed_word in word_count:
                # 计算配对的数量（取当前单词和反转单词的最小出现次数）
                pairs = min(word_count[word], word_count[reversed_word])
                result += pairs * 4  # 每对贡献4个字符
                # 将这两个单词标记为已处理
                processed.add(word)
                processed.add(reversed_word)
            else:
                # 如果反转单词不存在，当前单词无法配对，直接标记为已处理
                processed.add(word)

    return result + center  # 总长度加上中间部分的长度


def main():
    print(longestPalindrome(["lc", "cl", "gg"]))


if __name__ == '__main__':
    main()
