# PiPicoRFID
![](https://github.com/Saket-Upadhyay/PiPicoRFID/blob/main/docs/repository-poster.png)
Code and modified library to Read/Write data in MIFARE RFID Cards and Tokens using Raspberry Pi Pico Microcontroller and MFRC522 Module. Written in MicroPython.

### Pinout
#### Raspberry Pi Pico
#### RC522 RFID Module

### Hardware Connection (RC522 to Pico)

| **RC522 RFID Reader Module**        | **Raspberry Pi Pico**        |
|-------------------------------------|------------------------------|
|     VCC                             |     3.3V                     |
|     RST                             |     GP0                      |
|     GND                             |     GND                      |
|     IRQ                             |     Not connected            |
|     MISO                            |     GP4                      |
|     MOSI                            |     GP3                      |
|     SCK                             |     GP2                      |
|     SDA                             |     GP1                      |
