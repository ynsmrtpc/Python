import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk

# window = Tk()
# window.title = ("IMDB Top-250")
# # window.geometry("720x1080")
# window.configure(bg="white")
# window.resizable(True,True)
# ratingLabel = Label(
#     window, bg="white", fg="blueviolet", font=("Besley",24,"bold"), relief="flat"
# )
# bodyLabel = Label(
#     window, bg="white", fg="black", font=("Besley",20,"italic"), relief="flat"
# )

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

raitingInput = float(input("Raiting'i Girin: "))

i = 1
for baslik, rating in zip(basliklar,ratingler):
    baslik = baslik.text
    baslik = baslik.strip()
    baslik = baslik.replace("\n","")
    baslik = baslik.split(".")
    rating = rating.text
    rating = rating.strip()
    rating = rating.replace("\n","")
    if float(rating) > raitingInput:
        print("{}.".format(i) , baslik[1].lstrip(), " -- IMDB Puanı: ", rating)
    i += 1
    # bodyLabel.configure(text=baslik[1])
    # ratingLabel.configure(text=rating)
    # ratingLabel.pack(anchor="center")
    # bodyLabel.pack(anchor="center")

# window.mainloop()
x = input()