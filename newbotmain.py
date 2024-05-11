import pickle
from telethon import TelegramClient, events

api_id = 'your_api_id'
api_hash = 'your_api_hash'
bot_token = 'your_bot_token'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Load seen_files and excluded_files from file, or create new sets if file does not exist
try:
    with open('seen_files.pkl', 'rb') as f:
        seen_files = pickle.load(f)
except FileNotFoundError:
    seen_files = set()

try:
    with open('excluded_files.pkl', 'rb') as f:
        excluded_files = pickle.load(f)
except FileNotFoundError:
    excluded_files = set()

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! I am your duplicate file detection bot. I will help you detect and delete duplicate files in this group or channel belonging @moneshghuge commands /start /exclude /remove_exclude /clearhistory /clearexclude.')
    print('Bot started.')

@client.on(events.NewMessage(pattern='/exclude'))
async def exclude(event):
    file_id = event.message.text.split()[1]  # Get the file ID from the message text
    excluded_files.add(file_id)
    with open('excluded_files.pkl', 'wb') as f:  # Save excluded_files to file
        pickle.dump(excluded_files, f)
    await event.respond(f'File with id {file_id} has been excluded.')
    print(f'Excluded file with id {file_id}')

@client.on(events.NewMessage(pattern='/remove_exclude'))
async def remove_exclude(event):
    file_id = event.message.text.split()[1]  # Get the file ID from the message text
    if file_id in excluded_files:
        excluded_files.remove(file_id)
        with open('excluded_files.pkl', 'wb') as f:  # Save excluded_files to file
            pickle.dump(excluded_files, f)
        await event.respond(f'File with id {file_id} has been removed from the exclude list.')
        print(f'Removed file with id {file_id} from the exclude list')
    else:
        await event.respond(f'File with id {file_id} is not in the exclude list.')

@client.on(events.NewMessage(pattern='/clearhistory'))
async def clear_history(event):
    seen_files.clear()
    with open('seen_files.pkl', 'wb') as f:  # Save seen_files to file
        pickle.dump(seen_files, f)
    await event.respond('File history has been cleared.')
    print('File history has been cleared')

@client.on(events.NewMessage(pattern='/clearexclude'))
async def clear_exclude(event):
    excluded_files.clear()
    with open('excluded_files.pkl', 'wb') as f:  # Save excluded_files to file
        pickle.dump(excluded_files, f)
    await event.respond('Exclude list has been cleared.')
    print('Exclude list has been cleared')

@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.message.media:
        file_id = event.message.file.id
        if file_id in seen_files and file_id not in excluded_files:
            await client.delete_messages(event.chat_id, event.message.id)
            print(f'Deleted duplicate file with id {file_id}')
        else:
            seen_files.add(file_id)
            with open('seen_files.pkl', 'wb') as f:  # Save seen_files to file
                pickle.dump(seen_files, f)

client.run_until_disconnected()
