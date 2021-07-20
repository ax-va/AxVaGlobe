import math

from pyglobe3d.graphics.opengl.matrices.matrix_errs import EqualClippingPlanesError
from pyglobe3d.graphics.opengl.matrices.projection import Projection


class Perspective(Projection):
    def __init__(self, right, top, near, far, left=None, bottom=None):
        """
        Initializes a Perspective instance by instance._matrix equal to P_persp, where
        P_persp = [[ 2. * near / (right - left), 0., (right + left) / (right - left), 0.],
                   [0., 2. * near / (top - bottom), (top + bottom) / (top - bottom), 0.],
                   [0., 0., -(far + near) / (far - near), -2. * far * near / (far - near)],
                   [0., 0., -1., 0.]]

        :param right: right clipping plane from the origin
        :param top: top clipping plane from the origin
        :param near: distance of the near clipping plane from the eye in the origin
        :param far: distance of the far clipping plane from the eye in the origin
        :param left: left clipping plane from the origin
        :param bottom: bottom clipping plane from the origin
        """
        Projection.__init__(self, left, right, bottom, top, near, far)
        self._set_matrix_entries()

    @classmethod
    def create_perspective(cls, fov_y, aspect, near, far):
        """
        Creates a Perspective instance with instance._matrix equal to P_persp, where
        P_persp = [[1. / aspect, 0., 0., 0.],
                   [0., 1. / math.tan(math.radians(fov_y) / 2), 0., 0.],
                   [0., 0., -(far + near) / (far - near), -2. * far * near / (far - near)],
                   [0., 0., -1., 0.]

        :param fov_y: field of view in y, the vertical angle (in degrees) of viewable space
        :param aspect: aspect ratio, the ratio width/height of the near (and also far) clipping plane
        :param near: distance of the near clipping plane from the eye in the origin
        :param far: distance of the far clipping plane from the eye in the origin
        :return: Perspective instance
        """
        top = near * math.tan(math.radians(fov_y) / 2)
        right = aspect * top
        return cls(right, top, near, far)

    def _set_matrix_entries(self):
        """
        P_persp = [[ 2. * near / (right - left), 0., (right + left) / (right - left), 0.],
                   [0., 2. * near / (top - bottom), (top + bottom) / (top - bottom), 0.],
                   [0., 0., -(far + near) / (far - near), -2. * far * near / (far - near)],
                   [0., 0., -1., 0.]]
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
