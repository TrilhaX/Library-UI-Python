import tkinter as tk
import UI.library_ui as vui

def main():
    # Create the main window using the custom UI library 'vui'
    root = vui.Window(
        UIName="Exemplo UI - VUI",  # Window title
        Dimensions="760x480",       # Window size
        ResizableX=True,            # Allow horizontal resizing
        ResizableY=True,            # Allow vertical resizing
        bgColor="#f7f7fb",          # Background color
        topMost=False,              # Window not always on top
        l=760,                     # Window width (redundant with Dimensions but kept for library)
        a=480,                     # Window height
        opacity=0.98,              # Window transparency (98% opaque)
    )

    # Add a label widget with custom font and colors
    vui.Label(
        root,
        "Exemplo de library - João",
        fg="#222",
        bg="#f7f7fb",
        font=("Segoe UI", 16, "bold"),
    )

    # Create an Entry widget for text input
    entry = vui.Entry(root, width=36)
    # Create a button that prints the current Entry content when clicked
    vui.Button(root, "Imprimir Entry", lambda: print("Entry:", vui.getValue(entry)))

    # Create a SpinBox widget with range 0 to 50, starting at 7
    spin = vui.SpinBox(root, from_=0, to=50, initial=7)
    # Button to print the current value of the SpinBox
    vui.Button(
        root, "Imprimir SpinBox", lambda: print("SpinBox:", vui.getSpinBoxValue(spin))
    )

    # Create a StringVar to hold the current option in OptionMenu
    var_option = vui.StringVar(value="Opção A")
    # Create an OptionMenu widget with three options
    vui.OptionMenu(root, var_option, ["Opção A", "Opção B", "Opção C"])
    # Button to print the currently selected option
    vui.Button(
        root,
        "Imprimir OptionMenu",
        lambda: print("OptionMenu:", vui.getOptionMenuValue(var_option)),
    )

    # Create a Combobox widget with three values
    cb = vui.Combobox(root, ["Alpha", "Beta", "Gamma"])
    # Button to print the selected Combobox value
    vui.Button(root, "Imprimir Combobox (valor)", lambda: print("Combobox:", cb.get()))

    # Create a Text widget (multi-line text area)
    text_area = vui.Text(root, width=50, height=6)
    # Button to print the content of the Text widget
    vui.Button(
        root, "Imprimir Text", lambda: print("Text:", repr(vui.getText(text_area)))
    )

    # Create a Progressbar widget with specified length
    pb = vui.Progressbar(root, length=220)

    # Function to advance the progress bar value by 20, max 100
    def avancar_pb():
        current = pb["value"] if "value" in pb.keys() else 0
        pb["value"] = min(100, current + 20)
        print("Progressbar value:", pb["value"])

    # Button to advance the progress bar when clicked
    vui.Button(root, "Avançar Progressbar", avancar_pb)

    # Create a Treeview widget with two columns
    tree = vui.Treeview(root, columns=("Nome", "Score"))
    try:
        # Insert sample data rows into the Treeview
        tree.insert("", tk.END, values=("João", 1200))
        tree.insert("", tk.END, values=("Ana", 900))
    except Exception:
        pass

    # Function to print selected rows from the Treeview
    def imprimir_tree_sel():
        sel = tree.selection()
        rows = [tree.item(i)["values"] for i in sel]
        print("Treeview seleção:", rows)

    # Button to print the current selection in the Treeview
    vui.Button(root, "Imprimir seleção Treeview", imprimir_tree_sel)

    # Create a Canvas widget and add simple text
    canvas = vui.Canvas(root, width=200, height=100)
    canvas.create_text(100, 50, text="Canvas demo")

    # Define example menu command functions
    def abrir_exemplo():
        print("Menu -> Abrir acionado")

    def salvar_exemplo():
        # Open a save file dialog and print selected path
        path = vui.ask_save_file(
            defaultextension=".txt", filetypes=[("Texto", "*.txt")]
        )
        print("Salvar -> caminho:", path)

    # Define the menu structure for the menu bar
    menus = [
        (
            "Arquivo",
            [
                ("Abrir", abrir_exemplo),
                ("Salvar", salvar_exemplo),
                ("---", None),  # Separator in menu
                ("Sair", root.quit),
            ],
        ),
        ("Ajuda", [("Sobre", lambda: print("Sobre..."))]),
    ]
    # Create the menu bar with the specified menus
    vui.MenuDeBarra(root, menus, tearoff=False)

    # Function to ask the user for their name using an input popup
    def pedir_nome():
        nome = vui.Popup("askstring", title="Seu nome", prompt="Digite seu nome:")
        print("Popup askstring ->", nome)

    # Button to show the name input popup
    vui.Button(root, "Pedir nome (Popup)", pedir_nome)

    # Button to close the window
    vui.Button(root, "Fechar", lambda: root.destroy())

    # Center the window on the screen after initial rendering
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

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()