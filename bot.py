import discord
import responses
from dotenv import load_dotenv
import os
import random

# List of funny responses
funny_responses = [
    "Hold your horses, we're not in the fast lane just yet!",
    "Just simmer down like a slow-cooked stew while I handle this.",
    "Patience, young padawan. Processing your request, I am.",
    "Sit tight and grab some popcorn. This'll be worth the wait!",
    "Hang in there! Rome wasn't built in a day, and neither are bot responses.",
    "Don't worry, I'm not just twiddling my virtual thumbs here. Processing in progress!",
    "Chillax like a penguin on an iceberg. We'll get there.",
    "Loading... Just like a cat deciding whether to grace you with its presence.",
    "Hold on tight! I'm untangling the virtual spaghetti to get to your request.",
    "I'm on it like a sloth on a leisurely stroll. Expect a response soon!"
]

async def send_message(message, user_message) :
    try :
        response = responses.hanle_response(user_message)
        await message.channel.send(response)
    except Exception as e :
        print('exception')
        print(e)

def run_discord_bot() :
    load_dotenv()
    TOKEN = os.getenv('dc_token')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(message) :
        if message.author == client.user :
            return

        username = str(message.author.mention)
        user_message = str(message.content)

        if '?agencies' in user_message :
            await send_message(message, user_message)

        elif '?properties' in user_message :
            # Selecting a random response
            random_response = random.choice(funny_responses)
            await message.channel.send(f'{username} {random_response}')

            await send_message(message, user_message)

    client.run(TOKEN)