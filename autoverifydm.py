import discord

# Define the intents
intents = discord.Intents.default()
intents.messages = True  # Allow the bot to receive message events
intents.members = True  # Allow the bot to receive member events

# Create the Discord client with the specified intents
client = discord.Client(intents=intents)

# Define the message to send to new members
welcome_message = "YOUR MESSAGE - AUTO DMS WHEN A PERSON JOINS THE SERVER"

@client.event
async def on_ready():
    print('Bot started.')

@client.event
async def on_member_join(member):
    # Send a direct message to the member with the welcome message
    await member.send(welcome_message)
    print(f"Sent welcome message to {member.display_name}.")

@client.event
async def on_message(message):
    # Check if the message was sent in the specific channel
    if message.channel.id == YOUR_CHANNEL_ID:
        # Ensure that the message sender is not the bot itself
        if message.author != client.user:
            # Get the guild
            guild = client.get_guild(YOUR_GUILD_ID)
            if guild is not None:
                # Get the role you want to assign by ID
                role = discord.utils.get(guild.roles, id=YOUR_ROLE_ID)
                if role is not None:
                    # Assign the role to the author of the message
                    await message.author.add_roles(role)
                    # Send a direct message to the user including guild name
                    await message.author.send(f"{message.author.mention} you have been verified! Assigned ({role.name}) Role - {guild.name}")
                    # Send a message in the channel confirming verification
                    print(f"{message.author.name} has been assigned the role {role.name}.")
                else:
                    print("Role not found.")
            else:
                print("Guild not found.")

# Run the bot with your bot token
client.run('YOUR_BOT_TOKEN')
