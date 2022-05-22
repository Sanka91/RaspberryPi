from PIL import Image
import os
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

    def show_qr_code_onscreen(self):
        self.qr_code_location.show()

    def get_formatted_qr_code(self) -> Image:
        qr_code_sized = Image.open(os.path.join(self.qr_code_location)).resize((75, 75))
        return qr_code_sized
