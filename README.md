# 1. **Twitch Auto Rename Units Mod**

Steam Workshop: <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3433854519&result=1" target="_blank">Link to Steam Workshop Page</a>  <br />
- It is the same file which is available here - so better use steam because of autoupdate <br /><br />
### **Mod** *(tdw_twitch_auto_rename_units.pack & tdw_twitch_auto_rename_units.png)*: <br />
- 	**requires** the Mod Configuration Tool (or MCT) - available on Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2927955021
- both files needs to be placed in the data folder (..\Steam\steamapps\common\Total War WARHAMMER III\data) <br />
- The Mod will read out names from the tdw_bot_delivered_names.txt to apply as names to the units ingame (until no more names or units are available) <br />
- tracks kill and battle stats (automatically) <br />
- adds a panel with the Top 3 renamed units with most kills/battles + 3 randomly selected chat units <br />
- check for killed/disbanded units and also manages a panel with all lost units (including the kills, battles and death-turn for the units) <br />
- Add names to tdw_twitch_spec_frames_names.txt to allow semi-random Frame selection for the named Unit in the unit Panel <br />
<br /> <br />



# 2. Setup for Chat Bot: <br />
### a) Streamer.bot:
 - Action: define a keyword
 - Trigger: Command Triggered
 - Sub-Actions:
     - File Tail: Enabled,
     - Write to file(tdw_bot_delivered_names.txt) - make sure set the txt file into the Main Wh3 Folder (..\Steam\steamapps\common\Total War WARHAMMER III\data)
     - Optional: Setup a Twitch Message as automatic Response

- File Setup for: tdw_bot_delivered_names.txt and tdw_twitch_spec_frames_names.txt: 
- each line a name
- the ingame mod does some sanity checks: length (max 25 letters - Game limitation), filter out double entries
- both txt Files need to be in the main Warhammer 3 folder (..\Steam\steamapps\common\Total War WARHAMMER III)
<br />
<br />

### b) Simple local Read-Only Twitch Bot available here *(twitch_read_only_bot.exe or twitch_read_only_bot.py)* <br />
Use the exe if you dont know how to run a python script (Its exactly the same). <br />
Run it (Exe or Script) from the Main WH3 Dir <br />
 <br />
- Will write the names in tdw_bot_delivered_names.txt into the folder it runs from -> Main Warhammer 3 folder (..\Steam\steamapps\common\Total War WARHAMMER III) <br />
- Use tdw_twitch_bot_ignored_users.txt (in the Main WH3 dir) for blocked Users or to exclude Bots <br />
- Use tdw_twitch_bot_blocked_words.txt (in the Main WH3 dir) to block words <br /> 
- Selected Mode defines what is saved as name  <br /> <br />

#### DONT SHARE YOUR OAUTH TOKEN <br />
get oauth token from (if you dont know how to): https://twitchtokengenerator.com/ Use Read-Only Scope <br /> <br />

#### Mode desc <br />
suggest &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Keyword Name <br />
suggest_long &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Keyword Name Name  (for accepting spaces in the names) <br />
normal &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Username = Name <br />


## 3. Demo Video:  <br />
<a href="https://youtu.be/Nxhe_9w6_LE" target="_blank">Link to YouTube</a>

## 4. Peepo o7 Emotes on 7tv
<a href="https://7tv.app/emote-sets/01JN18FXZ9JG1BEGPY9KVG9BRJ" target="_blank">Link to 7tv</a>
- 3 default
- 3 Empire
- 3 kislev
- 2 Cathay
- 3 Greenskins
- 2 Dark Elf
- 1 Tombkings
