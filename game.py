import pyxel
import random

# 使う色（Pyxelの色番号）
COLOR_CODES = [8, 9, 11, 10, 13, 14]  # 赤, 青, 緑, 黄, 紫, オレンジ
COLOR_NAMES = ['RED', 'ORANGE', 'GREEN', 'YELLOW', 'GRAY', 'PINK']
COLOR_MAP = dict(zip(COLOR_CODES, COLOR_NAMES))

BUTTON_SIZE = 16

class App:
    def __init__(self):
        pyxel.init(160, 160, title="color get game")
        self.answer = [random.choice(COLOR_CODES) for _ in range(4)]
        print("debug anser:", [COLOR_MAP[c] for c in self.answer])  # 開発用
        self.guess = []
        self.history = []
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx, my = pyxel.mouse_x, pyxel.mouse_y

            # 色ボタンをクリックしたか？
            for i, color in enumerate(COLOR_CODES):
                x, y = 10 + i * (BUTTON_SIZE + 4), 10
                if x <= mx <= x + BUTTON_SIZE and y <= my <= y + BUTTON_SIZE:
                    if len(self.guess) < 4:
                        self.guess.append(color)

            # 決定ボタン
            if 10 <= mx <= 50 and 50 <= my <= 62:
                if len(self.guess) == 4:
                    self.check_answer()
                    self.guess = []

            # リセットボタン
            if 60 <= mx <= 100 and 50 <= my <= 62:
                self.guess = []

    def check_answer(self):
        guess = self.guess[:]
        temp_answer = self.answer[:]
        hit = 0
        blow = 0

        # ヒット判定
        for i in range(4):
            if guess[i] == temp_answer[i]:
                hit += 1
                guess[i] = temp_answer[i] = -1

        # ブロー判定
        for i in range(4):
            if guess[i] != -1 and guess[i] in temp_answer:
                blow += 1
                temp_answer[temp_answer.index(guess[i])] = -1

        self.history.append((self.guess[:], hit, blow))

        if hit == 4:
            print("correct!")

    def draw(self):
        pyxel.cls(7)  # 背景色 白

        # 色選択ボタン
        for i, color in enumerate(COLOR_CODES):
            x, y = 10 + i * (BUTTON_SIZE + 4), 10
            pyxel.rect(x, y, BUTTON_SIZE, BUTTON_SIZE, color)
            pyxel.rectb(x, y, BUTTON_SIZE, BUTTON_SIZE, 0)  # 黒フチ追加

        # 現在の選択
        pyxel.text(10, 30, "select:", 0)  # 黒文字
        for i, color in enumerate(self.guess):
            pyxel.circ(70 + i * 12, 35, 5, color)

        # 決定 / リセットボタン（ラベル付き）
        pyxel.rect(10, 50, 40, 12, 5)  # 決定ボタン背景（赤系）
        pyxel.text(13, 53, "diside", 7)  # 白文字

        pyxel.rect(60, 50, 40, 12, 9)  # リセットボタン背景（青系）
        pyxel.text(63, 53, "reset", 7)

        # 履歴表示
        pyxel.text(10, 70, "history:", 0)  # 黒文字
        for i, (guess, hit, blow) in enumerate(self.history[-5:]):
            y = 80 + i * 18  # 描画位置調整（元の 12 → 18 に変更）
            for j, color in enumerate(guess):
                pyxel.circ(10 + j * 12, y + 5, 4, color)
            pyxel.text(65, y, f"H:{hit} B:{blow}", 0)




App()
