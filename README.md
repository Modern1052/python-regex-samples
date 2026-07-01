# Python 正規表現サンプルコード
\n\n\n\n\n\n\n\n\n
## 動作環境
- Python 3.14

## 必要なライブラリ
以下は本コードで使用する非標準ライブラリです。該当コードを実行する前に別途インストールしてください。
| ライブラリ | インストールコマンド | 使用するコード |
|----|----|----|
| humre | py -3.14 -m pip install humre | 17_humre.py |
| pyperclip | py -3.14 -m pip install pyperclip | 18_phoneAndEmail.py |

## サンプルコード一覧
資料のページ番号に対応しています。
| ページ番号 | ファイル名 | 内容 | 主な構文 |
|----|----|----|----|
| 16-22 | 01_search.py | 文字列のマッチ | .search() |
| 24-25 | 02_group.py | グループ化 | ( ), .group() |
| 27-33 | 03_findall.py | 全パターンのマッチ | .findall() | 
| 39-41 | 04_escape.py | 特殊文字のエスケープ | \\ |
| 43-44 | 05_shorthandCharacterClass.py | 速記文字クラス | \d, \w, \s |
| 45 | 06_pipe.py | いずれかとマッチ | \| |
| 46-48 | 07_characterClass.py | 文字クラス | [abc], [^abc], [a-z] |
| 49 | 08_dot.py | すべての文字にマッチ | . |
| 51-53 | 09_quantifierSyntax.py | 量指定構文 | {m}, {m, n} |
| 54-56 | 10_quantifierOperator.py | 量指定演算子 | ?, *, + |
| 57-58 | 11_greedyAndNongreedy.py | 非強欲なマッチ | {m, n}? |
| 60-62 | 12_startsAndEnds.py | 冒頭または末尾でマッチ | ^, $, \b |
| 64-65 | 13_ignorecase.py | 大文字と小文字 | re.IGNORECASE |
| 66-67 | 14_dotall.py | すべての文字と改行にマッチ | re.DOTALL |
| 68-69 | 15_verbose.py | 正規表現の表記 | re.VERBOSE |
| 71-72 | 16_sub.py | 文字の置き換え | .sub() |
| 73-82 | 17_humre.py | 正規表現の別の表記 | humre |
| 84-91 | 18_phoneAndEmail.py | 電話番号とメールアドレスの検索 |
