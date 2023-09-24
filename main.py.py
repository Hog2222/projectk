import discord
from discord.ext import commands

import config

import asyncio
from discord.ui import Button, button, View

import chat_exporter
import github
from github import github

import time
import os

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.all(),
    status=discord.Status.dnd,
    activity=discord.Activity(
        type=discord.ActivityType.watching, name="Test Phase🎶"
    ),
    guild = discord.Object(id=1149272093800812584)
)


@bot.event
async def on_ready():
    print("Bot is ready!")
    bot.add_view(CreateButton())
    bot.add_view(CloseButton())
    bot.add_view(TrashButton())


# GET TRANSCRIPT
'''async def get_transcript(member: discord.Member, channel: discord.TextChannel):
    export = await chat_exporter.export(channel=channel)
    file_name=f"{member.id}.html"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(export)

# UPLOAD TO GITHUB
def upload(file_path: str, member_name: str):
    github = Github(config.GTOKEN)
    repo = github.get_repo("dhipesh1/Atrp")
    file_name = f"{int(time.time())}"
    repo.create_file(
        path=f"tickets/{file_name}.html",
        message="Ticket Log for {0}".format(member_name),
        branch="main",
        content=open(f"{file_path}","r",encoding="utf-8").read()
    )
    os.remove(file_path)

    return file_name


async def send_log(title: str, guild: discord.Guild, description: str, color: discord.Color):
    log_channel = guild.get_channel(1152321158851604541)
    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    await log_channel.send(embed=embed)'''

class CreateButton(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Character issue",style=discord.ButtonStyle.blurple, emoji="🎫",custom_id="character issue")
    async def Characterissue(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer(ephemeral=True)
        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id=1151819587311120474)
        for ch in category.text_channels:
            if ch.topic == f"{interaction.user.id} DO NOT CHANGE THE TOPIC OF THIS CHANNEL!":
                await interaction.followup.send("You already have a ticket in {0}".format(ch.mention), ephemeral=True)
                return
       
        r1 : discord.Role = interaction.guild.get_role(1149342623388139610)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            r1: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages = True, send_messages=True),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        
        channel = await category.create_text_channel(
            name=str(interaction.user),
            topic=f"{interaction.user.id} DO NOT CHANGE THE TOPIC OF THIS CHANNEL!",
            overwrites=overwrites
        )
        await channel.send(
            embed=discord.Embed(
                title="Ticket Created!",
                description="Don't ping a staff member, they will be here soon.",
                color = discord.Color.green()
            ),
            view = CloseButton()
        )
        await interaction.followup.send(
            embed= discord.Embed(
                description = "Created your ticket in {0}".format(channel.mention),
                color = discord.Color.blurple()
            ),
            ephemeral=True
        )

        await send_log(
            title="Ticekt Created",
            description="Created by {0}".format(interaction.user.mention),
            color=discord.Color.blurple(),
            guild=interaction.guild
        )
    @button(label="ooc",style=discord.ButtonStyle.green, emoji="🌍",custom_id="ooc ticket")
    async def ooc(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer(ephemeral=True)
        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id=1151819395283296327)
        for ch in category.text_channels:
            if ch.topic == f"{interaction.user.id} DO NOT CHANGE THE TOPIC OF THIS CHANNEL!":
                await interaction.followup.send("You already have a ticket in {0}".format(ch.mention), ephemeral=True)
                return
       
        r1 : discord.Role = interaction.guild.get_role(1149342623388139610)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            r1: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages = True, send_messages=True),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        
        channel = await category.create_text_channel(
            name=str(interaction.user),
            topic=f"{interaction.user.id} DO NOT CHANGE THE TOPIC OF THIS CHANNEL!",
            overwrites=overwrites
        )
        await channel.send(
            embed=discord.Embed(
                title="Ticket Created!",
                description="Don't ping a staff member, they will be here soon.",
                color = discord.Color.green()
            ),
            view = CloseButton()
        )
        await interaction.followup.send(
            embed= discord.Embed(
                description = "Created your ticket in {0}".format(channel.mention),
                color = discord.Color.green()
            ),
            ephemeral=True
        )

        await send_log(
            title="Ticekt Created",
            description="Created by {0}".format(interaction.user.mention),
            color=discord.Color.green(),
            guild=interaction.guild
        )

    @button(label="Bug issue",style=discord.ButtonStyle.red, emoji="🐞",custom_id="bug ticket")
    async def bug(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer(ephemeral=True)
        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id=1151819756911984720)
        for ch in category.text_channels:
            if ch.topic == f"{interaction.user.id} DO NOT CHANGE THE TOPIC OF THIS CHANNEL!":
                await interaction.followup.send("You already have a ticket in {0}".format(ch.mention), ephemeral=True)
                return
       
        r1 : discord.Role = interaction.guild.get_role(1149342623388139610)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            r1: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages = True, send_messages=True),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        
        channel = await category.create_text_channel(
            name=str(interaction.user),
            topic=f"{interaction.user.id} DO NOT CHANGE THE TOPIC OF THIS CHANNEL!",
            overwrites=overwrites
        )
        await channel.send(
            embed=discord.Embed(
                title="Ticket Created!",
                description="Don't ping a staff member, they will be here soon.",
                color = discord.Color.red()
            ),
            view = CloseButton()
        )
        await interaction.followup.send(
            embed= discord.Embed(
                description = "Created your ticket in {0}".format(channel.mention),
                color = discord.Color.red()
            ),
            ephemeral=True
        )

        await send_log(
            title="Ticekt Created",
            description="Created by {0}".format(interaction.user.mention),
            color=discord.Color.red(),
            guild=interaction.guild
        )
    @button(label="other issue",style=discord.ButtonStyle.grey, emoji="📝",custom_id="other issue")
    async def other(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer(ephemeral=True)
        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id=1151820493373059162)
        for ch in category.text_channels:
            if ch.topic == f"{interaction.user.id} DO NOT CHANGE THE TOPIC OF THIS CHANNEL!":
                await interaction.followup.send("You already have a ticket in {0}".format(ch.mention), ephemeral=True)
                return
       
        r1 : discord.Role = interaction.guild.get_role(1149342623388139610)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            r1: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages = True, send_messages=True),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        
        channel = await category.create_text_channel(
            name=str(interaction.user),
            topic=f"{interaction.user.id} DO NOT CHANGE THE TOPIC OF THIS CHANNEL!",
            overwrites=overwrites
        )
        await channel.send(
            embed=discord.Embed(
                title="Ticket Created!",
                description="Don't ping a staff member, they will be here soon.",
                color = discord.Color.greyple()
            ),
            view = CloseButton()
        )
        await interaction.followup.send(
            embed= discord.Embed(
                description = "Created your ticket in {0}".format(channel.mention),
                color = discord.Color.greyple()
            ),
            ephemeral=True
        )

        await send_log(
            title="Ticekt Created",
            description="Created by {0}".format(interaction.user.mention),
            color=discord.Color.greyple(),
            guild=interaction.guild
        )
    
        


