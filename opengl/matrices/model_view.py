import numpy as np
import math

from pyglobe3d.opengl.matrices.matrix import MatrixGL, RAD_DIV_DEG


class ModelViewMatrixGL(MatrixGL):
    def __init__(self):
        MatrixGL.__init__(self)
        self._inverse_matrix = MatrixGL()
        self._rotate_dict = {
            'x': self._rotate_around_x,
            'y': self._rotate_around_y,
            'z': self._rotate_around_z,
        }

    def rotate(self, around, degrees):
        radians = degrees * RAD_DIV_DEG
        self._rotate_dict.get(around, 'z')(radians)

    def _rotate_around_x(self, radians):
        rotation_matrix = np.array(
            [[1, 0, 0, 0],
             [0, math.cos(radians), -math.sin(radians), 0],
             [0, math.sin(radians), math.cos(radians), 0],
             [0, 0, 0, 1]]
        )
        inverse_rotation_matrix = np.array(
            [[1, 0, 0, 0],
             [0, math.cos(radians), math.sin(radians), 0],
             [0, -math.sin(radians), math.cos(radians), 0],
             [0, 0, 0, 1]]
        )
        self._matrix = rotation_matrix * self._matrix
        self._inverse_matrix = self._inverse_matrix * inverse_rotation_matrix

    def _rotate_around_y(self, radians):
        rotation_matrix = np.array(
            [[math.cos(radians), 0, math.sin(radians), 0],
             [0, 1, 0, 0],
             [-math.sin(radians), 0, math.cos(radians), 0],
             [0, 0, 0, 1]]
        )
        inverse_rotation_matrix = np.array(
            [[math.cos(radians), 0, -math.sin(radians), 0],
             [0, 1, 0, 0],
             [math.sin(radians), 0, math.cos(radians), 0],
             [0, 0, 0, 1]]
        )
        self._matrix = rotation_matrix * self._matrix
        self._inverse_matrix = self._inverse_matrix * inverse_rotation_matrix

    def _rotate_around_z(self, radians):
        rotation_matrix = np.array(
            [[math.cos(radians), -math.sin(radians), 0, 0],
             [math.sin(radians), 0, math.cos(radians), 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
        )
        inverse_rotation_matrix = np.array(
            [[math.cos(radians), math.sin(radians), 0, 0],
             [-math.sin(radians), 0, math.cos(radians), 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
        )
        self._matrix = rotation_matrix * self._matrix
        self._inverse_matrix = self._inverse_matrix * inverse_rotation_matrix
