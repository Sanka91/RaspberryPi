from PIL import Image
import io
import os


class FileSystemHelper:

    qr_directory = '/home/pi/Desktop/Raspberry_Pi/Recipe_QRs/'

    @classmethod
    def save_image(cls, filename: str, bytestring: bytes) -> os.path:
        image = Image.open(io.BytesIO(bytestring))
        file_path = "{}{}".format(FileSystemHelper.qr_directory, filename)
        image.save(file_path)
        return file_path
        # return Image.open(os.path.join(QRCode.qr_directory, self.filename))