## @brief
#  @param txt_path File path of .txt where you want to extract the ASCII-Hex sentences from
#  @param new_jpeg_path File path of where you want to store the new reconstructed JPEG image
def decode_ascii_hex(txt_path, new_jpeg_path):
    try:
        # Open the .txt file with ASCII-Hex sentences
        with open(txt_path, 'r') as file:
            all_sentences = file.readlines()
            
        # Data structure to store all reconstructed JPEG binary data
        jpeg_binary_sentences = []
        
        # Variable to store telemetry sentence
        telemetry_sentence = ""
        
        # Parse the ASCII-Hex portion related to image data through all sentences (byte 9 to 64) and combine into binary data, excluding the telemetry sentence
        for sentence in all_sentences:
            if sentence.startswith("@FACE"):
                telemetry_sentence = sentence
                break
            chunk_ascii_hex = sentence[9:65]
            chunk_raw_binary = bytes.fromhex(chunk_ascii_hex)
            jpeg_binary_sentences.append(chunk_raw_binary)
        
        # Decode telemetry sentence
        xxxx = int(telemetry_sentence[5:9], 16) # ASCII representation of HEX total amount of image + telemetry sentences in captured image data stream
        tries = int(telemetry_sentence[9:11], 16)  # 2 byte ASCII representation of HEX byte of number of internal communication sync tries
        iiiiii = int(telemetry_sentence[11:17], 16) # ASCII representation of HEX total amount of JPEG image raw bytes
        inputVoltage = int(telemetry_sentence[51:53], 16) # ASCII representation of HEX byte, equals to unit main power bus input voltage by following formula: V = InputVoltage * 0,02 [V]
        inputCurrent = int(telemetry_sentence[53:55], 16) # ASCII representation of HEX byte, 0xA3 = 0d163, equals to unit main power bus input current by following formula: I = InputCurrent [mA]
        coreVoltage = int(telemetry_sentence[55:57], 16) # ASCII representation of HEX byte, equals to unit core power bus input voltage by following formula: V = CoreVoltage * 0,02 [V]
        coreCurrent = int(telemetry_sentence[57:59], 16) # ASCII representation of HEX byte, equals to unit core power bus input current by following formula: I = CoreCurrent [mA]
        flash = int(telemetry_sentence[61:62], 16) # indicates whether the image was captured using activated Flash illumination (0x01 = 0d01), or without Flash (0x00 = 0d00)
        # indicates at which baudrate the image was telecommanded to and downlinked from the camera according to following baudrate list: 
        # 0 = 1200bps-8-n-1, 
        # 1 = 2400bps-8-n-1, 
        # 2 = 9600bps-8-n-1, 
        # 3 = 19200bps-8-n-1, 
        # 4 = 38400bps-8-n-1, 
        # 5 = 57600bps-8-n-1, 
        # 6 = 115200bps-8-n-1 (default after power up), 
        # 7 = 230400bps-8-n-1, 
        # 8 = 460800bps-8-n-1, 
        # 9 = 921600bps-8-n-1
        baudrate = int(telemetry_sentence[62:63])
        baudrate_map = [1200, 2400, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600] 
        fw_version = f"FW v {telemetry_sentence[63:64]}.{telemetry_sentence[64:65]}" # indicates the camera unit firmware version installed, 0x70 = FW v 7.0 
        
        # Display telemetry sentence info
        print(f"Image & Telemetry Sentences: {xxxx}")
        print(f"Internal Communication Sync Tries: {tries}")
        print(f"JPEG Image Raw Bytes: {iiiiii}")
        print(f"Unit Main Power Bus Input Voltage: {inputVoltage * 0.02} V")
        print(f"Unit Main Power Bus Input Current: {inputCurrent} mA")
        print(f"Unit Core Power Bus Input Voltage: {coreVoltage * 0.02} V")
        print(f"Unit Core Power Bus Input Current: {coreCurrent} mA")
        print(f"Flash: {bool(flash)}")
        print(f"Baudrate: {baudrate_map[baudrate]} bps")
        print(fw_version)
        
        # Combine raw binary sentences into a contiguous stream
        jpeg_binary_full = b''.join(jpeg_binary_sentences) # Binary data with padding to fit 28 bytes of image data per sentence
        jpeg_binary = jpeg_binary_full[:iiiiii] # Trim to actual size
        
        # Save jpeg 
        with open(new_jpeg_path, "wb") as file:
            file.write(jpeg_binary)
            
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        
    finally:
        print("JPEG image was successfully reconstructed from the ASCII-Hex encoding!")