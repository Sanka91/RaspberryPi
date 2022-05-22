from PIL import Image
import os
from display_controller import DisplayController
import datetime


class QRCode():

    qr_directory = '/home/pi/Desktop/Raspberry_Pi/Recipe_QRs'

    def __init__(self,
                 filename: str = "N/A",
                 recipe_id_ref: int = 0,
                 timestamp = datetime.date(1900, 1, 1)
                 ):
        self.filename = filename
        self.recipe_id_ref = recipe_id_ref
        self.timestamp = timestamp
        self.qr_code_location = Image.open(os.path.join(QRCode.qr_directory, self.filename))
        self.qr_code_formatted = self.qr_code_location.resize((75, 75))

    def show_qr_code_onscreen(self):
        self.qr_code_location.show()


