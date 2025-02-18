from twitchio.ext import commands

class ReadOnlyBot(commands.Bot):
    def __init__(self, token, channel_name, keyword, mode):
        super().__init__(
            token=token,  # Use token provided by user
            prefix="!",
            initial_channels=[channel_name]  # Use the channel name provided by user
        )
        self.keyword = keyword  # Store the keyword provided by the user
        self.mode = mode  # Store the operation mode

    async def event_ready(self):
        print(f"Connected as {self.nick}")

    async def event_message(self, message):
        # Check if the message contains the specified keyword
        if self.keyword.lower() in message.content.lower():  # Case-insensitive check
            if self.mode == 'suggest':  # Suggest mode
                parts = message.content.split()
                if len(parts) > 1:
                    name_to_save = parts[1][:25]  # Limit the name length to 25
                    with open("usernames.txt", "a", encoding="utf-8") as f:
                        f.write(f"{name_to_save}\n")
                    print(f"Written suggested name {name_to_save} to usernames.txt")
            elif self.mode == 'suggest_long':  # Suggest long mode
                parts = message.content.split()
                if len(parts) > 1:
                    # Join all parts after the keyword and limit to 25 characters
                    long_name = ' '.join(parts[1:])[:25]
                    with open("usernames.txt", "a", encoding="utf-8") as f:
                        f.write(f"{long_name}\n")
                    print(f"Written long suggested name {long_name} to usernames.txt")
            else:  # Normal mode
                with open("usernames.txt", "a", encoding="utf-8") as f:
                    f.write(f"{message.author.name}\n")
                print(f"Written {message.author.name} to usernames.txt")

        # Optional: print chat messages (you can remove this line if you don't want it)
        print(f"{message.author.name}: {message.content}")

# Ask the user for mode, token, channel name, and keyword
mode = input("Enter mode - leave empty for normal mode: ").strip() or "normal"
token = input("Enter your OAuth token: ")
channel_name = input("Enter the channel name: ")
keyword = input("Enter the keyword to listen for: ")

# Create bot instance and run it
bot = ReadOnlyBot(token, channel_name, keyword, mode)
bot.run()
