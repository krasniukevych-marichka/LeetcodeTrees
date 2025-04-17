# Pre-order traversal
def pre_order(node):
    order = [node.data]
    order += pre_order(node.left)
    order += pre_order(node.right)
    return order

# In-order traversal
def in_order(node):
    order = []
    order += in_order(node.left)
    order.append(node.data)
    order += in_order(node.right)
    return order

# Post-order traversal
def post_order(node):
    order = []
    order += post_order(node.left)
    order += post_order(node.right)
    order.append(node.data)
    return order
