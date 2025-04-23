import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.score += 1

        if pyxel.btnp(pyxel.KEY_S):
            print(f"SAVE:{self.score}")  # JavaScript側で拾う用のセーブ出力

        if pyxel.btnp(pyxel.KEY_L):
            print("LOAD")  # JavaScript側がローカルストレージから読み込んで渡してくる

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, f"Score: {self.score}", 7)
        pyxel.text(10, 30, "SPACE = +1", 6)
        pyxel.text(10, 40, "S = Save / L = Load", 6)

App()
