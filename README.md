# PyGlobe3D
PyGlobe3D is a free open-source logical-graphical Python library for creating globes by hexagon-like polygons.

A surface consists mainly of hexagon-like polygons that are six triangles and also of twelve additional pentagon-like polygons that are five triangles and are lying only in the vertices of an icosahedron. They approximate a sphere or any part of the sphere. 

<img src="https://user-images.githubusercontent.com/85578981/127783633-d5dc5e1b-57e8-426b-ae48-cb57790e715e.png" data-canonical-src="https://user-images.githubusercontent.com/85578981/127783633-d5dc5e1b-57e8-426b-ae48-cb57790e715e.png" width="700"/>

Changing the radius of the sphere for any surface unit can create arbitrary 3D surfaces on the sphere. The logical component is that each surface unit knows its nearest neighbors that is implemented algorithmically, not by storage. Due to that, discrete movement on the surface can be realized.

© 2021-2022 Alexander Vasiliev
