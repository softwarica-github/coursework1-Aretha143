import tkinter as tk
from googlesearch import search
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO

def search_google(query):
    try:
        results = list(search(query, num_results=5))
    except Exception as e:
        results = [f"Error: {e}"]
    return results

def handle_search():
    query = entry.get()
    search_button.config(text="Searching...", state="disabled")
    search_results = search_google(query)
    clear_results()
    result_count_label.config(text=f"Total results: {len(search_results)}")
    for i, result in enumerate(search_results):
        result_label = tk.Label(
            root,
            text=result,
            wraplength=600,
            justify='left',
            fg="#075e54",
            cursor="hand2",
            font=("Arial", 12, "italic"),
            bg="#ffffff"
        )
        result_label.bind("<Button-1>", lambda e, link=result: open_link(link))
        result_label.place(x=20, y=180 + (i * 30))
        result_label.update()
        # Animation
        result_label.config(fg="#128C7E")
        result_label.after(100, lambda label=result_label: label.config(fg="#075e54"))
        result_labels.append(result_label)
    search_button.config(text="Search", state="normal")

def open_link(link):
    webbrowser.open_new_tab(link)

def clear_results():
    for label in result_labels:
        label.destroy()
    result_labels.clear()

def display_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((100, 100), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        image_label = tk.Label(root, image=img_tk, bg="#ffffff")
        image_label.image = img_tk
        image_label.place(x=650, y=180)
        image_labels.append(image_label)
    except Exception as e:
        print(f"Error: {e}")

root = tk.Tk()
root.title("Google Search Chatbot")
root.geometry("900x700")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Enter your query:", bg="#f0f0f0", fg="#075e54", font=("Arial", 16, "bold"))
label.place(x=20, y=20)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.place(x=20, y=60)

search_button = tk.Button(root, text="Search", command=handle_search, bg="#25D366", fg="#ffffff", activebackground="#128C7E", activeforeground="#ffffff", font=("Arial", 12), cursor="hand2")
search_button.place(x=350, y=56)

result_count_label = tk.Label(root, text="Total results: 0", bg="#f0f0f0", fg="#075e54", font=("Arial", 12))
result_count_label.place(x=20, y=110)

result_labels = []
image_labels = []

# Example usage of displaying image
# Replace this URL with the actual URL of the image you want to display
image_url = "https://example.com/image.jpg"
display_image(image_url)

root.mainloop()
