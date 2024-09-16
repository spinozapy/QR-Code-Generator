import qrcode
from PIL import Image
import colorama
import os

colorama.init(autoreset=True)  

clear_command = "cls" if os.name == "nt" else "clear" 

def generate_qr_code(data, file_name, qr_color="black", bg_color="white"):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=bg_color)
    img.save(file_name)  

def main():
    while True:
        os.system(clear_command)
        print(colorama.Fore.GREEN + "[QR Code Generator]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the text or URL for QR code (type 'exit' to quit):")

        try:
            user_input = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE)
        except KeyboardInterrupt:
            print("")
            continue

        if user_input.lower() == 'exit':
            break

        if user_input.strip() == "":
            print(colorama.Fore.RED + "[QR Code Generator]: " + colorama.Fore.GREEN + "Invalid input. Please enter some text or a URL.")
            continue

        print(colorama.Fore.GREEN + "[QR Code Generator]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the QR code color in HEX format (e.g., #000000 for black). Press Enter to black.")
        qr_color = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE)

        print(colorama.Fore.GREEN + "[QR Code Generator]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the background color in HEX format (e.g., #FFFFFF for white). Press Enter to white.")
        bg_color = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE)

        if not qr_color:
            qr_color = "black"  
            print(colorama.Fore.GREEN + "[QR Code Generator]: " + colorama.Fore.LIGHTYELLOW_EX + "Default QR code color (black) will be used.")

        if not bg_color:
            bg_color = "white"  
            print(colorama.Fore.GREEN + "[QR Code Generator]: " + colorama.Fore.LIGHTYELLOW_EX + "Default background color (white) will be used.")

        file_name = "qr-code.png"

        try:
            generate_qr_code(user_input, file_name, qr_color=qr_color, bg_color=bg_color)
            print(colorama.Fore.GREEN + "[QR Code Generator]: " + colorama.Fore.LIGHTYELLOW_EX + f"QR code has been generated and saved as '{file_name}'")
        except Exception as e:
            print(colorama.Fore.RED + "[QR Code Generator]: " + colorama.Fore.GREEN + f"Error generating QR code: {str(e)}")

        print("")
        try:
            input(colorama.Fore.GREEN + "[QR Code Generator]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")
        except KeyboardInterrupt:
            continue

if __name__ == "__main__":
    main()
