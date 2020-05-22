NODE_VALUE = 0
NODE_MAX_SUB = 1
NODE_IDX_MAX = 2


class Node(object):
    def __init__(self, value, subtotal=None, crumble=None):
        self.value = value
        self._subtotal = subtotal
        self._crumble_to_max = crumble

    def get_subtotal(self):
        return self._subtotal if self._subtotal else self.value

    def max_path_watermark(self, leaf, leaf_idx):
        """
        Checks if leaf leads to new max, and if so update subtotal and crumble that leads to that max.
        :param leaf: leaf to check
        :type leaf: Node
        :param leaf_idx:
        :type leaf_idx: Integer
        """
        candidate_subtotal = self.value + leaf.get_subtotal()
        if candidate_subtotal > self.get_subtotal():
            self._subtotal = candidate_subtotal
            self._crumble_to_max = leaf_idx

    def get_crumble(self):
        return self._crumble_to_max


def get_index_pairs(a_list):
    """
    Generates pairs of indices for input list.
    :param a_list: list with  at least two items
    :type a_list: list
    :return: list of pairs
    :rtype: [(int, int)]
    """
    if len(a_list) < 2:
        raise ValueError("Can't make pairs with less than 2 items!")

    return [(i, i + 1) for i in range(len(a_list) - 1)]

