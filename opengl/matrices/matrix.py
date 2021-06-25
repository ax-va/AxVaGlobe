import array
import numpy as np

RAD_DIV_DEG = 1.745_329_251_994_330e-2


class MatrixGL:
    def __init__(self):
        self._matrix = np.identity(4)

    @property
    def entries(self):
        return array.array('f', self._matrix.flatten(order='F'))

    @property
    def matrix(self):
        return self._matrix

    def set_identity(self):
        self._matrix[:, :] = 0
        self._matrix[0, 0] = self._matrix[1, 1] = self._matrix[2, 2] = self._matrix[3, 3] = 1


if __name__ == '__main__':
    mt = MatrixGL()
    print(mt.entries)
