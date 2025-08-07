import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox, filedialog, colorchooser, simpledialog


# -------------------
# Window
# -------------------
def Window(
    UIName="Janela",
    Dimensions="800x600",
    ResizableX=True,
    ResizableY=True,
    iconPath=None,
    bgColor="white",
    fullscreen=False,
    topMost=False,
    l=200,
    a=200,
    borderTransparent=False,
    bgTransparent=False,
    opacity=1.0,
):
    root = tk.Tk()
    root.title(UIName)
    root.geometry(Dimensions)
    root.resizable(ResizableX, ResizableY)
    if iconPath:
        root.iconbitmap(iconPath)
    root.configure(bg=bgColor)
    root.attributes("-fullscreen", fullscreen)
    root.attributes("-topmost", topMost)
    root.attributes("-alpha", opacity)
    root.minsize(l, a)
    root.maxsize(l, a)
    root.overrideredirect(borderTransparent)
    if bgTransparent:
        root.wm_attributes("-transparentcolor", bgColor)
    opacity = opacity
    return root


# -------------------
# Widgets
# -------------------
def Label(Parent, text="", fg="black", bg="white", font=None):
    label = tk.Label(Parent, text=text, fg=fg, bg=bg, font=font)
    label.pack()
    return label


def Entry(Parent, width=20, bg="white", fg="black", font=None, show=None):
    entry = tk.Entry(Parent, width=width, bg=bg, fg=fg, font=font, show=show)
    entry.pack()
    return entry


def Button(Parent, text="Botão", callback=None):
    button = tk.Button(Parent, text=text, command=callback)
    button.pack()
    return button


def Checkbutton(Parent, text="", variable=None):
    check = tk.Checkbutton(Parent, text=text, variable=variable)
    check.pack()
    return check


def RadioButton(Parent, text="", variable=None, value=None):
    radio = tk.Radiobutton(Parent, text=text, variable=variable, value=value)
    radio.pack()
    return radio


def OptionMenu(Parent, variable, options):
    option_menu = tk.OptionMenu(Parent, variable, *options)
    option_menu.pack()
    return option_menu


def Listbox(Parent, items):
    listbox = tk.Listbox(Parent)
    for item in items:
        listbox.insert(tk.END, item)
    listbox.pack()
    return listbox


def SpinBox(Parent, from_=0, to=10, initial=None):
    spinbox = tk.Spinbox(Parent, from_=from_, to=to)
    spinbox.pack()
    if initial is not None:
        spinbox.delete(0, tk.END)
        spinbox.insert(0, initial)
    return spinbox


def Text(Parent, width=40, height=10):
    text = tk.Text(Parent, width=width, height=height)
    text.pack()
    return text


def LabelWithImage(Parent, text="", imagePath=None, fg="black", bg="white", font=None):
    image = PhotoImage(file=imagePath) if imagePath else None
    label = tk.Label(
        Parent, text=text, image=image, fg=fg, bg=bg, font=font, compound="top"
    )
    label.image = image
    label.pack()
    return label


def Frame(Parent, bg="white", width=None, height=None):
    frame = tk.Frame(Parent, bg=bg, width=width, height=height)
    frame.pack(fill=tk.BOTH, expand=True)
    return frame


def LabelFrame(Parent, text="", bg="white", fg="black", font=None):
    label_frame = tk.LabelFrame(Parent, text=text, bg=bg, fg=fg, font=font)
    label_frame.pack(fill=tk.BOTH, expand=True)
    return label_frame


def PanedWindow(Parent, orient=tk.HORIZONTAL):
    paned_window = tk.PanedWindow(Parent, orient=orient)
    paned_window.pack(fill=tk.BOTH, expand=True)
    return paned_window


def MenuDeBarra(Parent, menus, tearoff):
    menu_bar = tk.Menu(Parent)
    for main_label, sub_items in menus:
        submenu = tk.Menu(menu_bar, tearoff=tearoff)
        for label, command in sub_items:
            if label == "---":  # separador
                submenu.add_separator()
            else:
                submenu.add_command(label=label, command=command)
        menu_bar.add_cascade(label=main_label, menu=submenu)
    Parent.config(menu=menu_bar)
    return menu_bar


