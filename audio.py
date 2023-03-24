from pytube import YouTube


def download_audio():
    video_url = input('Введи посилання на видео з YouTube: ')
    yt = YouTube (video_url)
    name = f'{yt.streams[0].title}.mp3'
    yt.streams.filter(only_audio=True).first().download("C:\Нова папка", filename=name)
    print('Загрузка завершена!')


download_audio()


if name == "main":
    download_audio()