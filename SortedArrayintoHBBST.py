# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def createTree(num, node):
            n = len(num)
            if n==1:
                leaf = TreeNode(num[0])
                return leaf
            mid = n//2
            child = TreeNode(num[mid])
            if mid>0:
                child.left = createTree(num[:mid], child)
            if mid+1<n:
                child.right = createTree(num[mid+1:], child)
            return child
        
        n = len(nums)
        mid = n//2
        root = TreeNode(nums[mid])
        if mid>0:
            root.left = createTree(nums[:mid], root)
        if mid+1<n:
            root.right = createTree(nums[mid+1:], root)
        return root
