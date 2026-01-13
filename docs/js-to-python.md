# Javascript to Python

## Node vs Python version manager

|Language|Tools|Description||
|--|--|--|--|
|Node|`nvm`| a quick and simple tool to switch between different node version for your current system to run |[nvm](https://github.com/nvm-sh/nvm) |
|Python|`uv`| a modern multifunctional tool include python version management | [Astral - uv](https://docs.astral.sh/uv/) |

## Dependency Management

|Language|Tools|Description||
|--|--|--|--|
|Node|`npm`| npm is the default package manager for the JavaScript runtime environment Node.js and is included as a recommended feature in the Node.js installer [[source](https://en.wikipedia.org/wiki/Npm)] |[npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) |
|Python|`uv`| a modern multifunctional tool mainly for python package management. It will also automatically create a `.venv` in your project and move all the dependencies into there | [Astral - uv](https://docs.astral.sh/uv/) |


## Python Code Design Structure

Although Python and JS are both scripting language, the way their project structure is very different.

In python, we are not able to run like `JS`.

A python script should be decided at the beginning to either be:
- **A**: a runnable script (like application entry point `main.py`)
- **B**: a library/package script (a collections of features ready to be called)

One mistake I made in this project is that I try to mix between A and B in one single script for quick prototyping.

This bring me down to the rabbit hole of absoulte or relative import arguments, `PYTHONPATH` hardcoded configuration and even [`sys.path`](./js-to-python.md#syspath-modification-references) modification on run time, and I hit a lot (I MEAN A LOT) of `module not found` error.

> Side note for Jupyter, always remember to restart the Jupyter Kernel because it always cached previous run.

But the "Arkham Razor" for this is to separate their function. When one is decided to be a library function, it should only expect the entry point to be outside of the library module, and all `__main__()` should not ever be inside of them, even they are just for testing.

This clear my understanding on the script import path and the jupiter notebook module import path.

The most important take away here is:
- Runnable script (with `__main__()`) should be kept in root
- Library scripts should be kept in their own package directory
- Library scripts `import` should be absolute import, which including their package name
- no `__main__()` in library scripts, test them outside of the package
- [vscode] use `jupyter.notebookFileRoot` to control the environment root [[see](https://stackoverflow.com/a/73954768/7939633)]

```
+ pipeline-app
  + .python-version
  + pyproject.toml
  + main.py
  + playground.py // do quick prototype here or use pytest
  + notebook
    + notebook1.ipynb
  + pipeline-app // library scripts
    + feature-one
      + feature-one.py
    + feature-two
      + feature-two.py
```

### `sys.path` Modification References
- https://stackoverflow.com/a/71057808/7939633
- https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c/
- https://stackoverflow.com/a/35273613/7939633
- https://stackoverflow.com/a/44486700/7939633