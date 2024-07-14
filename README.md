# README: About pyOpenSci peer review metrics

This is a dashboard created using mystmd [![Made with MyST](https://img.shields.io/badge/made%20with-myst-orange)](https://myst.tools). Myst-md is a community developed tool that makes it easier for scientists to create fully reproducible (and interactive) workflows and reports that are easily shared.

## How to use this repository

To work with this repository do the following:

### 1. Create & activate a fresh Python environment.

```bash
mamba env create -f environment.yml
mamba activate pyos-myst
```

### 2. Create a .env file

Copy the .env-default file in this repository, and rename it to ".env". This is the file in which you'll paste your GitHub access token.

### 3. Configure your GitHub access token

This dashboard leverages pyOpenSci's package [`pyosMeta`](https://github.com/pyOpenSci/pyosMeta) to obtain contributor and peer review metadata. To use this package, the user needs to supply a GitHub access token, which can be obtained from their GitHub account. Click on your profile image and navigate to "Settings", and then "Developer Settings".

![Image of GitHub Developer Settings page](images/developer_settings.png "Developer Settings page")
<br/><br/>
Create a new fine-grained personal access token, adding a name, expiration, description, and ensure the "Repository Access" is set to "Public Repositories (read-only)". No other configuration needed. At the bottom of the page, click "Generate token". 

![Image of personal access token](images/token.png "Token configuration page")
<br/><br/>
Once the token has been generated, copy the token string and paste it into the ".env" file next to `GITHUB_TOKEN=`. You are now configured to work with the information harvested using `pyosMeta`.

### 4. Install nodejs

Next, install `nodejs` & `mystmd`.

```bash
mamba install -c conda-forge "nodejs>=20,<21" mystmd
```

### 5. Local preview

Finally preview this locally:

Run `myst` to create and run a local live server that will update as you
update your code / workflows.

To build the html files and run code use:

`myst build --execute` to execute code`

To build a local server that runs and executes code:
`myst start --execute`

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

`>> myst`

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
