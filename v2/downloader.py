from __future__ import unicode_literals
import youtube_dl, os
import shutil
import pygtk
movefiletodownloads = True
pygtk.require('2.0')
import gtk
os.chdir(".//")
ydl_opts = {}
clip = gtk.clipboard_get()
text = clip.wait_for_text()
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([text])
dira = os.listdir(".")
if movefiletodownloads == True:
  if os.path.isdir("./downloads") == True:
    for item in dira:
      if item == 'downloader.py':
        pass
      else:
        dirb = item
    try:
      shutil.move(dirb, "./downloads")
    except shutil.Error:
      print "allready exists"
