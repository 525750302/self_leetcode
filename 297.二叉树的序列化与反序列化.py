#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ""
        result = self.rootToStr(root,result)
        return result[:-1]
    
    def rootToStr(self,root,result):
        if root == None :
            result = result + "None,"
            return result
        result = result + str(root.val) + ","
        result = self.rootToStr(root.left, result)
        result = self.rootToStr(root.right, result)
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        return self.strToRoot(nodes)
    
    def strToRoot(self,nodes):
        if nodes:
                if nodes[0] == 'None':
                    nodes.pop(0)
                    return None
                root = TreeNode(nodes.pop(0))
                root.left = self.strToRoot(nodes)
                root.right = self.strToRoot(nodes)
                return root
        return None

            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

