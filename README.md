# Total Twitch War Mod – A Twitch Chat Integration Mod

This mod is designed for streamers. It requires a bot to function. Without a bot providing input from Twitch chat, the mod cannot perform its actions.

## Features

- **Automatic Unit Renaming**: Assigns Twitch chat-submitted names to in-game units.
- **Kill & Battle Tracking**: Automatically keeps track of renamed units' stats.
- **Top Units Panel**: Displays the top 3 units with the most kills/battles, plus 3 random viewer-named units.
- **Lost Units List**: Tracks units that are killed or disbanded, including their battle stats and turn of death.
- **Optional Graphical Feature**: Randomly assigns special faction frames to units of specific users (e.g., VIPs, mods, subs, or any designated users).
- **Script-Based Compatibility**: Safe to add or remove mid-campaign; names will not revert upon removal.
- **Queue System for Commands**: Commands from Twitch chat are handled in queue system.
- **Customizable Commands**: Some commands can be customized by the input variables through naming command convention.
- **Advanced Command Handling**: Streamers can configure their bot to decide which commands are active.

## Requirements

- **Mod Configuration Tool (MCT)**
- **A Chat Bot (configured to write names to a text file)**

## Setup for Chat Bot

1. **Required Files**:

   - **`tdw_bot_delivered_names.txt`**  
     The bot must write names from Twitch chat into this file for the automatic renaming system of the mod to function.

     **File Rules**:
     - Each name must be on a separate line.
     - The mod automatically handles the following:
       - Maximum name length: 25 characters (game limitation).
       - Duplicate names are automatically filtered.
     - Place the file in:  
       `..\Steam\steamapps\common\Total War WARHAMMER III\tdw_bot_delivered_names.txt`

     **Example file content**:
     ```
     name1
     name2
     name3
     ```

     > _Note_: Configuring your bot to filter duplicates or limit name length is optional. However, if you set up the bot to do this, it will help reduce the computing load for the game.
     
     > _Important_: The bot should also be used for additional filtering, such as blocking inappropriate names or any other aspects the streamer wants to prevent (e.g., offensive words or unwanted entries). The mod doesn’t handle this, so it's up to the streamer to ensure the names are appropriate.

   - **`tdw_twitch_points_punishment.txt`**  
     The bot must write names and commands retrieved from Twitch chat into this file for the command handling system of the mod to function.
     Commands can be triggered in various ways like chat commands, the Twitch channel points system, or other alerts tracked by the bot.

     **File Rules**:
     - Each Entry must be on a separate line.
     - entries must be in the following format:
       - name of the person triggering the event (can also be the bot).
       - an ': ' as seperator
       - the command to trigger the effect (For all available commands see 'Available Commands and Their Effects'-section)
     - Place the file in:  
       `..\Steam\steamapps\common\Total War WARHAMMER III\tdw_twitch_points_punishment.txt`

     **Example file content**:
     ```
     name1: nur_corruption_effect_all
     name2: spawn_armies_ksl_3
     ```


2. **Optional Files**:

   - **`tdw_twitch_spec_frames_names.txt`**  
     This file is **not required** but If used, it adds special faction-specific frames to certain users’ units in the panel.
      - Randomly assigns frames to users listed in tdw_twitch_spec_frames_names.txt.
      - can be used for VIPs, mods, subs, or any designated users.

     **File Rules**:
     - Each Entry must be on a separate line.

     **Example file content**:
     ```
     name1
     name2
     ```

   - **`tdw_priority_users.txt`**  
     This file is **not required** but If used, it contains the names of users whose triggered commands will always be placed in the priority queue.
      - can be used for VIPs, mods, subs, or any designated users.

     **File Rules**:
     - Each Entry must be on a separate line.

     **Example file content**:
     ```
     name1
     name2
     name3
     ```

## Commands and Queue System

The mod processes commands submitted by the chat bot, adding them to a queue, either the priority or normal queue. The commands trigger various in-game effects, and the mod attempts to execute them at the start of each round.

### Available Commands and Their Effects

---

#### **Diplomacy**

