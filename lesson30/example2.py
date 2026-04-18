from bs4 import BeautifulSoup

html_content = """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Beautiful Soup is a great tool</title>
                </head>
                <body>
                    <h1>Welcome to Beautiful Soup!</h1>
                    <p class="intro">Beautiful Soup makes web scraping easy!</p>
                    <div id="content">
                        <p>Here are some links:</p>
                        <a href="http://example.com/page1">Link 1</a>
                        <a href="http://example.com/page2">Link 2</a>
                        <a href="http://example.com/page3">Link 3</a>
                        <img src="test.png"/>
                        <img src="test1.png"/>
                        <img src="test2.png"/>
                        <img src="test3.png"/>
                        <img src="test4.png"/>
                    </div>
                </body>
            </html>
"""

soup = BeautifulSoup(html_content, 'html.parser')

print("Title of the page: ", soup.title.text)

intro_text = soup.find('p', class_='intro').text
print("Intro text:", intro_text)

div_content = soup.find('div', id="content")
imgs = div_content.find_all('img')
for img in imgs:
    print("Image: ", img['src'])

links = div_content.find_all('a')
for link in links:
    print("Link: ", link['href'])