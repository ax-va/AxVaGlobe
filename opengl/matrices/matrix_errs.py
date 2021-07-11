from pyglobe3d.opengl.opengl_errs import OpenGLError


class OpenGLMatrixError(OpenGLError):
    pass


class NotAOpenGLMatrix(OpenGLMatrixError):
    def __init__(self, instance, cls):
        self.message = f'The instance {instance} is not of the class {cls}'
        OpenGLMatrixError.__init__(self, self.message)


class ProjectionError(OpenGLMatrixError):
    pass


class EqualClippingPlanesError(ProjectionError):
    def __init__(self, plane1, plane2):
        self.message = f'The value ({plane2} - {plane1}) of clipping planes must be nonzero'
        ProjectionError.__init__(self, self.message)


