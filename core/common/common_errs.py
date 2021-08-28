from pyglobe3d.core.core_errs import CoreError


class CommonError(CoreError):
    pass


class ConstantAttributeRewriteError(CommonError):
    def __init__(self, attribute_name):
        self.message = f'The attribute {attribute_name!r} is constant and cannot be rewritten'
        CommonError.__init__(self, self.message)


class InvalidArgumentValueError(CommonError):
    def __init__(self, argument_name, argument_value):
        self.message = f'The argument value {argument_value} of {argument_name!r} is invalid'
        CommonError.__init__(self, self.message)
