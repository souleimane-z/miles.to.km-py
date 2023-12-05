import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
def convert():
    miles_input= entry_int.get()
    km_output= miles_input * 1.61
    output_string.set(km_output)

# window
window = ttk.Window(themename= 'darkly')
window.title('Convertisseur')
window.geometry('350x150')

# title
title_label = ttk.Label(master= window,
                        text= 'Miles vers Kilomètres',
                        font= 'Calibri 24 bold'
                       )
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame,
                  textvariable=entry_int)

button = ttk.Button(master=input_frame,
                    text= 'Convertir',
                    command= convert)

entry.pack(side='left', padx=5)
button.pack(side='left')
input_frame.pack(pady=10)

# output/result
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text= 'Résultat',
                         font= 'Calibri 22',
                         textvariable=output_string)
output_label.pack(pady=5)

# run
window.mainloop()