import os

from PIL import Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*",
               "+", ";", ":", ",", "^", "`", "'", ".", " "]

ASCII_CHARS10 = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c",
                 "v", "u", "n", "x", "r", "j", "f", "t", "/", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"",  "^", "`", "'", ".", " "]


def resize(image, fixed_height=300):
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent))) * 2
    resized_image = image.resize((width_size, fixed_height), Image.NEAREST)
    return(resized_image)


def to_greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""

    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//30]

    return ascii_str


def main():

    source = "./src/ascii-generator"
    output = "./dist/images"

    path = source + "/test.jpg"
    try:
        image = Image.open(path)
    except:
        print(path, "Unable to find image ")
    # resize image
    image = resize(image)
    # convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    # Check if dist folder exists
    if not os.path.exists(output):
        os.makedirs(output)
    # save the string to a file
    with open(output+"/ascii_image.txt", "w") as f:
        f.write(ascii_img)


main()
