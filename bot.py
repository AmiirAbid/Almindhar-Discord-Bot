import discord
import responses
import os

async def send_message(message, user_message) :
    try :
        response = responses.hanle_response(user_message)
        await message.channel.send(response)
    except Exception as e :
        print(e)

def run_discord_bot() :
    TOKEN = os.environ.get('dc_token')
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

        user_message = str(message.content)

        await send_message(message, user_message)            

    client.run(TOKEN)