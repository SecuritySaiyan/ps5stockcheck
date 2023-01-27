import discord
import requests
from bs4 import BeautifulSoup

# Insert your Discord bot token here
TOKEN = 'your_token_here'

# Create a new Discord client
client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.content == '!ps5':
        # Send a message to indicate that the bot is checking stock
        await message.channel.send('Checking stock...')
        
        # Use the requests library to get the website's HTML
        page = requests.get('https://www.bestbuy.com/site/playstation-5/pcmcat1483020809547.c?id=pcmcat1483020809547')
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Use BeautifulSoup to search for the specific element that contains the stock status
        stock = soup.find(class_='fulfillment-add-to-cart-button')
        
        # If the element is found and contains the text "Add to Cart", the product is in stock
        if stock and stock.text == 'Add to Cart':
            await message.channel.send('PS5 is in stock!')
        else:
            await message.channel.send('PS5 is out of stock.')

client.run(TOKEN)
