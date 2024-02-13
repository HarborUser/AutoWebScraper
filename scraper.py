import tkinter as tk

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from html.parser import HTMLParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="Enter Website:", anchor="w")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit", command = self.scape)
        self.output = tk.Label(self, text="")

        # lay the widgets out on the screen. 
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")

    def scape(self):
        

        try:
            i = self.entry.get()
            driver = webdriver.Chrome()

            driver.get(i)
            html = driver.page_source
           
            
            soup = BeautifulSoup(html, "html.parser")

            
            with open("Scaped_data.txt", "w", encoding='utf-8') as file:
                for pull in soup.find_all(["p","h2","li","td"]):
                    text_data = pull.text
                    file.write(f"{text_data}")
            
        except ValueError:
            result = "Please enter digits only"

        # set the output widget to have our result
        self.output.configure(text="Data has Been Scraped")

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tk Example")
    root.configure(background="blue")
    root.minsize(200, 200)  # width, height
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")
    Example(root).pack(fill="both", expand=True)
    root.mainloop()