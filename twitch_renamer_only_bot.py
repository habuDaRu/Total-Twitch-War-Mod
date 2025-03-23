from twitchio.ext import commands

# Define color codes
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'  # Red color for "empty" message
RESET = '\033[0m'

class ReadOnlyBot(commands.Bot):
    def __init__(self, token, channel_name, keyword, mode):
        super().__init__(
            token=token,
            prefix="!",
            initial_channels=[channel_name]
        )
        self.keyword = keyword  # Store the keyword provided by the user
        self.mode = mode  # Store the operation mode
        self.ignored_users = self.load_list_from_file("tdw_twitch_bot_ignored_users.txt")  # Load ignored users
        self.blocked_words = self.load_list_from_file("tdw_twitch_bot_blocked_words.txt")  # Load blocked words

    def load_list_from_file(self, filename):
        """Load a list from a file (one item per line) and return a set."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return set(line.strip().lower() for line in f if line.strip())
        except FileNotFoundError:
            return set()  # Return empty set if file doesn't exist

    async def event_ready(self):
        print(f"Connected as {BLUE}{self.nick}{RESET}")

    async def event_message(self, message):
        username = message.author.display_name
        message_content = message.content.lower()  # Convert to lowercase for case-insensitive matching

        # Ignore messages from blocked users
        if username.lower() in self.ignored_users:
            return

        # Ignore messages containing blocked words
        if any(word in message_content for word in self.blocked_words):
            return

        # Check if the message contains the specified keyword
        if self.keyword.lower() in message_content:
            if self.mode == 'suggest':  # Suggest mode
                parts = message.content.split()
                if len(parts) > 1:
                    name_to_save = parts[1][:25]  # Limit the name length to 25
                    with open("tdw_bot_delivered_names.txt", "a", encoding="utf-8") as f:
                        f.write(f"{name_to_save}\n")
                    print(f"{username}: {message.content}")
                    print(f"Unit name {GREEN}{name_to_save}{RESET} added to tdw_bot_delivered_names.txt")
            elif self.mode == 'suggest_long':  # Suggest long mode
                parts = message.content.split()
                if len(parts) > 1:
                    long_name = ' '.join(parts[1:])[:25]  # Join all parts after the keyword
                    with open("tdw_bot_delivered_names.txt", "a", encoding="utf-8") as f:
                        f.write(f"{long_name}\n")
                    print(f"{username}: {message.content}")
                    print(f"Unit name {GREEN}{long_name}{RESET} added to tdw_bot_delivered_names.txt")
            else:  # Normal mode
                with open("tdw_bot_delivered_names.txt", "a", encoding="utf-8") as f:
                    f.write(f"{username}\n")
                print(f"{username}: {message.content}")
                print(f"Unit name {GREEN}{username}{RESET} added to tdw_bot_delivered_names.txt")

# Ask the user for mode, token, channel name, and keyword
mode = input("Enter mode - leave empty for normal mode (or 'suggest', 'suggest_long'): ").strip() or "normal"
keyword = input("Enter the keyword to listen for: ")
token = input("Enter your OAuth token: ")
channel_name = input("Enter the channel name: ")
while not channel_name:
    channel_name = input(f"Enter the channel name {RED}(Can't be empty):{RESET} ").strip()

# Create bot instance and run it
bot = ReadOnlyBot(token, channel_name, keyword, mode)
bot.run()
