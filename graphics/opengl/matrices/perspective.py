from pyglobe3d.graphics.opengl.matrices.matrix_errs import EqualClippingPlanesError
from pyglobe3d.graphics.opengl.matrices.projection import Projection


class Perspective(Projection):
    def __init__(self, right, top, near, far, left=None, bottom=None):
        Projection.__init__(self, left, right, bottom, top, near, far)
        self._set_matrix_entries()

    def _set_matrix_entries(self):
        """
        P_persp = [[ 2. * near / (right - left), 0., (right + left) / (right - left), 0.],
                   [0., 2. * near / (top - bottom), (top + bottom) / (top - bottom), 0.],
                   [0., 0., -(far + near) / (far - near), -2. * far * near / (far - near)],
                   [0., 0., -1., 0.]]
        with v = P_persp * v
        """
        right_minus_left = self._right - self._left
        top_minus_bottom = self._top - self._bottom
        far_minus_near = self._far - self._near
        if right_minus_left == 0:
            raise EqualClippingPlanesError('left', 'right')
        if top_minus_bottom == 0:
            raise EqualClippingPlanesError('bottom', 'top')
        if far_minus_near == 0:
            raise EqualClippingPlanesError('near', 'far')
        self._matrix[0][0] = 2. * self._near / right_minus_left
        self._matrix[0][2] = (self._right + self._left) / right_minus_left
        self._matrix[1][1] = 2. * self._near / top_minus_bottom
        self._matrix[1][2] = (self._top + self._bottom) / top_minus_bottom
        self._matrix[2][2] = (self._far + self._near)/ far_minus_near
        self._matrix[2][3] = -2. * self._far * self._near / far_minus_near
        self._matrix[3][2] = -1.
        self._matrix[3][3] = 0.
