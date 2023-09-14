import json
import requests

class Restock:
    def __init__(self, url, imageurl, site, SKU, sizes, thumbnail):
        self.url = url
        self.imageurl = imageurl
        self.site = site
        self.sku = SKU
        self.sizes = sizes
        self.thumbnail = thumbnail

initialized = 0
global valid_hook_url

def hook_testing(hook_name):
    global valid_hook_url
    data = {
                "content" : "Nice, your webhook is valid!",
                "avatar_url" : "https://pittcsc.org/static/hero_image-efc2fb9872697662dfa106aafc81a94b.png",
                "username" : "Thanks Pitt CSC"
            }

    if(len(hook_name) > 0): #if we already got a valid webhook from above.
        response = requests.post(
                hook_name, data=json.dumps(data),
                headers={"Content-Type": "application/json"}
            )

        if(response.status_code == 204):
            valid_hook_url = hook_name
            print("webhook valid and working")
            return
        else:
            print(f"Webhook failed with status code {response.status_code}") #failed = let's continue manually 

    is_valid = False
    while is_valid == False:
        webhook = input("We were unable to find your configuration file or it failed. Please manually enter your Discord webhook: ")
        if(len(webhook) > 50):

            response = requests.post(
                webhook, data=json.dumps(data),
                headers={"Content-Type": "application/json"}
            )

            if(response.status_code == 204):
                is_valid = True
                valid_hook_url = webhook
            else:
                print(f"Webhook failed with status code {response.status_code}")

def ping(Restock):
    data = {
        "username": "Leowonderful Monitors",
        "avatar_url": "https://static.esea.net/cdn-cgi/image/metadata=none,anim=false,width=150,height=150/global/images/users/1308517.1556747549.jpg",
        "embeds": [
            {
                "author": {
                    "name": "Leowonderful Monitors",
                    "icon_url": "https://static.esea.net/cdn-cgi/image/metadata=none,anim=false,width=150,height=150/global/images/users/1308517.1556747549.jpg"
                },
            "title": Restock.site,
            "url": Restock.url,
            "description": "Sizes restocked in the product! Click Below.",
            "fields": [
                {
                    "name": "SKU",
                    "value": Restock.sku
                },
                {
                    "name": "Sizes",
                    "value": ', '.join(map(str,Restock.sizes))
                },
            ],
            "thumbnail": {
                    "url": Restock.thumbnail  # Replace with the URL of the item
                }
            }
        ],
    }
    
    response = requests.post(
                valid_hook_url, data=json.dumps(data),
                headers={"Content-Type": "application/json"}
            )

    if response.status_code == 204:
        # great success!
        return
    else:
        print(f"Internship found but webhook failed with status {response.status_code}")  # failed :(