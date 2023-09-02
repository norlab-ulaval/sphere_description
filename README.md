# sphere_description
URDF files for the Sphere sensor platform project


## How to sync urdf with the Onshape project

Follow [this](https://onshape-to-robot.readthedocs.io/en/latest/installation.html#api-key) guide, installing `onshape-to-robot` and setting Onshape API keys.
Then, navigate to the  **sphere_description** package and run
```bash
cd onshape_to_urdf
onshape-to-robot .
```
This synchronizes the Onshape project with the robot model, installs the meshes in appropriate locations and cleans the temporary files.
