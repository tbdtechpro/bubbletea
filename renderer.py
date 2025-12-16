"""Terminal renderer for Bubble Tea."""

import sys
import os
from typing import Optional, TextIO


class Renderer:
    """Handles rendering output to the terminal."""
    
    def __init__(
        self,
        output: TextIO = sys.stdout,
        fps: int = 60,
    ):
        self.output = output
        self.fps = fps
        self._last_render = ""
        self._cursor_hidden = False
        self._alt_screen = False
        self._lines_rendered = 0
    
    def render(self, view: str) -> None:
        """
        Render the view to the terminal.
        
        Uses differential rendering to minimize output.
        """
        if view == self._last_render:
            return
        
        # Clear previous render
        if self._lines_rendered > 0:
            # Move cursor up and clear lines
            for _ in range(self._lines_rendered):
                self.output.write("\x1b[A")  # Move up
                self.output.write("\x1b[2K")  # Clear line
        else:
            # First render, just clear current line
            self.output.write("\r\x1b[2K")
        
        # Write new content
        self.output.write(view)
        self.output.flush()
        
        # Track lines for next clear
        self._lines_rendered = view.count('\n')
        self._last_render = view
    
    def clear(self) -> None:
        """Clear the screen."""
        self.output.write("\x1b[2J\x1b[H")
        self.output.flush()
        self._lines_rendered = 0
        self._last_render = ""
    
    def enter_alt_screen(self) -> None:
        """Enter the alternate screen buffer."""
        if not self._alt_screen:
            self.output.write("\x1b[?1049h")
            self.output.flush()
            self._alt_screen = True
            self._lines_rendered = 0
            self._last_render = ""
    
    def exit_alt_screen(self) -> None:
        """Exit the alternate screen buffer."""
        if self._alt_screen:
            self.output.write("\x1b[?1049l")
            self.output.flush()
            self._alt_screen = False
    
    def hide_cursor(self) -> None:
        """Hide the terminal cursor."""
        if not self._cursor_hidden:
            self.output.write("\x1b[?25l")
            self.output.flush()
            self._cursor_hidden = True
    
    def show_cursor(self) -> None:
        """Show the terminal cursor."""
        if self._cursor_hidden:
            self.output.write("\x1b[?25h")
            self.output.flush()
            self._cursor_hidden = False
    
    def enable_mouse(self, all_motion: bool = False) -> None:
        """Enable mouse tracking."""
        if all_motion:
            self.output.write("\x1b[?1003h")  # All motion
        else:
            self.output.write("\x1b[?1002h")  # Cell motion
        self.output.write("\x1b[?1006h")  # SGR extended mode
        self.output.flush()
    
    def disable_mouse(self) -> None:
        """Disable mouse tracking."""
        self.output.write("\x1b[?1000l")
        self.output.write("\x1b[?1002l")
        self.output.write("\x1b[?1003l")
        self.output.write("\x1b[?1006l")
        self.output.flush()
    
    def set_window_title(self, title: str) -> None:
        """Set the terminal window title."""
        self.output.write(f"\x1b]0;{title}\x07")
        self.output.flush()
    
    def close(self) -> None:
        """Clean up the renderer."""
        self.show_cursor()
        self.exit_alt_screen()
        self.disable_mouse()


class NullRenderer(Renderer):
    """A renderer that does nothing (for testing)."""
    
    def render(self, view: str) -> None:
        pass
    
    def clear(self) -> None:
        pass
    
    def enter_alt_screen(self) -> None:
        pass
    
    def exit_alt_screen(self) -> None:
        pass
    
    def hide_cursor(self) -> None:
        pass
    
    def show_cursor(self) -> None:
        pass
    
    def enable_mouse(self, all_motion: bool = False) -> None:
        pass
    
    def disable_mouse(self) -> None:
        pass
    
    def set_window_title(self, title: str) -> None:
        pass
    
    def close(self) -> None:
        pass
