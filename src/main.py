## @file main.py
#
#  @brief This program emulates receiving pictures from the SkyFox Labs piCAM 
#         by encoding JPEGs into ASCII-Hex UART packets, and reconstructs JPEG 
#         images from received ASCII-Hex data.
#
#  @author Kent Hong
#
#  @date 06-29-2025
#
#  @version 0.0.1

from src.uart_transmit import encode_jpeg, ascii_hex_transmit
from src.uart_receive import ascii_hex_receive
from src.ascii_to_jpeg import decode_ascii_hex

def main():
    
    # User enters file path of desired jpeg image to be encoded
    jpeg_path = input("Enter jpeg file path: ")
    
    # Convert JPEG binary data to ASCII-Hex
    ascii_hex_sentences = encode_jpeg(jpeg_path)
    
    sentence_length = len(ascii_hex_sentences)
    
    # User enters virtual COM port to transmit ASCII-Hex bytes
    transmit_port = input("Enter virtual COM port to transmit: ")
    
    # Transmit the ASCII-Hex sentences over UART
    ascii_hex_transmit(ascii_hex_sentences, transmit_port)
    
    # User enters virtual COM port to receive ASCII-Hex bytes
    receive_port = input("Enter virtual COM port to receive: ")
    
    # User enters file path of desired output txt file
    txt_path = input("Enter output .txt path: ")
    
    # Receive the ASCII-Hex sentences over UART and store in a .txt file
    ascii_hex_receive(receive_port, txt_path, sentence_length)
    
    # User enters file path they desire to store reconstructed JPEG image
    new_jpeg_path = input("Enter new jpeg file path: ")
    
    # Convert ASCII-Hex sentences to JPEG binary
    decode_ascii_hex(txt_path, new_jpeg_path)
    
    
if __name__ == '__main__':
    main()