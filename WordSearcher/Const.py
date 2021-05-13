##
##    Copyright (C) 2021 kapifuji
##
##    This file is part of WordSearcher.
##
##    WordSearcher is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License.
##
##
##    WordSearcher is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with WordSearcher.  If not, see <https://www.gnu.org/licenses/>.
##

# 検索先リスト
searchRef = {
    "Wikipedia": "https://ja.m.wikipedia.org/wiki/",
    "Weblio英和・和英": "https://ejje.weblio.jp/content/",
    "英辞郎": "https://eow.alc.co.jp/search?q=",
    "Google翻訳　日英": "https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=ja&tl=en&text=",
    "Google翻訳　英日": "https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ja&text=",
    "DeepL　日英": "https://www.deepl.com/translator#ja/en/",
    "DeepL　英日": "https://www.deepl.com/translator#en/ja/",
    "Google検索": "https://www.google.com/search?q=",
    "Weblio辞書": "https://www.weblio.jp/content/",
    "コトバンク": "https://kotobank.jp/word/",
    "Twitter": "https://twitter.com/search?q=",
    "Googleトレンド": "https://trends.google.co.jp/trends/explore?geo=JP&q=",
    "WolframAlpha": "https://m.wolframalpha.com/input/?i=",
}

# ウインドウの名前とサイズ
windowName = "WordSearcher"
windowSizeX = 500
windowSizeY = 600

# 使用するUserAgent
webViewUA = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) CriOS/61.0.3163.73 Mobile/15A372 Safari/602.1"

# 起動時画面用HTML
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