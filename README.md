# README: About pyOpenSci peer review metrics
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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

### 4. Local preview

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

## Build using Nox

You can use nox to build the dashboard locally. Nox will
create an environment for you with all needed dependencies.

To start, install [nox](https://nox.thea.codes/en/stable/):

Using `pip`:

`python -m pip install nox`

or [`pipx` for global install](https://pipx.pypa.io/stable/):

`pipx install nox`

### Build a static html website

To build the html version of the dashboard use

`nox -s build`

### Build a live local server dashboard

To build the dashboard as a local server that will update
as you update the files use:

`nox -s serve`

One a mac you can use `ctrl + d` to stop a live server.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kaiyamag"><img src="https://avatars.githubusercontent.com/u/98053751?v=4?s=100" width="100px;" alt="kaiyamag"/><br /><sub><b>kaiyamag</b></sub></a><br /><a href="https://github.com/pyOpenSci/peer-review-metrics/commits?author=kaiyamag" title="Code">💻</a> <a href="https://github.com/pyOpenSci/peer-review-metrics/pulls?q=is%3Apr+reviewed-by%3Akaiyamag" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ehinman"><img src="https://avatars.githubusercontent.com/u/121896266?v=4?s=100" width="100px;" alt="Elise Hinman"/><br /><sub><b>Elise Hinman</b></sub></a><br /><a href="https://github.com/pyOpenSci/peer-review-metrics/commits?author=ehinman" title="Code">💻</a> <a href="https://github.com/pyOpenSci/peer-review-metrics/pulls?q=is%3Apr+reviewed-by%3Aehinman" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.santisoler.com"><img src="https://avatars.githubusercontent.com/u/11541317?v=4?s=100" width="100px;" alt="Santiago Soler"/><br /><sub><b>Santiago Soler</b></sub></a><br /><a href="https://github.com/pyOpenSci/peer-review-metrics/commits?author=santisoler" title="Code">💻</a> <a href="https://github.com/pyOpenSci/peer-review-metrics/pulls?q=is%3Apr+reviewed-by%3Asantisoler" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/fwkoch"><img src="https://avatars.githubusercontent.com/u/9453731?v=4?s=100" width="100px;" alt="Franklin Koch"/><br /><sub><b>Franklin Koch</b></sub></a><br /><a href="https://github.com/pyOpenSci/peer-review-metrics/commits?author=fwkoch" title="Code">💻</a> <a href="https://github.com/pyOpenSci/peer-review-metrics/pulls?q=is%3Apr+reviewed-by%3Afwkoch" title="Reviewed Pull Requests">👀</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!