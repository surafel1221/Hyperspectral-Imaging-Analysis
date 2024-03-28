import tkinter as tk
from tkinter import Label,Button
def on_start_button_click():
    print("Start button clicked!") 
    
def on_start_scanning_click():
    print("Start Scanning clicked!")

def on_run_example_click():
    print("Run Example clicked!")

def on_view_cube_click():
    print("View Cube clicked!")

def on_exit_click():
    root.destroy()
    
        
def main():
    global root
    root = tk.Tk()
    root.title("Hyperspectral Imaging System")
    root.geometry("700x400")
    root.configure(background='light gray')  

    lbl = Label(root, text="Welcome To Hyperspectral Imaging Analysis",
                font=("Arial", 16, "bold"),
                bg='light gray',  
                fg='dark blue')
    lbl.grid(padx=20, pady=20, sticky="ew", columnspan=2)  

   
    button_font = ("Arial", 12)
    button_bg = "light blue"
    button_fg = "black"

    buttons = [
        ("Start Scanning", on_start_scanning_click),
        ("Run Example", on_run_example_click),
        ("View Cube", on_view_cube_click),
        ("Exit", on_exit_click)
    ]

    for i, (text, command) in enumerate(buttons):
        btn = Button(root, text=text, font=button_font, command=command, bg=button_bg, fg=button_fg)
        btn.grid(row=i+1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    root.grid_rowconfigure(len(buttons) + 1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()