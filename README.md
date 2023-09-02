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

<img width="389" alt="image" src="https://github.com/norlab-ulaval/sphere_description/assets/47394922/5211a38f-82ec-4070-b0a7-fd94016297a7">
