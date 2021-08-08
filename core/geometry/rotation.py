import numpy as np
import math

from typing import List


def get_angle_between(vertex0, vertex1) -> float:
    return math.acos((vertex0[0] * vertex1[0] + vertex0[1] * vertex1[1] + vertex0[2] * vertex1[2]) 
                     / (norm(vertex0) * norm(vertex1)))


def norm(vertex) -> float:
    return math.sqrt(vertex[0]**2 + vertex[1]**2 + vertex[2]**2)


def normalize_np_vertex(np_vertex: np.array) -> np.array:
    return np_vertex / norm(np_vertex)


def get_rotation_list_matrix(x: float, y: float, z: float, cos_t: float, sin_t: float) -> List:
    _1_minus_cos_t = 1. - cos_t
    xy = x * y
    xz = x * z
    yz = y * z
    return [[cos_t + _1_minus_cos_t * x**2, _1_minus_cos_t * xy - sin_t * z, _1_minus_cos_t * xz + sin_t * y],
            [_1_minus_cos_t * xy + sin_t * z, cos_t + _1_minus_cos_t * y**2, _1_minus_cos_t * yz - sin_t * x],
            [_1_minus_cos_t * xz - sin_t * y, _1_minus_cos_t * yz + sin_t * x, cos_t + _1_minus_cos_t * z**2]]


def get_rotated_np_vertex(np_vertex0: np.array, vertex1: np.array, radians: float) -> np.array:
    np_normal = np.cross(np_vertex0, np_vertex1)
    x, y, z = normalize_np_vertex(np_normal)
    cos_t = math.cos(radians)
    sin_t = math.sin(radians)
    rotation_np_matrix = np.array(get_rotation_list_matrix(x, y, z, cos_t, sin_t))
    return np.dot(rotation_np_matrix, vertex0)



