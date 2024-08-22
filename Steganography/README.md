
# Steganography with Python: Hiding Text in a Image

Welcome to the Steganography project! 

This Python-based program allows you to hide and reveal secret messages within images using the Least Significant Bit (LSB) technique. Additionally, for enhanced security, the hidden text is encrypted using the Fernet encryption method, ensuring that your data remains secure even if detected.


## How Steganography Works

Steganography involves hiding a secret message within another medium, such as an image, without altering the medium's visual appearance. This project uses the Least Significant Bit (LSB) steganography technique, where the least significant bits of the image's pixels are modified to store the hidden data.

For example:

- Original Image
- Encrypted Image

Despite containing hidden text, the image appears identical to the original, making the hidden message undetectable to the naked eye.

### Understanding Digital Images and LSB Steganography

#### What is a Digital Image?

When we talk about a "digital image," we're referring to a picture made up of tiny dots called pixels. These pixels are arranged in a grid, much like a mosaic, to create the image you see. Digital images come in different formats (like JPEG, PNG, etc.), but the basic idea is the same: a grid of pixels with specific colors.

#### What is a Pixel?

A pixel is the smallest part of an image. Each pixel holds information about its color, and the more pixels an image has, the clearer it appears. The color of each pixel can change, which means more detailed pictures have more pixels.

#### How are Colors Represented?

In digital images, colors are usually represented using the RGB color model, which stands for Red, Green, and Blue. Each pixel in an RGB image is defined by three numbers:

- Red value
- Green value
- Blue value

![](https://cdn-images-1.medium.com/max/2000/1*tcTa2Cst3FXkDpxTg-_1mA.jpeg)

Each of these values can range from 0 to 255. So, a pixel in an image might look like this:

- Red: 150
- Green: 75
- Blue: 0
This combination creates a specific color.

#### Binary Numbers in Pixels

Computers use binary numbers (1s and 0s) to store information. Each RGB value (ranging from 0 to 255) can be written as an 8-bit binary number. For example:

- 150 in binary is 10010110
- 75 in binary is 01001011
- 0 in binary is 00000000

![](https://cdn-images-1.medium.com/max/2000/1*Mt3yDPhS3aq_spPfWTW9BA.png)


#### What Are Significant Bits?

In an 8-bit binary number, each digit has a different impact on the final value:

- Most Significant Bit (MSB): The leftmost digit, which has the largest impact. Changing it can drastically change the color.

- Least Significant Bit (LSB): The rightmost digit, which has the smallest impact. Changing it only slightly changes the color, often in a way that isn’t noticeable.

![Screenshot 2024-08-22 214646](https://github.com/user-attachments/assets/88739052-e7f7-4be3-83c2-a4dc7222ace2)

#### How Does LSB Steganography Work?

LSB Steganography is a technique that hides information inside an image by altering the LSBs of the pixels.

Hiding Information:

To hide a secret message in an image, you can change the LSB of each pixel’s color value to match the binary code of the message.
Since changing the LSB only slightly alters the color, the image will look almost the same to the human eye, but it now contains hidden information.
Example:

- Original Pixel: (Red: 200, Green: 173, Blue: 227)
- Binary: (11001000, 10101101, 11100011)
After Hiding "1" in Each LSB:
- Modified Pixel: (Red: 201, Green: 172, Blue: 226)
- Binary: (11001001, 10101100, 11100010)

The change is so small that it’s hard to notice, but now the image contains a hidden message.

## Visual Example of LSB Steganography


By slightly altering the LSBs of Original Image’s pixels, you can hide text inside it.

- Original Image:

![Original_Image](https://github.com/user-attachments/assets/c11dac50-1e9e-4a51-b09a-0c195c28c276)


- Encrypted Image:(Image with a hidden text)

![Encrypted_Image](https://github.com/user-attachments/assets/eb1eed12-da3c-4dcc-82a3-1da748db67f7)

Even though the image now contains a text, it still looks very similar to the original.

#### Extracting the Hidden Image

To reveal the hidden text from the altered Image, you reverse the process.
Extract the LSBs from Original Image’s pixels. Combine them to reconstruct Image B.
## Installation

1. To get started, clone the repository:

```bash
git clone https://github.com/YourUsername/Steganography-Project.git
cd Steganography-Project
```
2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```    
3. Run the program:
- For encoding a message:
```bash
encoder.py
``` 
- For decoding a message:
```bash
decoder.py
``` 