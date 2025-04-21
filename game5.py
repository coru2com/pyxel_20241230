import pyxel
import random
import json

# Color settings
COLOR_CODES = [8, 9, 11, 10, 13, 14]  # RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE
COLOR_NAMES = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'PURPLE', 'ORANGE']
COLOR_MAP = dict(zip(COLOR_CODES, COLOR_NAMES))

BUTTON_SIZE = 16

class App:
    def __init__(self):
        pyxel.init(160, 160, title="Color Guess Game")
        pyxel.load("assets.pyxres")
        pyxel.mouse(True)
        # JSONから音楽データ読み込み
        with open("music.json", "rt") as f:
            self.music = json.load(f)
        self.mode = "title"  # title, game, result
        self.reset_game()

        pyxel.run(self.update, self.draw)

    def play_music_on_startup(self):
        for ch, sfx in enumerate(self.music):
            pyxel.sound(ch).set(*sfx)
            pyxel.play(ch, ch, loop=True)
        self.playing = True

    def reset_game(self):
        self.answer = [random.choice(COLOR_CODES) for _ in range(4)]
        print("DEBUG Answer:", [COLOR_MAP[c] for c in self.answer])
        self.guess = []
        self.history = []
        self.cleared = False
        self.is_game_over = False


    def update(self):
        if self.mode == "title":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.mode = "game"
                self.reset_game()

        elif self.mode == "game":
            self.update_game()

        elif self.mode == "result":

            # 「Back to Title」ボタン
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                mx, my = pyxel.mouse_x, pyxel.mouse_y
                if 40 <= mx <= 120 and 60 <= my <= 72:
                    self.mode = "title"



    def update_game(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx, my = pyxel.mouse_x, pyxel.mouse_y

            # Color buttons
            for i, color in enumerate(COLOR_CODES):
                x, y = 10 + i * (BUTTON_SIZE + 4), 10
                if x <= mx <= x + BUTTON_SIZE and y <= my <= y + BUTTON_SIZE:
                    if len(self.guess) < 4:
                        self.guess.append(color)

            # Submit button
            if 10 <= mx <= 50 and 50 <= my <= 62:
                if len(self.guess) == 4:
                    self.check_answer()
                    self.guess = []

            # Reset button
            if 60 <= mx <= 100 and 50 <= my <= 62:
                self.guess = []

    def check_answer(self):
        guess = self.guess[:]
        temp_answer = self.answer[:]
        hit = 0
        blow = 0

        for i in range(4):
            if guess[i] == temp_answer[i]:
                hit += 1
                guess[i] = temp_answer[i] = -1

        for i in range(4):
            if guess[i] != -1 and guess[i] in temp_answer:
                blow += 1
                temp_answer[temp_answer.index(guess[i])] = -1

        self.history.append((self.guess[:], hit, blow))

        if hit == 4:
            self.cleared = True
            self.mode = "result"
        elif len(self.history) >= 10:
            self.is_game_over = True
            self.mode = "result"

    def draw(self):
        pyxel.cls(7)

        if self.mode == "title":
            pyxel.text(50, 40, "Color Guess Game", 0)
            pyxel.rect(40, 60, 80, 12, 9)
            pyxel.text(65, 63, "START", 7)

        elif self.mode == "game":
            self.draw_game()

        elif self.mode == "result":
            self.draw_game()
            self.draw_result()

    def draw_game(self):
        # Color buttons
        for i, color in enumerate(COLOR_CODES):
            x, y = 10 + i * (BUTTON_SIZE + 4), 10
            pyxel.rect(x, y, BUTTON_SIZE, BUTTON_SIZE, color)
            pyxel.rectb(x, y, BUTTON_SIZE, BUTTON_SIZE, 0)

        # Current selection
        pyxel.text(10, 30, "Selected:", 0)
        for i, color in enumerate(self.guess):
            pyxel.circ(70 + i * 12, 35, 5, color)

        # Submit / Reset buttons
        pyxel.rect(10, 50, 40, 12, 5)
        pyxel.text(16, 53, "OK", 7)
        pyxel.rect(60, 50, 40, 12, 9)
        pyxel.text(66, 53, "Reset", 7)

        # History (2 columns × 5 rows)
        pyxel.text(10, 70, "History:", 0)
        for i, (guess, hit, blow) in enumerate(self.history[-10:]):
            col = i % 2
            row = i // 2
            x_base = 10 + col * 76
            y_base = 80 + row * 14
            for j, color in enumerate(guess):
                pyxel.circ(x_base + j * 10, y_base + 5, 4, color)
            pyxel.text(x_base + 40, y_base + 4, f"H:{hit} B:{blow}", 0)

    def draw_result(self):
        pyxel.rect(10, 10, 140, 55, 3)
        if self.cleared:
            pyxel.text(20, 20, "CLEAR!", 7)
        else:
            pyxel.text(20, 20, "GAME OVER", 7)

        pyxel.text(20, 35, "CORRECT ANSWER:", 7)
        for i, color in enumerate(self.answer):
            pyxel.circ(105 + i * 12, 40, 4, color)

        pyxel.rect(40, 60, 80, 12, 9)
        pyxel.text(60, 63, "RETRY", 7)


App()
