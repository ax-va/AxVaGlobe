from pyglobe3d.opengl.opengl_errs import OpenGLError


class MatrixError(OpenGLError):
    pass


class OrthographicError(MatrixError):
    pass


class EqualClippingPlanesError(OrthographicError):
    def __init__(self, plane1, plane2):
        self.message = f'The value of ({plane2} - {plane1}) of clipping planes must be nonzero'
        OrthographicError.__init__(self, self.message)
