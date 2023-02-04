from PIL import Image,ImageDraw,ImageFont
import os
import sys


class EPaperUtil:

    font_dir = '/home/pi/Desktop/Raspberry_Pi_Projects/Raspberry_Pi_EPaper/Fonts'

    def setup_library(self):
        lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
        if os.path.exists(lib_dir):
            sys.path.append(lib_dir)

    font10 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 10)
    font11 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 11)
    font12 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 12)
    font13 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 13)
    font14 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 14)
    font15 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 15)
    font16 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 16)
    font17 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 17)
    font18 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 18)
    font19 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 19)
    font20 = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-Regular.ttf'), 20)

    font10_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 10)
    font11_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 11)
    font12_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 12)
    font13_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 13)
    font14_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 14)
    font15_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 15)
    font16_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 16)
    font17_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 17)
    font18_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 18)
    font19_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 19)
    font20_bold = ImageFont.truetype(os.path.join(font_dir, 'BalooPaaji2-SemiBold.ttf'), 20)
