import tkinter as tk
from tkinter import ttk
import UI.library_ui as vui  # sua UI library importada

def main():
    root = vui.Window(
        UIName="UI Library Demo - Complete",
        Dimensions="1280x720",
        ResizableX=True,
        ResizableY=True,
        bgColor="#f0f0f0",
        opacity=1,
        topMost=False,
        fullscreen=True,
        
    )

    # Variables for some widgets
    var_check = vui.BooleanVar(root, value=False)
    var_radio = vui.StringVar(root, value="option1")
    var_option = vui.StringVar(root, value="Option 1")

    # Frame to hold inputs
    input_frame = vui.Frame(root, bg="white")
    input_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=False)

    # Create widgets WITHOUT pack, so we can grid them
    lbl_name = vui.LabelNoPack(input_frame, text="Name:", fg="black", bg="white", font=("Arial", 12))
    entry_name = vui.EntryNoPack(input_frame, width=30, bg="white", fg="black", font=("Arial", 12))

    chk_subscribe = vui.CheckbuttonNoPack(input_frame, text="Subscribe to newsletter", variable=var_check, bg="white")

    rb1 = vui.RadioButtonNoPack(input_frame, text="Option 1", variable=var_radio, value="option1", bg="white")
    rb2 = vui.RadioButtonNoPack(input_frame, text="Option 2", variable=var_radio, value="option2", bg="white")

    opt_menu = vui.OptionMenuNoPack(input_frame, var_option, ["Option 1", "Option 2", "Option 3"])

    spin_age = vui.SpinBoxNoPack(input_frame, from_=0, to=100)
    spin_age.delete(0, tk.END)
    spin_age.insert(0, "25")

    txt_comments = vui.TextNoPack(input_frame, width=40, height=5)

    # Use grid for layout inside input_frame
    lbl_name.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_name.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    chk_subscribe.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

    rb1.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    rb2.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    opt_menu.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    spin_age.grid(row=3, column=1, sticky="w", padx=5, pady=5)

    txt_comments.grid(row=4, column=0, columnspan=2, sticky="w", padx=5, pady=5)

    # Dictionary of widgets and variables to save/load
    widgets_to_save = {
        "name": entry_name,
        "subscribe": var_check,
        "choice": var_radio,
        "dropdown": var_option,
        "age": spin_age,
        "comments": txt_comments,
    }

    # Log Text widget on bottom
    log_text = vui.Text(root, width=100, height=15)
    log_text.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

    def save_data():
        vui.save_all_widgets("UI/config/config.json", widgets_to_save, log_widget=log_text)
        vui.Popup("info", title="Save", message="Data saved successfully!")

    def load_data():
        vui.load_all_widgets("UI/config/config.json", widgets_to_save, log_widget=log_text)
        vui.Popup("info", title="Load", message="Data loaded successfully!")
        
    def clear_widgets():
        vui.clear_fields(widgets_to_save)

    # Buttons frame
    buttons_frame = vui.Frame(root, bg="#ddd")
    buttons_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

    btn_save = vui.Button(buttons_frame, text="Save Data", callback=save_data)
    if vui.check_file_exists("UI/config/config.json"):
        load_data()

    btn_clear_fields = vui.Button(buttons_frame, text="Clear Fields", callback=clear_widgets)


    # Menu bar with About and Exit
    def on_about():
        vui.Popup("info", title="About", message="UI Library Demo\nAuthor: Your Name")

    def on_exit():
        if vui.ask_yes_no(title="Exit", message="Do you really want to exit?"):
            root.destroy()

    menus = [
        ("File", [("Exit", on_exit)]),
        ("Help", [("About", on_about)]),
    ]
    vui.MenuDeBarra(root, menus, tearoff=0)

    root.mainloop()

if __name__ == "__main__":
    main()