import pyxel
import json

class App:
    def __init__(self):
        # JSONから音楽データ読み込み
        with open("music.json", "rt") as f:
            self.music = json.load(f)

        self.playing = False
        self.play_music_on_startup()  # 起動時に再生！

    def play_music_on_startup(self):
        for ch, sfx in enumerate(self.music):
            pyxel.sound(ch).set(*sfx)
            pyxel.play(ch, ch, loop=True)
        self.playing = True

    def update(self):

    def draw(self):
        pyxel.cls(0)

App()
