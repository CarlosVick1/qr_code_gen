import qrcode

def generate_qrcode(text):
#def generate_qrcode(img):
    
    qrc = qrcode.QRCode(
        version = 2,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 11,
        border = 1,
    )
    
    
    qrc.add_data(text)
    #qrc.add_data(img)
    qrc.make(fit=True)
    image = qrc.make_image(fill_color="brown", back_color="white")
    image.save("Godhead_qrcode.png")
Info = input("Please, type the information: ")
generate_qrcode(Info)