import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# 1. getting html

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# 2. parse html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# 3. html tree traversal

#object types:
# tag
# NavigableString
# BeautifulSoup
# Comment

# print(type(soup))
# print(type(title))
# print(type(title.string))

#get title
title = soup.title
print(title)

# get paragraphs from page
paras = soup.find_all('p')
# print(paras)

anchors = soup.find_all('a')
# print(anchors)

# print(soup.find('p')['class'])

# class lead elements
# print(soup.find_all('p',class_='lead'))

# get text from elements
# print(soup.find('p').get_text())
# print(soup.get_text())

# get all links from page:
all_links = set()                     # for non repeating links

for link in anchors:
    if (link.get('href') != '#'):
        linkText = 'https://codewithharry.com' + link.get('href')
        all_links.add(linkText)
        # print(linkText)


#for comment obj type
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p)
# print(type(soup2.p.string))


navbarSupportedContent = soup.find(id = 'navbarSupportedContent')

# .contents - a tag's childern are available in list
# .children - a tag's childern are available as a generator

# print(navbarSupportedContent)
# for elem in navbarSupportedContent.contents:
    # print(elem)


# print(navbarSupportedContent.children)
# for elem in navbarSupportedContent.childern:
#     print(elem)

# for item in navbarSupportedContent.strings:
    # print(item)

# for item in navbarSupportedContent.stripped_strings:
    # print(item)

# print(navbarSupportedContent.parent)

# print(navbarSupportedContent.parents)         #generator: can be iterated
# for item in navbarSupportedContent.parents:
    # print(item.name)

# print(navbarSupportedContent.next_sibling)
# print(navbarSupportedContent.next_sibling.next_sibling)         #counts spaces and empty lines also therefore error

# print(navbarSupportedContent.previous_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('#loginModal')
# print(elem)
# elem = soup.select('.modal-footer')
# print(elem)




