# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # # Solution with recursion -------- 
        # if not root:
        #     return 0
        # # 1 is for the root
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        # # iterative BFS ---------------- 
        # if not root:
        #     return 0
        
        # level = 0
        # # this deque function is working as a queue
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node=q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # iterative DFS - pre-order
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        
        return res