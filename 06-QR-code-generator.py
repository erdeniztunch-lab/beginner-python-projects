# QR Code Generator -- Algorithm
# Ask the user for text or URL data
# Ask the user for output file name
# Create a QR code object with size and border settings
# Add the user data into the QR object
# Generate the image and save it to the given file
# Print a success message

import qrcode

# Get clean input values by removing leading/trailing spaces.
data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()

# Create the QR object first, then feed it data and render an image.
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f"QR code saved as {filename}")

# Program summary:
# The script takes user text, converts it into a QR image, and saves it.
# QR settings are defined in one object to control output size and spacing.
# The flow is linear so beginners can follow each step from input to output.
