
import telebot
from youtubesearchpython import VideosSearch
import youtube_dl
import requests
from io import BytesIO
token = '6317356905:AAGQ2p8Lo0Kc4mkChTmE7ZbI2p1bzw9cIO8' # Your bot token from @BotFather
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cid=message.chat.id
    bot.reply_to(message, 'Welcome to MusicBot! Use /search to find and download music.')
    res = requests.get("https://rr1---sn-t0a7lnee.googlevideo.com/videoplayback?expire=1704126634&ei=SpSSZfWVK5iO_9EPmrWf2AI&ip=15.235.87.68&id=o-AIn-Pe8FMtipMxrvTSgBgYXmeUcRXRNudbr8rR3UxHwr&itag=17&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=Hi&mm=31%2C26&mn=sn-t0a7lnee%2Csn-p5qlsnrl&ms=au%2Conr&mv=m&mvi=1&pl=24&initcwndbps=121250&vprv=1&mime=video%2F3gpp&gir=yes&clen=399620&dur=48.390&lmt=1698811213016097&mt=1704104710&fvip=2&fexp=24007246&c=ANDROID_EMBEDDED_PLAYER&txp=5318224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgSx-wUYOyV2XZqT90DsM0DxNvND3ZRlx9m-39P18E5vYCIF8was1bO_5eor0C1vJICYxsCpeEIRN6vSk-j5RAgKE2&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AAO5W4owRgIhANoyV-KKDADBHyJ3h5IOxB8hKy7y-PJ4PDP0snJz9_25AiEA2B_ZergE-nkCG6A7wU-Hqd-tNyP9gUgJctCjJNn28LM%3D")
    print(res)
    vi_fi=BytesIO(res.content)
    print(vi_fi)
    bot.send_video(cid,vi_fi)
    # bot.send_message(cid,"https://rr1---sn-t0a7lnee.googlevideo.com/videoplayback?expire=1704126634&ei=SpSSZfWVK5iO_9EPmrWf2AI&ip=15.235.87.68&id=o-AIn-Pe8FMtipMxrvTSgBgYXmeUcRXRNudbr8rR3UxHwr&itag=17&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=Hi&mm=31%2C26&mn=sn-t0a7lnee%2Csn-p5qlsnrl&ms=au%2Conr&mv=m&mvi=1&pl=24&initcwndbps=121250&vprv=1&mime=video%2F3gpp&gir=yes&clen=399620&dur=48.390&lmt=1698811213016097&mt=1704104710&fvip=2&fexp=24007246&c=ANDROID_EMBEDDED_PLAYER&txp=5318224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgSx-wUYOyV2XZqT90DsM0DxNvND3ZRlx9m-39P18E5vYCIF8was1bO_5eor0C1vJICYxsCpeEIRN6vSk-j5RAgKE2&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AAO5W4owRgIhANoyV-KKDADBHyJ3h5IOxB8hKy7y-PJ4PDP0snJz9_25AiEA2B_ZergE-nkCG6A7wU-Hqd-tNyP9gUgJctCjJNn28LM%3D")
@bot.message_handler(commands=['search'])
def search_music(message):
    # Get the query from the user
    query = message.text[8:]
    print(query)
    if not query:
        bot.reply_to(message, 'Please enter a music name after /search.')
        return

    # Search for the first video result on YouTube
    videos_search = VideosSearch(query, limit = 1)
    video = videos_search.result()['result'][0]
    url = video['link']
    print("urrrlll::",url)
    title = video['title']
    print("title::",title)
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



# def test_format_selection_audio_exts(self):
#     formats = [
#         {'format_id': 'mp3-64', 'ext': 'mp3', 'abr': 64, 'url': 'http://_', 'vcodec': 'none'},
#         {'format_id': 'ogg-64', 'ext': 'ogg', 'abr': 64, 'url': 'http://_', 'vcodec': 'none'},
#         {'format_id': 'aac-64', 'ext': 'aac', 'abr': 64, 'url': 'http://_', 'vcodec': 'none'},
#         {'format_id': 'mp3-32', 'ext': 'mp3', 'abr': 32, 'url': 'http://_', 'vcodec': 'none'},
#         {'format_id': 'aac-32', 'ext': 'aac', 'abr': 32, 'url': 'http://_', 'vcodec': 'none'},
#     ]
#     info_dict = _make_result(formats)
#     ydl = YDL({'format': 'best'})
#     ie = YoutubeIE(ydl)
#     ie._sort_formats(info_dict['formats'])
#     ydl.process_ie_result(copy.deepcopy(info_dict))
#     downloaded = ydl.downloaded_info_dicts[0]
#     self.assertEqual(downloaded['format_id'], 'aac-64')
#     ydl = YDL({'format': 'mp3'})
#     ie = YoutubeIE(ydl)
#     ie._sort_formats(info_dict['formats'])
#     ydl.process_ie_result(copy.deepcopy(info_dict))
#     downloaded = ydl.downloaded_info_dicts[0]
#     self.assertEqual(downloaded['format_id'], 'mp3-64')
#     ydl = YDL({'prefer_free_formats': True})
#     ie = YoutubeIE(ydl)
#     ie._sort_formats(info_dict['formats'])
#     ydl.process_ie_result(copy.deepcopy(info_dict))
#     downloaded = ydl.downloaded_info_dicts[0]
#     self.assertEqual(downloaded['format_id'], 'ogg-64')
bot.infinity_polling()