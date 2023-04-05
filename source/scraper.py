import httpx
from selectolax.parser import HTMLParser
import os
import datetime




def get_html():
    try:
        url = "https://www.larepublica.co/"
        response = httpx.get(url)
        if response.status_code == 200:
            return HTMLParser(response.text)
        
        else:
            raise ValueError (f"bug:  {response.status_code}")
        
    except ValueError as ve:
        print(ve)




def parse_links(html):
    links = [link.css_first("a").attributes["href"] for link in html.css("div.home div.col-5.pl-0.pr-3")]
    return links




def parse_news(link):
    try:
        res = httpx.get(link)
        if res.status_code == 200:
            html = HTMLParser(res.text)
            title = []
            introduction = []
            author = []
            content = []
            for new in html.css("div[data-epica-module-name=Contenido] "):
                try:
                    title.append(new.css_first("div.mb-auto h2").text().strip().replace('"', '' ))
                except AttributeError as ar:
                    title.append("None")
                try:
                    introduction.append(new.css_first("div.lead  p").text())
                except AttributeError as ar:
                    introduction.append("None")
                try:
                    author.append(new.css_first("div.author-article button").text())
                except AttributeError as ar:
                    author.append("None")

                try:
                    content.append(new.css_first("div.html-content").text().strip())
                except AttributeError as ar:
                    content.append("None")
                
                
            return title,introduction,author,content
            
        
        else:
            raise ValueError (f"Error: {res.status_code}")
    except ValueError as ve:
        print(ve)




def today():
    today = datetime.date.today().strftime("%d-%m-%Y")
    if not os.path.isdir("./News/" + today):
        os.mkdir("./News/" + today)
        print("Directorio creado:", os.path.abspath("./News/" + today))

    return today




def save_news(title, introduction, author, content,day):    
    with open(f"./News/{day}/{title}.txt", mode="w", encoding="utf-8") as file:
        file.write(title)
        file.write("\n")
        file.write(introduction)
        file.write("\n")
        file.write(author)
        file.write("\n")
        for i in content:
            file.write(f"{i} \n")
            

            

def run():
    day = today()
    html = get_html()
    links = parse_links(html)
    for link in links:
       title,intro,author,content  = parse_news(link)
       save_news(title[0],intro[0],author[0],content,day)




if __name__ == "__main__":
    run()