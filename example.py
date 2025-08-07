import tkinter as tk
import UI.library_ui as vui  # your custom UI library

def main():
    # Create the main window with custom parameters
    root = vui.Window(
        UIName="Example UI - VUI",
        Dimensions="760x480",
        ResizableX=True,
        ResizableY=True,
        bgColor="#f7f7fb",
        topMost=False,
        l=760,
        a=480,
        opacity=0.98,
    )

    # Add a label with custom font and colors
    vui.Label(
        root,
        "Example UI Library",
        fg="#222",
        bg="#f7f7fb",
        font=("Segoe UI", 16, "bold"),
    )

    # Create an Entry widget for text input
    entry = vui.Entry(root, width=36)
    # Button to print the current Entry content when clicked
    vui.Button(root, "Print Entry", lambda: print("Entry:", vui.getValue(entry)))

    # Create a SpinBox widget with range 0 to 50, starting at 7
    spin = vui.SpinBox(root, from_=0, to=50, initial=7)
    # Button to print the current SpinBox value
    vui.Button(
        root, "Print SpinBox", lambda: print("SpinBox:", vui.getSpinBoxValue(spin))
    )

    # Create a StringVar for the OptionMenu selection
    var_option = vui.StringVar(value="Option A")
    # Create an OptionMenu with three options
    vui.OptionMenu(root, var_option, ["Option A", "Option B", "Option C"])
    # Button to print the selected OptionMenu value
    vui.Button(
        root,
        "Print OptionMenu",
        lambda: print("OptionMenu:", vui.getOptionMenuValue(var_option)),
    )

    # Create a Combobox widget with three values
    cb = vui.Combobox(root, ["Alpha", "Beta", "Gamma"])
    # Button to print the selected Combobox value
    vui.Button(root, "Print Combobox", lambda: print("Combobox:", cb.get()))

    # Create a multi-line Text widget
    text_area = vui.Text(root, width=50, height=6)
    # Button to print the Text content
    vui.Button(
        root, "Print Text", lambda: print("Text:", repr(vui.getText(text_area)))
    )

    # Create a Progressbar widget
    pb = vui.Progressbar(root, length=220)

    # Function to advance the progress bar by 20, max 100
    def advance_progressbar():
        current = pb["value"] if "value" in pb.keys() else 0
        pb["value"] = min(100, current + 20)
        print("Progressbar value:", pb["value"])

    # Button to advance the progress bar
    vui.Button(root, "Advance Progressbar", advance_progressbar)

    # Create a Treeview with two columns
    tree = vui.Treeview(root, columns=("Name", "Score"))
    try:
        # Insert sample data into Treeview
        tree.insert("", tk.END, values=("Alice", 1200))
        tree.insert("", tk.END, values=("Bob", 900))
    except Exception:
        pass

    # Function to print the selected rows from the Treeview
    def print_tree_selection():
        selected = tree.selection()
        rows = [tree.item(i)["values"] for i in selected]
        print("Treeview selection:", rows)

    # Button to print Treeview selection
    vui.Button(root, "Print Treeview Selection", print_tree_selection)

    # Create a Canvas and add text
    canvas = vui.Canvas(root, width=200, height=100)
    canvas.create_text(100, 50, text="Canvas demo")

    # Example menu command functions
    def open_example():
        print("Menu -> Open selected")

    def save_example():
        path = vui.ask_save_file(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
        )
        print("Save -> path:", path)

    # Define menus structure
    menus = [
        (
            "File",
            [
                ("Open", open_example),
                ("Save", save_example),
                ("---", None),  # separator
                ("Exit", root.quit),
            ],
        ),
        ("Help", [("About", lambda: print("About selected"))]),
    ]
    # Create the menu bar
    vui.MenuDeBarra(root, menus, tearoff=False)

    # Popup example to ask user input
    def ask_name():
        name = vui.Popup("askstring", title="Your Name", prompt="Enter your name:")
        print("Popup askstring ->", name)

    vui.Button(root, "Ask Name (Popup)", ask_name)

    # Button to close the window
    vui.Button(root, "Close", lambda: root.destroy())

    # Center the window on the screen
    try:
        root.update_idletasks()
        w = root.winfo_width()
        h = root.winfo_height()
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        root.geometry(f"{w}x{h}+{x}+{y}")
    except Exception:
        pass

    root.mainloop()


if __name__ == "__main__":
    main()