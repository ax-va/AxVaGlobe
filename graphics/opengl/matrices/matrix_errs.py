from pyglobe3d.graphics.opengl.opengl_errs import OpenGLError


class OpenGLMatrixError(OpenGLError):
    pass


class ZeroLengthVectorError(OpenGLMatrixError):
    def __init__(self, vector):
        self.message = f'The vector {vector} must not have zero length'


class ProjectionError(OpenGLMatrixError):
    pass


class EqualClippingPlanesError(ProjectionError):
    def __init__(self, plane1, plane2):
        self.message = f'The value ({plane2} - {plane1}) of clipping planes must be nonzero'
        ProjectionError.__init__(self, self.message)


