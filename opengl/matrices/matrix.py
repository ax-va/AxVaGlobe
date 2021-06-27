import array
import itertools


class Matrix:
    def __init__(self):
        self._matrix = [[1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [0., 0., 0., 1.]]

    @property
    def as_array(self):
        return array.array('f', (self._matrix[i][j] for i in range(4) for j in range(4)))

    @property
    def matrix(self):
        return self._matrix

    def set_identity(self):
        for i, j in itertools.product(range(4), range(4)):
            self._matrix[i][j] = 0. if i != j else 1.


if __name__ == '__main__':
    mt = Matrix()
    print(mt.matrix)
    print(mt.as_array)
