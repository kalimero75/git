from pytube import YouTube
import urllib.request
import re
import os
import glob
import shutil

# Text Formatierungen
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
YELLOW = '\033[93m'
GREEN = '\033[92m'

# BG-Color
MAGENTA_BG = '\033[105m'



os.system('clear')
suche = input(f'{BOLD}{CYAN} Suchbegriff : {RESET}')
Eintraege = input(f'{BOLD}{CYAN} Anzahl an Links : {RESET}')
html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={suche}")
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())


for link in video_ids[:int(Eintraege)]:
            
            vid = "https://www.youtube.com/watch?v=" + link
            yt = YouTube(vid)
            yt.title.strip()
                   
            print('>' * 15 + f'{MAGENTA_BG}' + yt.title + f'{RESET}')
            print('>' * 5 + f'{BOLD}{CYAN} Link zum Video : ' + vid + f'{RESET}')
            print('>' * 5 + f'{MAGENTA} Views : ' + str(yt.views) + f'{RESET}')
            print('>' * 5 + f'{BOLD}{CYAN} Hochgeladen : ' + str(yt.publish_date) + f'{RESET}')
            print('>' * 15 + f'{MAGENTA_BG} ' + yt.author + f'{RESET}')
            print("")
            
            
















