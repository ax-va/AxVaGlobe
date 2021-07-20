import itertools
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
        self._scale_funcs = {
            'x': self._scale_x,
            'y': self._scale_y,
            'z': self._scale_z,
        }
        self._translate_funcs = {
            'x': self._translate_along_x,
            'y': self._translate_along_y,
            'z': self._translate_along_z,
        }

    def rotate(self, degrees, around):
        if isinstance(around, str):
            for deg, ax in itertools.product(degrees, around):
                rad = math.radians(deg)
                self._rotate_funcs[ax](math.cos(rad), math.sin(rad))
        else:
            for deg, ax in itertools.product(degrees, around):
                rad = math.radians(deg)
                self._rotate_around_axis(math.cos(rad), math.sin(rad), ax)

    def scale(self, scaling, axes='xyz'):
        """
        S = [[x_scaling, 0., 0., 0.],
             [0., y_scaling, 0., 0.],
             [0., 0., z_scaling, 0.],
             [0., 0., 0., 1.]]
        with A = S * A and v_new = A * v_old
        """
        if scaling != 1:
            for ax in axes:
                selself._scale-funcs[ax](scaling)

    def translate(self, translation):
        """
        T = [[1., 0., 0., x_translation],
             [0., 1., 0., y_translation],
             [0., 0., 1., z_translation],
             [0., 0., 0., 1.]]
        with A = T * A and v_new = A * v_old
        """
        x_tr, y_tr, z_tr = translation
        if x_tr != 0:
            self._translate_along_x(x_tr)
        if y_tr != 0:
            self._translate_along_y(y_tr)
        if z_tr != 0:
            self._translate_along_z(z_tr)

    def _rotate_around_axis(self, cos_t, sin_t, axis):
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
        with A = R * A and v_new = A * v_old
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
        self.multiply(by_matrix=OpenGLMatrix(matrix=rotation_matrix))

    def _rotate_around_x(self, cos_t, sin_t):
        """
        R_x = [[1., 0., 0., 0.],
               [0., math.cos(radians), -math.sin(radians), 0.],
               [0., math.sin(radians), math.cos(radians), 0.],
               [0., 0., 0., 1.]]
        with A = R_x * A and v_new = A * v_old
        """
        for j in range(4):
            self._matrix[1][j], self._matrix[2][j] = \
                cos_t * self._matrix[1][j] - sin_t * self._matrix[2][j], \
                sin_t * self._matrix[1][j] + cos_t * self._matrix[2][j]

    def _rotate_around_y(self, cos_t, sin_t):
        """
        R_y = [[math.cos(radians), 0., math.sin(radians), 0.],
               [0., 1., 0., 0.],
               [-math.sin(radians), 0., math.cos(radians), 0.],
               [0., 0., 0., 1.]]
        with A = R_y * A and v_new = A * v_old
        """
        for j in range(4):
            self._matrix[0][j], self._matrix[2][j] = \
                cos_t * self._matrix[0][j] + sin_t * self._matrix[2][j], \
                -sin_t * self._matrix[0][j] + cos_t * self._matrix[2][j]

    def _rotate_around_z(self, cos_t, sin_t):
        """
        R_z = [[math.cos(radians), -math.sin(radians), 0., 0.],
               [math.sin(radians), math.cos(radians), 0., 0.],
               [0., 0., 1., 0.],
               [0., 0., 0., 1.]]
        with A = R_z * A and v_new = A * v_old
        """
        for j in range(4):
            self._matrix[0][j], self._matrix[1][j] = \
                cos_t * self._matrix[0][j] - sin_t * self._matrix[1][j], \
                sin_t * self._matrix[0][j] + cos_t * self._matrix[1][j]

    def _scale_x(self, x_scaling):
        """
        S_x = [[x_scaling, 0., 0., 0.],
               [0., 1., 0., 0.],
               [0., 0., 1., 0.],
               [0., 0., 0., 1.]]
        with A = S_x * A and v_new = A * v_old
        """
        self._matrix[0][0] *= x_scaling

    def _scale_y(self, y_scaling):
        """
        S_y = [[1., 0., 0., 0.],
               [0., y_scaling, 0., 0.],
               [0., 0., 1., 0.],
               [0., 0., 0., 1.]]
        with A = S_y * A and v_new = A * v_old
        """
        self._matrix[1][1] *= y_scaling

    def _scale_z(self, z_scaling):
        """
        S_z = [[1., 0., 0., 0.],
               [0., 1., 0., 0.],
               [0., 0., z_scaling, 0.],
               [0., 0., 0., 1.]]
        with A = S_z * A and v_new = A * v_old
        """
        self._matrix[2][2] *= z_scaling

    def _translate_along_x(self, x_translation):
        """
        T_x = [[1., 0., 0., x_translation],
               [0., 1., 0., 0.],
               [0., 0., 1., 0.],
               [0., 0., 0., 1.]]
        with A = T_x * A and v_new = A * v_old
        """
        for j in range(4):
            self._matrix[0][j] += x_translation * self._matrix[3][j]

    def _translate_along_y(self, y_translation):
        """
        T_y = [[1., 0., 0., 0.],
               [0., 1., 0., y_translation],
               [0., 0., 1., 0.],
               [0., 0., 0., 1.]]
        with A = T_y * A and v_new = A * v_old
        """
        for j in range(4):
            self._matrix[1][j] += y_translation * self._matrix[3][j]

    def _translate_along_z(self, z_translation):
        """
        T_z = [[1., 0., 0., 0.],
               [0., 1., 0., 0.],
               [0., 0., 1., z_translation],
               [0., 0., 0., 1.]]
        with A = T_y * A and v_new = A * v_old
        """
        for j in range(4):
            self._matrix[2][j] += z_translation * self._matrix[3][j]


if __name__ == '__main__':
    mat = ModelView()
    print(mat.float32_array)
    mat.rotate(degrees=[-90, 30], around='xz')
    print(mat.float32_array)
    mat.rotate(degrees=[-90, 60], around=[[1, 1, 1], [1, 2, 3]])
    print(mat.float32_array)
    mat.translate(translation=[-1, -1, -1])
    mat.scale(scaling=2)
    print(mat.float32_array)
