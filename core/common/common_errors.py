class CommonError(Exception):
    pass


class ConstantAttributeRewriteError(CommonError):
    def __init__(self, attribute_name):
        self.message = f'The attribute {attribute_name} is constant and cannot be rewritten'
        CommonError.__init__(self, self.message)
