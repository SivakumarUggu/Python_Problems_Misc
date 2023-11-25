#In-order traversal of a binary search tree.
def in_order_bst(n):
    if n<=0:
        return 0
    else:
        return in_order_bst(n-1)+1+in_order_bst(n-1)

Number_of_levels=int(input(f'Enter total number of levels: '))
print(f'Total number of nodes in all levels are: {in_order_bst(Number_of_levels)}')