import tkinter as tk

window = tk.Tk()

window.title("Egg Timer")
window.configure(background='azure')
window.geometry('800x500')

output_label = Label(window,text="Your eggs are ready!!!!")

output_label.pack()

window.mainloop()
