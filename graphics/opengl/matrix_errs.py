from pyglobe3d.graphics.graphics_errs import GraphicsError


class OpenGLMatrixError(GraphicsError):
    pass


class ZeroNormError(OpenGLMatrixError):
    def __init__(self, vector):
        self.message = f'The vector {vector} must not have zero lenght'


class ProjectionError(OpenGLMatrixError):
    pass


class EqualClippingPlanesError(ProjectionError):
    def __init__(self, plane1, plane2):
        self.message = f'The value ({plane2} - {plane1}) of clipping planes must be nonzero'
        ProjectionError.__init__(self, self.message)


