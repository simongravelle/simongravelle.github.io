[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Workflow Status](https://github.com/simongravelle/simongravelle.github.io/actions/workflows/gh-pages.yml/badge.svg)

# Academic template

A simple academic template that is easy to deploy on GitHub page, and relatively
easy to customize using css. You can find the [live](https://simongravelle.github.io/)
version, and my resume [here](https://simongravelle.github.io/files/resume/resume-simon-gravelle.pdf).

## Overview

[![image](https://user-images.githubusercontent.com/43388542/216845033-cc7b0a28-60ff-4e86-a5ce-2c93930e08e2.png)](https://simongravelle.github.io/)

[![image](https://user-images.githubusercontent.com/43388542/216845176-a6effb49-db58-42b2-8b36-f65d5b959e39.png)](https://simongravelle.github.io/)

[![image](https://user-images.githubusercontent.com/43388542/216845058-77fe9c11-5086-494f-b83d-83d26c252a5b.png)](https://simongravelle.github.io/)

## Credit

This template was originally taken from [wowchemy](https://wowchemy.com/), with some custom CSS
adapted from [nickballousite](https://github.com/nballou) webpage.

## Build locally

To build locally on your computer, type:

```bash
hugo server
```

## How to modify

After cloning this repository, you can adapt it by:

- add your own content in the [content](content/) folder,
- custom css script can be written in [assets/scss/custom.scss](assets/scss/custom.scss),
- each publication can be entered as a folder in [content/publication/](content/publication/).

## How to deploy

In Settings, Pages, select:
- Deploy from a branch as Source
- gh-pages, `/(root)` as Branch
