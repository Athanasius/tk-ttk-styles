import tkinter as tk
from tkinter import ttk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Theme Example")
        self.style = ttk.Style(self)
        # Get the available themes
        themes = self.style.theme_names()
        print(themes)
        # Set the default theme
        self.theme_var = tk.StringVar()
        self.theme_var.set("default")
        self.style.theme_use(self.theme_var.get())

        # Some text to make a decently sized window
        label = ttk.Label(self, text='Select a theme to activate from those below:')
        label.pack()
        # Create a frame to hold the radio buttons
        theme_frame = ttk.LabelFrame(self, text="Themes")
        theme_frame.pack(padx=10, pady=10)
        # Create a radio button for each theme
        for theme in themes:
            rb = ttk.Radiobutton(theme_frame, text=theme, value=theme, variable=self.theme_var, command=self.change_theme)
            # rb.bind("<ButtonRelease>", self.change_theme)
            rb.pack(expand=True, fill='both')

    def change_theme(self):
        # Set the new theme
        self.style.theme_use(self.theme_var.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()
