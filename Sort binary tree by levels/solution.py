from collections import deque
def tree_by_levels(node):
    if node is None:
        return []
    queue = deque()
    queue.append(node)
    order = []
    while queue:
        cur_node = queue.popleft()
        order.append(cur_node.n)
        if cur_node.L is not None:
            queue.append(cur_node.L)
        if cur_node.R is not None:
            queue.append(cur_node.R)
    return order