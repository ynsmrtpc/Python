from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title = ("Saat")
window.geometry("485x320")
window.configure(bg="blueviolet")
window.resizable(False,False)

clock_label = Label(
    window, bg="white", fg="blueviolet", font=("Besley",72,"bold"), relief="flat"
)
clock_label.place(x=20, y=20)

def update_label():
    current_time = strftime("%H: %M: %S\n---------------\n%d-%m-%Y")
    clock_label.configure(text=current_time)
    clock_label.after(160, update_label)
    clock_label.pack(anchor="center")

update_label()
window.mainloop()