from waveshare_epd import epd2in9
from PIL import Image,ImageDraw, ImageFont
from epaperutil import EPaperUtil


class DisplayController:

    __controller = epd2in9.EPD()
    __image_controller = Image.new("1", (296, 128), 255)
    __draw_controller = ImageDraw.Draw(__image_controller)

    def update_display(self):
        DisplayController.__controller.init(DisplayController.__controller.lut_full_update)
        self.__controller.Clear(0xFF)
        self.__controller.display(self.__controller.getbuffer(self.__image_controller))

    def add_text_to_frame(self, text: str, coordinates: tuple, font_size=EPaperUtil.font12):
        self.__draw_controller.text(coordinates, text, font=font_size)
        print("in Add Text to frame")

    def add_image_to_frame(self, image: Image, coordinates: tuple):
        print("in Add Image to frame")
        self.__image_controller.paste(im=image, box=coordinates)

    def add_line_to_frame(self, x1y1x2y2: tuple):
        self.__draw_controller.line(x1y1x2y2)

    def clear_display(self):
        self.__controller.Clear(0xFF)

