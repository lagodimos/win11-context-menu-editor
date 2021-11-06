import winreg
import tkinter as tk
import tkinter.ttk as ttk
import os

def make_registry_changes(option, restart_windows_explorer):

    if option == "classic_context_menu":
        
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32")
        winreg.SetValue(winreg.HKEY_CURRENT_USER, "Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32", winreg.REG_SZ, "")

    elif option == "new_context_menu":
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, "Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32")
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, "Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}")
        except:
            pass

    if restart_windows_explorer:
        os.system("Taskkill /IM \"explorer.exe\" /F & start explorer")

window = tk.Tk()

window.title("Context menu editor")
window.geometry("280x170")
window.resizable(False, False)

restart_explorer_var = tk.IntVar()
restart_explorer_var.set(1)

menu_var = tk.StringVar()
menu_var.set("classic_context_menu")

set_context_menu = ttk.Label(window, text=" Set context menu to:")
restart_explorer = ttk.Checkbutton(window, text="Restart Explorer",variable=restart_explorer_var, takefocus=False)
classic_menu_option = ttk.Radiobutton(window, text="Classic context menu", value="classic_context_menu", variable=menu_var, takefocus=False)
new_menu_option = ttk.Radiobutton(window, text="New context menu", value="new_context_menu", variable=menu_var, takefocus=False)
apply_changes = ttk.Button(window, text=" Apply\nChanges", command = lambda: make_registry_changes(menu_var.get(), restart_explorer_var.get()), takefocus=False)
message = ttk.Label(window, text="Changes will apply only to current user.")



set_context_menu.place(x=10, y=20)
restart_explorer.place(x=160, y=30)
classic_menu_option.place(x=10, y=50)
new_menu_option.place(x=10, y=70)
apply_changes.place(x=170, y=75)
message.place(x=15, y=140)

window.mainloop()