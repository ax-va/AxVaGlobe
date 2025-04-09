# NavGlobe

## What is NavGlobe?

**NavGlobe** is a graphical-logical library for creating globes by hexagon-or-pentagon-like polygons and for navigating on them.

## Why graphical?

A *surface unit* is a hexagon-like polygon consisting of six triangles or a pentagon-like polygon consisting of five triangles that share one vertex of the icosahedron. The surface units approximate the sphere or some part of the sphere. 

<img src="https://user-images.githubusercontent.com/85578981/127783633-d5dc5e1b-57e8-426b-ae48-cb57790e715e.png" data-canonical-src="https://user-images.githubusercontent.com/85578981/127783633-d5dc5e1b-57e8-426b-ae48-cb57790e715e.png" width="700"/>

Changing the radius of the sphere for the surface units can create arbitrary 3D surfaces on the sphere. 

## Why logical?

The logical component is that each surface unit knows its nearest neighbors that is implemented algorithmically, not by storage. Due to that, discrete movement on the surface is possible.

© 2021–2025 Alexander Vasiliev
