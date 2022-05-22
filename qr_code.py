from PIL import Image
import os
from display_controller import DisplayController
import datetime


class QRCode:

    def __init__(self,
                 bytestring: bytes,
                 filename: str,
                 recipe_id_ref: int,
                 timestamp: datetime.date,
                 qr_code_location: os.path
                 ):
        self.bytestring = bytestring
        self.filename = filename
        self.recipe_id_ref = recipe_id_ref
        self.timestamp = timestamp
        self.qr_code_location = qr_code_location
        self.qr_code_formatted = self.qr_code_location.resize((75, 75))

    def show_qr_code_onscreen(self):
        self.qr_code_location.show()


