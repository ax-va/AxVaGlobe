import array

RAD_DIV_DEG = 1.745_329_251_994_330e-2


class MatrixGL:
    def __init__(self):
        self._matrix = [[1., 0., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 1., 0.],
                        [0., 0., 0., 1.]]

    @property
    def c_array(self):
        return array.array('f', self.column_concat)

    @property
    def column_concat(self):
        concat = [None] * 16
        concat[:4] = self._matrix[0]
        concat[4:8] = self._matrix[1]
        concat[8:12] = self._matrix[2]
        concat[12:] = self._matrix[3]
        return concat

    def set_identity(self):
        for i in range(4):
            for j in range(4):
                self._matrix[i][j] = 0. if i != j else 1.


if __name__ == '__main__':
    mt = MatrixGL()
    print(mt.column_concat)
    print(mt.c_array)
    print(RAD_DIV_DEG)
