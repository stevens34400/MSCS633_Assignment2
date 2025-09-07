"""
QR Code Generator
-----------------
This script generates a QR code from a given URL.
Author: Steven Sisjayawan
"""

import qrcode

def generate_qr(url: str, filename: str = "qrcode.png") -> None:
    """
    Generate a QR code from the given URL and save it as an image.
    
    :param url: The URL to encode in the QR code
    :param filename: The output image filename (default: qrcode.png)
    """
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 = small, 40 = large)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each "box" in pixels
        border=4,  # Border thickness (minimum = 4)
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as a file
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")


if __name__ == "__main__":
    print("=== QR Code Generator ===")
    url = input("Enter a URL: ").strip()
    generate_qr(url)
