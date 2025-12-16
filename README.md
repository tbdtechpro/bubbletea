# Bubble Tea (Python Port)

<p>
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="https://stuff.charm.sh/bubbletea/bubble-tea-v2-light.png" width="308">
      <source media="(prefers-color-scheme: dark)" srcset="https://stuff.charm.sh/bubbletea/bubble-tea-v2-dark.png" width="312">
      <img src="https://stuff.charm.sh/bubbletea/bubble-tea-v2-light.png" width="308" />
    </picture>
    <br>
    <a href="https://pypi.org/project/bubbletea/"><img src="https://img.shields.io/pypi/v/bubbletea.svg" alt="PyPI Version"></a>
    <a href="https://pypi.org/project/bubbletea/"><img src="https://img.shields.io/pypi/pyversions/bubbletea.svg" alt="Python Versions"></a>
    <a href="https://github.com/charmbracelet/bubbletea"><img src="https://img.shields.io/badge/ported%20from-Go-00ADD8.svg" alt="Ported from Go"></a>
</p>

The fun, functional and stateful way to build terminal apps. A Python framework
based on [The Elm Architecture][elm]. Bubble Tea is well-suited for simple and
complex terminal applications, either inline, full-window, or a mix of both.

> **Note**: This is a Python port of the original [Go Bubble Tea library][original] 
> by [Charm][charm].

<p>
    <img src="https://stuff.charm.sh/bubbletea/bubbletea-example.gif" width="100%" alt="Bubble Tea Example">
</p>

### Requirements

- Python 3.10+
- Unix-like OS (Linux, macOS) — Windows support is planned

---

## Tutorial

Bubble Tea is based on the functional design paradigms of [The Elm
Architecture][elm], which works beautifully with Python. It's a delightful way
to build applications.

This tutorial assumes you have a working knowledge of Python.

The source code for this program is available in [`examples/basics.py`](examples/basics.py).

[elm]: https://guide.elm-lang.org/architecture/
[original]: https://github.com/charmbracelet/bubbletea
[charm]: https://charm.sh

### Let's get to it

For this tutorial, we're making a shopping list.

To start, we'll import the Bubble Tea library, which we'll call `tea` for short:
