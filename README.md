# AxVaGlobe

## Project

**AxVaGlobe** is a project for creating globes using hexagon- and pentagon-like polygons, with support for navigation on them. The project targets multiple programming languages, prioritizing Python and Rust.

## Geometrу

A ***surface unit*** is a hexagon-like polygon built from six triangles or a pentagon-like polygon built from five triangles, all sharing one vertex of the icosahedron in the second case. The surface units approximate the sphere or a portion of it. 

<img src="https://user-images.githubusercontent.com/85578981/127783633-d5dc5e1b-57e8-426b-ae48-cb57790e715e.png" data-canonical-src="https://user-images.githubusercontent.com/85578981/127783633-d5dc5e1b-57e8-426b-ae48-cb57790e715e.png" width="700"/>

By changing the radius of the sphere at the surface units, you can create arbitrary 3D surfaces on the sphere. 

## Navigation

Each surface unit at the logical level knows its nearest neighbors, which is implemented algorithmically rather than through storage. As a result, discrete movement on the surface is possible.
