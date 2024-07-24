import tkinter as tk
import json
import requests
root = tk.Tk()
root.title("Quotes App")
root.geometry("800x800")

def createlist(root, items):
    listbox = tk.Listbox(root)
    listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    for i in items:
        listbox.insert(tk.END, i)


url = "https://jsonguide.technologychannel.org/quotes.json"
f = requests.get(url)
quotes = json.loads(f.text)
quotes_list = []

for quote in quotes:
    quotes_list.append(quote["text"])

for i in range(len(quotes_list)):
    quotes_list.append(quotes_list[i])
    
createlist(root, quotes_list)
root.mainloop()