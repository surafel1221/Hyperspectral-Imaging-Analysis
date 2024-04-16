import tkinter as tk
from tkinter import ttk
import sv_ttk
from StartPoint import sserial, initialize, MoveLeft, Light



class ScanningParams(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Scanning Parameters", padding=15)
        self.grid(sticky="ew")
        self.setup_widgets()

    def setup_widgets(self):
        ttk.Label(self, text="Length:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        length_options = ["50mm", "100mm"]
        self.length_var = tk.StringVar()
        length_combobox = ttk.Combobox(self, textvariable=self.length_var, values=length_options, state="readonly")
        length_combobox.current(0)
        length_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(self, text="Speed:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        speed_options = ["1 mm/s", "5mm/s","1mm/s" ]  
        self.speed_var = tk.StringVar()
        speed_combobox = ttk.Combobox(self, textvariable=self.speed_var, values=speed_options, state="readonly")
        speed_combobox.current(0)
        speed_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        
class CheckBoxDemo(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Start Point", padding=15)
        self.add_widgets()

    def add_widgets(self):
        greeting_label = ttk.Label(self, text="Position to starting point by moving it 1 or 5 meters left, or 1 or 5 meters right.", font=("Helvetica", 13, "italic"))
        greeting_label.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 10))

class MovementButton(ttk.LabelFrame):
    def __init__(self, parent, direction, move_command):
        super().__init__(parent, text=f"Move {direction}", padding=15)
        self.ser = sserial()  
        self.add_widgets(move_command)

    def add_widgets(self, move_command):
        ttk.Button(self, text="One Meter", command=lambda: move_command(self.ser, 1000)).grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        ttk.Button(self, text="Five Meters", command=lambda: move_command(self.ser, 5000)).grid(row=1, column=0, sticky="ew", padx=10, pady=5)

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=15)
        self.parent = parent
        self.setup_layout()

    def setup_layout(self):
        self.grid(sticky="nsew")
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)
        
        

        CheckBoxDemo(self).grid(row=0, column=0, columnspan=2, sticky="nsew", padx=(0, 10), pady=(0, 10))
        MovementButton(self, "Left", MoveLeft).grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        MovementButton(self, "Right", lambda ser, x: MoveLeft(ser, -x)).grid(row=1, column=1, sticky="nsew", padx=(0, 10))

        ttk.Button(self, text="Finish", command=self.finish_action).grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

    def finish_action(self):
        for widget in self.winfo_children():
            widget.destroy()
        Appp(self.parent).pack(fill='both', expand=True)

class Appp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.parent = parent
        self.setup_layout()

    def setup_layout(self):
        ScanningParams(self).grid(row=0, column=0, columnspan=2, sticky="nsew")
        MovementButton(self, "Left", MoveLeft).grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        MovementButton(self, "Right", lambda ser, x: MoveLeft(ser, -x)).grid(row=1, column=1, sticky="nsew", padx=(0, 10))
        
        ttk.Button(self, text="Start Scanning", command=self.back_action).grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

    def back_action(self):
        self.destroy()
        App(self.parent).pack(fill='both', expand=True)

def main():
    root = tk.Tk()
    root.title("Hyperspectral Imaging Device")
    root.geometry("800x400")
    sv_ttk.set_theme("dark")
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    app = App(root)
    app.pack(expand=True, fill='both')

    root.mainloop()
if __name__ == "__main__":
    main()
    
