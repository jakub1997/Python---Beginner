from pytube import YouTube
import os


def Download_video(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path="Path")
    except:
        print("There is some issue with downloading!!")
    else:
        print(f'{youtubeObject.title} has been successfuly downloaded!')

def Download_audio(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio=True).last()
    try:
        dwn = youtubeObject.download(output_path="Path")
        base, ext = os.path.splitext(dwn)
        mp3 = base + '.mp3'
        os.rename(dwn, mp3)
    except:
        print("There is some issue with downloading!!")
    else:
        print(f'{youtubeObject.title} has been successfuly downloaded!')

def Download_cc(link):
    try:
        youtubeObject = YouTube(link)
        title = youtubeObject.title
        caption = youtubeObject.captions.get_by_language_code('en')
        srt = caption.generate_srt_captions()
        text_file = open("Path\Output.txt", "w")
        text_file.write(srt)
        text_file.close()
    except:
        print("There is some issue with downloading!!")
    else:
        print(f'{youtubeObject.title} has been successfuly downloaded!')


link = input("Please put your YouTube link here. URL: ")
type_of_file = input("Please type 'video','audio' or 'cc' ")
if type_of_file == "video":
    Download_video(link)
    print(title)
elif type_of_file == "audio":
    Download_audio(link)
elif type_of_file == "cc":
    Download_cc(link)
else:
    print("There is some issue!!")


