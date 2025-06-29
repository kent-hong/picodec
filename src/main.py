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

from uart_transmit import encode_jpeg, ascii_hex_transmit
from uart_receive import ascii_hex_receive
from ascii_to_jpeg import decode_ascii_hex
import threading
import time
import sys

def main():
    
    # User enters file path of desired jpeg image to be encoded
    jpeg_path = input("Enter jpeg file path: ")
    
    # Convert JPEG binary data to ASCII-Hex
    ascii_hex_sentences = encode_jpeg(jpeg_path)
    
    sentence_length = len(ascii_hex_sentences)
    
    # User enters virtual COM port to transmit ASCII-Hex bytes
    tx_port = input("Enter virtual COM port to transmit: ")
    
    # User enters virtual COM port to receive ASCII-Hex bytes
    rx_port = input("Enter virtual COM port to receive: ")
    
    # User enters file path of desired output txt file
    txt_path = input("Enter output .txt path: ")
    
    # User enters file path they desire to store reconstructed JPEG image
    new_jpeg_path = input("Enter new jpeg file path: ")
    
    print(f"Transmitting on {tx_port}, receiving on {rx_port}")
    
    # Create threads for simultaneous transmission and reception
    tx_thread = threading.Thread(target=ascii_hex_transmit, args=(ascii_hex_sentences, tx_port))
    rx_thread = threading.Thread(target=ascii_hex_receive, args=(rx_port, txt_path, sentence_length))
    
    # Start both threads
    rx_thread.start()  # Start receiver first
    time.sleep(0.1)    # Small delay to ensure receiver is ready
    tx_thread.start()  # Then start transmitter
    
    # Wait for both threads to complete
    tx_thread.join()
    rx_thread.join()
    
    print("UART communication completed.")
    
    # Convert ASCII-Hex sentences to JPEG binary
    decode_ascii_hex(txt_path, new_jpeg_path)
    
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
        sys.exit(0)