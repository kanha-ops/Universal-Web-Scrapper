import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Function to perform web scraping
def scrape_website():
    url = entry_url.get()

    try:
        data = {'title' : [] , 'price' :[]}

        
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text,'html.parser')

        spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
        prices = soup.select("span.a-price")
        for span in spans:
            # print(span.string)
            data["title"].append(span.string)

        for price in prices:
            if not ("a-text-price" in price.get("class")):
                # print(price.find("span").get_text())
                data["price"].append(price.find("span").get_text())
        #  if len(data["price"])==len(data["title"]):
        #     break


        df = pd.DataFrame.from_dict(data) 

        df.to_excel("data.xlsx",index=False)   

        messagebox.showinfo("Scraping and Saving", "Product data scraped and saved to 'data.xlsx'")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def scrape_website2():
    url = entry_url.get()

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extracting all paragraph text and displaying it in a messagebox
        paragraphs = soup.find_all('p')
        text = '\n'.join([p.get_text() for p in paragraphs])

        messagebox.showinfo("Web Scraping Result", text)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main application window
app = tk.Tk()
app.title("Web Scraper")

# Create and place widgets (labels, entry, button)
label_url = tk.Label(app, text="Enter URL:")
label_url.pack()

entry_url = tk.Entry(app, width=40)
entry_url.pack()

button_scrape = tk.Button(app, text="Scrape Data to excel", command=scrape_website)
button_scrape.pack()

button_scrape2 = tk.Button(app, text="Scrape Only Text", command=scrape_website2)
button_scrape2.pack()

# Start the main application loop
app.mainloop()
