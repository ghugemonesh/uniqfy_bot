# Telegram Duplicate File Detection Bot

This is a simple Telegram bot that detects and deletes duplicate files in a group or channel. 
The bot uses the unique file ID assigned by Telegram to each file to detect duplicates. It also provides commands to exclude certain files from being deleted.

## Features

- Detects and deletes duplicate files in a group or channel.
- Allows you to exclude certain files from being deleted using the `/exclude` command.
- Allows you to remove files from the exclude list using the `/remove_exclude` command.
- Remembers the file IDs of seen and excluded files across different runs of the script.

## Requirements

- Python 3.6 or higher
- python-telegram-bot library
- A Telegram bot token
- A Telegram group or channel where the bot has the necessary permissions to delete messages

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/telegram-duplicate-file-detection-bot.git
    cd telegram-duplicate-file-detection-bot
    ```

2. Install the required Python libraries:

    ```bash
    pip install python-telegram-bot
    ```
     ```bash
    pip install telethon
    ```
3. Replace `'your_api_id'`, `'your_api_hash'`, and `'your_bot_token'` in the script with your actual Telegram API ID, API hash, and bot token respectively.

4. Run the bot:

    ```bash
    python bot.py
    ```

## Usage

1. Add the bot to your Telegram group or channel.
2. Use the `/exclude <file_id>` command to exclude a file from being deleted.
3. Use the `/remove_exclude <file_id>` command to remove a file from the exclude list.

