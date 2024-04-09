import tkinter as tk
from tkinter import Label,Button,simpledialog, messagebox  
from Scanning import start_scan
from Example.Run_example import load_dispaly_Cube
from Example.Run_example import Display_RGB


    
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


        image_path = 'C:\\Users\\suraf\\Desktop\\Hyperspectral-Imaging-Analysis\\src\\Example\\92AV3C (2).lan'



def on_run_example_click():
    try:
        image_path = 'C:\\Users\\suraf\\Desktop\\Hyperspectral-Imaging-Analysis\\src\\Example\\92AV3C (2).lan'

        new_window = tk.Toplevel(root)
        new_window.title("Display Options")
        new_window.geometry("300x150")  # You can adjust the size as needed

        button_font = ("Arial", 12)
        button_bg = "light blue"
        button_fg = "black"

        raw_cube_btn = tk.Button(new_window, text="Display Raw Cube", font=button_font, bg=button_bg, fg=button_fg, 
                                 command=lambda: load_dispaly_Cube(image_path))
        raw_cube_btn.pack(pady=10)  
        rgb_btn = tk.Button(new_window, text="Display RGB", font=button_font, bg=button_bg, fg=button_fg, 
                            command=lambda: Display_RGB(image_path, root))
        rgb_btn.pack(pady=10)  

        print("Run Example operation completed successfully!")
    except Exception as e:
        print(f"Error during Run Example operation: {e}")
 

def on_view_cube_click():
    print("View Cube clicked!")

def on_exit_click():
    root.destroy()

def on_click_alinmnet():
    Alignment()
    
        
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
        ("Alignment", on_click_alinmnet),
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
