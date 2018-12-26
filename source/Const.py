searchRef = {
    "Wikipedia": "https://ja.m.wikipedia.org/wiki/",
    "Weblio英和・和英": "https://ejje.weblio.jp/content/",
    "Weblio辞書": "https://www.weblio.jp/content/",
    "英辞郎": "https://eow.alc.co.jp/search?q=",
    "Google翻訳": "https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ja&text="
}

windowName = "WordSeacher"
windowSizeX = 500
windowSizeY = 500

webViewUA = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) CriOS/61.0.3163.73 Mobile/15A372 Safari/602.1"

welcomePage = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <style type="text/css">
    body { font-family: -apple-system, BlinkMacSystemFont,
     "Helvetica Neue", YuGothic, "ヒラギノ角ゴ ProN W3",
      Hiragino Kaku Gothic ProN, Arial, "メイリオ", Meiryo, sans-serif; }
    </style>
</head>
<body>
    <h1>使い方</h1><br>
    1. 調べたい語句を選択して C + Ctrl または 右クリック → コピー<br><br>
    2. 検索結果が表示される<br><br>
    3. 検索先を変えたい場合は右上のプルダウンメニューから選択<br><br>
</body>
</html>
"""