def Popup(popup_type, **kwargs):
    if popup_type == "info":
        return messagebox.showinfo(
            kwargs.get("title", "Info"), kwargs.get("message", "Mensagem")
        )
    elif popup_type == "warning":
        return messagebox.showwarning(
            kwargs.get("title", "Aviso"), kwargs.get("message", "Mensagem")
        )
    elif popup_type == "error":
        return messagebox.showerror(
            kwargs.get("title", "Erro"), kwargs.get("message", "Mensagem")
        )
    elif popup_type == "askopenfile":
        return filedialog.askopenfilename(
            title=kwargs.get("title", "Abrir arquivo"),
            filetypes=kwargs.get("filetypes", [("Todos os arquivos", "*.*")]),
        )
    elif popup_type == "askcolor":
        return colorchooser.askcolor(title=kwargs.get("title", "Escolha uma cor"))
    elif popup_type == "askstring":
        return simpledialog.askstring(
            kwargs.get("title", "Entrada"), kwargs.get("prompt", "Digite algo:")
        )
    else:
        raise ValueError("Tipo de popup inválido!")


def Canvas(Parent, width=200, height=200, bg="white", layout="pack", **layout_opts):
    canvas = tk.Canvas(Parent, width=width, height=height, bg=bg)
    _apply_layout(canvas, layout, layout_opts)
    return canvas


def Combobox(Parent, values, state="readonly", layout="pack", **layout_opts):
    cb = ttk.Combobox(Parent, values=values, state=state)
    _apply_layout(cb, layout, layout_opts)
    return cb


def Progressbar(
    Parent,
    length=200,
    orient=tk.HORIZONTAL,
    mode="determinate",
    layout="pack",
    **layout_opts,
):
    pb = ttk.Progressbar(Parent, length=length, orient=orient, mode=mode)
    _apply_layout(pb, layout, layout_opts)
    return pb


def Notebook(Parent, layout="pack", **layout_opts):
    nb = ttk.Notebook(Parent)
    _apply_layout(nb, layout, layout_opts)
    return nb


def Treeview(Parent, columns, show="headings", layout="pack", **layout_opts):
    tree = ttk.Treeview(Parent, columns=columns, show=show)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    _apply_layout(tree, layout, layout_opts)
    return tree


def Separator(Parent, orient=tk.HORIZONTAL, layout="pack", **layout_opts):
    sep = ttk.Separator(Parent, orient=orient)
    _apply_layout(sep, layout, layout_opts)
    return sep


def Scrollbar(Parent, orient=tk.VERTICAL, command=None, layout="pack", **layout_opts):
    sb = tk.Scrollbar(Parent, orient=orient, command=command)
    _apply_layout(sb, layout, layout_opts)
    return sb


def _apply_layout(widget, layout, layout_opts):
    if layout == "pack":
        widget.pack(**layout_opts)
    elif layout == "grid":
        widget.grid(**layout_opts)
    elif layout == "place":
        widget.place(**layout_opts)
    else:
        raise ValueError(f"Layout inválido: {layout}")


def StringVar(root=None, value=""):
    return tk.StringVar(root, value=value)


def IntVar(root=None, value=0):
    return tk.IntVar(root, value=value)


def DoubleVar(root=None, value=0.0):
    return tk.DoubleVar(root, value=value)


def BooleanVar(root=None, value=False):
    return tk.BooleanVar(root, value=value)


def bind_event(widget, sequence, func, add=None):
    widget.bind(sequence, func, add=add)


def ask_save_file(**kwargs):
    return filedialog.asksaveasfilename(**kwargs)


def ask_save_file_obj(**kwargs):
    return filedialog.asksaveasfile(**kwargs)


def ask_yes_no(title="Confirmação", message="Deseja continuar?"):
    return messagebox.askyesno(title, message)


def ask_ok_cancel(title="Confirmação", message="Deseja continuar?"):
    return messagebox.askokcancel(title, message)


def close_window(window):
    window.destroy()


def minimize_window(window):
    window.iconify()


def maximize_window(window):
    window.state("zoomed")


def restore_window(window):
    window.state("normal")

def sidebar(Parent, width=200, bg="lightgray", layout="pack", side="left", fill="y", **layout_opts):
    sidebar_frame = tk.Frame(Parent, width=width, bg=bg)
    sidebar_frame.pack_propagate(False)
    
    if layout == "pack":
        if "side" not in layout_opts:
            layout_opts["side"] = side
        if "fill" not in layout_opts:
            layout_opts["fill"] = fill

    _apply_layout(sidebar_frame, layout, layout_opts)
    return sidebar_frame


# -------------------
# Funções de manipulação
# -------------------
def getText(Obj):
    return Obj.get("1.0", tk.END).strip()


def getValue(Obj):
    return Obj.get()


def deleteValue(Obj):
    Obj.delete(0, tk.END)


def setValue(Obj, value):
    Obj.delete(0, tk.END)
    Obj.insert(0, value)


def getSpinBoxValue(Obj):
    return Obj.get()


def getOptionMenuValue(var):
    return var.get()