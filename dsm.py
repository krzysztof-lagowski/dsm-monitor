import collections
from os import error
import requests
import re
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook,DiscordEmbed
import time
import datetime
from datetime import datetime




URL= "https://london.doverstreetmarket.com/new-items"
keywords = ["nike","dunk","comme","Dunk","Jordan","Nike","Yeezy","yeezy"]

starter  = []

def monitor(starter):

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    picc= soup.select("h2")[0].text
    
    title = picc.strip()

    print(title) 
    splitter = title.split(" ")   
    bildd = soup.find_all("img",{"class": "img img-responsive"})[0]

    bild= bildd["src"]
    print(bildd)
    # links = [a['href'] for a in soup.select('a[href]')][17]
    # print(links)
    links2 = [a['href'] for a in soup.select('a[href]')][18]
    print(links2)
    # alllinks = [a['href'] for a in soup.select('a[href]')]
    # print(alllinks)
    
    # for i in range(len(alllinks)):
    #         key = keywords[i]
    #         if any(key in s for s in splitter):
    #             print(alllinks[i])
    ausloeser = False
    
    for i in range(len(keywords)):
            key = keywords[i]
            
            if any(key in s for s in splitter):
                ausloeser = True

    if ausloeser == True:            
        if title != starter:
                        webhook = DiscordWebhook(url='PASTE WEBHOOK HERE')

                        #create embed object for webhook
                        embed = DiscordEmbed(title='DSM NEW RAFFLE LOADED: '+title, description="store: DSM" , color='e10000')



                        # set thumbnail
                        embed.set_thumbnail(url=bild)

                        # set footer
                        embed.set_footer(text='KrzysztofMonitors', icon_url='https://i.imgur.com/HejEDR2.png')

                        # set timestamp (default is now)
                        embed.set_timestamp()

                        # add fields to embed
                        embed.add_embed_field(name=title, value=links2)




                        # add embed object to webhook
                        webhook.add_embed(embed)

                        response = webhook.execute()
                        starter = title
                        print("Ping exectued!")
                        
        else:
            print("Keyword hit.... but pinged already...")                
    else:
                print("NO Keyword hit!!! Monitoring DSM....")
                starter = []

    time.sleep(30)
    monitor(starter)



while True:
    monitor(starter)
    time.sleep(30)

