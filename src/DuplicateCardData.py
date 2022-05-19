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
from time import sleep


class RFIDCard:

    def __init__(self) -> None:
        self.rdr = mfrc522.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)

    def ReadData(self):
        # rdr = mfrc522.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)
        print("")
        print("Place Original card before reader.")
        print("")
        try:
            while True:
                (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)
                if stat == self.rdr.OK:
                    (stat, raw_uid) = self.rdr.anticoll()
                    if stat == self.rdr.OK:
                        print("CARD DETECTED")
                        print(" -  TAG TYPE : 0x%02x" % tag_type)
                        print(" -  UID      : 0x%02x%02x%02x%02x" %
                              (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                        print("")
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
            # exit()
        # except Exception:
        #     print("Error, Exiting Program.")
        #     # exit()

    def WriteData(self, databytes):
        rdr = mfrc522.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)
        print("")
        print("Place Clone card before reader.")
        print("")
        try:
            while True:
                (stat, tag_type) = rdr.request(rdr.REQIDL)
                if stat == rdr.OK:
                    (stat, raw_uid) = rdr.anticoll()
                    if stat == rdr.OK:
                        print("CARD DETECTED")
                        print(" -  TAG TYPE : 0x%02x" % tag_type)
                        print(" -  UID      : 0x%02x%02x%02x%02x" %
                              (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                        print("")
                        if rdr.select_tag(raw_uid) == rdr.OK:
                            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                            if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                                stat = rdr.write(8, databytes)
                                rdr.stop_crypto1()
                                if stat == rdr.OK:
                                    print("DATA WRITTEN TO ADDRESS 0x08")
                                    return (0)
                                else:
                                    print("FAILED")
                            else:
                                print("AUTH ERR")
                        else:
                            print("Failed to select tag")
        except KeyboardInterrupt:
            print("EXITING PROGRAM.")
            # exit()
        # except Exception:
        #     print("Error, Exiting Program.")
        # exit()


if __name__ == "__main__":
    print("Initialising Module=> " + str(uname()[0]))
    CardObject = RFIDCard()
    Secret = CardObject.ReadData()
    print(Secret)
    print(bytes(Secret))
    print("remove the card.")
    sleep(2)
    CardObject.WriteData(bytes(Secret))
