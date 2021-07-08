from pyglobe3d.opengl.matrices.matrix import OpenGLMatrix
from pyglobe3d.opengl.matrices.matrix_errs import EqualClippingPlanesError

class OpenGLOrthographic(OpenGLMatrix):
    def __init__(self, right, top, near, far, left=None, bottom=None):
        OpenGLMatrix.__init__(self)
        self._set_attributes(left, right, top, bottom, near, far)

    def _set_attributes(self, left, right, top, bottom, near, far):
        self._right = right
        self._left = left if left is not None else -self._right
        self._top = top
        self._bottom = bottom if bottom is not None else -self._top
        self._near = near
        self._far = far
        self._set_matrix_entries()

    def _set_matrix_entries(self):
        """
        [[ 2. / (right - left), 0., 0., -(right + left) / (right - left)],
         [0., 2. / (top - bottom), 0., -(top + bottom) / (top - bottom)],
         [0., 0., 2. / (far - near), -(far + near) / (far - near)],
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
        self._matrix[2, 2] = 2. / far_minus_near
        self._matrix[2, 3] = -(self._far + self._near) / far_minus_near
