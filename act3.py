import random

# Respon dalam dictionary
respons = {
    "hai": ["Halo", "welcome"],
    "nama kamu siapa?": ["saya chatbot", "saya kiper"],
    "bye": ["sampai jumpa", "bye"]
}

# function yg bisa dipanggil
def chatbot():
    while True:
        user_input = input("kamu: ")
        if user_input in respons:
            print("Bot:", random.choice(respons[user_input]))
        elif user_input == "keluar":
            print("Bot: Sampai jumpa")
            break
        else:
            print("Bot: maaf saya tidak mengerti")

chatbot()
