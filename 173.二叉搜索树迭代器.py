# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.iterator = 0
        self.result = []
        self.dfs(root)


    def next(self) -> int:
        self.iterator += 1
        return self.result[self.iterator-1]

    def hasNext(self) -> bool:
        return self.iterator < len(self.result)
    
    def dfs(self, root):
        if root.left:
            self.dfs(root.left)
        self.result.append(root.val)
        if root.right:
            self.dfs(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()