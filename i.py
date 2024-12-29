import pyxel  # Pyxelライブラリをインポート

# アプリケーションのメインクラス
class App:
    def __init__(self):
        # 画面サイズを設定してPyxelを初期化（幅160ピクセル、高さ120ピクセル）
        # タイトルバーに表示するタイトルを "Hello Pyxel" に設定
        pyxel.init(160, 120, title="Hello Pyxel")

        # Pyxelの画像バンクに画像をロード
        # images[0]の(0, 0)位置に "assets/pyxel_logo_38x16.png" の画像を読み込む
        # pyxel.images[0].load(0, 0, "assets/pyxel_logo_38x16.png")

        # ゲームループを開始
        # updateメソッドとdrawメソッドを引数として渡す
        pyxel.run(self.update, self.draw)

    # ゲームの状態を更新するメソッド
    def update(self):
        # Qキーが押されたときにアプリケーションを終了する
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    # 画面を描画するメソッド
    def draw(self):
        # 画面を黒色 (カラーコード 0) でクリア
        pyxel.cls(0)

        # "Hello, Pyxel!" というテキストを画面に描画
        # テキストの色はフレームカウントによって変化（16色の循環）
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)

        # 画像を描画
        # 画像バンク0 (images[0]) の (0, 0) から幅38、高さ16の画像を
        # 画面上の (61, 66) に描画
        # pyxel.blt(61, 66, 0, 0, 0, 38, 16)

        # "Lorem Ipsum"という文字列を描画
        pyxel.text(61, 66, "Lorem Ipsum", 7)  # 7は文字色（白）

# アプリケーションのインスタンスを作成して実行
App()
