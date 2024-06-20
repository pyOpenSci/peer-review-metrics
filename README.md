# MyST Quickstart

[![Made with MyST](https://img.shields.io/badge/made%20with-myst-orange)](https://myst.tools)

This repository contains the files used in the [quickstart guide](https://myst.tools/docs/mystjs/quickstart), and can be used to follow that guide, before trying MyST with your own content.

> **Note** This is **not** a good example of an actual myst project! The repositories purpose is to be a simple markdown + notebook repository that can be transformed throughout a tutorial.

The goals of the [quickstart guide](https://myst.tools/docs/mystjs/quickstart) are:

1. Create a `myst` site, using the standard template
2. Improve the frontmatter, to add authors, affiliations and other metadata
3. Export the paper as a PDF, Word document, and LaTeX files
4. Integrate a Jupyter Notebook output into our paper, to improve reproducibility
5. Publish a website of with our work 🚀

## Improving Frontmatter and MyST Site

![](./images/frontmatter-after.png)

## Export as a PDF

![](./images/export-pdf.png)



Create environment
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

pip install 

* jupyterlab-code-formatter
* jupyterlab_myst

pip install black isort


pyos-myst

