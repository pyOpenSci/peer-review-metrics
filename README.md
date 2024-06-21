# pyOpenSci peer review metrics 


This is a dashboard created using mystmd [![Made with MyST](https://img.shields.io/badge/made%20with-myst-orange)](https://myst.tools). Myst-md is a community developed 
tool that makes it easier for scientists to create fully reproducible (and interactive)
workflows and reports that are easily shared. 

## How to use 

To work with this repository do the following:

First, create an fresh environment.

mamba create -n pyos-myst python=3.11
mamba activate pyos-myst 

# Install node
mamba install -c conda-forge 'nodejs>=20,<21'
# install myst 
mamba install mystmd -c conda-forge

Run `myst` - to create a live server

myst build --execute to execute code


## When i tried to use md files to executive code (which is preferred) it couldn't find the kernel 
🪐 Jupyter server did not start
Unable to instantiate connection to Jupyter Server 

If we use juyter then we want to ensure 

jupyterlab_myst is installed to be able to use eval statements

`myst start --execute`
to run and execute code. 


To run - jupyterlab_myst
## Environment 

use the environment.yml file 

`>> myst `

you will get:

```
Welcome to the MyST Markdown CLI!! 🎉 🚀

myst init walks you through creating a myst.yml file.

You can use myst to:

 - create interactive websites from markdown and Jupyter Notebooks 📈
 - build & export professional PDFs and Word documents 📄

Learn more about this CLI and MyST Markdown at: https://mystmd.org


✅ Project already initialized with config file: myst.yml
✅ Site already initialized with config file: myst.yml

? Would you like to run myst start now? (Y/n) y
```


```
📖 Built README.md in 32 ms.
📖 Built 03-leah.ipynb in 32 ms.
📚 Built 4 pages for project in 147 ms.


        ✨✨✨  Starting Book Theme  ✨✨✨



🔌 Server started on port 3000!  🥳 🎉


        👉  http://localhost:3000  👈
```
