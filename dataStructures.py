# list
my_list = [1, "hello", 3.14, True]  # 创建列表
my_list.append(4)  # 添加元素 → [1, "hello", 3.14, True, 4]
sliced = my_list[1:3]  # 切片 → ["hello", 3.14]
print(sliced)  # ['hello', 3.14]
# tuple
coordinates = (10, 20)  # 创建元组
x, y = coordinates  # 解包 → x=10, y=20
print(x, y)  # 10 20

# dict
person = {"name": "Alice", "age": 25, "addr": "earth"}  # 创建字典
person["city"] = "New York"  # 添加键值对
name = person.get("name", "Unknown")  # 安全获取值 → "Alice"
print(name)  # Alice

# set
primes = {2, 3, 5, 7}  # 创建集合
primes.add(11)  # 添加元素 → {2, 3, 5, 7, 11}
evens = {2, 4, 6}
common = primes & evens  # 交集 → {2}
print(common)  # {2}

# stack
stack = []
stack.append(1)  # 入栈 → [1]
top = stack.pop()  # 出栈 → 1（栈空）
print(stack)  # [ ]

# queue
from collections import deque

queue = deque()
queue.append(1)  # 入队 → deque([1])
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

front = queue.popleft()  # 出队
print(queue)  # deque([2, 3])


# linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_temp = curr.next  # 暂存下一个节点
        curr.next = prev  # 反转指针
        prev = curr  # 前移prev
        curr = next_temp  # 前移curr
    return prev


"""
初始化指针：
prev = None（相当于一本合上的书）
curr = head（当前页是第一页）

第一次循环：
暂存下一页地址：next_temp = 2
反转指针：让第一页的下一页指向prev（即None），变成1→None
移动指针：prev来到第一页，curr来到第二页

第二次循环：
暂存下一页地址：next_temp = 3
反转指针：让第二页的下一页指向prev（即第一页），变成2→1→None
移动指针：prev来到第二页，curr来到第三页

重复直到末尾：最终所有箭头反向，形成5→4→3→2→1→None
"""

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" → " if current.next else "")
        current = current.next
    print()


print("原链表：", end="")
print_linked_list(head)  # 原链表：1 → 2 → 3 → 4 → 5
reversed_head = reverseList(head)

print("反转后链表：", end="")
print_linked_list(reversed_head)  # 反转后链表：5 → 4 → 3 → 2 → 1


# tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)  # 根节点
root.left = TreeNode(2)
print(root)  # <__main__.TreeNode object at 0x10a5b0f70>

# heap
import heapq

heap = []
heapq.heappush(heap, 3)  # 入堆 → [3]
min_val = heapq.heappop(heap)  # 弹出最小值

# word count
text = "apple banana apple orange banana banana"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # {'apple': 2, 'banana': 3, 'orange': 1}
