from abc import ABCMeta

from pyglobe3d.graphics.opengl.matrix import Matrix


class Projection(Matrix, metaclass=ABCMeta):
    def __init__(self, left, right, bottom, top, near, far):
        Matrix.__init__(self)
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
