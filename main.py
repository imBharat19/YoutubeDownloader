from pytube import YouTube


def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("There has been error in downloading the video...")
  print("This download has been completed.")


link = input("Please put your youtube link here... : ")
Download(link)
