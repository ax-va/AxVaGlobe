from pyglobe3d.opengl.opengl_errs import OpenGLError


class MatrixError(OpenGLError):
    pass


class OrthographicError(MatrixError):
    pass


class RightMinusLeftValueError(OrthographicError):
    def __init__(self):
        self.message = 'The value of (right - left) of clipping planes is zero'
        OrthographicError.__init__(self, self.message)


class TopMinusBottomValueError(OrthographicError):
    def __init__(self):
        self.message = 'The value of (top - bottom) of clipping planes is zero'
        OrthographicError.__init__(self, self.message)


class FarMinusNearValueError(OrthographicError):
    def __init__(self):
        self.message = 'The value of (far - near) of clipping planes is zero'
        OrthographicError.__init__(self, self.message)