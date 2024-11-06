import qrcode

url="https://github.com/nehabiswal1"

qr=qrcode.make(url)


output_path = "/app/homework7.png"
qr.save(output_path)


print("QR Code Created! Saved as homework7.png")