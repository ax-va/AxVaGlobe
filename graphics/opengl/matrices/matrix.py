import array
import itertools
import math


class OpenGLMatrix:    
    def __init__(self, matrix=None):
        self._matrix = [[1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [0., 0., 0., 1.]]

        if matrix is not None:
            self._set_matrix(matrix)
        
        self._multiply_funcs = {
            'left': self._multiply_left, 
            'right': self._multiply_right, 
            'element-wise': self._multiply_element_wise,
        }
        
    @property
    def float32_array(self):
        """
        instance.float32_array returns the matrix instance._matrix in the form of the column-wise array,
        the entries of which are of the C type float
        """
        return array.array('f', (self._matrix[i][j] for j in range(4) for i in range(4)))

    @property
    def matrix(self):
        return self._matrix
    
    @matrix.setter
    def matrix(self, matrix):
        self._set_matrix(matrix)
            
    def multiply(self, other, way='left'):
        """
        instance.multiply(other) changes the matrix instance._matrix as A = B * A, and
        instance.multiply(other, way='right') changes that as A = A * B,
        where A, B, and * denote instance._matrix, other._matrix, and the matrix product
        referred to as the dot product, respectively.
        instance.multiply(other, way='element-wise') changes the matrix instance._matrix by
        the element-wise product of instance._matrix and other._matrix.
        """
        self._multiply_funcs[way](other)
     
    def set_entries(self, entries):
        """
        instance.set_entries(entries) sets the entries of the matrix instance._matrix 
        given by an iterable object containing iterable subobjects with a row index, 
        a column index, and a value. 
        For example, entries = [[0, 0, .25], [0, 1, .5]] sets
        instance._matrix[0][0] = .25 and instance._matrix[0][1] = .5.
        """
        for i, j, v in entries:
            self._matrix[i][j] = float(v)
    
    def set_identity(self):
        """
        instance.set_identity() sets the matrix instance._matrix to the identity matrix
        """
        for i, j in itertools.product(range(4), range(4)):
            self._matrix[i][j] = 0. if i != j else 1.
            
    def set_zeros(self):
        """
        instance.set_zeros() sets the matrix instance._matrix to zero entries
        """
        for i, j in itertools.product(range(4), range(4)):
            self._matrix[i][j] = 0.
            
    def transpose(self):
        """
        instance.transpose() transposes the matrix instance._matrix
        """
        for i in range(0, 3):
            for j in range(i + 1, 4):
                self._matrix[i][j], self._matrix[j][i] = self._matrix[j][i], self._matrix[i][j]
                
    def _multiply_element_wise(self, other):
        """
        instance._multiply_element_wise(other) changes the matrix instance._matrix by
        the element-wise product of instance._matrix and other._matrix
        """
        for i, j in itertools.product(range(4), range(4)):
            self._matrix[i][j] = self._matrix[i][j] * other.matrix[i][j]

    def _multiply_left(self, other):
        """
        instance._multiply_left(other) changes the matrix instance._matrix as A = B * A,
        where A, B, and * denote instance._matrix, other._matrix, and the matrix product
        referred to as the dot product, respectively
        """
        for j in range(4):
            self._matrix[0][j], self._matrix[1][j], self._matrix[2][j], self._matrix[3][j] = \
                math.fsum(other.matrix[0][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[1][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[2][k] * self._matrix[k][j] for k in range(4)), \
                math.fsum(other.matrix[3][k] * self._matrix[k][j] for k in range(4))

    def _multiply_right(self, other):
        """
        instance._multiply_right(other) changes the matrix instance._matrix as A = A * B,
        where A, B, and * denote instance._matrix, other._matrix, and the matrix product
        referred to as the dot product, respectively
        """
        for i in range(4):
            self._matrix[i][0], self._matrix[i][1], self._matrix[i][2], self._matrix[i][3] = \
                math.fsum(self._matrix[i][k] * other.matrix[k][0] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][1] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][2] for k in range(4)), \
                math.fsum(self._matrix[i][k] * other.matrix[k][3] for k in range(4))

    def _set_matrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self._matrix[i][j] = float(matrix[i][j])


if __name__ == '__main__':
    mt = OpenGLMatrix()
    print(mt.matrix)
    print(mt.float32_array)
