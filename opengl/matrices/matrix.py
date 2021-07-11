import array
import itertools
import math

from abc import ABCMeta

from pyglobe3d.opengl.matrices.matrix_errs import NotAOpenGLMatrixError


class OpenGLMatrix(metaclass=ABCMeta):
    def __init__(self):
        self._matrix = [[1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [0., 0., 0., 1.]]
        self._multiply_functions = (self.multiply_left, self.multiply_right)
        
    @property
    def float32_array(self):
        """
        instance.float32_array returns the matrix instance._matrix as the column wise array,
        the entries of which are of the C type float
        """
        return array.array('f', (self._matrix[i][j] for j in range(4) for i in range(4)))

    @property
    def matrix(self):
        return self._matrix
    
    def multiply(self, other, right=False):
        """
        instance.mutliply(other) changes the matrix instance._matrix as A = B * A, and
        instance.mutliply(other, right=True) changes the matrix instance._matrix as A = A * B,
        where A, B, and * denote instance._matrix, other._matrix, and matrix multiplication
        referred to as dot, respectively
        """
        self._multiply_functions[right](other)

    def multiply_left(self, other):
        """
        instance.mutliply_left(other) changes the matrix instance._matrix as A = B * A,
        where A, B, and * denote instance._matrix, other._matrix, and matrix multiplication
        referred to as dot, respectively
        """
        if other is None or self.__class__ != other.__class__:
            raise NotAOpenGLMatrixError(other, self.__class__.__name__)
        for j in range(4):
            self._matrix[0][j], self._matrix[1][j], self._matrix[2][j], self._matrix[3][j] = \
                math.fsum(other.matrix[0][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[1][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[2][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[3][k] * self._matrix[k][j] for k in range(4))

    def multiply_right(self, other):
        """
        instance.mutliply_right(other) changes the matrix instance._matrix as A = A * B,
        where A, B, and * denote instance._matrix, other._matrix, and matrix multiplication
        referred to as dot, respectively
        """
        if other is None or self.__class__ != other.__class__:
            raise NotAOpenGLMatrixError(other, self.__class__.__name__)
        for i in range(4):
            self._matrix[i][0], self._matrix[i][1], self._matrix[i][2], self._matrix[i][3] = \
                math.fsum(self._matrix[i][k] * other.matrix[k][0] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][1] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][2] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][3] for k in range(4))

    def set_identity(self):
        """
        instance.set_indentity() sets the matrix instance._matrix to the identity matrix
        """
        for i, j in itertools.product(range(4), range(4)):
            self._matrix[i][j] = 0. if i != j else 1.
            
    def transpose(self):
        """
        instance.transpose() transposes the matrix instance._matrix
        """
        for i in range(0, 3):
            for j in range(i + 1, 4):
                self._matrix[i][j], self._matrix[j][i] = self._matrix[j][i], self._matrix[i][j]


if __name__ == '__main__':
    mt = OpenGLMatrix()
    print(mt.matrix)
    print(mt.float32_array)
