class PyGlobe3DWarning:
    def __init__(self, message):
        self._message = message
        print('Warning:', message)