from abc import ABCMeta

from pyglobe3d.opengl.matrices.matrix import OpenGLMatrix


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
