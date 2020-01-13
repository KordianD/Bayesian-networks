import numpy as np


def split(list):
    return list[::2], list[1::2]


def get_offsets(elements_count):
    A = np.array([[elements_count, elements_count + 1], [1, -4]])
    B = np.array([[1], [0]])

    offsets = np.linalg.inv(A) @ B

    element_size = offsets[0, 0]
    space_between_elements = offsets[1, 0]
    return float(format(element_size, '.2f')), float(format(space_between_elements, '.2f'))