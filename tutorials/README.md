# Tutorials for the IR Lab in WiSe 2023

This directory contains the tutorials that we will use in the IR lab in WiSe 2023.

We recommend that you run this tutorials using dev containers with Docker (please find a suitable installation instruction [here](https://code.visualstudio.com/docs/devcontainers/containers)).
A dev container allows you to directly work in the prepared Docker container so that you do not have to install the dependencies (which can sometimes be a bit tricky) on your own. If you do not have Docker installed (we highly recommend that you have a look into Docker), you can run everything within Google Colab.

To run the tutorials on your machine, please:

- Install [VS Code](https://code.visualstudio.com/download) and [Docker](https://docs.docker.com/engine/install/) on your machine
- Clone this repository: `git clone ...`
- Open this directory with VS Code (it should ask you to open the repository in a dev container)


### Content

- [tutorial-01-ir-datasets.ipynb](Tutorial 1: Topics, Documents, and Relevance Judgments) (Open in [tutorial-01-ir-datasets.ipynb](Github) or [Google Colab](https://colab.research.google.com/drive/1oWh9nFT6ZsGfZLRDG1QrwUgyMIzLbw_H?usp=sharing))

### Changes to the Dev-Container

We are happy if you find ways to improve the dev container. You can adjust the image as you like, if you think your changes might be helpful to others, please let us know so that we can adjust the published image.

Instructions to build and publish the image are:

```
docker build -t webis/ir-lab-wise-2023:0.0.1 .
docker push webis/ir-lab-wise-2023:0.0.1
```

