import math

from typing import List


def change_vertex_norm(vertex, norm: float) -> None:
    alpha = norm / get_vertex_norm(vertex)
    vertex[0] = alpha * vertex[0]
    vertex[1] = alpha * vertex[1]
    vertex[2] = alpha * vertex[2]


def get_angle_between(vertex0, vertex1) -> float:
    return math.acos((vertex0[0] * vertex1[0] + vertex0[1] * vertex1[1] + vertex0[2] * vertex1[2])
                     / (get_vertex_norm(vertex0) * get_vertex_norm(vertex1)))


def get_dot_product_3x3_3(matrix, vertex) -> List:
    return [matrix[0][0] * vertex[0] + matrix[0][1] * vertex[1] + matrix[0][2] * vertex[2],
            matrix[1][0] * vertex[0] + matrix[1][1] * vertex[1] + matrix[1][2] * vertex[2],
            matrix[2][0] * vertex[0] + matrix[2][1] * vertex[1] + matrix[2][2] * vertex[2]]


def get_normalized_vertex(vertex) -> List:
    norm = get_vertex_norm(vertex)
    return [vertex[0] / norm, vertex[1] / norm, vertex[2] / norm]


# def get_normalized_np_vertex(vertex: np.array) -> np.array:
#     return vertex / get_np_norm(vertex)


def get_rotation_matrix(axis: List, cos_t: float, sin_t: float) -> List:
    x, y, z = get_normalized_vertex(axis)
    xy = x * y
    xz = x * z
    yz = y * z
    _1_minus_cos_t = 1. - cos_t
    return [[cos_t + _1_minus_cos_t * x**2, _1_minus_cos_t * xy - sin_t * z, _1_minus_cos_t * xz + sin_t * y],
            [_1_minus_cos_t * xy + sin_t * z, cos_t + _1_minus_cos_t * y**2, _1_minus_cos_t * yz - sin_t * x],
            [_1_minus_cos_t * xz - sin_t * y, _1_minus_cos_t * yz + sin_t * x, cos_t + _1_minus_cos_t * z**2]]


def get_rotated_vertex(vertex0, vertex1, radians) -> List:
    normal = get_vertex_cross_product(vertex0, vertex1)
    cos_t = math.cos(radians)
    sin_t = math.sin(radians)
    return get_dot_product_3x3_3(get_rotation_matrix(normal, cos_t, sin_t), vertex0)


def get_triangle_midpoint_vertex(vertex0, vertex1, vertex2) -> List:
    return [(vertex0[0] + vertex1[0] + vertex2[0]) / 3,
            (vertex0[1] + vertex1[1] + vertex2[1]) / 3,
            (vertex0[2] + vertex1[2] + vertex2[2]) / 3]


def get_vertex_cross_product(vertex0, vertex1) -> List:
    return [vertex0[1] * vertex1[2] - vertex0[2] * vertex1[1],
            vertex0[2] * vertex1[0] - vertex0[0] * vertex1[2],
            vertex0[0] * vertex1[1] - vertex0[1] * vertex1[0]]


def get_vertex_norm(vertex) -> float:
    return math.sqrt(vertex[0]**2 + vertex[1]**2 + vertex[2]**2)


# def get_np_norm(vertex) -> float:
#     return np.sqrt(np.sum(vertex**2))


# def get_rotated_np_vertex(np_vertex0: np.array, np_vertex1: np.array, radians: float) -> List:
#     normal = np.cross(np_vertex0, np_vertex1)
#     cos_t = math.cos(radians)
#     sin_t = math.sin(radians)
#     rotation_np_matrix = np.array(get_rotation_matrix(normal, cos_t, sin_t))
#     return np.dot(rotation_np_matrix, np_vertex0)


# v1 = np.array([0.6789, 0.333679, 0.198754])
# v2 = np.array([0.947565, 0.12345, 0.453289])

# %timeit get_vertex_norm(v1)
# 2.73 µs ± 59.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
# %timeit get_np_norm(v1)
# 13.6 µs ± 185 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# %timeit get_normalized_vertex(v1)
# 4 µs ± 39.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
# %timeit get_normalized_np_vertex(v1)
# 5 µs ± 67.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# %timeit get_rotated_vertex(v1, v2, 2.23)
# 19.9 µs ± 165 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# %timeit get_rotated_np_vertex(v1, v2, 2.23)
# 91.9 µs ± 630 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)


