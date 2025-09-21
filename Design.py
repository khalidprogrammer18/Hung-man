def shape1(text):
    return (f"\n     ---<( {text} )>---")

def shape2( text , symbol = "=" ):
    if len(symbol) == 1 :
        print()
        print( f"{ symbol }" * ( len(text) + 8 ) )
        print( f"{ symbol * 3 } {text} { symbol * 3 }" )
        print( f"{ symbol }" * ( len(text) + 8 ) , end="\n\n")
    else:
        print("\n     ---<( Frame must be one singal symbol )>---\n")

def shape3(text):
    width = len(text) + 4
    print("\n╔" + "═" * width + "╗")
    print(f"║  {text}  ║")
    print("╚" + "═" * width + "╝" , end="\n\n")

def shape4( text , edge = "+" , frame = "-" ):
    if len(edge) == 1 and len(frame) == 1 :
        line = f"{edge}" + f"{frame}" * (len(text) + 4) + f"{edge}"
        print()
        print(line)
        print(f"|  {text}  |")
        print( line , end= "\n\n" )
    else:
        print("\n     ---<( Frame must be one singal symbol and singal frame )>---\n")

def shape5(text, frame = "="):
    if len(frame) == 1 :
        line = "<" + f"{frame}" * (len(text) + 4) + ">"
        print()
        print( line )
        print(f"|  {text}  |")
        print( line , end = "\n\n" )
    else:
        print("\n     ---<( Frame must be one singal symbol )>---\n")

def PartLine(symbol):
    if len(symbol) == 1 :
        print()
        print( f"{symbol}" * 157 , end="\n\n" )
    else:
        print("\n     ---<( Frame must be one singal symbol )>---\n")

def FullLine(symbol):
    if len(symbol) == 1 :
        print()
        print( f"{symbol}" * 199 , end="\n\n" )
    else:
        print("\n     ---<( Frame must be one singal symbol )>---\n")

def FullLinePlus(symbol):
    if len(symbol) == 1 :
        print()
        print( f"{symbol}" * 209 , end="\n\n" )
    else:
        print("\n     ---<( Frame must be one singal symbol )>---\n")

def correct():
    return "✅"

def wrong():
    return "❌"

def square(color):
    if color == "RED" or color == "red" or color == "R" or color == "r":
        return "🟥"
    elif color == "ORANGE" or color == "orange" or color == "O" or color == "o":
        return"🟧"
    elif color == "YELLOW" or color == "yellow" or color == "Y" or color == "y":
        return "🟨"
    elif color == "GREEN" or color == "green" or color == "G" or color == "g":
        return "🟩"
    elif color == "BLUE" or color == "blue":
        return "🟦"
    elif color == "PURPLE" or color == "purple" or color == "P" or color == "p":
        return "🟪"
    elif color == "BLACK" or color == "black":
        return "⬛"
    elif color == "WHITE" or color == "white" or color == "W" or color == "w":
        return "⬜"
    else:
        print("\n     ---<( You must enter the color in full upper case or full lower case or a singal first letter )>---\n")

def circle(color):
    if color == "RED" or color == "red" or color == "R" or color == "r":
        return"🔴"
    elif color == "ORANGE" or color == "orange" or color == "O" or color == "o":
        return "🟠"
    elif color == "YELLOW" or color == "yellow" or color == "Y" or color == "y":
        return "🟡"
    elif color == "GREEN" or color == "green" or color == "G" or color == "g":
        return "🟢"
    elif color == "BLUE" or color == "blue":
        return "🔵"
    elif color == "PURPLE" or color == "purple" or color == "P" or color == "p":
        return "🟣"
    elif color == "BLACK" or color == "black":
        return "⚫"
    elif color == "WHITE" or color == "white" or color == "W" or color == "w":
        return "⚪"
    else:
        print("\n     ---<( You must enter the color in full upper case or full lower case or a singal first letter )>---\n")

def sign(sign_type):
    if sign_type == "upper" or sign_type == "UPPER":
        return "🔠"
    elif sign_type == "lower" or sign_type == "LOWER":
        return "🔡"
    elif sign_type == "int" or sign_type == "INT" or sign_type == "intger" or sign_type == "INTGER":
        return "🔢"
    elif sign_type == "smb" or sign_type == "SMB" or sign_type == "symbol" or sign_type == "SYMBOL":
        return "🔣"
    else:
        print("\n     ---<( You must enter the type ( upper or lower or intger(int) or symbol(smb) ) )>---\n")

def numbers(number):
    if number == "ZERO" or number == "zero" or number == "0" or number == 0:
        return "0️⃣"
    elif number == "ONE" or number == "one" or number == "1" or number == 1:
        return "1️⃣"
    elif number == "TWO" or number == "two" or number == "2" or number == 2:
        return "2️⃣"
    elif number == "THREE" or number == "three" or number == "3" or number == 3:
        return "3️⃣"
    elif number == "FOUR" or number == "four" or number == "4" or number == 4:
        return "4️⃣"
    elif number == "FIVE" or number == "five" or number == "5" or number == 5:
        return "5️⃣"
    elif number == "SIX" or number == "six" or number == "6" or number == 6:
        return "6️⃣"
    elif number == "SEVEN" or number == "seven" or number == "7" or number == 7:
        return "7️⃣"
    elif number == "EIGHT" or number == "eight" or number == "8" or number == 8:
        return "8️⃣"
    elif number == "NINE" or number == "nine" or number == "9" or number == 9:
        return "9️⃣"
    elif number == "TEN" or number == "ten" or number == "10" or number == 10:
        return "🔟"
    else:
        print("\n     ---<( You must enter a number from ( 0 to 10 ) )>---\n")

