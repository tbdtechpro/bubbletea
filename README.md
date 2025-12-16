# Bubble Tea (Python Port)


The fun, functional and stateful way to build terminal apps. A Python framework
based on [The Elm Architecture][elm]. Bubble Tea is well-suited for simple and
complex terminal applications, either inline, full-window, or a mix of both.

> **Note**: This is a Python port of the original [Go Bubble Tea library][original] 
> by [Charm][charm].



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