class CloseButton(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Close the ticket",style=discord.ButtonStyle.red,custom_id="closeticket",emoji="🔒")
    async def close(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer(ephemeral=True)

        await interaction.channel.send("Closing this ticket in 3 seconds!")

        await asyncio.sleep(3)

        category: discord.CategoryChannel = discord.utils.get(interaction.guild.categories, id = 1152528875130208266)
        r1 : discord.Role = interaction.guild.get_role(1149342623388139610)
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            r1: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=True),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        await interaction.channel.edit(category=category, overwrites=overwrites)
        await interaction.channel.send(
            embed= discord.Embed(
                description="Ticket Closed!",
                color = discord.Color.red()
            ),
            view = TrashButton()
        )
        '''member = interaction.guild.get_member(int(interaction.channel.topic.split(" ")[0]))
        await get_transcript(member=member, channel=interaction.channel)
        file_name = upload(f'{member.id}.html',member.name)
        link = f"https://github.com/dhipesh1/Atrp{file_name}"
        await send_log(
            title="Ticket Closed",
            description=f"Closed by: {interaction.user.mention}\n[click for transcript]({link})",
            color=discord.Color.yellow(),
            guild=interaction.guild
        )'''
    

class TrashButton(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Delete the ticket", style=discord.ButtonStyle.red, emoji="🚮", custom_id="trash")
    async def trash(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        await interaction.channel.send("Deleting the ticket in 3 seconds")
        await asyncio.sleep(3)

        await interaction.channel.delete()
        await send_log(
            title="Ticket Deleted",
            description=f"Deleted by {interaction.user.mention}, ticket: {interaction.channel.name}",
            color=discord.Color.red(),
            guild=interaction.guild
        )
        

@bot.command(name="ticket")
@commands.has_permissions(administrator=True)
async def ticket(ctx):
    await ctx.send(
        embed = discord.Embed(
            description="Press the button to create a new ticket!"
        ),
        view = CreateButton()
    )


bot.run(config.TOKEN)