from importlib.resources import contents
from turtle import title
import requests
from bs4 import BeautifulSoup
import pprint
import json
pages = ['ktc-intern-data-science','ktc-intern-digital-marketing','ktc-intern-entrepreneurship','ktc-intern-marketing', 'ktc-intern-technology', 'ktc-intern-ux'] # list of pages to be scraped
bloglist = {} #set that will contain the program and concepts
def getProgram(page):   
        url = f"https://knowthychoice.in/blog/{page}/"  #URL of the pages 
        r = requests.get(url)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, "html.parser")
        parent = soup.find("article", class_="blog-single-post")

        program = parent.find("h2").text   #Name of the program being fetched
        content = parent.select("ul:nth-of-type(4)")   #Selecting the class of the concepts

        concepts = list()
        for li in content[0].find_all("li"):   #Selecting each concept
                concepts.append(li.text)
        
        blog = {
                program : concepts,   # Key and value pair
        }
        bloglist.update(blog)    #Add elements in dictionary
        return

for page in pages:
        getProgram(page)

pretty = pprint.PrettyPrinter(width= 500)
pretty.pprint(bloglist)  #Printing the set
