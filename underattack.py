import requests
discord_webhook_url = 'https://discord.com/put-your-webhook-url-here' 
data = {
    "content": "Server is a under a DDoS attack"
}
requests.post(discord_webhook_url, data=data)

##KimYoJong
