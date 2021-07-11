import array
import itertools
import math

from abc import ABCMeta

from pyglobe3d.opengl.matrices.matrix_errs import NotAOpenGLMatrix


class OpenGLMatrix(metaclass=ABCMeta):
    def __init__(self):
        self._matrix = [[1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [0., 0., 0., 1.]]

    @property
    def float32_array(self):
        return array.array('f', (self._matrix[i][j] for j in range(4) for i in range(4)))

    @property
    def matrix(self):
        return self._matrix
    
    def dot(self, other, side='left'):
        """
        mat.dot(other) changes 'mat._matrix' as A = B * A or as A = A * B if side = 'right',
        where mat._matrix is A, other._matrix is B, and * is matrix multiplication
        """
        if side == 'left':
            self.left_dot(other)
        elif side == 'right':
            self.right_dot(other)
        else:
            pass

    def left_dot(self, other):
        """
        mat.left_dot(other) changes mat._matrix as A = B * A,
        where mat._matrix is A, other._matrix is B, and * is matrix multiplication
        """
        if other is None or self.__class__ == other.__class__:
            raise NotAOpenGLMatrix(other, self.__class__.__name__)

        for j in range(4):
            self._matrix[0][j], self._matrix[1][j], self._matrix[2][j], self._matrix[3][j] = \
                math.fsum(other.matrix[0][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[1][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[2][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[3][k] * self._matrix[k][j] for k in range(4))

    def right_dot(self, other):
        """
        mat.right_dot(other) changes mat._matrix as A = A * B,
        where mat._matrix is A, other._matrix is B, and * is matrix multiplication
        """
        if other is None or self.__class__ == other.__class__:
            raise NotAOpenGLMatrix(other, self.__class__.__name__)

        for i in range(4):
            self._matrix[i][0], self._matrix[i][1], self._matrix[i][2], self._matrix[i][3] = \
                math.fsum(self._matrix[i][k] * other.matrix[k][0] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][1] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][2] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][3] for k in range(4))

    def set_identity(self):
        for i, j in itertools.product(range(4), range(4)):
            self._matrix[i][j] = 0. if i != j else 1.
            
    def transpose(self):
        for i in range(0, 3):
            for j in range(i + 1, 4):
                self._matrix[i][j], self._matrix[j][i] = self._matrix[j][i], self._matrix[i][j]


if __name__ == '__main__':
    mt = OpenGLMatrix()
    print(mt.matrix)
    print(mt.float32_array)
