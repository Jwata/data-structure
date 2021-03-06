class Node:
    def __init__(self):
        self.children = [None, None] # 0 or 1

    def next(self, b):
        if not self.children[b]:
            self.children[b] = Node()
        return self.children[b]

class Trie:
    NUM_BITS = 32

    def __init__(self):
        self.root = Node()
        self.index = None

    def add(self, v, index):
        root = self.root
        for i in range(self.NUM_BITS-1, -1, -1):
            if v & (1 << i) > 0:
                root = root.next(1)
            else:
                root = root.next(0)
        root.index = index

    def search_max_xor(self, v):
        max_xor = 0

        root = self.root
        for i in range(self.NUM_BITS-1, -1, -1):
            if v & (1 << i) > 0:
                b = 1
                b_op = 0
            else:
                b = 0
                b_op = 1

            if root.children[b_op]: # go to opposite direction
                root = root.next(b_op)
                max_xor |= (1 << i)
            else: # go to same 
                root = root.next(b)

        return max_xor, root.index

def find_max_xor(arr):
    n = len(arr)
    if n == 0:
        return 0

    cur_xor = 0
    max_xor = 0
    from_index = 0
    to_index = 0
    trie = Trie()

    for i in range(n):
        v = arr[i]
        cur_xor ^= v
        trie.add(cur_xor, i)
        xor, index = trie.search_max_xor(cur_xor)
        if xor > max_xor:
            max_xor = xor
            from_index = index + 1
            to_index = i

    return max_xor, from_index, to_index

print(find_max_xor([4, 6]))
print(find_max_xor([1, 2, 3, 4]))
print(find_max_xor([8, 1, 2, 12, 7, 6]))
