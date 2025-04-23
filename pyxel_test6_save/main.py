import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, f"Hello!", 7)

App()
