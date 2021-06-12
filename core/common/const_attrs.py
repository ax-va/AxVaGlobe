class ConstantAttributes:
    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value
        else:
            raise AttributeError('The attribute is constant and cannot be rewritten')