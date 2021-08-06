import numpy as np
import math

from typing import List


def get_rotation_matrix(x, y, z, cos_t, sin_t) -> List:
    _1_minus_cos_t = 1. - cos_t
    xy = x * y
    xz = x * z
    yz = y * z
    return [[cos_t + _1_minus_cos_t * x**2, _1_minus_cos_t * xy - sin_t * z, _1_minus_cos_t * xz + sin_t * y],
            [_1_minus_cos_t * xy + sin_t * z, cos_t + _1_minus_cos_t * y**2, _1_minus_cos_t * yz - sin_t * x],
            [_1_minus_cos_t * xz - sin_t * y, _1_minus_cos_t * yz + sin_t * x, cos_t + _1_minus_cos_t * z**2]]


def rotate(vertex0: np.array, vertex1: np.array, radians: float) -> np.array:
    vector = np.cross(vertex0, vertex1)
    x, y, z = vector / np.sqrt(np.sum(vector**2))
    cos_t = math.cos(radians)
    sin_t = math.sin(radians)
    rotation_matrix = np.array(get_rotation_matrix(x, y, z, cos_t, sin_t))
    return np.dot(rotation_matrix, vertex0)