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
            " 0x", # NEXT CHARACTERS BINARY STREAM
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
            "\u00F7", # DIVIDE
            "'", # APOSTROPHE/SINGLE QUOTE
            "\"", # DOUBLE QUOTE
            "%", # PERCENT
            "Solon", # SOLON, actual symbol not available on Unicode systems
            "Nock", # NOCK, actual symbol not available on Unicode systems
            "#", # PUNCH
            "\u00A7", # SECTION
            "(", # OPENING PARENTHESIS
            ")", # CLOSING PARENTHESIS
            "", # SUPERSCRIPT TOGGLE
            "", # SUBSCRIPT TOGGLE
            "{", # OPENING SET
            "}", # CLOSING SET
            "<", # EXPAND/LESS THAN
            ">", # CONTRACT/GREATER THAN
            "|", # PIPE
            "`", # ANGLE APOSTROPHE
            "_", # UNDERSCORE
            "^", # EXPONENT
            "\u2192", # RIGHT ARROW
            "\u2190", # LEFT ARROW
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "p",
            "P",
            "\u03c0", # small pi
            "b",
            "B",
            "\u03b2", # small beta
            "f",
            "F",
            "\u03c6", # small phi
            "v",
            "V",
            "t",
            "T",
            "\u03c4", # small tau
            "s",
            "S",
            "\u03c3", # small sigma
            "d",
            "D",
            "\u03b4", # small delta
            "\u03c2", # small final sigma
            "\u03a3", # big sigma
            "z",
            "Z",
            "\u03b6", # small zeta
            "k",
            "K",
            "\u03ba", # small kappa
            "g",
            "G",
            "j",
            "J",
            "x",
            "X",
            "\u03c7", # small chi
            "h",
            "H",
            "r",
            "R",
            "\u03c1", # small rho
            "l",
            "L",
            "\u03c8", # small psi
            "M",
            "N",
            "m",
            "n",
            "a",
            "A",
            "e",
            "E",
            "\u03b5", # small epsilon
            "i",
            "I",
            "\u03b9", # small iota
            "o",
            "O",
            "\u03c9", # small omega
            "u",
            "U",
            "\u03c5", # small upsilon
            "\u00e7", # latin small letter c with cedilla
            "\u03b7", # small eta
            "y",
            "\u00e6", # latin small letter ae
            "c",
            "C",
            "\u00c7", # latin capital letter c with cedilla
            "\u0294", # latin letter glottal stop
            "\u03b1", # greek small letter alpha
            "\u03b3", # greek small letter gamma
            "\u0393", # greek capital letter gamma
            "\u0394", # greek capital letter delta
            "\u03b8", # greek small letter theta
            "\u0398", # greek capital letter theta
            "\u0399", # greek capital letter iota
            "\u03bb", # greek small letter lambda
            "\u039b", # greek capital letter lambda
            "\u03bc", # greek small letter mu
            "\u03bd", # greek small letter nu
            "\u03be", # greek small letter xi
            "\u039e", # greek capital letter xi
            "\u03a0", # greek capital letter pi
            "\u03a1", # greek capital letter rho
            "\u03a6", # greek capital letter phi
            "\u03a8", # greek capital letter psi
            "\u03a9", # greek capital letter omega
            "q",
            "Q",
            "W",
            "w",
            "Y",
            "", # MOVE UP
            "", # MOVE DOWN
            "", # MOVE LEFT
            "", # MOVE RIGHT
            "", # SHIFT
            "", # FUNC 1
            "", # FUNC 2
            "", # FUNC 3
            "", # FUNC 4
            "", # ALTERNATE
            "", # COMMAND
            "", # EMPHASIZE
            "", # FUNC 5
            "", # FUNC 6
            "", # FUNC 7
            ""] #FUNC 8
    # Greek-English unicode characters for effectively identical characters
    engrequiv = {
            "\u0391":"A",
            "\u0392":"B",
            "\u0395":"E",
            "\u0396":"Z",
            "\u0397":"H",
            "\u039a":"K",
            "\u039c":"M",
            "\u039d":"N",
            "\u039f":"O",
            "\u03a4":"T",
            "\u03a5":"Y",
            "\u03a6":"X"
        }
    

    # Converts SETI 1.0 codes to Unicode characters.
    def seti_code_to_ascii(this, code, asserts_off=False):
        if code < len(this.char):
            # Binary stream is meaningless when converting single characters
            return this.char[code]
        elif not asserts_off:
            raise ValueError("Invalid character code '" + str(code) + "'!")
        
    # Converts unicode to seti
    def ascii_char_to_seti(this, char, asserts_off=False):
        pass


# Various tests.
if __name__ == "__main__":
    converter = seti2ascii()
    for i in range(176):
        print(converter.seti_code_to_ascii(i))
