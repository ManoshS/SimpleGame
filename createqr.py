import qrcode

def generate_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)

if __name__ == "__main__":
    url = ""
    file_name = "qrcode.png"
    generate_qr_code(url, file_name)
    print(f"QR Code generated and saved as {file_name}")

