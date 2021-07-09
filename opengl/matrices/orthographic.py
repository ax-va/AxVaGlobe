from pyglobe3d.opengl.matrices.matrix_errs import EqualClippingPlanesError
from pyglobe3d.opengl.matrices.projection import Projection


class Orthographic(Projection):
    def __init__(self, right, top, near, far, left=None, bottom=None):
        Projection.__init__(self, left, right, bottom, top, near, far)
        self._set_matrix_entries()

    def _set_matrix_entries(self):
        """
        [[ 2. / (right - left), 0., 0., -(right + left) / (right - left)],
         [0., 2. / (top - bottom), 0., -(top + bottom) / (top - bottom)],
         [0., 0., -2. / (far - near), -(far + near) / (far - near)],
         [0., 0., 0., 1.]]
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
        self._matrix[0, 0] = 2. / right_minus_left
        self._matrix[0, 3] = -(self._right + self._left) / right_minus_left
        self._matrix[1, 1] = 2. / top_minus_bottom
        self._matrix[1, 3] = -(self._top + self._bottom) / top_minus_bottom
        self._matrix[2, 2] = -2. / far_minus_near
        self._matrix[2, 3] = -(self._far + self._near) / far_minus_near
