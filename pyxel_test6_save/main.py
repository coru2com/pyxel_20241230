import pyxel
from js import window  # これが超重要！

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.score = 0
        self.load_score()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.score += 1

        if pyxel.btnp(pyxel.KEY_S):
            self.save_score()

        if pyxel.btnp(pyxel.KEY_L):
            self.load_score()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, f"Score: {self.score}", 7)
        pyxel.text(10, 30, "SPACE = +1", 6)
        pyxel.text(10, 40, "S = Save / L = Load", 6)

    def save_score(self):
        window.localStorage.setItem("score", str(self.score))

    def load_score(self):
        data = window.localStorage.getItem("score")
        if data:
            self.score = int(data)

App()
