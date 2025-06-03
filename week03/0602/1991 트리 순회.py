#트리 순회
import sys


N = int(sys.stdin.readline().strip())
tree = {} #딕셔너리

#트리 V 입력 받기
for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]
    
#전위 순회(preorder traversal)
def preorder(root):
    if root != '.':
        print(root, end = '') #root
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right

#중위 순회(inorder traversal)
def inorder(root):
    if root != '.':
        inorder(tree[root][0])#left
        print(root, end = '') #root
        inorder(tree[root][1]) #right

#후위 순회(postorder traversal)
def postorder(root):
    if root != '.':
        postorder(tree[root][0]) #left
        postorder(tree[root][1]) #right
        print(root, end = '') #root

preorder('A')
print()
inorder('A')
print()
postorder('A')