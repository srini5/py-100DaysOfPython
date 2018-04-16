import requests, html, re

def new_quote():
    resp = requests.get("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1")
    resp_json = resp.json()    #This returns a list containing a single dictionary having content, title, link and id

    m = re.match(r'<p>(.*)</p>', resp_json[0]['content']) # content has a string enclosed between <p> and </p> tags
    print()
    print(html.unescape(m.group(1)))  #Need to use html.unescape to convert the html encoded string into readable form
    print('--', resp_json[0]['title'])
    print('Find more about',resp_json[0]['title'],'at',resp_json[0]['link'],sep=' ')

print("Hello World and welcome to the Random Quote Machine powered by the Random Quotes API @https://quotesondesign.com/api-v4-0/")

while True:
    new_quote()
    more = input("Do you want to see another quote? (Y/N): ")

    while more not in ('Y','N'):
        print("I didn't quite get that. Please try again")
        more = input("Do you want to see another quote? (Y/N): ")

    if more == 'Y':
        print('OK. One more coming up.....')
        continue
    elif more == 'N':
        print('Thanks for using the Random Quote Machine. ')
        break
