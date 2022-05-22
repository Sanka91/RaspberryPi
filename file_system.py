from PIL import Image
import io


class FileSystemHelper:

    @classmethod
    def save_qr_code(cls, qr_code):
        image = Image.open(io.BytesIO(qr_code.bytestring))
        image.save('/home/pi/Desktop/Raspberry_Pi/Recipe_QRs/{}'.format(qr_code.filename))

