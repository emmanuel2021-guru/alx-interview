#!/usr/bin/python3

"""This module contains a method that determines if all boxes in a
list of lists can be opened"""


def canUnlockAll(boxes):
    """This method determines if all boxes in a
    list of lists can be opened"""
    box_range = []
    unlocked_boxes = [0]

    for i in range(len(boxes)):
        box_range.append(i)

    for i in unlocked_boxes:
        if boxes[i] in boxes:
            for j in boxes[i]:
                if j not in unlocked_boxes:
                    unlocked_boxes.append(j)
    unlocked_boxes.sort()

    return box_range == unlocked_boxes
