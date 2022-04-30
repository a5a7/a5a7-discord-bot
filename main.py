import discord
import os
from grpc import channel_ready_future
import requests
import json

client = discord.Client()

prefix = "$"

def changePrefixTo(pref):
    global prefix
    prefix = pref

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'hello'):
        await message.add_reaction("✋")
        await message.reply('Hello!')

    if message.content.startswith(prefix + 'hi'):
        await message.add_reaction("✋")
        await message.reply("Hi!")

    if message.content.startswith(prefix + 'info'):
        await message.reply('This is a5a7\'s bot. It is currently a work in progress.')

    if message.content.startswith(prefix + 'set_prefix'):
        new_prefix = message.content[-2]
        changePrefixTo(new_prefix)
        await message.reply('Set new prefix to: ' + new_prefix)
    
    if message.content.startswith(prefix+"scibowl"):
        #do nothing
        page = requests.get("https://scibowldb.com/api/questions/random")
        jsonObj = json.loads(page.text)
        await message.channel.send("**" + jsonObj['question']['category']+"  Tossup:**\n*" + jsonObj["question"]["tossup_format"]+"*\n" + jsonObj["question"]["tossup_question"])
        channel = message.channel;
        author = message.author;
        def check(m):
            return m.channel == channel and author == m.author;
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['tossup_answer'] + "'**.\n\n Respond 'bonus' to receive the bonus answer!")
        def secondCheck(m):
            return m.channel == channel and author == m.author and m.content == 'bonus';
        msg = await client.wait_for("message", check=secondCheck)
        await message.channel.send("**Bonus:**\n*" + jsonObj["question"]["bonus_format"]+"*\n" + jsonObj["question"]["bonus_question"])
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['bonus_answer'] + "'**.")
  
    if message.content.startswith(prefix+"es"):
        #do nothing
        page = requests.post("https://scibowldb.com/api/questions/random", json = {'categories': ["EARTH AND SPACE", "EARTH SCIENCE", "ASTRONOMY"]})
        jsonObj = json.loads(page.text)
        await message.channel.send("**" + jsonObj['question']['category']+"  Tossup:**\n*" + jsonObj["question"]["tossup_format"]+"*\n" + jsonObj["question"]["tossup_question"])
        channel = message.channel;
        author = message.author;
        def check(m):
            return m.channel == channel and author == m.author;
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['tossup_answer'] + "'**.\n\n Respond 'bonus' to receive the bonus answer!")
        def secondCheck(m):
            return m.channel == channel and author == m.author and m.content == 'bonus';
        msg = await client.wait_for("message", check=secondCheck)
        await message.channel.send("**Bonus:**\n*" + jsonObj["question"]["bonus_format"]+"*\n" + jsonObj["question"]["bonus_question"])
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['bonus_answer'] + "'**.")

    if message.content.startswith(prefix+"chem"):
        #do nothing
        page = requests.post("https://scibowldb.com/api/questions/random", json = {'categories': ["CHEMISTRY"]})
        jsonObj = json.loads(page.text)
        await message.channel.send("**" + jsonObj['question']['category']+"  Tossup:**\n*" + jsonObj["question"]["tossup_format"]+"*\n" + jsonObj["question"]["tossup_question"])
        channel = message.channel;
        author = message.author;
        def check(m):
            return m.channel == channel and author == m.author;
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['tossup_answer'] + "'**.\n\n Respond 'bonus' to receive the bonus answer!")
        def secondCheck(m):
            return m.channel == channel and author == m.author and m.content == 'bonus';
        msg = await client.wait_for("message", check=secondCheck)
        await message.channel.send("**Bonus:**\n*" + jsonObj["question"]["bonus_format"]+"*\n" + jsonObj["question"]["bonus_question"])
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['bonus_answer'] + "'**.")
    
    if message.content.startswith(prefix+"math"):
        #do nothing
        page = requests.post("https://scibowldb.com/api/questions/random", json = {'categories': ["MATH"]})
        jsonObj = json.loads(page.text)
        await message.channel.send("**" + jsonObj['question']['category']+"  Tossup:**\n*" + jsonObj["question"]["tossup_format"]+"*\n" + jsonObj["question"]["tossup_question"])
        channel = message.channel;
        author = message.author;
        def check(m):
            return m.channel == channel and author == m.author;
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['tossup_answer'] + "'**.\n\n Respond 'bonus' to receive the bonus answer!")
        def secondCheck(m):
            return m.channel == channel and author == m.author and m.content == 'bonus';
        msg = await client.wait_for("message", check=secondCheck)
        await message.channel.send("**Bonus:**\n*" + jsonObj["question"]["bonus_format"]+"*\n" + jsonObj["question"]["bonus_question"])
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['bonus_answer'] + "'**.")

    if message.content.startswith(prefix+"bio"):
        #do nothing
        page = requests.post("https://scibowldb.com/api/questions/random", json = {'categories': ["BIOLOGY"]})
        jsonObj = json.loads(page.text)
        await message.channel.send("**" + jsonObj['question']['category']+"  Tossup:**\n*" + jsonObj["question"]["tossup_format"]+"*\n" + jsonObj["question"]["tossup_question"])
        channel = message.channel;
        author = message.author;
        def check(m):
            return m.channel == channel and author == m.author;
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['tossup_answer'] + "'**.\n\n Respond 'bonus' to receive the bonus answer!")
        def secondCheck(m):
            return m.channel == channel and author == m.author and m.content == 'bonus';
        msg = await client.wait_for("message", check=secondCheck)
        await message.channel.send("**Bonus:**\n*" + jsonObj["question"]["bonus_format"]+"*\n" + jsonObj["question"]["bonus_question"])
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['bonus_answer'] + "'**.")

    if message.content.startswith(prefix+"phys"):
        #do nothing
        page = requests.post("https://scibowldb.com/api/questions/random", json = {'categories': ["PHYSICS", "COMPUTER SCIENCE"]})
        jsonObj = json.loads(page.text)
        await message.channel.send("**" + jsonObj['question']['category']+"  Tossup:**\n*" + jsonObj["question"]["tossup_format"]+"*\n" + jsonObj["question"]["tossup_question"])
        channel = message.channel;
        author = message.author;
        def check(m):
            return m.channel == channel and author == m.author;
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['tossup_answer'] + "'**.\n\n Respond 'bonus' to receive the bonus answer!")
        def secondCheck(m):
            return m.channel == channel and author == m.author and m.content == 'bonus';
        msg = await client.wait_for("message", check=secondCheck)
        await message.channel.send("**Bonus:**\n*" + jsonObj["question"]["bonus_format"]+"*\n" + jsonObj["question"]["bonus_question"])
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['bonus_answer'] + "'**.")

    if message.content.startswith(prefix+"gs"):
        #do nothing
        page = requests.post("https://scibowldb.com/api/questions/random", json = {'categories': ["GENERAL SCIENCE"]})
        jsonObj = json.loads(page.text)
        await message.channel.send("**" + jsonObj['question']['category']+"  Tossup:**\n*" + jsonObj["question"]["tossup_format"]+"*\n" + jsonObj["question"]["tossup_question"])
        channel = message.channel;
        author = message.author;
        def check(m):
            return m.channel == channel and author == m.author;
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['tossup_answer'] + "'**.\n\n Respond 'bonus' to receive the bonus answer!")
        def secondCheck(m):
            return m.channel == channel and author == m.author and m.content == 'bonus';
        msg = await client.wait_for("message", check=secondCheck)
        await message.channel.send("**Bonus:**\n*" + jsonObj["question"]["bonus_format"]+"*\n" + jsonObj["question"]["bonus_question"])
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['bonus_answer'] + "'**.")

    if message.content.startswith(prefix+"energy"):
        #do nothing
        page = requests.post("https://scibowldb.com/api/questions/random", json = {'categories': ["ENERGY"]})
        jsonObj = json.loads(page.text)
        await message.channel.send("**" + jsonObj['question']['category']+"  Tossup:**\n*" + jsonObj["question"]["tossup_format"]+"*\n" + jsonObj["question"]["tossup_question"])
        channel = message.channel;
        author = message.author;
        def check(m):
            return m.channel == channel and author == m.author;
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['tossup_answer'] + "'**.\n\n Respond 'bonus' to receive the bonus answer!")
        def secondCheck(m):
            return m.channel == channel and author == m.author and m.content == 'bonus';
        msg = await client.wait_for("message", check=secondCheck)
        await message.channel.send("**Bonus:**\n*" + jsonObj["question"]["bonus_format"]+"*\n" + jsonObj["question"]["bonus_question"])
        msg = await client.wait_for("message", check=check)
        await channel.send("I got the response as: \n'" + msg.content + "'\n\n" + "The answer is **'" + jsonObj['question']['bonus_answer'] + "'**.")

    return;
    

client.run(os.getenv("TOKEN"))
input = input("")
client.close()