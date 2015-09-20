# surface_searchlight
An implementation of surface-based decoding

***

This is (going to be) an implementation of cortical-surface based searchlight decoding, similar to what was produced in the [Haynes Lab](https://sites.google.com/site/hayneslab/projects/surface-based-decoding). 

I have previously written a MATLAB implementation, but it ran prohibitively slowly so I never used it for anything. This project will be implemented in python (with decoding handled by scikit-learn) and I there are a few things that will help this run faster. 

### To definitely do

* [x] Implement a symmetric matrix class based on NumPy
* [ ] Floyd-Warshall algorithm to compute all-node shortest paths
* [ ] Read in FreeSurfer meshes
* [ ] Find voxel coverage of the triangular prisms that define greymatter volume
* [ ] Find mapping between the greymatter cylinder centered at each node and voxels
* [ ] Classification for voxels sets

### To maybe do

* [ ] Parellelize classification
* [ ] Space-efficient matrix class storing upper triangle only
* [ ] Faster shortest path code using repeated calls to Dijkstra's algorithm with Fibonacci heap: O(V(E + V log V)) instead of O(V^3)
