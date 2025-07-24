# <img width="38" height="38" alt="Clyde Discord Emoji" src="https://github.com/user-attachments/assets/65aa64ff-f812-4da0-92ce-e43620829e4a" /> <span>Discord Translation Bot<span/>

A Discord bot that translates messages into multiple languages using flag emoji reactions! Powered by [discord.py](https://github.com/Rapptz/discord.py) and [googletrans](https://github.com/ssut/py-googletrans).

---

## Features

- 🌍 **Translate any message**: React to a message with a flag emoji, and the bot will reply with a translation in that language.
- 🏳️‍🌈 **Supports 40+ languages**: Just use the corresponding country flag emoji!
- 🔊 **Pronunciation**: Get the pronunciation of the translated text.
- 🕵️ **Language detection**: The bot detects the original language and shows detection confidence.

---

## Supported Languages

| Flag | Language | Code | Flag | Language | Code |
|------|----------|------|------|----------|------|
| 🇺🇸  | English  | en   | 🇩🇪  | German   | de   |
| 🇫🇷  | French   | fr   | 🇪🇸  | Spanish  | es   |
| 🇮🇹  | Italian  | it   | 🇵🇹  | Portuguese | pt  |
| 🇷🇺  | Russian  | ru   | 🇦🇱  | Albanian | sq   |
| 🇸🇦  | Arabic   | ar   | 🇧🇦  | Bosnian  | bs   |
| 🇧🇬  | Bulgarian| bg   | 🇨🇳  | Chinese (Simplified) | zh-CN |
| 🇭🇷  | Croatian | hr   | 🇨🇿  | Czech    | cs   |
| 🇩🇰  | Danish   | da   | 🇪🇪  | Estonian | et   |
| 🇫🇮  | Finnish  | fi   | 🇬🇷  | Greek    | el   |
| 🇭🇺  | Hungarian| hu   | 🇮🇩  | Indonesian | id  |
| 🇮🇳  | Hindi    | hi   | 🇮🇪  | Irish    | ga   |
| 🇮🇸  | Icelandic| is   | 🇮🇱  | Hebrew   | he   |
| 🇯🇵  | Japanese | ja   | 🇰🇷  | Korean   | ko   |
| 🇱🇻  | Latvian  | lv   | 🇱🇹  | Lithuanian | lt  |
| 🇲🇹  | Maltese  | mt   | 🇲🇪  | Serbian  | sr   |
| 🇳🇱  | Dutch    | nl   | 🇳🇴  | Norwegian| no   |
| 🇵🇰  | Urdu     | ur   | 🇵🇱  | Polish   | pl   |
| 🇷🇴  | Romanian | ro   | 🇷🇸  | Serbian  | sr   |
| 🇸🇰  | Slovak   | sk   | 🇸🇮  | Slovenian| sl   |
| 🇸🇬  | Swedish  | sv   | 🇹🇭  | Thai     | th   |
| 🇹🇷  | Turkish  | tr   | 🇹🇼  | Chinese (Traditional) | zh-TW |
| 🇺🇦  | Ukrainian| uk   | 🇻🇦  | Latin    | la   |

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/translation-bot.git
cd translation-bot
```

### 2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your Discord bot token

- Create a `.env` file in the project root:
  ```
  TOKEN=your_discord_bot_token_here
  ```

### 5. Run the bot

```bash
python main.py
```

---

## Usage

1. Invite the bot to your server.
2. React to any message with a supported flag emoji.
3. The bot will reply with a translation, pronunciation, and detected language.

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss what you would like to change.
