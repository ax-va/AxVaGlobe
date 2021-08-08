import numpy as np
import math

from typing import List


def get_angle_between(vertex0: np.array, vertex1: np.array) -> float:
    return math.acos(np.sum(vertex0 * vertex1) / (norm(vertex0) * norm(vertex1)))


def norm(vertex: np.array) -> float:
    return np.sqrt(np.sum(vertex**2))


def normalize(vertex: np.array) -> np.array:
    return vertex / norm(vertex)


def get_rotation_matrix(x: float, y: float, z: float, cos_t: float, sin_t: float) -> List:
    _1_minus_cos_t = 1. - cos_t
    xy = x * y
    xz = x * z
    yz = y * z
    return [[cos_t + _1_minus_cos_t * x**2, _1_minus_cos_t * xy - sin_t * z, _1_minus_cos_t * xz + sin_t * y],
            [_1_minus_cos_t * xy + sin_t * z, cos_t + _1_minus_cos_t * y**2, _1_minus_cos_t * yz - sin_t * x],
            [_1_minus_cos_t * xz - sin_t * y, _1_minus_cos_t * yz + sin_t * x, cos_t + _1_minus_cos_t * z**2]]


def get_rotated_vertex(vertex0: np.array, vertex1: np.array, radians: float) -> np.array:
    normal = np.cross(vertex0, vertex1)
    x, y, z = normalize(normal)
    cos_t = math.cos(radians)
    sin_t = math.sin(radians)
    rotation_matrix = np.array(get_rotation_matrix(x, y, z, cos_t, sin_t))
    return np.dot(rotation_matrix, vertex0)



