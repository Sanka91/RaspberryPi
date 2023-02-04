from PIL import Image
import os
import datetime
from FileSystem.file_system import FileSystemHelper


class QRCode:

    file_system = FileSystemHelper()

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

    def show_onscreen(self):
        self.qr_code_location.show()

    def get_sized_qr_code(self) -> Image:
        qr_code_sized = Image.open(os.path.join(self.qr_code_location)).resize((75, 75))
        return qr_code_sized

    def save_on_file_system(self):
        QRCode.file_system.save_image(filename=self.filename, bytestring=self.bytestring)

    @classmethod
    def from_bytestring_and_recipe(cls, qr_bytestring: bytes, recipe_ref):
        filename = "ID_{}_Date_{}.png".format(recipe_ref.recipe_id, recipe_ref.timestamp)

        qr_code = QRCode(
            bytestring=qr_bytestring,
            filename=filename,
            recipe_id_ref=recipe_ref.recipe_id,
            timestamp=recipe_ref.timestamp,
            qr_code_location="{}{}".format(cls.file_system.qr_directory, filename)
        )
        return qr_code

