def findAll(container, target):
    idx_list = []
    for idx in range(len(container)):
        if (container[idx] == target):
            idx_list.append(idx)
    return idx_list