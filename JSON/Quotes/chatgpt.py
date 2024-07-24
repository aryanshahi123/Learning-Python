import tkinter as tk
import json
import requests

def create_card(frame, quote):
    card = tk.Frame(frame, bg="#ffffff", bd=2, relief="raised")
    card.pack(pady=10, padx=10, fill=tk.X)

    label = tk.Label(card, text=quote, wraplength=700, bg="#ffffff", fg="#333333", font=("Helvetica", 12), padx=10, pady=10)
    label.pack(fill=tk.X)

root = tk.Tk()
root.title("Quotes App")
root.geometry("800x800")
root.configure(bg="#f0f0f0")

url = "https://jsonguide.technologychannel.org/quotes.json"
f = requests.get(url)
quotes = json.loads(f.text)
quotes_list = [quote["text"] for quote in quotes]

canvas = tk.Canvas(root, bg="#f0f0f0")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

for quote in quotes_list:
    create_card(scrollable_frame, quote)

root.mainloop()