def phrases(word):
    if word == "VS" or word == "vs":
        return "🆚"
    elif word == "FREE" or word == "free":
        return "🆓"
    elif word == "COOL" or word == "cool":
        return "🆓"
    elif word == "OK" or word == "ok":
        return "🆗"
    elif word == "NEW" or word == "new":
        return "🆕"
    elif word == "RESTART" or word == "restart":
        return "🔄"
    else:
        print("\n     ---<( You must choose among ( VS or FREE or COOL or OK or NEW ) )>---\n")

def marks(mark,color):
    if mark == "QUESTION" or mark == "question" or mark == "Q" or mark == "q":
        if color == "RED" or color == "red" or color == "R" or color == "r":
            return "❓"
        elif color == "WHITE" or color == "white" or color == "W" or color == "w":
            return "❔"
        else:
            print("\n     ---<( You must choose a color between ( red(R) or white(W) ) )>---\n")
    elif mark == "EXCLAMATION" or mark == "exclamation" or mark == "E" or mark == "e":
        if color == "RED" or color == "red" or color == "R" or color == "r":
            return "❗"
        elif color == "WHITE" or color == "white" or color == "W" or color == "w":
            return "❕"
        else:
            print("\n     ---<( You must choose a color between ( red(R) or white(W) ) )>---\n")
    else:
        print("\n     ---<( You must choose a mark between ( question(Q) or exclamation(E) ) )>---\n")

def arrow(direction):
    if direction == "UP" or direction == "up":
        return "⬆️"
    elif direction == "DOWN" or direction == "down":
        return "⬇️"
    elif direction == "RIGHT" or direction == "right":
        return "➡️"
    elif direction == "LEFT" or direction == "left":
        return "⬅️"
    else:
        print("\n     ---<( You must choose a direction among ( UP or DOWN or RIGHT or LEFT ) )>---\n")

def hands(position):
    if position == "HI" or position == "hi":
        return "👋"
    elif position == "RIGHT" or position == "right":
        return "👉"
    elif position == "LEFT" or position == "left":
        return "👈"
    elif position == "UP" or position == "up":
        return "👆"
    elif position == "DOWN" or position == "down":
        return "👇"
    elif position == "GOOD" or position == "good":
        return "👍"
    elif position == "BAD" or position == "bad":
        return "👎"
    elif position == "CLAP" or position == "clap":
        return "👏"
    elif position == "HEART" or position == "heart":
        return "🫶"
    else:
        print("\n     ---<( You must choose among ( HI or RIGHT or LEFT or UP or DOWN or GOOD or BAD or CLAP or HEART ) )>---\n")

def heart(color):
    if color == "RED" or color == "red" or color == "R" or color == "r":
        return "❤️"
    elif color == "PINK" or color == "pink" or color == "P" or color == "p":
        return "🩷"
    elif color == "ORANGE" or color == "orange" or color == "O" or color == "o":
        return"🧡"
    elif color == "YELLOW" or color == "yellow" or color == "Y" or color == "y":
        return "💛"
    elif color == "GREEN" or color == "green" or color == "G" or color == "g":
        return "💚"
    elif color == "BLUE" or color == "blue":
        return "💙"
    elif color == "PURPLE" or color == "purple" or color == "P" or color == "p":
        return "💜"
    elif color == "LIGHT BLUE" or color == "light blue" or color == "LB" or color == "lb":
        return "🩵"
    elif color == "BLACK" or color == "black":
        return "🖤"
    elif color == "GREY" or color == "grey" or color == "G" or color == "g":
        return "🩶"
    elif color == "WHITE" or color == "white" or color == "W" or color == "w":
        return "🤍"
    else:
        print("\n     ---<( You must enter the color in full upper case or full lower case or a singal first letter )>---\n")

def emojies(case):
    if case == "LAUGH" or case == "laugh":
        return "😂"
    elif case == "HARDLAUGH" or case == "hardlaugh":
        return "🤣"
    elif case == "SMILE" or case == "smile":
        return "🙂"
    elif case == "FLIPSMILE" or case == "flipsmile":
        return "🙃"
    elif case == "LOVE" or case == "love":
        return "🥰"
    elif case == "LOVE2" or case == "love2":
        return "😍"
    elif case == "TEAR" or case == "tear":
        return "🥲"
    elif case == "LINES" or case == "lines":
        return "😑"
    elif case == "SAD" or case == "sad":
        return "☹️"
    elif case == "ANGRY" or case == "angry":
        return "😡"
    elif case == "SKULL" or case == "skull":
        return "☠️"
    else:
        print("\n     ---<( You must enter a case of emogy ( smile - flipsmile - love - love2 - tear - lines - sad - angry - skull ) )>---\n")

def color(text,color="",font="" ,background_color="") :

    '''\n
                                            ---<( color function )>---\n
    color : black - red - green - yellow - blue - magenta - cyan - white ( also can use 'color(0-255)' or 'rbg(r,b,g)' )
    font : bold - dim	- italic - underline - strike - blink - reverse
    backgroundcolor : on black - on red - on green - on yellow - on blue - on magenta - on cyan - on white
    '''
    from rich.console import Console
    console = Console()
    return console.print(f"[{font} {color} {background_color}] {text}[/{font} {color} {background_color}]")