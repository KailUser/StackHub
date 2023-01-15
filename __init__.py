import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import time
class StackRu:
    def OverRu():
        os.system("clear")
        print("""
░██████╗████████╗░█████╗░░█████╗░██╗░░██╗░█████╗░██╗░░░██╗███████╗██████╗░███████╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗░░░██████╗░██╗░░░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔════╝██║░░░░░██╔══██╗░██║░░██╗░░██║░░░██╔══██╗██║░░░██║
╚█████╗░░░░██║░░░███████║██║░░╚═╝█████═╝░██║░░██║╚██╗░██╔╝█████╗░░██████╔╝█████╗░░██║░░░░░██║░░██║░╚██╗████╗██╔╝░░░██████╔╝██║░░░██║
░╚═══██╗░░░██║░░░██╔══██║██║░░██╗██╔═██╗░██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗██╔══╝░░██║░░░░░██║░░██║░░████╔═████║░░░░██╔══██╗██║░░░██║
██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██║░░░░░███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░██╗██║░░██║╚██████╔╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░""")
        print("File Name")
        name_file = input()
        file = open(f'{name_file}.html', 'w', encoding='utf-8')
        print("Ваш айди на StackOverFlow.Ru:")
        url = input("") # replace with the URL of the website you want to scrape
        print("Имя на StackOverFlow.Ru:")
        url_name = str.lower(input())
        url2 = f"https://ru.stackoverflow.com/users/{url}/{url_name}?tab=profile"

        # Make a request to the website
        
        response = requests.get(url2)

        # Parse the HTML content
        soup = bs(response.content, "html.parser")

        # Find the elements with the class "d-flex flex__allitems6 gs16 fw-wrap md:jc-space-between"
        data = soup.find_all("div", class_="d-flex flex__allitems6 gs16 fw-wrap md:jc-space-between")

        # Print the data, you can use it for whatever you want

        saved = file.write(str(data))
        print(f"File Saved to {name_file}.html")
        file.close
        input("Press Enter to exit")
class StackEng:
    def OverEng():
        os.system("clear")
        print("""
░██████╗████████╗░█████╗░░█████╗░██╗░░██╗░█████╗░██╗░░░██╗███████╗██████╗░███████╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗░░░███████╗███╗░░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔════╝██║░░░░░██╔══██╗░██║░░██╗░░██║░░░██╔════╝████╗░██║
╚█████╗░░░░██║░░░███████║██║░░╚═╝█████═╝░██║░░██║╚██╗░██╔╝█████╗░░██████╔╝█████╗░░██║░░░░░██║░░██║░╚██╗████╗██╔╝░░░█████╗░░██╔██╗██║
░╚═══██╗░░░██║░░░██╔══██║██║░░██╗██╔═██╗░██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗██╔══╝░░██║░░░░░██║░░██║░░████╔═████║░░░░██╔══╝░░██║╚████║
██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██║░░░░░███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░██╗███████╗██║░╚███║
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝""")
        print("File Name")
        name_file = input()
        file = open(f'{name_file}.html', 'w', encoding='utf-8')
        print("Your User ID on Stackoverflow:")
        url = input("") # replace with the URL of the website you want to scrape
        print("Your Name on Stackoverflow")
        url_name = str.lower(input())
        url2 = f"https://stackoverflow.com/users/{url}/{url_name}?tab=profile"

        # Make a request to the website
        
        response = requests.get(url2)

        # Parse the HTML content
        soup = bs(response.content, "html.parser")

        # Find the elements with the class "d-flex flex__allitems6 gs16 fw-wrap md:jc-space-between"
        data = soup.find_all("div", class_="d-flex flex__allitems6 gs16 fw-wrap md:jc-space-between")

        # Print the data, you can use it for whatever you want

        saved = file.write(str(data))
        print(f"File Saved to {name_file}.html")
        file.close
        input("Press Enter to exit")
#Create KailUser(☄ S͇͇y͇͇i͇͇r͇͇e͇͇z͇͇z͇͇ ☄#2023)
