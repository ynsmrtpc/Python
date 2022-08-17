import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk

window = Tk()
window.title = ("Şiir")
# window.geometry("720x1080")
window.configure(bg="white")
window.resizable(True,True)

titleLabel = Label(
    window, bg="white", fg="blueviolet", font=("Besley",24,"bold"), relief="flat"
)
# titleLabel.place(x=50, y=50)

bodyLabel = Label(
    window, bg="white", fg="black", font=("Besley",12,"italic"), relief="flat"
)
# bodyLabel.place(x=50, y=50)

# scroll = Scrollbar()
# scroll.pack(side="right",fill="y")

def randomPoem():
    url = "https://www.antoloji.com/siir/rastgele/"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,"html.parser")
    title = soup.find("div", attrs={"class": "pd-title-a"})
    content = soup.find("div", attrs={"class": "pd-text"})

    titleLabel.configure(text=title.text)
    bodyLabel.configure(text=content.text)
    titleLabel.pack(anchor="center")
    bodyLabel.pack(anchor="center") # ,yscrollcommand=scroll.set

# scroll.config(command=bodyLabel.yview)
button = tk.Button(window,text="Rastgele Şiir Gelsin",command=randomPoem)
button.pack(side="bottom")

window.mainloop()