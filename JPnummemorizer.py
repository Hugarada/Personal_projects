#Imports

import random

#functions/subprorams

def clear():
    print("\n" * 1000)

#main

while True:
    clear()
    num = random.randint(0,10000)
    stringnum = str(num)
    numwhole = ""
    numhiragana = ""
    if num == 10000:
        numwhole = "ichi man"
        numhiragana = "いちまん"
    elif len(stringnum) == 4:
        if stringnum[0] == "1":
            numwhole = "issen"
            numhiragana = "いっせん"
        elif stringnum[0] == "2":
            numwhole = "ni sen"
            numhiragana = "にせん"
        elif stringnum[0] == "3":
            numwhole = "san zen"
            numhiragana = "さんぜん"
        elif stringnum[0] == "4":
            numwhole = "yon sen"
            numhiragana = "よんせん"
        elif stringnum[0] == "5":
            numwhole = "go sen"
            numhiragana = "ごせん"
        elif stringnum[0] == "6":
            numwhole = "roku sen"
            numhiragana = "ろくせん"
        elif stringnum[0] == "7":
            numwhole = "nana sen"
            numhiragana = "ななせん"
        elif stringnum[0] == "8":
            numwhole = "hassen"
            numhiragana = "はっせん"
        elif stringnum[0] == "9":
            numwhole = "kyuu sen"
            numhiragana = "きゅうせん"
        numwhole += " "
        if stringnum[1] == "1":
            numwhole += "hyaku"
            numhiragana += "ひゃく"
        elif stringnum[1] == "2":
            numwhole += "ni hyaku"
            numhiragana += "にひゃく"
        elif stringnum[1] == "3":
            numwhole += "san byaku"
            numhiragana += "さんびゃく"
        elif stringnum[1] == "4":
            numwhole += "yon hyaku"
            numhiragana += "よんひゃく"
        elif stringnum[1] == "5":
            numwhole += "go hyaku"
            numhiragana += "ごひゃく"
        elif stringnum[1] == "6":
            numwhole += "roppyaku"
            numhiragana += "ろっぴゃく"
        elif stringnum[1] == "7":
            numwhole += "nana hyaku"
            numhiragana += "ななひゃく"
        elif stringnum[1] == "8":
            numwhole += "happyaku"
            numhiragana += "はっぴゃく"
        elif stringnum[1] == "9":
            numwhole += "kyuu hyaku"
            numhiragana += "きゅうひゃく"
        numwhole += " "
        if stringnum[2] == "1":
            numwhole += "jyuu"
            numhiragana += "じゅう"
        elif stringnum[2] == "2":
            numwhole += "ni jyuu"
            numhiragana += "にじゅう"
        elif stringnum[2] == "3":
            numwhole += "san jyuu"
            numhiragana += "さんじゅう"
        elif stringnum[2] == "4":
            numwhole += "yon jyuu"
            numhiragana += "よんじゅう"
        elif stringnum[2] == "5":
            numwhole += "go jyuu"
            numhiragana += "ごじゅう"
        elif stringnum[2] == "6":
            numwhole += "roku jyuu"
            numhiragana += "ろくじゅう"
        elif stringnum[2] == "7":
            numwhole += "nana jyuu"
            numhiragana += "ななじゅう"
        elif stringnum[2] == "8":
            numwhole += "hachi jyuu"
            numhiragana += "はちじゅう"
        elif stringnum[2] == "9":
            numwhole += "kyuu jyuu"
            numhiragana += "きゅうじゅう"
        numwhole += " "
        if stringnum[3] == "0":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "1":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "2":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "3":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "4":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "5":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "6":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "7":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "8":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[3] == "9":
            numwhole += "rei"
            numhiragana += "れい"
    elif len(stringnum) == 3:
        if stringnum[0] == "1":
            numwhole = "hyaku"
            numhiragana = "ひゃく"
        elif stringnum[0] == "2":
            numwhole = "ni hyaku"
            numhiragana = "にひゃく"
        elif stringnum[0] == "3":
            numwhole = "san byaku"
            numhiragana = "さんびゃく"
        elif stringnum[0] == "4":
            numwhole = "yon hyaku"
            numhiragana = "よんひゃく"
        elif stringnum[0] == "5":
            numwhole = "go hyaku"
            numhiragana = "ごひゃく"
        elif stringnum[0] == "6":
            numwhole = "roppyaku"
            numhiragana = "ろっぴゃく"
        elif stringnum[0] == "7":
            numwhole = "nana hyaku"
            numhiragana = "ななひゃく"
        elif stringnum[0] == "8":
            numwhole = "happyaku"
            numhiragana = "はっぴゃく"
        elif stringnum[0] == "9":
            numwhole = "kyuu hyaku"
            numhiragana = "きゅうひゃく"
        numwhole += " "
        if stringnum[1] == "1":
            numwhole += "jyuu"
            numhiragana += "じゅう"
        elif stringnum[1] == "2":
            numwhole += "ni jyuu"
            numhiragana += "にじゅう"
        elif stringnum[1] == "3":
            numwhole += "san jyuu"
            numhiragana += "さんじゅう"
        elif stringnum[1] == "4":
            numwhole += "yon jyuu"
            numhiragana += "よんじゅう"
        elif stringnum[1] == "5":
            numwhole += "go jyuu"
            numhiragana += "ごじゅう"
        elif stringnum[1] == "6":
            numwhole += "roku jyuu"
            numhiragana += "ろくじゅう"
        elif stringnum[1] == "7":
            numwhole += "nana jyuu"
            numhiragana += "ななじゅう"
        elif stringnum[1] == "8":
            numwhole += "hachi jyuu"
            numhiragana += "はちじゅう"
        elif stringnum[1] == "9":
            numwhole += "kyuu jyuu"
            numhiragana += "きゅうじゅう"
        numwhole += " "
        if stringnum[2] == "0":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "1":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "2":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "3":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "4":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "5":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "6":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "7":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "8":
            numwhole += "rei"
            numhiragana += "れい"
        elif stringnum[2] == "9":
            numwhole += "rei"
            numhiragana += "れい"
        numwhole += " "
    elif len(stringnum) == 2:
        if stringnum[0] == "1":
            numwhole = "jyuu"
            numhiragana = "じゅう"
        elif stringnum[0] == "2":
            numwhole = "ni jyuu"
            numhiragana = "にじゅう"
        elif stringnum[0] == "3":
            numwhole = "san jyuu"
            numhiragana = "さんじゅう"
        elif stringnum[0] == "4":
            numwhole = "yon jyuu"
            numhiragana = "よんじゅう"
        elif stringnum[0] == "5":
            numwhole = "go jyuu"
            numhiragana = "ごじゅう"
        elif stringnum[0] == "6":
            numwhole = "roku jyuu"
            numhiragana = "ろくじゅう"
        elif stringnum[0] == "7":
            numwhole = "nana jyuu"
            numhiragana = "ななじゅう"
        elif stringnum[0] == "8":
            numwhole = "hachi jyuu"
            numhiragana = "はちじゅう"
        elif stringnum[0] == "9":
            numwhole = "kyuu jyuu"
            numhiragana = "きゅうじゅう"
        numwhole += " "
        if stringnum[1] == "0":
            numwhole = "rei"
            numhiragana = "れい"
        elif stringnum[1] == "1":
            numwhole += "icchi"
            numhiragana += "いっち"
        elif stringnum[1] == "2":
            numwhole += "ni"
            numhiragana += "に"
        elif stringnum[1] == "3":
            numwhole += "san"
            numhiragana += "さん"
        elif stringnum[1] == "4":
            numwhole += "yon"
            numhiragana += "よん"
        elif stringnum[1] == "5":
            numwhole += "go"
            numhiragana += "ご"
        elif stringnum[1] == "6":
            numwhole += "roku"
            numhiragana += "ろく"
        elif stringnum[1] == "7":
            numwhole += "nana"
            numhiragana += "なな"
        elif stringnum[1] == "8":
            numwhole += "hachi"
            numhiragana += "はっち"
        elif stringnum[1] == "9":
            numwhole += "kyuu"
            numhiragana += "きゅう"
    elif len(stringnum) == 1:
        if stringnum[0] == "0":
            numwhole = "rei"
            numhiragana = "れい"
        elif stringnum[0] == "1":
            numwhole = "icchi"
            numhiragana = "いっち"
        elif stringnum[0] == "2":
            numwhole = "ni"
            numhiragana = "に"
        elif stringnum[0] == "3":
            numwhole = "san"
            numhiragana = "さん"
        elif stringnum[0] == "4":
            numwhole = "yon"
            numhiragana = "よん"
        elif stringnum[0] == "5":
            numwhole = "go"
            numhiragana = "ご"
        elif stringnum[0] == "6":
            numwhole = "roku"
            numhiragana = "ろく"
        elif stringnum[0] == "7":
            numwhole = "nana"
            numhiragana = "なな"
        elif stringnum[0] == "8":
            numwhole = "hachi"
            numhiragana = "はっち"
        elif stringnum[0] == "9":
            numwhole = "kyuu"
            numhiragana = "きゅう"
    print(num)
    input()
    print(numwhole)
    print(numhiragana)
    something = input()
    if something == "0":
        break
