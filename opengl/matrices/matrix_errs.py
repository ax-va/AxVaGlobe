from pyglobe3d.opengl.opengl_errs import OpenGLError


class MatrixError(OpenGLError):
    pass


class ProjectionError(MatrixError):
    pass


class EqualClippingPlanesError(ProjectionError):
    def __init__(self, plane1, plane2):
        self.message = f'The value ({plane2} - {plane1}) of clipping planes must be nonzero'
        ProjectionError.__init__(self, self.message)
