from abc import ABCMeta

from pyglobe3d.graphics.opengl_matrices.matrix import OpenGLMatrix


class Projection(OpenGLMatrix, metaclass=ABCMeta):
    def __init__(self, left, right, bottom, top, near, far):
        OpenGLMatrix.__init__(self)
        self._set_attributes(left, right, bottom, top, near, far)

    def _set_attributes(self, left, right, bottom, top, near, far):
        self._right = right
        self._left = left if left is not None else -self._right
        self._top = top
        self._bottom = bottom if bottom is not None else -self._top
        self._near = near
        self._far = far
        self._right_minus_left = self._right - self._left
        self._top_minus_bottom = self._top - self._bottom
        self._far_minus_near = self._far - self._near
        if self._right_minus_left == 0:
            raise EqualClippingPlanesError('left', 'right')
        if self._top_minus_bottom == 0:
            raise EqualClippingPlanesError('bottom', 'top')
        if self._far_minus_near == 0:
            raise EqualClippingPlanesError('near', 'far')
