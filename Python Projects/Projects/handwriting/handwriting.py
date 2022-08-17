import pywhatkit

with open("ornek.txt", "r", encoding="utf-8") as ornek:
    yazi = ornek.read()


print("işlem başlatıldı...")

pywhatkit.text_to_handwriting(yazi,"elyazisi.png")

print("İşlem tamamlandı!")