- **`random_war_declaration`**  
  Declares a random faction war, targeting non-vassal, alive factions that are not already at war with the player, not allied with the player, and have no non-aggression pact with the player.

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: random_war_declaration
```

---

#### **Corruption Effects**

- **`random_corruption_effect_all`**  
  Applies a random corruption effect to all provinces with randomized strength and duration for each province.

- **`nur_corruption_effect_all`**  
  Applies Nurgle’s corruption effect to all provinces with randomized strength and duration for each province.

- **`kho_corruption_effect_all`**  
  Applies Khorne’s corruption effect to all provinces with randomized strength and duration for each province.

- **`sla_corruption_effect_all`**  
  Applies Slaanesh’s corruption effect to all provinces with randomized strength and duration for each province.

- **`tze_corruption_effect_all`**  
  Applies Tzeentch’s corruption effect to all provinces with randomized strength and duration for each province.

- **`skv_corruption_effect_all`**  
  Applies Skaven’s corruption effect to all provinces with randomized strength and duration for each province.

- **`chs_corruption_effect_all`**  
  Applies Chaos corruption effect to all provinces with randomized strength and duration for each province.

- **`vmp_corruption_effect_all`**  
  Applies Vampire corruption effect to all provinces with randomized strength and duration for each province.

> **Note:** All corruption, public order, replenishment, and combat stats effects have individual cooldowns, randomized strength, and randomized duration per province.

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: nur_corruption_effect_all
```

---

#### **Public Order Effects**

- **`po_boni_effect_all`**  
  Increases public order (happiness) in all provinces with randomized strength and duration for each province.

- **`po_mali_effect_all`**  
  Decreases public order (happiness) in all provinces with randomized strength and duration for each province.

> **Note:** All corruption, public order, replenishment, and combat stats effects have individual cooldowns, randomized strength, and randomized duration per province.

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: po_boni_effect_all
```

---

#### **Replenishment Effects**

- **`repl_boni_effect_all`**  
  Increases army replenishment rate for all provinces with randomized strength and duration for each province.

- **`repl_mali_effect_all`**  
  Decreases army replenishment rate for all provinces with randomized strength and duration for each province.

> **Note:** All corruption, public order, replenishment, and combat stats effects have individual cooldowns, randomized strength, and randomized duration per province.

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: repl_boni_effect_all
```

---

#### **Combat Stats Effects in Provinces**

- **`damage_melee_boni_effect_province`**  
  Increases melee damage for units in a province with randomized strength and cooldown for each province.

- **`damage_ranged_boni_effect_province`**  
  Increases ranged damage for units in a province with randomized strength and cooldown for each province.

- **`armor_boni_effect_province`**  
  Increases armor for units in a province with randomized strength and cooldown for each province.

- **`melee_defence_boni_effect_province`**  
  Increases melee defense for units in a province with randomized strength and cooldown for each province.

- **`movement_range_boni_effect_province`**  
  Increases movement range for units in a province with randomized strength and cooldown for each province.

> **Note:** All corruption, public order, replenishment, and combat stats effects have individual cooldowns, randomized strength, and randomized duration per province.

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: damage_melee_boni_effect_province
```

---

#### **Money**

- **`toss_a_coin_xx`**  
  Gives the player `xx * 1000` money (where `xx` is the amount).  

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: toss_a_coin_10
```
This gives the player 10,000 money.

---

#### **Enemy Armies**

- **`spawn_armies_xxx_yy`**  
  Spawns `yy` enemy armies for a faction `xxx`, which is hostile towards the player. These armies will have randomized faction-specific units and randomized army sizes.  
  - `yy` defines the number of armies spawned.  
  - `xxx` can include specific factions or group options:
    - **Specific Factions:**
      - `grn` (Greenskins)
      - `ogr` (Ogres)
      - `bst` (Beastmen)
      - `nor` (Norsca)
      - `skv` (Skaven)
      - `def` (Dwarfs)
      - `chs` (Chaos)
      - `chd` (Chaos Dwarfs)
      - `brt` (Bretonnia)
      - `cth` (Cathay)
      - `wef` (Wood Elves)
      - `lzd` (Lizardmen)
      - `hef` (High Elves)
      - `ksl` (Kislev)
      - `dwf` (Dwarfs)
      - `emp` (Empire)
      - `nur` (Nurgle)
      - `kho` (Khorne)
      - `sla` (Slaanesh)
      - `tze` (Tzeentch)
      - `vmp` (Vampire Coast)
      - `cst` (Tomb Kings)
      - `tmb` (Tomb Kings)
    - **Group Options:**
      - `dem = demons`
      - `ded = Undead`
      - `god = Good factions`
      - `bad = Bad factions`
      - `hmn = Human factions`
      - `elf = Elf factions`
      - `neu = Neutral factions (Greenskins, Ogres)`
      - `any = All factions`

