# Converts Standard Elladian Text Interface to ASCII/Unicode and back again
class seti2ascii:
    # Dictionary that contains all SETI 1.0 characters in order as their ASCII/unicode counterparts, starting from 0x00.
    # Remember that Bosnisil machines "count backwards," i.e. 0b11111111 is 0, 0b11111110 is 1, etc. Thus, any incoming bytes need to be flipped.
    # Many control codes do not have an equivalent ASCII or Unicode character; some delineators (E.g. 0x0A SUBSECTION) have placeholder values for visual quality.
    char = ["\0", # STOP/EOM
            "", # PAUSE/EOP/EOF
            "", # CANCEL MESSAGE
            "\a", # BELL, likely to be ignored by system
            "", # PING
            "", # ACKNOWLEDGE/PONG
            "\10", # CHARCANCEL/BACKSPACE, likely to be ignored by system
            "", # NEXT CHARACTERS BINARY STREAM
            "", # END BINARY STREAM
            "=====\n", # SUBSECTION
            "", # END SUBSECTION
            "*", # TOGGLE BOLD
            "\n", # NEWLINE
            "\t", # HORIZONTAL TABULATE
            "\v", # VERTICAL TABULATE
            "", # FILE INTO CACHE
            "", # PASTE CACHE INTO INCOMING MESSAGE
            "", # RESPOND WITH CACHE/FORWARD CACHE
            "", # REVISE PREVIOUS MESSAGE
            " ", # SPACE
            " ", # 0% BLOCK
            "\u2591", # 25% BLOCK
            "\u2592", # 50% BLOCK
            "\u2593", # 75% BLOCK
            "\u2588", # 100% BLOCK
            ".", # PERIOD
            ",", # COMMA
            ":", # COLON
            ";", # SEMICOLON
            "?", # QUESTION MARK
            "-", # HYPHEN
            "\u2013", # EN DASH
            "\u2014", # EM DASH
            "/", # FORWARD SLASH
            "\\", # BACKSLASH
            "=", # EQUAL
            "+", # PLUS

