import math

from pyglobe3d.graphics.opengl_matrices.matrix_errs import EqualClippingPlanesError
from pyglobe3d.graphics.opengl_matrices.projection import Projection


class Perspective(Projection):
    """
    Describes an OpenGL perspective-projection matrix
    """
    def __init__(self, right, top, near, far, left=None, bottom=None):
        """
        Initializes a Perspective instance by instance._matrix equal to P_persp, where
        P_persp = [[ 2. * near / (right - left), 0., (right + left) / (right - left), 0.],
                   [0., 2. * near / (top - bottom), (top + bottom) / (top - bottom), 0.],
                   [0., 0., -(far + near) / (far - near), -2. * far * near / (far - near)],
                   [0., 0., -1., 0.]]

        :param right: displacement of the right clipping plane from the origin
        :param top: displacement of the top clipping plane from the origin
        :param near: distance of the near clipping plane from the eye in the origin
        :param far: distance of the far clipping plane from the eye in the origin
        :param left: displacement of the left clipping plane from the origin
        :param bottom: displacement of the bottom clipping plane from the origin
        """
        Projection.__init__(self, left, right, bottom, top, near, far)
        self._set_matrix_entries()

    @classmethod
    def create_perspective(cls, fovy, aspect, near, far):
        """
        Creates a Perspective instance with instance._matrix equal to P_persp, where
        P_persp = [[1. / aspect, 0., 0., 0.],
                   [0., 1. / math.tan(math.radians(fovy) / 2), 0., 0.],
                   [0., 0., -(far + near) / (far - near), -2. * far * near / (far - near)],
                   [0., 0., -1., 0.]

        :param fovy: field of view in y, that is, the vertical angle (in degrees) of viewable space
        :param aspect: aspect ratio, that is, the ratio width/height of the near (and also far) clipping plane
        :param near: distance of the near clipping plane from the eye in the origin
        :param far: distance of the far clipping plane from the eye in the origin
        :return: Perspective instance
        """
        top = near * math.tan(math.radians(fovy) / 2)
        right = aspect * top
        return cls(right, top, near, far)

    def _set_matrix_entries(self):
        """
        Sets the entries of instance._matrix according to 
        P_persp = [[ 2. * near / (right - left), 0., (right + left) / (right - left), 0.],
                   [0., 2. * near / (top - bottom), (top + bottom) / (top - bottom), 0.],
                   [0., 0., -(far + near) / (far - near), -2. * far * near / (far - near)],
                   [0., 0., -1., 0.]]
        """
        try:
            self._matrix[0][0] = 2. * self._near / self._right_minus_left
            self._matrix[0][2] = (self._right + self._left) / self._right_minus_left
        except ZeroDivisionError:
            raise EqualClippingPlanesError('left', 'right')
        try:
            self._matrix[1][1] = 2. * self._near / self._top_minus_bottom
            self._matrix[1][2] = (self._top + self._bottom) / self._top_minus_bottom
        except ZeroDivisionError:
            raise EqualClippingPlanesError('bottom', 'top')
        try:
            self._matrix[2][2] = (self._far + self._near)/ self._far_minus_near
            self._matrix[2][3] = -2. * self._far * self._near / self._far_minus_near
        except ZeroDivisionError:
            raise EqualClippingPlanesError('near', 'far')
        self._matrix[3][2] = -1.
        self._matrix[3][3] = 0.


if __name__ == '__main__':
    p = Perspective(right=1, top=1, near=1, far=2)
    help(p.__init__)
    help(Perspective.create_perspective)
