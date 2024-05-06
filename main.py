import qrcode #libraries

data = "https://github.com/Zylles/qr-code_generator-python" #enter the data you want

img = qrcode.make(data) 
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png") # Qr Code Png Name