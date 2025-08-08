import tkinter as tk
import json
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox, filedialog, colorchooser, simpledialog
from pathlib import Path
import json

ConfigFolder = Path("./UI/config")
DebugFolder = Path("./UI/debug")
ImagesFolder = Path("./UI/images")

# -------------------
# Window
# -------------------
def Window(
    UIName="Janela",
    Dimensions="1280x720",
    ResizableX=True,
    ResizableY=True,
    iconPath=None,
    bgColor="white",
    fullscreen=False,
    topMost=False,
    lMin=200,
    aMin=200,
    lMax=1920,
    aMax=720,
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
    root.minsize(lMin, aMin)
    root.maxsize(lMax, aMax)
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


def sidebar(
    Parent,
    width=200,
    bg="lightgray",
    layout="pack",
    side="left",
    fill="y",
    **layout_opts,
):
    sidebar_frame = tk.Frame(Parent, width=width, bg=bg)
    sidebar_frame.pack_propagate(False)

    if layout == "pack":
        if "side" not in layout_opts:
            layout_opts["side"] = side
        if "fill" not in layout_opts:
            layout_opts["fill"] = fill

    _apply_layout(sidebar_frame, layout, layout_opts)
    return sidebar_frame

def LabelNoPack(Parent, **kwargs):
    return tk.Label(Parent, **kwargs)

def EntryNoPack(Parent, **kwargs):
    return tk.Entry(Parent, **kwargs)

def CheckbuttonNoPack(Parent, **kwargs):
    return tk.Checkbutton(Parent, **kwargs)

def RadioButtonNoPack(Parent, **kwargs):
    return tk.Radiobutton(Parent, **kwargs)

def OptionMenuNoPack(Parent, variable, options):
    option_menu = tk.OptionMenu(Parent, variable, *options)
    return option_menu

def SpinBoxNoPack(Parent, **kwargs):
    spinbox = tk.Spinbox(Parent, **kwargs)
    return spinbox

def TextNoPack(Parent, **kwargs):
    return tk.Text(Parent, **kwargs)


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


# -------------------
# Função de Salvar botões
# -------------------

def save_to_json(filename, data_dict):
    with open(filename, "w") as f:
        json.dump(data_dict, f, indent=4)


def load_from_json(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def logTXT(text_widget, message):
    if text_widget:
        try:
            text_widget.insert(tk.END, message + "\n")
            text_widget.see(tk.END)
        except Exception:
            pass
    Filename = "./UI/debug/log.txt"

def _log(message, log_widget=None):
    logTXT(log_widget, message)

def save_all_widgets(filename, widgets_dict, log_widget=None):
    data = {}
    _log(f"Saving widgets to {filename}...", log_widget)
    for key, widget in widgets_dict.items():
        try:
            if isinstance(widget, tk.Entry):
                data[key] = widget.get()
            elif isinstance(widget, tk.Text):
                data[key] = widget.get("1.0", tk.END).rstrip('\n')
            elif isinstance(widget, ttk.Combobox):
                data[key] = widget.get()
            elif isinstance(widget, tk.Spinbox):
                data[key] = widget.get()
            elif isinstance(widget, (tk.IntVar, tk.StringVar, tk.BooleanVar, tk.DoubleVar)):
                data[key] = widget.get()
            else:
                try:
                    data[key] = widget.get()
                except Exception:
                    data[key] = None
            _log(f"  [{key}] -> {data[key]!r}", log_widget)
        except Exception as e:
            _log(f"  Failed to read widget {key}: {e}", log_widget)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        _log(f"Saved {len(data)} values to {filename}.", log_widget)
    except Exception as e:
        _log(f"Error saving file {filename}: {e}", log_widget)

def load_all_widgets(filename, widgets_dict, log_widget=None):
    _log(f"Loading widgets from {filename}...", log_widget)
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        _log(f"File not found: {filename}", log_widget)
        return
    except Exception as e:
        _log(f"Error reading {filename}: {e}", log_widget)
        return

    for key, widget in widgets_dict.items():
        if key not in data:
            _log(f"Key {key} not in saved data, skipping.", log_widget)
            continue

        value = data[key]
        _log(f"\nKey: {key}", log_widget)
        _log(f"  Widget type: {type(widget)}", log_widget)
        _log(f"  Saved value (from file): {value!r}", log_widget)

        # Combobox first (ttk.Combobox subclasses Entry)
        if isinstance(widget, ttk.Combobox):
            _log("  Matched: ttk.Combobox", log_widget)
            try:
                combo_values = widget.cget('values')
            except Exception:
                combo_values = widget['values']
            _log(f"  Combobox values: {combo_values!r}", log_widget)

            try:
                values_list = list(combo_values)
            except Exception:
                try:
                    values_list = list(widget['values'])
                except Exception:
                    values_list = []

            if value in values_list:
                index = values_list.index(value)
                _log(f"  Value found in combobox values at index {index}, calling current({index})", log_widget)
                try:
                    widget.current(index)
                except Exception as e:
                    _log(f"  widget.current failed: {e} -> trying widget.set(value)", log_widget)
                    widget.set(value)
            else:
                _log("  Value NOT found in combobox values, calling set(value) to show it anyway", log_widget)
                try:
                    widget.set(value)
                except Exception as e:
                    _log(f"  widget.set failed: {e}", log_widget)

        elif isinstance(widget, tk.Entry):
            _log("  Matched: tk.Entry", log_widget)
            try:
                widget.delete(0, tk.END)
                widget.insert(0, value)
            except Exception as e:
                _log(f"  Failed to set Entry: {e}", log_widget)

        elif isinstance(widget, tk.Text):
            _log("  Matched: tk.Text", log_widget)
            try:
                widget.delete("1.0", tk.END)
                widget.insert("1.0", value)
            except Exception as e:
                _log(f"  Failed to set Text: {e}", log_widget)

        elif isinstance(widget, tk.Spinbox):
            _log("  Matched: tk.Spinbox", log_widget)
            try:
                widget.delete(0, tk.END)
                widget.insert(0, value)
            except Exception as e:
                _log(f"  Failed to set Spinbox: {e}", log_widget)

        elif isinstance(widget, (tk.IntVar, tk.StringVar, tk.BooleanVar, tk.DoubleVar)):
            _log("  Matched: Variable (IntVar/StringVar/BooleanVar/DoubleVar)", log_widget)
            try:
                widget.set(value)
            except Exception as e:
                _log(f"  Failed to set Variable: {e}", log_widget)

        else:
            _log("  No exact match, trying generic widget.set(value)", log_widget)
            try:
                widget.set(value)
                _log("  generic set succeeded", log_widget)
            except Exception as e:
                _log(f"  generic set failed: {e}", log_widget)

def clear_fields(widgets_dict):
    for widget in widgets_dict.values():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        elif isinstance(widget, tk.BooleanVar):
            widget.set(False)
        elif isinstance(widget, tk.StringVar):
            widget.set("")
        elif isinstance(widget, tk.Spinbox):
            widget.delete(0, tk.END)
            widget.insert(0, "0")
        elif isinstance(widget, tk.Text):
            widget.delete("1.0", tk.END)
    Popup("info", title="Clear", message="Fields cleared!")
    
def check_file_exists(file):
    filename = file
    if Path(filename).exists():
        return True