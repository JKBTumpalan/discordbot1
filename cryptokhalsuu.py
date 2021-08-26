import discord
import os
from decouple import config
import requests
import json

client = discord.Client()
supported_currencies = {
    'slp': 'smooth-love-potion',
    'bnb': 'binancecoin',
    'axs': 'axie-infinity',
    'pvu': 'plant-vs-undead-token',
    'eth': 'ethereum',
    'btc': 'bitcoin'
}
BOT_TOKEN = config('TOKEN')

def get_crypto_price(id):
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=php'.format(supported_currencies[id]))
    json_data = json.loads(response.text)
    print(json_data)
    
    return str(json_data[supported_currencies[id]]['php'])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello there!')

    if message.content.startswith('$price'):
        message_blocks = message.content.split(' ')

        await message.channel.send('PHP ' + get_crypto_price(message_blocks[1]))

print(BOT_TOKEN)                       
client.run(BOT_TOKEN)