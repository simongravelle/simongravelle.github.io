[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Workflow Status](https://github.com/simongravelle/simongravelle.github.io/actions/workflows/gh-pages.yml/badge.svg)

# Academic template

A simple academic template that is easy to deploy on GitHub page, and relatively
easy to customize using css. You can find the [live](https://simongravelle.github.io/)
version, and my resume [here](https://simongravelle.github.io/files/resume/resume-simon-gravelle.pdf).

## Automatic update of the publication list

The list of publications is updated automatically from Google Scholar using
the [scholar-collector](https://github.com/simongravelle/scholar-collector).

## Overview

[![image](static/img/Screenshot01.png)](https://simongravelle.github.io/)

[![image](static/img/Screenshot02.png)](https://simongravelle.github.io/)

## Credit

This template was originally taken from [wowchemy](https://wowchemy.com/), with
some custom CSS adapted from [nickballousite](https://github.com/nballou) webpage.

## How to build locally

To build locally on your computer, type:

```bash
hugo server
```

## How to modify

After cloning this repository:

- add your own content in the [content](content/) folder,
- modify the custom css script in [assets/scss/custom.scss](assets/scss/custom.scss),
- enter your publications in [content/publication/](content/publication/).
- replace Simon Gravelle by your name in [layouts/partials/widgets/about.html](layouts/partials/widgets/about.html).

## How to deploy

In Settings, Pages, select:

- Deploy from a branch as Source
- gh-pages, `/(root)` as Branch
