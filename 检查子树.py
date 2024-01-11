# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        string_t1_be = self.dfs_tree(t1)
        string_t1_mi = self.dfs_tree_str(t1)
        string_t1_ed = self.dfs_tree_ed(t1)
        string_t2_be = self.dfs_tree(t2)
        string_t2_mi = self.dfs_tree_str(t2)
        string_t2_ed = self.dfs_tree_ed(t2)
        flag = 0
        print(string_t1_be,string_t2_be,string_t1_mi,string_t2_mi,string_t1_ed,string_t2_ed)
        for i in range(len(string_t1_mi)):
            if string_t1_mi[i:i+len(string_t2_mi)] == string_t2_mi:
                flag = 1
                break
        if flag == 1:
            for i in range(len(string_t1_be)):
                if string_t1_be[i:i+len(string_t2_be)] == string_t2_be:
                    flag = 2
                    break
        if flag == 2:
            for i in range(len(string_t1_ed)):
                if string_t1_ed[i:i+len(string_t2_ed)] == string_t2_ed:
                    flag = 3
                    break
        if flag == 3:
            return True
        else:
            return False

    
    #中序遍历
    def dfs_tree(self, node):
        if not node:
            return [-1]
        return [node.val] + self.dfs_tree(node.left) + self.dfs_tree(node.right)

    def dfs_tree_str(self, node):
        if not node:
            return [-1]
        return self.dfs_tree_str(node.left) + [node.val] + self.dfs_tree_str(node.right)
    
    def dfs_tree_ed(self, node):
        if not node:
            return [-1]
        return self.dfs_tree_ed(node.left) + self.dfs_tree_ed(node.right) + [node.val]
