import math
import serial
import time

## @brief This function encodes a JPEG image into ASCII Hex format for UART transmission
#  @param jpeg_path JPEG image file path
def encode_jpeg(jpeg_path):
    # Open the jpeg file and read as binary data
    with open(jpeg_path, "rb") as file:
        binary_data = file.read()

    # Calculate total number of image data sentences and convert into ASCII-Hex
    image_sentences = math.ceil(len(binary_data) / 28) # ceiling(Total number of bytes / # of allowed bytes per sentence) = # of image sentences
    total_sentences = image_sentences + 1 # Include one telemetry sentence at the end
    xxxx = f"{image_sentences:04X}" # Convert # of image sentences into 4 Hex ASCII characters
    

    # Initialize data structure to store ASCII-Hex sentences and telemetry sentence
    all_sentences = []
    

    # Loop through total number of sentences and create a sentence of 67 bytes for each line
    # Add constructed sentence to data structure every loop
    for i in range(image_sentences):
        current_sentence = i
        nnnn = f"{current_sentence:04X}"
        start_index = i * 28
        binary_chunk = binary_data[start_index:start_index + 28]
        data = binary_chunk.hex().upper()
        sentence = f"@{nnnn}{xxxx}{data}\r\n"
        all_sentences.append(sentence)
        

    # Create fake telemetry sentence and store in data structure
    telemetry_sentence = f"@FACE{xxxx}1E{len(binary_data):06X}" + "00112233445566778899AABBCCDDEEFF" + "00A35B9F4D000670\r\n"
    all_sentences.append(telemetry_sentence)

    # Output a message to confirm conversion was successful
    print("JPEG image was successfully converted into ASCII-Hex.")
    
    return all_sentences


## @brief This function transmits ASCII-Hex sentences over UART
#  @param sentences Returned list of ASCII-Hex sentences from encode_jpeg()
#  @param tx_port Port name we wish to transmit the ASCII-Hex sentences from
def ascii_hex_transmit(sentences, tx_port):
    try:
        # Set up UART Tx port
        ser_tx = serial.Serial(port=tx_port, baudrate=115200)
        
        # Confirm UART Tx port was set up correctly
        print(f"Transmitting {len(sentences)} ASCII-Hex sentences...")
    
        # Loop through each ASCII-Hex sentence
        for i, sentence in enumerate(sentences):
            ser_tx.write(sentence.encode()) # Send ASCII-Hex sentences as bytes
            print(f"{i+1}/{len(sentences)} sentences transmitted")
            
            
    except serial.SerialException as e:
        print(f"UART Transmit Error: {e}")
    
    finally:
        if 'ser_tx' in locals(): # Check if ser_tx exists in variable local scope
            # Close the port to free it up in case it's used by another program   
            ser_tx.close()
    
    
    
    
