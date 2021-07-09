import array as array_
import itertools


class OpenGLMatrix:
    def __init__(self):
        self._matrix = [[1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [0., 0., 0., 1.]]

    @property
    def array(self):
        return array_.array('f', (self._matrix[i][j] for j in range(4) for i in range(4)))

    @property
    def matrix(self):
        return self._matrix

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
    print(mt.array)
