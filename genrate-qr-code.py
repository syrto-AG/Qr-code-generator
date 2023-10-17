import qrcode
from PIL import Image


def generate_qr_with_logo(url, logo_path, output_path):
# taking image which user wants 
# in the QR code center
    
    logo = Image.open(logo_path)
    
    # taking base width
    basewidth = 100
    
    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.LANCZOS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    
    
    # adding URL or text to QRcode
    QRcode.add_data(url)
    
    # generating QR code
    QRcode.make()
    
    # taking color name from user
    QRcolor = 'Black'
    
    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
    
    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    
    
    QRimg.paste(logo,pos)
    
    # save the QR code generated
    QRimg.save(output_path)

# Example usage
generate_qr_with_logo('https://www.karte.alptracker-ag.ch', 'logo3.png', 'output_qr.png')
