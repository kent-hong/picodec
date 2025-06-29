import serial

## @brief This function receives ASCII-Hex sentences over UART
#  @param port Port number we receive the ASCII-Hex data from
#  @param txt_path Path where you want to store the ASCII-Hex sentences in a .txt file
#  @param Amount of ASCII-Hex sentences to be received from ascii_hex_transmit()
def ascii_hex_receive(rx_port, txt_path, sentence_length):
    try:
        # Set up UART Rx port
        ser_rx = serial.Serial(port=rx_port, baudrate=115200, timeout=1)
        
        # Confirm UART Rx port was set up correctly
        print(f"Receiving {sentence_length} ASCII-Hex sentences...")
        
        # Initialize list to store ASCII-Hex sentences
        all_sentences = []
        
        # Read all ASCII-Hex lines over UART and store in list until the last telemetry line is read
        while True:
            ascii_hex_sentence_raw = ser_rx.readline()
            
            if ascii_hex_sentence_raw:
                ascii_hex_sentence = ascii_hex_sentence_raw.decode()
                all_sentences.append(ascii_hex_sentence)
                print(f"{len(all_sentences)}/{sentence_length} sentences received")
                if ascii_hex_sentence.startswith("@FACE"):
                    break

        # Write the ASCII-Hex list into a file            
        with open(txt_path, "w") as file:
            for sentence in all_sentences:
                file.write(sentence)
        
    except serial.SerialException as e:
        print(f"UART Receive Error: {e}")
        
    finally:
        if 'ser_rx' in locals():
            ser_rx.close()
            