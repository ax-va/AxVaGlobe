import math

from pyglobe3d.opengl.matrices.matrix import Matrix4X4


class ModelView(Matrix4X4):
    def __init__(self):
        MatrixGL.__init__(self)
        self._rotate_funcs = {
            'x': self._rotate_around_x,
            'y': self._rotate_around_y,
            'z': self._rotate_around_z,
        }

    def rotate(self, around, degrees):
        radians = degrees / 180. * math.pi
        cos_t = math.cos(radians)
        sin_t = math.sin(radians)
        self._rotate_funcs.get(around, 'x')(cos_t, sin_t)

    def _rotate_around_x(self, cos_t, sin_t):
        """
        R = [[1., 0., 0., 0.],
             [0., math.cos(radians), -math.sin(radians), 0.],
             [0., math.sin(radians), math.cos(radians), 0.],
             [0., 0., 0., 1.]]
        A = R * A
        """
        self._matrix[1][0], self._matrix[2][0] = \
            cos_t * self._matrix[1][0] - sin_t * self._matrix[2][0], \
            sin_t * self._matrix[1][0] + cos_t * self._matrix[2][0]

        self._matrix[1][1], self._matrix[2][1] = \
            cos_t * self._matrix[1][1] - sin_t * self._matrix[2][1], \
            sin_t * self._matrix[1][1] + cos_t * self._matrix[2][1]

        self._matrix[1][2], self._matrix[2][2] = \
            cos_t * self._matrix[1][2] - sin_t * self._matrix[2][2], \
            sin_t * self._matrix[1][2] + cos_t * self._matrix[2][2]

        self._matrix[1][3], self._matrix[2][3] = \
            cos_t * self._matrix[1][3] - sin_t * self._matrix[2][3], \
            sin_t * self._matrix[1][3] + cos_t * self._matrix[2][3]

    def _rotate_around_y(self, cos_t, sin_t):
        """
        R = [[math.cos(radians), 0., math.sin(radians), 0.],
             [0., 1., 0., 0.],
             [-math.sin(radians), 0., math.cos(radians), 0.],
             [0., 0., 0., 1.]]
        A = R * A
        """
        self._matrix[0][0], self._matrix[2][0] = \
            cos_t * self._matrix[0][0] + sin_t * self._matrix[2][0], \
            -sin_t * self._matrix[0][0] + cos_t * self._matrix[2][0]

        self._matrix[0][1], self._matrix[2][1] = \
            cos_t * self._matrix[0][1] + sin_t * self._matrix[2][1], \
            -sin_t * self._matrix[0][1] + cos_t * self._matrix[2][1]

        self._matrix[0][2], self._matrix[2][2] = \
            cos_t * self._matrix[0][2] + sin_t * self._matrix[2][2], \
            -sin_t * self._matrix[0][2] + cos_t * self._matrix[2][2]

        self._matrix[0][3], self._matrix[2][3] = \
            cos_t * self._matrix[0][3] + sin_t * self._matrix[2][3], \
            -sin_t * self._matrix[0][3] + cos_t * self._matrix[2][3]

    def _rotate_around_z(self, cos_t, sin_t):
        """
        R = [[math.cos(radians), -math.sin(radians), 0., 0.],
             [math.sin(radians), math.cos(radians), 0., 0.],
             [0., 0., 1., 0.],
             [0., 0., 0., 1.]]
        A = R * A
        """
        self._matrix[0][0], self._matrix[1][0] = \
            cos_t * self._matrix[0][0] - sin_t * self._matrix[1][0], \
            sin_t * self._matrix[0][0] + cos_t * self._matrix[1][0]

        self._matrix[0][1], self._matrix[1][1] = \
            cos_t * self._matrix[0][1] - sin_t * self._matrix[1][1], \
            sin_t * self._matrix[0][1] + cos_t * self._matrix[1][1]

        self._matrix[0][2], self._matrix[1][2] = \
            cos_t * self._matrix[0][2] - sin_t * self._matrix[1][2], \
            sin_t * self._matrix[0][2] + cos_t * self._matrix[1][2]

        self._matrix[0][3], self._matrix[1][3] = \
            cos_t * self._matrix[0][3] - sin_t * self._matrix[1][3], \
            sin_t * self._matrix[0][3] + cos_t * self._matrix[1][3]


if __name__ == '__main__':
    mat = ModelView()
    print(mat.as_array)
    mat.rotate(around='x', degrees=-90.)
    print(mat.as_array)

