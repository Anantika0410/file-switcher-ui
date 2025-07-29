import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Sample data
open_files = ["main.py", "app.py", "ui.py", "readme.md"]
tool_windows = ["Terminal", "Output", "Debug Console", "File Explorer"]

class FileSwitcherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("✨ File Switcher UI")
        self.geometry("500x350")
        self.configure(bg="#1e1e2e")

        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        # Custom styles
        self.style.configure("TNotebook", background="#1e1e2e", borderwidth=0)
        self.style.configure("TNotebook.Tab", background="#3b3b4f", foreground="white", padding=10)
        self.style.map("TNotebook.Tab", background=[("selected", "#5e60ce")])

        self.style.configure("TFrame", background="#1e1e2e")
        self.style.configure("TButton", background="#5e60ce", foreground="white", font=("Segoe UI", 10, "bold"))
        self.style.map("TButton", background=[("active", "#7c83f5")])

        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self, text="🔄 File & Tool Switcher", font=("Segoe UI", 16, "bold"), foreground="white", background="#1e1e2e")
        title.pack(pady=15)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both', padx=15, pady=10)

        file_frame = ttk.Frame(notebook)
        notebook.add(file_frame, text='🗂️ Open Files')
        for file in open_files:
            ttk.Button(file_frame, text=file, command=lambda f=file: self.select_item(f)).pack(pady=6, padx=10)

        tool_frame = ttk.Frame(notebook)
        notebook.add(tool_frame, text='🧰 Tool Windows')
        for tool in tool_windows:
            ttk.Button(tool_frame, text=tool, command=lambda t=tool: self.select_item(t)).pack(pady=6, padx=10)

    def select_item(self, name):
        print(f"Switched to: {name}")
        messagebox.showinfo("Switched", f"You selected: {name}")

if __name__ == "__main__":
    app = FileSwitcherApp()
    app.mainloop()


