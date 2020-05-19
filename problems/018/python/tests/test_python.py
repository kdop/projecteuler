from python.utils import get_index_pairs, Node
import pytest


def test_get_index_pairs_1_items():
    payload = [1]
    with pytest.raises(ValueError):
        get_index_pairs(payload)


def test_get_index_pairs_2_items():
    payload = [1, 2]
    expect = [(0, 1)]
    actual = get_index_pairs(payload)
    assert expect == actual


def test_get_index_pairs_3_items():
    payload = [1, 2, 3]
    expect = [(0, 1), (1, 2)]
    actual = get_index_pairs(payload)
    assert expect == actual


def test_max_path_watermark():
    root = Node(10)
    leaf1 = Node(10)
    leaf2 = Node(9)
    leaf3 = Node(11)

    expect = 20
    root.max_path_watermark(leaf1, 0)
    assert expect == root.get_subtotal()

    expect = 20
    root.max_path_watermark(leaf2, 0)
    assert expect == root.get_subtotal()

    expect = 21
    root.max_path_watermark(leaf3, 0)
    assert expect == root.get_subtotal()
