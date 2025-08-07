# Trilha UI Library (Trilha\_ui)

A lightweight and easy-to-use Python UI library built on top of **Tkinter** and **ttk**.
Provides a simplified interface to create windows, widgets, popups, menus, and manage layouts with less boilerplate code.

---

## Features

* Create customizable windows with options like opacity, transparency, fullscreen, and always-on-top.
* Simplified wrapper functions for common Tkinter widgets: `Label`, `Button`, `Entry`, `Checkbutton`, `RadioButton`, `SpinBox`, `OptionMenu`, `Text`, `Canvas`, `Combobox`, `Progressbar`, `Treeview`, and more.
* Popup dialogs for info, warnings, errors, file dialogs, color chooser, and input prompts.
* Easy menu bar creation with nested menus and separators.
* Layout management supporting `pack`, `grid`, and `place` layouts via a unified interface.
* Wrapper functions for Tkinter variable classes: `StringVar`, `IntVar`, `DoubleVar`, `BooleanVar`.
* Utility functions for window control (close, minimize, maximize, restore).
* Functions to get/set widget values with simple calls.

---

## Installation

Since this library is a single Python module, simply place `library_ui.py` inside your project folder or Python path and import it:

```python
import library_ui as vui
```

---

## Usage Example

```python
import tkinter as tk
import library_ui as vui

def main():
    root = vui.Window(
        UIName="Example Window",
        Dimensions="600x400",
        bgColor="#f0f0f0",
        opacity=0.95,
    )

    vui.Label(root, "Welcome to Trilha UI", font=("Segoe UI", 14))
    entry = vui.Entry(root, width=30)
    vui.Button(root, "Print Entry", lambda: print("Entry content:", vui.getValue(entry)))

    root.mainloop()

if __name__ == "__main__":
    main()
```

---

## API Overview

### Window Creation

* `Window(UIName, Dimensions, ResizableX, ResizableY, iconPath, bgColor, fullscreen, topMost, l, a, borderTransparent, bgTransparent, opacity)`

### Widgets

* `Label(Parent, text, fg, bg, font)`
* `Entry(Parent, width, bg, fg, font, show)`
* `Button(Parent, text, callback)`
* `Checkbutton(Parent, text, variable)`
* `RadioButton(Parent, text, variable, value)`
* `OptionMenu(Parent, variable, options)`
* `Listbox(Parent, items)`
* `SpinBox(Parent, from_, to, initial)`
* `Text(Parent, width, height)`
* `LabelWithImage(Parent, text, imagePath, fg, bg, font)`
* `Frame(Parent, bg, width, height)`
* `LabelFrame(Parent, text, bg, fg, font)`
* `PanedWindow(Parent, orient)`
* `MenuDeBarra(Parent, menus, tearoff)`
* `Canvas(Parent, width, height, bg, layout, **layout_opts)`
* `Combobox(Parent, values, state, layout, **layout_opts)`
* `Progressbar(Parent, length, orient, mode, layout, **layout_opts)`
* `Notebook(Parent, layout, **layout_opts)`
* `Treeview(Parent, columns, show, layout, **layout_opts)`
* `Separator(Parent, orient, layout, **layout_opts)`
* `Scrollbar(Parent, orient, command, layout, **layout_opts)`

### Popup Dialogs

* `Popup(type, **kwargs)` — supports `"info"`, `"warning"`, `"error"`, `"askopenfile"`, `"askcolor"`, `"askstring"`

### Variables

* `StringVar(root, value)`
* `IntVar(root, value)`
* `DoubleVar(root, value)`
* `BooleanVar(root, value)`

### Utility Functions

* `bind_event(widget, sequence, func, add)`
* `ask_save_file(**kwargs)`
* `ask_save_file_obj(**kwargs)`
* `ask_yes_no(title, message)`
* `ask_ok_cancel(title, message)`
* `close_window(window)`
* `minimize_window(window)`
* `maximize_window(window)`
* `restore_window(window)`
* `getText(widget)`
* `getValue(widget)`
* `deleteValue(widget)`
* `setValue(widget, value)`
* `getSpinBoxValue(widget)`
* `getOptionMenuValue(variable)`

---

## Notes

* This library wraps native Tkinter widgets but simplifies creation and layout management.
* Supports basic widget packing by default, with options for `grid` and `place` layouts where specified.
* Works on Python 3.x with Tkinter installed.

---

## License

MIT License — feel free to use and modify for personal or commercial projects.

---

## Contact

Created by João Trilha.
Feel free to reach out for questions or contributions.