class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return None
        
        # Start with the root node
        leftmost = root
        
        while leftmost.left:
            # Iterate the "linked list" starting from the head node and using the next pointers
            head = leftmost
            while head:
                # Connect the left and right children
                head.left.next = head.right
                
                # Connect the right child to the next subtree's left child
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node in the current level
                head = head.next
            
            # Move to the next level
            leftmost = leftmost.left
        
        return root