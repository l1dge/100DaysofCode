items = [
    {"id": 1, "name": "laptop", "value": 1000},
    {"id": 2, "name": "chair", "value": 300},
    {"id": 3, "name": "book", "value": 20},
]

# import unittest, copy
import copy


def duplicate_items(items):
    clone = copy.deepcopy(items)
    return clone[:]


# class TestDuplicateMethods(unittest.TestCase):
#     def test_change_copy_only(self):
#         items_copy = duplicate_items(items)
#         items_copy = items_copy.copy()
#         assert items == items_copy

#         # modify the copy
#         items_copy[0]["name"] = "macbook"
#         items_copy[1]["id"] = 4
#         items_copy[2]["value"] = 30

#         # only copy should have been updated, check original items values
#         assert items[0]["name"] == "laptop"
#         assert items[1]["id"] == 2
#         assert items[2]["value"] == 20


# if __name__ == "__main__":
#     unittest.main()