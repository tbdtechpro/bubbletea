"""Commands for Bubble Tea."""

from typing import Callable, Optional, List, Any, Union
from dataclasses import dataclass
from .messages import Msg, QuitMsg, CustomMsg


# A Cmd is a callable that returns an optional Msg
Cmd = Callable[[], Optional[Msg]]


def quit_cmd() -> Msg:
    """
    Command to quit the program.
    
    Usage:
        return model, quit_cmd
    """
    return QuitMsg()


def batch(*cmds: Optional[Cmd]) -> Optional[Cmd]:
    """
    Combine multiple commands into one.
    Commands will be executed concurrently.
    
    Args:
        *cmds: Commands to batch together
        
    Returns:
        A single command that runs all given commands
    """
    valid_cmds = [c for c in cmds if c is not None]
    
    if not valid_cmds:
        return None
    
    if len(valid_cmds) == 1:
        return valid_cmds[0]
    
    def batched() -> Optional[Msg]:
        # Return first message, others will be handled by program
        for cmd in valid_cmds:
            result = cmd()
            if result is not None:
                return result
        return None
    
    # Store all commands for the program to execute
    batched._batch_cmds = valid_cmds  # type: ignore
    return batched


def sequence(*cmds: Optional[Cmd]) -> Optional[Cmd]:
    """
    Run commands in sequence, one after another.
    
    Args:
        *cmds: Commands to run sequentially
        
    Returns:
        A single command that runs commands in order
    """
    valid_cmds = [c for c in cmds if c is not None]
    
    if not valid_cmds:
        return None
    
    def sequenced() -> Optional[Msg]:
        for cmd in valid_cmds:
            result = cmd()
            if result is not None:
                return result
        return None
    
    sequenced._sequence_cmds = valid_cmds  # type: ignore
    return sequenced


def set_window_title(title: str) -> Cmd:
    """
    Command to set the terminal window title.
    
    Args:
        title: The window title
        
    Returns:
        A command that sets the window title
    """
    @dataclass
    class WindowTitleMsg(Msg):
        title: str
    
    def cmd() -> Msg:
        return WindowTitleMsg(title=title)
    
    return cmd


def clear_screen() -> Cmd:
    """
    Command to clear the screen.
    
    Returns:
        A command that clears the terminal screen
    """
    @dataclass
    class ClearScreenMsg(Msg):
        pass
    
    def cmd() -> Msg:
        return ClearScreenMsg()
    
    return cmd


def tick(duration_seconds: float, fn: Callable[[], Msg]) -> Cmd:
    """
    Command to send a message after a delay.
    
    Args:
        duration_seconds: Delay in seconds
        fn: Function that returns the message to send
        
    Returns:
        A command that sends a message after the delay
    """
    import time
    
    def cmd() -> Optional[Msg]:
        time.sleep(duration_seconds)
        return fn()
    
    return cmd


def every(interval_seconds: float, fn: Callable[[], Msg]) -> Cmd:
    """
    Command to repeatedly send a message at an interval.
    
    Note: This is meant to be called once and will keep running.
    
    Args:
        interval_seconds: Interval in seconds
        fn: Function that returns the message to send
    """
    # This is a placeholder - actual implementation would need
    # to be integrated with the event loop
    return tick(interval_seconds, fn)
