import array as arr


class MatrixGL:
    def __init__(self):
        self._matrix = [[1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [0., 0., 0., 1.]]

    @property
    def array(self):
        return arr.array('f', (self._matrix[i][j] for i in range(4) for j in range(4)))

    @property
    def matrix(self):
        return self._matrix

    def set_identity(self):
        for i in range(4):
            for j in range(4):
                self._matrix[i][j] = 0. if i != j else 1.


if __name__ == '__main__':
    mt = MatrixGL()
    print(mt.matrix)
    print(mt.as_array)
