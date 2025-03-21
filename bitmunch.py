# Copyright 2025 Thomas Gingele <b1tc0r3@proton.me>
import random
import string


class BitMunch():
    """
    Wrapper class for the Bitmunch algorithm invented my Mich.
    """
    def __init__(self):
        self.base = "(+!+[])"
        self.preset={
            "a": "(![]+[])[+!+[]]",
            "b": "([]+{})[+!+[]+!+[]]",
            "c": "([]+{})[+!+[]+!+[]+!+[]+!+[]+!+[]]",
            "d": "([][[]]+[])[+!+[]+!+[]]",
            "e": "(!![]+[])[+!+[]+!+[]+!+[]]",
            "f": "(![]+[])[+[]]",
            "g": "(()=>{try{(+[]).toExponential(+[]-+!+[]);}catch(^X^){return ^X^.message;}})()[(+!+[]+!+[]+!+[]+!+[]+!+[])*(+!+[]+!+[]+!+[]+!+[])+!+[]+!+[]+!+[]]".replace("^X^", self._randomize()),
            "h": "(()=>{try{RegExp('[')}catch(^X^){return ^X^.message;}})()[((+!+[]+!+[]+!+[]+!+[]+!+[])*(+!+[]+!+[]+!+[]))-+!+[]]".replace("^X^", self._randomize()),
            "i": "([][[]]+[])[+!+[]+!+[]+!+[]+!+[]+!+[]]",
            "j": "([]+{})[+!+[]+!+[]+!+[]]",
            "k": "(()=>{try{vzwkq}catch(^X^){return ^X^.message;}})()[+!+[]+!+[]+!+[]]".replace("^X^", self._randomize()),
            "l": "(![]+[])[+!+[]+!+[]]",
            "m": "(()=>{try{RegExp('[')}catch(^X^){return ^X^.message;}})()[+!+[]+!+[]+!+[]+!+[]+!+[]]".replace("^X^", self._randomize()),
            "n": "([][[]]+[])[+!+[]]",
            "o": "([]+{})[+!+[]]",
            "p": "(()=>{try{(+[]).toExponential(+[]-+!+[]);}catch(^X^){return ^X^.message;}})()[+[]]".replace("^X^", self._randomize()),
            "q": "(()=>{try{vzwkq}catch(^X^){return ^X^.message;}})()[+!+[]+!+[]+!+[]+!+[]]".replace("^X^", self._randomize()),
            "r": "(!![]+[])[+!+[]]",
            "s": "(![]+[])[+!+[]+!+[]+!+[]]",
            "t": "(!![]+[])[+[]]",
            "u": "(!![]+[])[+!+[]+!+[]]",
            "v": "(()=>{try{vzwkq}catch(^X^){return ^X^.message;}})()[+[]]".replace("^X^", self._randomize()),
            "w": "(()=>{try{vzwkq}catch(^X^){return ^X^.message;}})()[+!+[]+!+[]]".replace("^X^", self._randomize()),
            "x": "(()=>{try{JSON.parse([])}catch(^X^){return ^X^.message;}})()[(+!+[]+!+[]+!+[]+!+[]+!+[])*(+!+[]+!+[]+!+[])]".replace("^X^", self._randomize()),
            "y": "((+!+[]/+[])+[])[(+!+[]+!+[]+!+[])*(+!+[]+!+[])+!+[]]",
            "z": "(()=>{try{vzwkq}catch(^X^){return ^X^.message;}})()[+!+[]]".replace("^X^", self._randomize()),
            " ": "([]+{})[(+!+[]+!+[]+!+[])*(+!+[]+!+[])+!+[]]"
        }

    def _randomize(self) -> str:
        result = ""

        for _ in range(1, random.choice(range(2, 10))):
            result += random.choice(string.ascii_letters)

        return result

    def _manual_char_encode(self, x) -> str:
        result = self.base

        x = ord(x)
        for _ in range(0, x - 1):
            result += "+" + self.base

        return result

    def _generate_padding(self, amount: int) -> str:
        result = ""

        for i in range(0, amount):
            junk = self._randomize()
            result += self.encode(junk)

            if i < amount - 1:
                result += "+"

        return result

    def encode(self, content: str) -> str:
        """
        Encode a string using BitMunch.

        Parameters:
            content: str
                The string that will be encoded.
        Returns: str
            The encoded text.
        """
        result = ""

        for i, byte in enumerate(content):
            if byte in self.preset.keys():
                result += self.preset[byte]

            else:
                result += "String.fromCharCode(" + self._manual_char_encode(byte) + ")"

            if i < len(content) - 1:
                result += "+"

        return result

    def encode_self_executing(self, content: str, padding: int) -> str:
        """
        Encode a string using BitMunch. The string will be executed as javascript code
        when pasted into a terminal.

        Parameters:
            content: str
                The string that will be encoded.

            padding: int
                Add anywhere between padding * 2 and padding * 10
                characters (randmoized) to the start and end of
                the function call for extra obfuscation.

        Returns: str
            The encoded text.
        """
        result = ""
        result +=  self._generate_padding(padding)
        result += "+" if padding else ""
        result += "new Function("
        result += self.encode(content)
        result += ")()"
        result += "+" if padding else ""
        result += self._generate_padding(padding)
        return result
