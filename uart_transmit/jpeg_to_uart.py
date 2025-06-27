import math

## @brief This function encodes a JPEG image into ASCII Hex format for UART transmission
#  @param jpeg_path JPEG image file path
#  @param output_txt_path Path where you want to store the ASCII Hex data in a .txt file
def encode_jpeg(jpeg_path, output_txt_path):
    with open(jpeg_path, "rb") as f:
        jpeg_data = f.read()

    chunk_size = 28 # Each sentence stores 28 bytes of raw image data
    total_data_sentences = math.ceil(len(jpeg_data) / chunk_size) # Calculate number of image sentences (take the ceiling to account for sentences shorter than 28 bytes)
    total_sentences = total_data_sentences + 1  # +1 for simulated telemetry
    xxxx = f"{total_sentences - 1:04X}" # Number of image sentences in ASCII-Hex format (string)

    uart_lines = [] # List of strings that stores all ASCII-Hex sentences

    for i in range(total_data_sentences):
        start = i * chunk_size
        chunk = jpeg_data[start:start + chunk_size]
        hex_ascii = chunk.hex().upper()
        nnnn = f"{i:04X}"
        line = f"@{nnnn}{xxxx}{hex_ascii}\r\n"
        uart_lines.append(line)

    # Simulated telemetry sentence
    telemetry_line = f"@FACE{xxxx}1E{len(jpeg_data):06X}" + "AABBCCDDEEFF"*2 + "00A35B9F4D000670\r\n"
    uart_lines.append(telemetry_line)

    with open(output_txt_path, "w") as f:
        f.writelines(uart_lines)

    print(f"Saved JPEG as ASCII-Hex to {output_txt_path}")
