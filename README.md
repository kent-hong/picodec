# picodec

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is developed as part of [**SharkSat**](https://www.csulbaiaa.org/sharksat), a student-led initiative at **California State University, Long Beach (CSULB)**, focused on designing and launching a CubeSat to monitor blue light pollution from space.

**`picodec`** is a Python-based tool designed to simulate image transmission using the SkyFox Labs **piCAM**. It encodes JPEG images into ASCII-Hex formatted UART packets for transmission, and decodes received ASCII-Hex data back into valid JPEG files. This utility helps validate image encoding and transmission pipelines in satellite communication systems.


<!-- GETTING STARTED -->
## Getting Started

To begin using this tool, you’ll need to set up virtual COM ports to emulate UART transmission. A free option to achieve the desired behaviour is using **Null-modem emulator (com0com)** which is an open-source kernel-mode virtual serial port driver for Windows.

### Prerequisites
* [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
> **Git** is used to clone this repository in order to use the `picodec` in your terminal or code editor

* [**Git Bash**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
> While optional, **Git Bash** offers a more intuitive terminal experience for navigating directories and running commands, especially on Windows. 
> It is also included automatically in the **Git** installation.

* [**Python**](https://www.python.org/downloads/)
 > To avoid bugs or dependency issues, it's recommended to install the most recent stable version of Python. As of June 2025, that version is **3.13.5**.

### Installation

#### Install Null-modem emulator (com0com):
1. Disable **Secure Boot** on Windows.
> The option to disable **Secure Boot** should be in your BIOS. Make sure to re-enable **Secure Boot** after using `picodec`.

2. Enable test signing.
> The com0com.sys is a test-signed kernel-mode driver that will not load by
  default. To enable test signing, in your cmd terminal as admin, enter the command:
```sh
bcdedit.exe -set TESTSIGNING ON
```
**NOTE:** Enabling test signing will impair computer security. To disable test signing after using `picodec`:
```sh
bcdedit.exe -set TESTSIGNING OFF
``` 

3. Reboot the computer.

4. Install [**com0com**](https://sourceforge.net/projects/com0com/).
5. Extract `Setup_com0com_v3.0.0.0_W7_x64_signed` from the zip file and run as admin.
6. Go through the installation process and leave everything as default.
7. Launch the Setup Command Prompt
8. Enter the install command, for example:
```sh
command> install PortName=COM10 PortName=COM11
```
**NOTE:** To uninstall all virtual COM ports, run `command> uninstall`

#### Install picodec:

1. Copy the repo URL
    ```sh
    https://github.com/kent-hong/picodec.git
    ```

2. Clone the repo
   ```sh
   git clone https://github.com/kent-hong/picodec.git
   ```

**Alternative:** Download the repo
> Download the repo by clicking on the green code button on the repository landing page and clicking on `Download ZIP`. Just extract the repository to your desired location.



<!-- USAGE EXAMPLES -->
## Usage

1. Add an image in the **jpegs** folder in your cloned `picodec` repository.

2. Navigate to the **src** folder
   ```sh
   cd /picodec/src
   ```
3. Run `main.py`
   ```sh
   python main.py
   ```

4. Enter the file path of the JPEG image you wish to use. For example:
    ```sh
    C:/Users/name/Documents/picodec/jpegs/black-hole.jpeg
    ```

5. Enter the COM port name you are transmitting from. 
> In the example above, we are using `COM10`

6. Enter the COM port name you are receiving from.
> In the example above, we are using `COM11`

7. Enter the file path of the .txt file you wish to store the decoded ASCII-Hex sentences to. For example:
    ```sh
    C:/Users/name/Documents/picodec/txt/ascii-hex.txt
    ```

8. Enter the file path you wish to store the reconstructed JPEG image to. For example:
    ```sh
    C:/Users/name/Documents/picodec/new_jpegs/reconstructed.jpeg
    ```

Congratulations! The program should now decode and reconstruct the JPEG image from the encoded ASCII-Hex sentences from your .txt file.



<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Kent Hong - [kent.n.hong@gmail.com]

Project Link: [https://github.com/kent-hong/picodec](https://github.com/kent-hong/picodec)




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [com0com](https://github.com/diegopego/com0com-1?tab=readme-ov-file)
* [SharkSat](https://www.csulbaiaa.org/sharksat)
* [README.md Template](https://github.com/othneildrew/Best-README-Template)
* [SkyFox Labs piCAM](https://www.skyfoxlabs.com/product/27-picam)
* [Git](https://git-scm.com/)
* [Python](https://www.python.org/)