> **Note:** If the specified faction is unavailable, the mod will use rebels as a fallback.

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: spawn_armies_ksl_3
```
This will spawn 3 armies for a Kislev faction which is hostile towards the player.

---

#### **Lift Fog of War**

- **`peak_10`, `peak_5`, `peak_2`, `peak_1`**  
  Lifts the fog of war by revealing a random number of regions.  
  - The number represents the early cancel chance (cumulative) for each region. These chances build up over time to 100% (sure cancel).
  - Resulting in a maximum of 10, 20, 50, 100 provinces revealed for the player.
  - The revealed AI Faction will act according the normal Total War Logic towards being revealed

> **Note:** randomly selected region can also be sea regions or player controlled regions.

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: peak_10
```
This will lift the fog of war for up to 10 regions with a chance to cancel the process earlier with 10% per allready revealed region.

---

#### **Switch Cities Around**

- **`switcharoo_XX`**  
  Switches cities for a total of `XX` random alive factions. In each iteration, one of the factions gets a city, while the following factions receive one of their cities.  
  As initual city to reassign an empty city is used somewhere on the map.

- **`switcharoo_XX_ai`**  
  Similar to `switcharoo_XX`, but only AI factions are affected. The player is excluded from this process.

> **Note:** If there is no empty city availble it will try to use a city occupied by a faction with more than 2 cities.

**Example Usage** in `tdw_twitch_points_punishment.txt`:
```txt
name1: switcharoo_5
```
This will swap 1 city for 5 factions, assigning them new cities as per the logic described.

---

### Queue Handling and Prioritization

Commands are processed from two seperate queues: a **priority queue** and a **normal queue**. Users in the `tdw_priority_users.txt` file are prioritized, meaning their commands are handled first.

both queues are processed in a **stack**-style order (LIFO - Last In, First Out), meaning the most recently added commands are checked first. This means that the most recent commands take precedence over earlier added ones.

1. **Successful Commands**: Logged in `tdw_twitch_points_handled.txt`.
   **Example Output** in  `tdw_twitch_points_handled.txt`:
   ```txt
   Handled Entry: ID = 6, Keyword = nur_corruption_effect_all, User = name1
   Handled Entry: ID = 5, Keyword = kho_corruption_effect_all, User = name2
   ```

2. **Unsuccessful Commands**: Retry in the next round.

--- 

## Example Setup for Streamer.bot

(For other bots, configure them similarly.)

1. Create a chat command (e.g., `!WH3name`) for viewers to submit names.
2. Set up a command trigger when `!WH3name` is used.
3. Configure the bot to:
   - Write submitted names into `tdw_bot_delivered_names.txt`.
   - Ensure the file is saved in the correct Warhammer III directory.
   - Optionally, send a Twitch chat response confirming the rename.

For a visual guide, see: [Imgur setup example](https://imgur.com)

## Additional Links
### o7 Peepo Emotes

- Peepo o7 Emotes available on 7TV: [Click here](https://7tv.app/emote-sets/01JN18FXZ9JG1BEGPY9KVG9BRJ)
  - **Default Emotes**: 3
  - **Empire Emotes**: 4
  - **Kislev Emotes**: 3
  - **Cathay Emotes**: 2
  - **Greenskins Emotes**: 3
  - **Dark Elf Emotes**: 2
  - **Tomb Kings Emotes**: 2
  - **Lizardmen Emotes**: 1

> **Note**: To access these emotes, ensure that you have **7TV** installed and set up for your Twitch channel. The emotes can be added to your chat for any viewer to use during your streams
> For more information about **7tv** and to get started, visit [7TV](https://7tv.app).

- GitHub Repository: [Click here](https://github.com)
