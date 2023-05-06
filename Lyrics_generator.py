from bs4 import BeautifulSoup
import requests
import webbrowser
import re
import urllib.parse
import validators 

def get_lyrics_url():
    selected_singer = input("Wpisz nazwe piosenkarza: ").strip()
    singer = re.sub(r"\s+", '-', selected_singer)
    song = input(f"Wpisz piosenke {selected_singer}: ").strip()
    genius_url = 'http://genius.com/'
    lyrics_url = f"{genius_url}{singer}-{song.lower()}-lyrics"
    return lyrics_url


def trim_lyrics_url(lyrics_url):
    return re.sub(r"\s+", '-', lyrics_url)


def open_lyrics_url(lyrics_url):
    decoded_url = urllib.parse.unquote(lyrics_url).replace(" ", "-")
    
    webbrowser.open_new_tab(decoded_url)
            


if __name__ == "__main__":
    lyrics_url = get_lyrics_url()
    trimmed_lyrics_url = trim_lyrics_url(lyrics_url)
    open_lyrics_url(trimmed_lyrics_url)

    