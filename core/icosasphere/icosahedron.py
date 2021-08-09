import math


class Icosahedron:
    def __init__(self, radius: float = 1.0):
        self._radius = radius
        self._cos_theta = math.sqrt(2. / (5. + math.sqrt(5.)))
        self._theta = math.acos(self._cos_theta)  # the first angle of rotation in radians from the z-axis
        self._sin_theta = math.sin(self._theta)
        self._phi = 0.4 * math.pi  # 72 degrees in radians

    @property
    def index_array(self):
        return [[0, 1, 2],  # vertex indices [index0, index1, index2] of triangle 0
                [0, 2, 3],  # triangle 1
                [0, 3, 4],  # triangle 2
                [0, 4, 5],  # triangle 3
                [0, 5, 1],  # triangle 4
                [1, 6, 7],  # triangle 5
                [1, 7, 2],  # triangle 6
                [2, 7, 8],  # triangle 7
                [2, 8, 3],  # triangle 8
                [3, 8, 9],  # triangle 9
                [3, 9, 4],  # triangle 10
                [4, 9, 10],  # triangle 11
                [4, 10, 5],  # triangle 12
                [5, 10, 6],  # triangle 13
                [5, 6, 1],  # triangle 14
                [6, 11, 7],  # triangle 15
                [7, 11, 8],  # triangle 16
                [8, 11, 9],  # triangle 17
                [9, 11, 10],  # triangle 18
                [10, 11, 6]]  # triangle 19

    @property
    def theta(self):
        return self._theta

    @property
    def vertex_array(self):
        """
        x = r * math.sin(theta) * math.cos(phi)
        y = r * math.sin(theta) * math.sin(phi)
        z = r * math.cos(theta)
        """
        r = self._radius
        ph = self._phi
        r_cos_th = r * self._cos_theta
        r_sin_th = r * self._sin_theta
        return [[0., 0., r],  # [x, y, z] of vertex 0
                [r_sin_th, 0., r_cos_th],  # vertex 1
                [r_sin_th * math.cos(ph), r_sin_th * math.sin(ph), r_cos_th],  # vertex 2
                [r_sin_th * math.cos(2. * ph), r_sin_th * math.sin(2. * ph), r_cos_th],  # vertex 3
                [r_sin_th * math.cos(3. * ph), r_sin_th * math.sin(3. * ph), r_cos_th],  # vertex 3
                [r_sin_th * math.cos(4. * ph), r_sin_th * math.sin(4. * ph), r_cos_th],  # vertex 4
                [r_sin_th * math.cos(5. * ph), r_sin_th * math.sin(5. * ph), r_cos_th],  # vertex 5
                [r_sin_th * math.cos(-0.5 * ph), r_sin_th * math.sin(-0.5 * ph), -r_cos_th],  # vertex 6
                [r_sin_th * math.cos(0.5 * ph), r_sin_th * math.sin(0.5 * ph), -r_cos_th],  # vertex 7
                [r_sin_th * math.cos(1.5 * ph), 0., -r_cos_th],  # vertex 8
                [r_sin_th * math.cos(2.5 * ph), r_sin_th * math.sin(2.5 * ph), -r_cos_th],  # vertex 9
                [r_sin_th * math.cos(3.5 * ph), r_sin_th * math.sin(3.5 * ph), -r_cos_th],  # vertex 10
                [0., 0., -r]]  # vertex 11


if __name__ == "__main__":
    ics = Icosahedron()
    print(ics.vertex_array)
    print(ics.index_array)
