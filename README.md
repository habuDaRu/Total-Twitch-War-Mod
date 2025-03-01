# Simple local Read-Only Twitch Bot for WH3 Mod <br />

Use the exe if you dont know how to run a python script (Its exactly the same). <br />
Run it (Exe or Script) from the Main WH3 Dir <br />
 <br />
SteamLink (for the Mod only): <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3433854519&result=1" target="_blank">Link to Steam Workshop</a>  <br />
### Regarding Bot: <br />
- Will write the names in tdw_bot_delivered_names.txt into the folder it runs from -> Main Warhammer 3 folder (..\Steam\steamapps\common\Total War WARHAMMER III) <br />
- Use tdw_twitch_bot_ignored_users.txt (in the Main WH3 dir) for blocked Users or to exclude Bots <br />
- Use tdw_twitch_bot_blocked_words.txt (in the Main WH3 dir) to block words <br /> 
- Selected Mode defines what is saved as name  <br /> <br />

### Regarding Mod: <br />
- tdw_twitch_renamer.pack needs to be placed in the data folder (..\Steam\steamapps\common\Total War WARHAMMER III\data) <br />
- tdw_twitch_renamer.pack requires the Mod Configuration Tool (or MCT) - available on Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2927955021
- The tdw_twitch_renamer.pack mod will use the tdw_bot_delivered_names.txt to get strings to apply as names  <br />
- Add names to tdw_twitch_spec_frames_names.txt to allow semi-random Frame selection for the named Unit in the unit Panel <br />
- It is the same file which is available on the Steam Workshop <br />
<br /> <br />

#### File-Setup for other Bots: <br />
tdw_bot_delivered_names.txt & tdw_twitch_spec_frames_names.txt: 
- each line a name
- the mod does some sanity checks: length (max 25 letters - Game limitation), filter out double entries
- both txt Files need to be in the main Warhammer 3 folder (..\Steam\steamapps\common\Total War WARHAMMER III)

### DONT SHARE YOUR OAUTH TOKEN <br />
get oauth token from (if you dont know how to): https://twitchtokengenerator.com/ Use Read-Only Scope <br /> <br />

## Mode desc <br />
suggest &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Keyword Name <br />
suggest_long &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Keyword Name Name  (for accepting spaces in the names) <br />
normal &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Username = Name <br />


## Demo Video:  <br />
<a href="https://youtu.be/Nxhe_9w6_LE" target="_blank">Link to YouTube</a>

## Peepo o7 Emotes
<a href="https://7tv.app/emote-sets/01JN18FXZ9JG1BEGPY9KVG9BRJ" target="_blank">Link to 7tv</a>
- 2 default o7 emotes (o7
