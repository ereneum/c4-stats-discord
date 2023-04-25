import subprocess
import discord
import os
import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('Bot is ready')


@client.event
async def on_message(message):
  if message.content.startswith('c4-stats'):
    args = message.content[9:].strip()
    cmd = 'python c4-stats.py {}'.format(args)
    output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
    if len(output) >= 4000:
      await message.channel.send("Output is bigger than 4000.")
    await message.channel.send(output)

  if message.content.startswith('c4-help'):
    embed = discord.Embed(title="How to Use Warden Stalker?", color=0xa600ff)
    embed.set_author(
      name="Warden Stalker",
      icon_url=
      "https://gateway.pinata.cloud/ipfs/QmWrJDM88F4vHnebEJe3FmE9GR4Um3b3acnaDMndso6ir1?filename=63f694420713be4737dd8497_MqgFiqtLGScKH66wMJTCcZca8u3cZe-zVn8Ie7nhYPw.png"
    )
    embed.add_field(
      name="Prefix :",
      value=
      "c4-stats {command} {warden or contest number},                                           Usage : c4-stats basic cmichel, c4-stats contest 50 etc.",
      inline=False)
    embed.add_field(
      name="Commands : ",
      value="basic, list-contests, contest, by-contest, gini, gini-wardens",
      inline=False)
    embed.add_field(name="100proof's Github Repo with a detailed README :",
                    value="https://github.com/one-hundred-proof/c4-stats",
                    inline=False)
    await message.channel.send(embed=embed)


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))
