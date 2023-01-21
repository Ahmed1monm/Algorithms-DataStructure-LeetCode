# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution(object):
   
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        q = queue.Queue() 
        q.put(root[0],block=True,timeout=None)
        tree = []
    
        while not q.empty() :
            current = q.get(block= True, timeout=False)
            tree.append(current)

            while root[current] :

                q.put(root[current].left,block=True,timeout=None)
                q.put(root[current].right,block=True,timeout=None)
        
        result = 0
        for i in range( len(tree)):
            if tree[i] >= low and tree[i] <= high:
                result = result + tree[i]
            else:
                continue
        return result

test = Solution()
resulst = test.rangeSumBST([10,5,15,3,7,None,18],7,15)
print(resulst)