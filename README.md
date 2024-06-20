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
📖 Built 01-paper.md in 33 ms.
📖 Built 02-notebook.ipynb in 32 ms.
📖 Built 03-leah.ipynb in 32 ms.
📚 Built 4 pages for project in 147 ms.


        ✨✨✨  Starting Book Theme  ✨✨✨



🔌 Server started on port 3000!  🥳 🎉


        👉  http://localhost:3000  👈
```
