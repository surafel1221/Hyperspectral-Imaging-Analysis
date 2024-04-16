import tkinter as tk
from tkinter import ttk
import sv_ttk
from View_Cube.Visualize import App 

def start_action():
    global new_page
    main_frame.pack_forget()  
    new_page = App(root)  
    new_page.pack(fill='both', expand=True)  
    

        
root = tk.Tk()
root.title("Hyperspectral Imaging Device")  

root.geometry("700x700")

sv_ttk.set_theme("dark")

main_frame = ttk.Frame(root, style='TFrame')
main_frame.pack(expand=True, fill=tk.BOTH)
main_frame.columnconfigure(0, weight=1)

main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.rowconfigure(4, weight=1)

welcome_label = ttk.Label(main_frame, text="Welcome To Our Project!", font=("Arial", 16, "bold"), anchor='center')
welcome_label.grid(row=1, column=0, sticky=tk.NSEW)

subtitle_label = ttk.Label(main_frame, text="Hyperspectral Imaging Camera (HIC)", font=("Arial", 14), anchor='center')
subtitle_label.grid(row=2, column=0, sticky=tk.NSEW)

info_label = ttk.Label(main_frame, 
                       text="Click 'Start' to begin your journey.",
                       font=("Arial", 10), 
                       justify="center",
                       anchor='center',
                       wraplength=500)  
info_label.grid(row=3, column=0, sticky=tk.NSEW)

button = ttk.Button(main_frame, text="Start", command=start_action)
button.grid(row=4, column=0, sticky=tk.EW)

main_frame.rowconfigure(0, weight=2)
main_frame.rowconfigure(5, weight=2)

new_page = ttk.Frame(root, style='TFrame')
new_page.columnconfigure(0, weight=1)
new_page.rowconfigure(0, weight=1)  

new_page_label = ttk.Label(new_page, text="New Page Content Goes Here", font=("Arial", 16, "bold"), anchor='center')
new_page_label.grid(row=0, column=0, sticky=tk.NSEW)



root.mainloop()