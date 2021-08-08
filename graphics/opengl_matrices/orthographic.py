from pyglobe3d.graphics.opengl_matrices.matrix_errs import EqualClippingPlanesError
from pyglobe3d.graphics.opengl_matrices.projection import Projection


class Orthographic(Projection):
    def __init__(self, right, top, near, far, left=None, bottom=None):
        Projection.__init__(self, left, right, bottom, top, near, far)
        self._set_matrix_entries()

    def _set_matrix_entries(self):
        """
        P_ortho = [[ 2. / (right - left), 0., 0., -(right + left) / (right - left)],
                   [0., 2. / (top - bottom), 0., -(top + bottom) / (top - bottom)],
                   [0., 0., -2. / (far - near), -(far + near) / (far - near)],
                   [0., 0., 0., 1.]]
        """
        try:
            self._matrix[0][0] = 2. / self._right_minus_left
            self._matrix[0][3] = -(self._right + self._left) / self._right_minus_left
        except ZeroDivisionError:
            raise EqualClippingPlanesError('left', 'right')
        try:
            self._matrix[1][1] = 2. / self._top_minus_bottom
            self._matrix[1][3] = -(self._top + self._bottom) / self._top_minus_bottom
        except ZeroDivisionError:
            raise EqualClippingPlanesError('bottom', 'top')
        try:
            self._matrix[2][2] = -2. / self._far_minus_near
            self._matrix[2][3] = -(self._far + self._near) / self._far_minus_near
        except ZeroDivisionError:
            raise EqualClippingPlanesError('near', 'far')
