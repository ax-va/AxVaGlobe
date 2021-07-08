from pyglobe3d.opengl.opengl_errs import OpenGLError


class MatrixError(OpenGLError):
    pass


class OrthographicError(MatrixError):
    pass


class ClippingPlanesError(OrthographicError):
    def __init__(self, value1, value2):
        self.message = f'The value of ({value2} - {value1}) of clipping planes must be nonzero'
        OrthographicError.__init__(self, self.message)
