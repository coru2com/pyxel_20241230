import pyxel
import json

class App:
    def __init__(self):
        pyxel.init(160, 120, title="8bit BGM Player")

        # JSONから音楽データ読み込み
        with open("music.json", "rt") as f:
            self.music = json.load(f)

        self.playing = False
        self.play_music_on_startup()  # 起動時に再生！

        pyxel.run(self.update, self.draw)

    def play_music_on_startup(self):
        for ch, sfx in enumerate(self.music):
            pyxel.sound(ch).set(*sfx)
            pyxel.play(ch, ch, loop=True)
        self.playing = True

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.playing:
                pyxel.stop()
                self.playing = False
            else:
                self.play_music_on_startup()

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(30, 50, "[SPACE] Play / Stop", 7)
        pyxel.text(30, 60, "[ESC] Exit", 7)

App()
