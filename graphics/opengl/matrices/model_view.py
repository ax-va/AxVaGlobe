import math

from pyglobe3d.graphics.opengl.matrices.matrix import OpenGLMatrix
from pyglobe3d.graphics.opengl.matrices.matrix_errs import ZeroVectorLengthError


class ModelView(OpenGLMatrix):
    def __init__(self):
        OpenGLMatrix.__init__(self)
        self._rotate_funcs = {
            'x': self._rotate_around_x,
            'y': self._rotate_around_y,
            'z': self._rotate_around_z,
        }

    def rotate(self, around, degrees):
        radians = math.radians(degrees)
        cos_t = math.cos(radians)
        sin_t = math.sin(radians)
        if around == 'x' or around == 'y' or around == 'z':
            self._rotate_funcs[around](cos_t, sin_t)
        else:
            self._rotate_around_axis(around, cos_t, sin_t)
            
    def _rotate_around_axis(self, axis, cos_t, sin_t):
        """
        R = [[math.cos(radians) + (1. - math.cos(radians)) * x**2,
              (1. - math.cos(radians)) * x * y - math.sin(radians) * z,
              (1. - math.cos(radians)) * x * z + math.sin(radians) * y, 0.],
             [(1. - math.cos(radians)) * y * x + math.sin(radians) * z,
              math.cos(radians) + (1. - math.cos(radians)) * y**2,
              (1. - math.cos(radians)) * y * z - math.sin(radians) * x, 0.],
             [(1. - math.cos(radians)) * z * x - math.sin(radians) * y,
              (1. - math.cos(radians)) * z * y + math.sin(radians) * x,
              math.cos(radians) + (1. - math.cos(radians)) * z**2, 0.],
             [0., 0., 0., 1.]]
        A = R * A
        """
        vector_length = math.hypot(*axis)
        if vector_length == 0:
            raise ZeroVectorLengthError(axis)
        x, y, z = (coord / vector_length for coord in axis)
        _1_minus_cos_t = 1. - cos_t
        xy = x * y
        xz = x * z
        yz = y * z
        rotation_matrix = [
            [cos_t + _1_minus_cos_t * x**2, _1_minus_cos_t * xy - sin_t * z, _1_minus_cos_t * xz + sin_t * y],
            [_1_minus_cos_t * xy + sin_t * z, cos_t + _1_minus_cos_t * y**2, _1_minus_cos_t * yz - sin_t * x],
            [_1_minus_cos_t * xz - sin_t * y, _1_minus_cos_t * yz + sin_t * x, cos_t + _1_minus_cos_t * z**2]
        ]
        rotation = OpenGLMatrix(matrix=rotation_matrix)
        self.multiply(with_matrix=rotation, way='left')

    def _rotate_around_x(self, cos_t, sin_t):
        """
        R = [[1., 0., 0., 0.],
             [0., math.cos(radians), -math.sin(radians), 0.],
             [0., math.sin(radians), math.cos(radians), 0.],
             [0., 0., 0., 1.]]
        A = R * A
        """
        for j in range(4):
            self._matrix[1][j], self._matrix[2][j] = \
                cos_t * self._matrix[1][j] - sin_t * self._matrix[2][j], \
                sin_t * self._matrix[1][j] + cos_t * self._matrix[2][j]

    def _rotate_around_y(self, cos_t, sin_t):
        """
        R = [[math.cos(radians), 0., math.sin(radians), 0.],
             [0., 1., 0., 0.],
             [-math.sin(radians), 0., math.cos(radians), 0.],
             [0., 0., 0., 1.]]
        A = R * A
        """
        for j in range(4):
            self._matrix[0][j], self._matrix[2][j] = \
                cos_t * self._matrix[0][j] + sin_t * self._matrix[2][j], \
                -sin_t * self._matrix[0][j] + cos_t * self._matrix[2][j]

    def _rotate_around_z(self, cos_t, sin_t):
        """
        R = [[math.cos(radians), -math.sin(radians), 0., 0.],
             [math.sin(radians), math.cos(radians), 0., 0.],
             [0., 0., 1., 0.],
             [0., 0., 0., 1.]]
        A = R * A
        """
        for j in range(4):
            self._matrix[0][j], self._matrix[1][j] = \
                cos_t * self._matrix[0][j] - sin_t * self._matrix[1][j], \
                sin_t * self._matrix[0][j] + cos_t * self._matrix[1][j]


if __name__ == '__main__':
    mat = ModelView()
    print(mat.float32_array)
    mat.rotate(around='x', degrees=-90.)
    print(mat.float32_array)
    mat.rotate(around=[1, 1, 1], degrees=-90.)
    print(mat.float32_array)
