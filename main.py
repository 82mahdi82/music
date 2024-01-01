
import telebot
from youtubesearchpython import VideosSearch
import youtube_dl

token = '6317356905:AAGQ2p8Lo0Kc4mkChTmE7ZbI2p1bzw9cIO8' # Your bot token from @BotFather
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to MusicBot! Use /search to find and download music.')

@bot.message_handler(commands=['search'])
def search_music(message):
    # Get the query from the user
    query = message.text[8:]
    if not query:
        bot.reply_to(message, 'Please enter a music name after /search.')
        return

    # Search for the first video result on YouTube
    videos_search = VideosSearch(query, limit = 1)
    video = videos_search.result()['result'][0]
    url = video['link']
    title = video['title']

    # Download the audio file from YouTube
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        filename = f'{title}.mp3'

    # Send the audio file in the chat
    bot.reply_to(message, f'Here is the audio file for {query}:')
    audio = open(filename, 'rb')
    bot.send_audio(message.chat.id, audio)

bot.infinity_polling()