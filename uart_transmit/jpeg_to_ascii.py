import math

## @brief This function encodes a JPEG image into ASCII Hex format for UART transmission
#  @param jpeg_path JPEG image file path
#  @param txt_path Path where you want to store the ASCII Hex data in a .txt file
def encode_jpeg(jpeg_path, txt_path):
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

    # Save ASCII-Hex data structure into a file
    with open(txt_path, "w") as file:
        file.writelines(all_sentences)

    # Output a message to confirm conversion was successful
    print("JPEG image was successfully converted into ASCII-Hex and stored in a .txt file.")
    
