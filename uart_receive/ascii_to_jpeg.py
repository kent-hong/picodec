## @brief This function takes a ASCII-Hex file and extracts all image binary data to convert into a JPEG
#  @param txt_path File path of the ASCII-Hex .txt file
#  @param new_jpeg_path File path of the reconstructed JPEG image you wish to save to
def decode_ascii_hex(txt_path, new_jpeg_path):
    # Open text file and read all sentences
    with open(txt_path, "r") as file:
        all_sentences = file.read()
        
    # Initialize data structure to store extracted image binary
    image_binary = []
    
    