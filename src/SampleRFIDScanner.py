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

import mfrc522
from os import uname


class RFIDCard:

    def __init__(self) -> None:
        self.rdr = mfrc522.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)

    def ConvertToHexString(self, data):
        hexstring = ""
        for i in data:
            hexstring = hexstring + (hex(i))
        return hexstring

    def AuthCard(self, HSD, FKD):
        FIXHASH = ""
        for i in FKD:
            FIXHASH = FIXHASH + hex(ord(i))

        if HSD == FKD:
            return 1
        return 0

    def ReadData(self):
        print("")
        print("Place the access card before the reader.")
        print("")
        try:
            while True:
                (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)
                if stat == self.rdr.OK:
                    (stat, raw_uid) = self.rdr.anticoll()
                    if stat == self.rdr.OK:
                        print("CARD DETECTED")
                        if self.rdr.select_tag(raw_uid) == self.rdr.OK:
                            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                            if self.rdr.auth(self.rdr.AUTHENT1A, 8, key, raw_uid) == self.rdr.OK:
                                data = self.rdr.read(8)
                                return (data)
                            else:
                                print("AUTH ERR")
                        else:
                            print("Failed to select tag")

        except KeyboardInterrupt:
            print("EXITING PROGRAM.")


if __name__ == "__main__":
    CardObject = RFIDCard()
    FIXKEYSTR = "DwMo0G8ImmULsJDe"
    CardData = CardObject.ReadData()

    if CardObject.AuthCard(CardObject.ConvertToHexString(list(CardData)), FIXKEYSTR):
        print("AUTH SUCCESS. Access Granted.")
    else:
        print("Access Denied.")
