"""Mouse handling for Bubble Tea."""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, Tuple


class MouseButton(Enum):
    """Mouse button types."""
    NONE = auto()
    LEFT = auto()
    MIDDLE = auto()
    RIGHT = auto()
    WHEEL_UP = auto()
    WHEEL_DOWN = auto()
    WHEEL_LEFT = auto()
    WHEEL_RIGHT = auto()
    BUTTON_4 = auto()
    BUTTON_5 = auto()


class MouseAction(Enum):
    """Mouse action types."""
    PRESS = auto()
    RELEASE = auto()
    MOTION = auto()


@dataclass
class MouseEvent:
    """Represents a mouse event."""
    x: int
    y: int
    button: MouseButton
    action: MouseAction
    alt: bool = False
    ctrl: bool = False
    shift: bool = False


def parse_mouse_event(data: bytes) -> Optional[MouseEvent]:
    """
    Parse SGR mouse event from raw bytes.
    
    SGR format: ESC [ < Cb ; Cx ; Cy M/m
    Where:
    - Cb is button info
    - Cx is column (1-based)
    - Cy is row (1-based)
    - M is press, m is release
    """
    try:
        text = data.decode('utf-8', errors='ignore')
        
        # SGR extended mouse mode
        if text.startswith('\x1b[<'):
            # Remove prefix and find terminator
            rest = text[3:]
            
            if 'M' in rest:
                parts, _ = rest.split('M', 1)
                is_release = False
            elif 'm' in rest:
                parts, _ = rest.split('m', 1)
                is_release = True
            else:
                return None
            
            nums = parts.split(';')
            if len(nums) != 3:
                return None
            
            cb = int(nums[0])
            cx = int(nums[1]) - 1  # Convert to 0-based
            cy = int(nums[2]) - 1  # Convert to 0-based
            
            # Parse modifiers
            shift = bool(cb & 4)
            alt = bool(cb & 8)
            ctrl = bool(cb & 16)
            
            # Parse button
            motion = bool(cb & 32)
            button_num = cb & 3
            
            # Wheel events
            if cb & 64:
                if button_num == 0:
                    button = MouseButton.WHEEL_UP
                elif button_num == 1:
                    button = MouseButton.WHEEL_DOWN
                elif button_num == 2:
                    button = MouseButton.WHEEL_LEFT
                else:
                    button = MouseButton.WHEEL_RIGHT
                action = MouseAction.PRESS
            else:
                # Regular buttons
                if button_num == 0:
                    button = MouseButton.LEFT
                elif button_num == 1:
                    button = MouseButton.MIDDLE
                elif button_num == 2:
                    button = MouseButton.RIGHT
                else:
                    button = MouseButton.NONE
                
                if motion:
                    action = MouseAction.MOTION
                elif is_release:
                    action = MouseAction.RELEASE
                else:
                    action = MouseAction.PRESS
            
            return MouseEvent(
                x=cx,
                y=cy,
                button=button,
                action=action,
                alt=alt,
                ctrl=ctrl,
                shift=shift,
            )
    except (ValueError, IndexError):
        pass
    
    return None
