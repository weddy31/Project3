import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import re
import urllib.parse
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Otwieranie tekstów piosenek")
        self.setGeometry(100, 100, 400, 150)

        # Etykiety i pola tekstowe
        self.singer_label = QLabel("Nazwa piosenkarza:", self)
        self.singer_label.move(10, 10)

        self.singer_entry = QLineEdit(self)
        self.singer_entry.move(120, 10)

        self.song_label = QLabel("Nazwa piosenki:", self)
        self.song_label.move(10, 40)

        self.song_entry = QLineEdit(self)
        self.song_entry.move(120, 40)

        # Przycisk
        self.open_button = QPushButton("Otwórz tekst piosenki", self)
        self.open_button.setGeometry(10, 80, 380, 30)
        self.open_button.clicked.connect(self.open_lyrics)

    # Funkcje
    def get_lyrics_url(self):
        selected_singer = self.singer_entry.text().strip()
        singer = re.sub(r"\s+", '-', selected_singer)
        song = self.song_entry.text().strip()
        genius_url = 'http://genius.com/'
        lyrics_url = f"{genius_url}{singer}-{song.lower()}-lyrics"
        return lyrics_url

    def trim_lyrics_url(self, lyrics_url):
        return re.sub(r"\s+", '-', lyrics_url)

    def open_lyrics(self):
        lyrics_url = self.get_lyrics_url()
        trimmed_lyrics_url = self.trim_lyrics_url(lyrics_url)
        decoded_url = urllib.parse.unquote(trimmed_lyrics_url).replace(" ", "-")
        webbrowser.open_new_tab(decoded_url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

