from pyglobe3d.core.common.common_errs import ConstantAttributeRewriteError


class ConstantAttributes:
    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value
        else:
            raise ConstantAttributeRewriteError(attribute_name=key)