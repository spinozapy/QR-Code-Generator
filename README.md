# QR Code Generator

**QR Code Generator** is a Python tool that allows you to generate QR codes based on user input. It supports customizable QR code colors and background colors. If no color is provided, it defaults to black and white.

## Requirements

- Python 3.x
- `qrcode` library (Install using `pip install qrcode`)
- `Pillow` library (Install using `pip install Pillow`)
- `colorama` library (Install using `pip install colorama`)

## Installation

1. Clone the repository.
2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file includes the following dependencies:

    ```
    qrcode[pil]
    Pillow
    colorama
    ```

3. Run the tool:

    ```bash
    python main.py
    ```

## Usage

1. Start the QR Code Generator:

    ```bash
    python main.py
    ```

2. Enter the text or URL for the QR code when prompted.

3. Customize the QR code's colors:

    - You will be prompted to enter the foreground (QR code) and background colors in HEX format.
    - If no colors are provided, the QR code will be generated in default black and white colors.

4. The generated QR code will be saved in the `QR Codes` directory with the name you provided.

## Features

- **Customizable Colors:** Users can input HEX codes for the QR code and background colors.
- **Default Colors:** If no color is provided, the default QR code color is black, and the background color is white.
- **Directory Organization:** QR codes are saved in a directory named `QR Codes`, with filenames based on user input.
- **Clear Terminal Interface:** The tool offers a clear terminal interface with color-coded messages using `colorama`.

## Example

```bash
QR Code Generator
=================

[QR Code Generator]: Enter the text or URL for QR code (type 'exit' to quit):
root@you:~$ Hello World

[QR Code Generator]: Enter the QR code color in HEX format (e.g., #000000 for black).
root@you:~$ #FF5733

[QR Code Generator]: Enter the background color in HEX format (e.g., #FFFFFF for white).
root@you:~$ #FFFFFF

[QR Code Generator]: QR code has been generated and saved as 'QR Codes/Hello World.png'
