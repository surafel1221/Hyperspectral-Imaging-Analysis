import tkinter as tk
from tkinter import Label,Button,simpledialog
from src import start_scan


    
def on_start_scanning_click():
    camera_fps = simpledialog.askinteger("Input","Enter the Camera FPS:",
                                parent=root, minvalue=1,maxvalue=100)
    
    rail_speed = simpledialog.askfloat("Input", "Enter the speed of the rail in mm/s (e.g., 1 for 1mm/s):",
                                       parent=root, minvalue=0.1, maxvalue=100.0)
   
    rail_length = simpledialog.askfloat("Input", "Enter the total length of the scan area in mm (e.g., 2360 for 2.36 meters):",
                                        parent=root, minvalue=1.0, maxvalue=10000.0)


    if camera_fps is not None and rail_speed is not None and rail_length is not None:
        try:
            start_scan(camera_fps, rail_speed, rail_length)
            print("Scanning started!")
        except Exception as e:
            print(f"Error during scanning: {e}")
    else:
        print("Scanning canceled or incomplete input.")





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