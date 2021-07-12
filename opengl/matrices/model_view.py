import math

from pyglobe3d.opengl.matrices.matrix import OpenGLMatrix


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
        if len(around) == 1:
            self._rotate_funcs[around](cos_t, sin_t)
        else:
            self._rotate_around_axis(around, cos_t, sin_t)
            
    def _rotate_around_axis(self, axis, cos_t, sin_t):
        pass

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
