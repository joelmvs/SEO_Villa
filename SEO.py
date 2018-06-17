from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import urllib.error
import re
import requests

url= input("Which page would you like to check? Enter Full URL: ")
keyword = input("What is you seo keyword? ")
keyword = keyword.casefold()

try:
    req= Request(url, headers={'User-Agent': 'Mozilla/6.0'})
    html= urllib.request.urlopen(req)
except HTTPError as e:
    print(e)





#html = urllib.request.urlopen(url)

data=BeautifulSoup(html, "html.parser")

def seo_title_found(keyword, data):
    global status
    if data.title:
        if keyword.casefold() in data.title.text.casefold():
            status="Found"
        else:
            status="Not Found"
    else:
        status = "No title"
    return status

words=0
def stop_words(data):
    global words
    words=0
    list_words = []
    if data.title:
        with open('stopwords.txt', 'r') as f:
            for line in f:
                if re.search(r'\b' + line.rstrip('\n') + r'\b', data.title.text.casefold()):
                    words += 1
                    list_words.append(line.rstrip('\n'))
        if words == 0:
            stop_words_found= "We found no stop words, good job"
    else:
        stop_words_found='Title not found'
    if words > 0:
        print("We found {} stop words in your title. You should consider deleting them".format(len(list_words)) )
        for w in list_words:
            print("        ",w)
    else:
        print("No stop words found. Don't worry about this")
    return

def seo_title_length(data):
    if data.title:
        if  len(data.title.text) < 60:
            length = "Your length is under the maximum suggested length of 60 characters. Your title is {} characters long".format(len(data.title.text))
        else:
            length = "Your title length is too long. Your title is {} characters long".format(len(data.title.text))
    else:
        length = "No title was found"

    return length

def seo_url(url):
    if url:
        if keyword in url:
            surl = "Your keyword was found in your url"
        else:
            surl = "Your keyword was not found in your url. It is suggested to add your keyword to your slug."
    else:
        surl= "No url was returned"

    return surl

def seo_url_length(url):
    if url:
        if len(url) < 100:
            url_length = "Your URL is less than the 100 character maximum. Good."
        else:
            url_length= "Your URL length is over 100 character. Your url is currently at {} characters".format(len(url))
    else:
        url_length= "URL was not found"

    return url_length

def seo_h1(keyword, data):
    total_h1= 0
    total_keywords_h1= 0
    if data.h1:
        all_tags= data.find_all('h1')
        for tag in all_tags:
            total_h1 += 1
            tag= str(tag.string)
            if keyword in tag.casefold():
                total_keyword_h1 += 1
                h1_tag="Found keyword in h1 tag. You have a total of {} H1 Tags and you keyword was found in {} of them.".format(total_h1, total_keyword_h1)
            else:
                h1_tag= "Did not find a keyword in h1 tag."
    else:
        h1_tag="No H1 Tags Found"
        
    return h1_tag

def seo_h2(keyword,data):
    if data.h2:
        all_tags= data.find_all('h2')
        for tag in all_tags:
            tag= str(tag.string)
            if keyword in tag.casefold():
                h2_tag= "Found your keyword in at least one"
            else:
                h2_tag='We did not found your keyword in an h2 tag. You should add {} to h2 tag.'.format(keyword)
    else:
        h2_tag="No h2 tags found. You should have at least 1 containing your keyword"

    return h2_tag


    




#def processor(data):
#    href = data.get('href')
#    if not href: return False
#    return True if (href.find("google") == -1) else False


#back_links = data.findAll(processor, href=re.compile(r"^http"))


def backlinks(data):
#    print("orange juice")
    lnks=data.findAll('a')
#    print(lnks)
    places={}
    for bob in lnks:
        flds=bob.get('href')#.strip().split('/')
        if flds != None:
            flds=flds.strip().split('/')
#            print(flds)
            if len(flds)>3:
                if flds[2] in places:
                    places[flds[2]] += 1
                else:
                    places[flds[2]]=1
    print(places)
#    print("Tacos")


def images(data):
    images=[]
    count=0
    images=data.findAll('img')
    for image in images:
        fields=image.get('src')
#        print(fields)
        if fields != None:
            if fields[0] == "h":
                count+=1
    print("Your website contains {} images".format(count))
        
  

            
if status == "Found":
    print("20 points")
else:
    print("0 points")


if words>5:
    print("0 points")
    if words==0:
        print("10 points")
elif words<=5:
        print("5 points")

if len(data.title.text)<60:
    print("5 points")
else:
    print("0 points")

if seo_url == True:
    print("5 point")
else:
    print("0 points")

                  

    
#increase traffic and monetize
#bring more people
#traffic to translate into economic
#service
#how many rankings go up



print(seo_title_found(keyword,data))
stop_words(data)
#print(seo_title_length(data))
#print(seo_url(url))
#print(seo_url_length(url))
#print(seo_h1(keyword,data))
#print(seo_h2(keyword,data))
#print(back_links)
#backlinks(data)
#images(data)


