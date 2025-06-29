# Import functions from your modules
from uart_transmit import encode_jpeg, ascii_hex_transmit
from uart_receive import ascii_hex_receive
from ascii_to_jpeg import decode_ascii_hex
import os

def main():
    
    jpeg_path = os.path.join("C:\\", "Users", "kentn", "Documents", "python-projects", "picodec", "images", "BlackHoleSimNASA.jpeg")
    
    # Convert JPEG binary data to ASCII-Hex
    ascii_hex_sentences = encode_jpeg(jpeg_path)
    
    sentence_length = len(ascii_hex_sentences)
    
    # Transmit the ASCII-Hex sentences over UART
    ascii_hex_transmit(ascii_hex_sentences, "COM10")
    
    txt_path = os.path.join("C:\\", "Users", "kentn", "Documents", "python-projects", "picodec", "sentences", "ascii_hex.txt")
    
    # Receive the ASCII-Hex sentences over UART and store in a .txt file
    ascii_hex_receive("COM11", txt_path, sentence_length)
    
    new_jpeg_path = os.path.join("C:\\", "Users", "kentn", "Documents", "python-projects", "picodec", "new_images", "test.jpeg")
    
    # Convert ASCII-Hex sentences to JPEG binary
    decode_ascii_hex(txt_path, new_jpeg_path)
    
    
if __name__ == '__main__':
    main()