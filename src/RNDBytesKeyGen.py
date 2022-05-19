# MIT License

# Copyright (c) 2022 Saket Upadhyay

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import string
import random

from pip import main


class GetKey:
    def getRandomKey(self, keylen):
        LETTERS = string.ascii_letters
        NUMBERS = string.digits
        passlength = keylen
        printable = f'{LETTERS}{NUMBERS}'
        printable = list(printable)
        random.shuffle(printable)
        random_password = random.choices(printable, k=passlength)
        random_password = ''.join(random_password)
        return random_password


if __name__ == "__main__":
    DataLength = 16
    RNDKEY = GetKey()
    datastring = RNDKEY.getRandomKey(16)
    print("Key : "+datastring)
    datahex = []
    for i in datastring:
        datahex.append(hex(ord(i)))
    if len(datahex) != 16:
        Padding = 16-len(datahex)

    ModData = ""
    for val in datahex:
        ModData = ModData+"\\"+str(val)[1:]

    if len(datahex) != 16:
        for i in range(0, Padding):
            ModData = ModData+"\\x00"
    print("HexData to Write : \""+ModData+"\"")
