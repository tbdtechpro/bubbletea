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

---

## Installation

bash pip install bubbletea

Or install from source:

bash git clone [https://github.com/your-repo/bubbletea-python.git](https://github.com/your-repo/bubbletea-python.git) cd bubbletea-python pip install -e .


### Requirements

- Python 3.10+
- Unix-like OS (Linux, macOS) — Windows support is planned

---

## Quick Start


python import bubbletea as tea from typing import Optional, Tuple
class MyModel(tea.Model): def init(self): self.count = 0

def init(self) -> Optional[tea.Cmd]:
    return None

def update(self, msg: tea.Msg) -> Tuple["MyModel", Optional[tea.Cmd]]:
    if isinstance(msg, tea.KeyMsg):
        if msg.key in ("q", "ctrl+c"):
            return self, tea.quit_cmd
        elif msg.key == "up":
            self.count += 1
        elif msg.key == "down":
            self.count -= 1
    return self, None

def view(self) -> str:
    return f"Count: {self.count}\n\nPress up/down to change, q to quit."

if name == "main": tea.Program(MyModel()).run()


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

python import bubbletea as tea from typing import Optional, Tuple, Dict


Bubble Tea programs are comprised of a **model** that describes the application
state and three simple methods on that model:

- **init()** — Returns an initial command for the application to run
- **update(msg)** — Handles incoming events and updates the model accordingly
- **view()** — Renders the UI based on the data in the model

### The Model

Let's start by defining our model which will store our application's state.
In Python, we create a class that inherits from `tea.Model`:

python class ShoppingListModel(tea.Model): def init(self.choices: list[str],.cursor: int = 0,selected: Optional[Dict[int, bool]] = None,): self.choices = choices # items on the to-do list self.cursor = cursor # which item our cursor is pointing at self.selected = selected or {} # which items are selected


### Initialization

Next, we'll define our application's initial state and the `init` method:

python def initial_model() -> ShoppingListModel: return ShoppingListModel(choices=["Milk", "Eggs", "Bread"])

The `init` method can return a `Cmd` that could perform some initial I/O. 
For now, we don't need to do any I/O, so we'll just return `None`:

python def init(self) -> Optional[tea.Cmd]: # Just return None, which means "no I/O right now, please." return None


### The Update Method

Next up is the update method. The update function is called when "things
happen." Its job is to look at what has happened and return an updated model in
response.

The "something happened" comes in the form of a `Msg`. Messages are the result
of some I/O that took place, such as a keypress, timer tick, or a response from
a server.

We use `isinstance()` to determine which type of message we received:

python def update(self, msg: tea.Msg) -> Tuple["ShoppingListModel", Optional[tea.Cmd]]: # Is it a key press? if isinstance(msg, tea.KeyMsg): key = msg.key

    # These keys should exit the program
    if key in ("ctrl+c", "q"):
        return self, tea.quit_cmd
    
    # The "up" and "k" keys move the cursor up
    if key in ("up", "k"):
        if self.cursor > 0:
            self.cursor -= 1
    
    # The "down" and "j" keys move the cursor down
    elif key in ("down", "j"):
        if self.cursor < len(self.choices) - 1:
            self.cursor += 1
    
    # The "enter" key and spacebar toggle selection
    elif key in ("enter", " "):
        if self.cursor in self.selected:
            del self.selected[self.cursor]
        else:
            self.selected[self.cursor] = True

# Return the updated model
return self, None

Note that <kbd>ctrl+c</kbd> and <kbd>q</kbd> return `tea.quit_cmd` with the model.
That's a special command which instructs the Bubble Tea runtime to quit.

### The View Method

At last, it's time to render our UI. The view method returns a `string` — that
string is our UI!

python def view(self) -> str: # The header s = "What should we buy at the market?\n\n"

# Iterate over our choices
for i, choice in enumerate(self.choices):
    # Is the cursor pointing at this choice?
    cursor = ">" if i == self.cursor else " "
    
    # Is this choice selected?
    checked = "x" if i in self.selected else " "
    
    # Render the row
    s += f"{cursor} [{checked}] {choice}\n"

# The footer
s += "\nPress q to quit.\n"

return s


### All Together Now

The last step is to run our program. We pass our initial model to
`tea.Program` and call `run()`:

python def main(): p = tea.Program(initial_model()) final_model = p.run()
if == "**main**": main() **name**

### Running the Example

bash python examples/basics.py


---

## Features

| Feature | Status | Description |
|---------|--------|-------------|
| Elm Architecture | ✅ | Model-Update-View pattern |
| Keyboard Input | ✅ | Full key handling with modifiers |
| Mouse Support | ✅ | SGR extended mouse mode |
| Alternate Screen | ✅ | Full-screen TUI support |
| Window Resize | ✅ | `WindowSizeMsg` on terminal resize |
| Commands | ✅ | Async operations with `Cmd` |
| Batch Commands | ✅ | Run multiple commands concurrently |
| Cursor Control | ✅ | Show/hide cursor |
| Focus Events | ✅ | Terminal focus/blur detection |
| Windows Support | 🚧 | Planned |

---

## API Reference

### Core Classes

#### `tea.Model`

Abstract base class for your application model. Implement these methods:

python class MyModel(tea.Model): def init(self) -> Optional[tea.Cmd]: """Return initial command or None."""

def update(self, msg: tea.Msg) -> Tuple[Model, Optional[tea.Cmd]]:
    """Handle a message and return (new_model, optional_command)."""
    
def view(self) -> str:
    """Return the UI as a string."""


#### `tea.Program`

The main program runner.

python
Basic usage
p = tea.Program(model) final_model = p.run()
With options
p = tea.Program

(model,alt,creen = True,#Usealternate screen=True,window_size=None,mous

``` 
### Message Types

| Message | Attributes | Description |
|---------|------------|-------------|
| `tea.KeyMsg` | `key: str`, `alt: bool` | Keyboard input |
| `tea.MouseMsg` | `x`, `y`, `button`, `action`, `alt`, `ctrl`, `shift` | Mouse events |
| `tea.WindowSizeMsg` | `width: int`, `height: int` | Terminal resize |
| `tea.FocusMsg` | — | Terminal gained focus |
| `tea.BlurMsg` | — | Terminal lost focus |

### Key Names

Common key names returned in `KeyMsg.key`:

- Letters: `"a"`, `"b"`, ..., `"z"`
- With Ctrl: `"ctrl+a"`, `"ctrl+c"`, etc.
- With Alt: `"alt+a"`, `"alt+x"`, etc.
- Arrow keys: `"up"`, `"down"`, `"left"`, `"right"`
- Navigation: `"home"`, `"end"`, `"pgup"`, `"pgdown"`
- Editing: `"enter"`, `"tab"`, `"backspace"`, `"delete"`, `"escape"`
- Function keys: `"f1"` through `"f12"`
- Space: `" "` (literal space character)

### Commands
```

python
Quit the program
return model, tea.quit_cmd
Run multiple commands concurrently
cmd = tea.batch(cmd1, cmd2, cmd3)
Run commands in sequence
cmd = tea.sequence(cmd1, cmd2, cmd3)
Screen control
tea.enter_alt_screen() # Enter alternate screen buffer tea.exit_alt_screen() # Exit alternate screen buffer tea.hide_cursor() # Hide terminal cursor tea.show_cursor() # Show terminal cursor
Mouse control
tea.enable_mouse_cell_motion() # Enable mouse tracking tea.enable_mouse_all_motion() # Track all mouse movement tea.disable_mouse() # Disable mouse tracking``` 

### Custom Commands

Create commands that perform async work:
```

python import time from dataclasses import dataclass
@dataclass class TickMsg(tea.Msg): time: float
def tick_cmd() -> tea.Cmd: def cmd() -> tea.Msg: time.sleep(1.0) return TickMsg(time=time.time()) return cmd``` 

---

## Debugging

### Logging

You can't log to stdout because your TUI is using it. Log to a file instead:
```

python import logging
logging.basicConfig
In your update method:
logging.debug(f"Received message: {msg}")``` 

To see logs in real time, run in another terminal:

```bash
tail -f debug.log
```
```

 
Project Structure``` 
bubbletea/
├── __init__.py       # Package exports
├── tea.py            # Core Program class and event loop
├── model.py          # Model abstract base class
├── messages.py       # Message types (KeyMsg, MouseMsg, etc.)
├── keys.py           # Key parsing and constants
├── mouse.py          # Mouse event parsing
├── commands.py       # Command helpers (quit, batch, etc.)
├── renderer.py       # Terminal renderer
├── screen.py         # Screen control sequences
└── examples/
    └── basics.py     # Shopping list tutorial example
```

 
Comparison with Go Version
Go
Python
Notes
tea.NewProgram(model)
tea.Program(model)
Constructor
p.Run()
p.run()
Blocking run
tea.Quit
tea.quit_cmd
Quit command
tea.Batch(...)
tea.batch(...)
Batch commands
Type switch
isinstance()
Message type checking
tea.KeyMsg
tea.KeyMsg
Same name
Interface
Abstract base class
Model definition
 
Related Libraries
Python TUI ecosystem:
Rich — Rich text and beautiful formatting
Textual — TUI framework (CSS-based styling)
prompt_toolkit — Interactive CLI building
blessed — Terminal capabilities wrapper
curses — Standard library terminal handling
 
Acknowledgments
This is a Python port of the excellent Bubble Tea library by Charm.
Bubble Tea is based on The Elm Architecture by Evan Czaplicki et alia and the excellent go-tea by TJ Holowaychuk.
 
License
MIT
 
Ported from Bubble Tea, part of Charm.
 
Charm热爱开源 • Charm loves open source • نحنُ نحب المصادر المفتوحة``` 

This `PyREADME.md` file is a complete, standalone readme for the Python port with:

- Installation instructions
- Quick start example
- Full tutorial (ported from Go to Python)
- Feature checklist
- Complete API reference
- Key name reference
- Debugging tips
- Project structure
- Go-to-Python comparison table
- Related libraries
- Proper attribution
```
