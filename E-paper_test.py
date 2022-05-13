#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

fontdir = '/home/pi/Desktop/Raspberry_Pi/Fonts'
imagedir = '/home/pi/Desktop/Raspberry_Pi/Images'
qrdir = '/home/pi/Desktop/Raspberry_Pi/Recipe_QRs'
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in9
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

print('imports successful')


epd = epd2in9.EPD()
logging.info("init and Clear")
epd.init(epd.lut_full_update)
epd.Clear(0xFF)

font10 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 10)
font11 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 11)
font12 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 12)
font13 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 13)
font14 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 14)
font15 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 15)
font16 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 16)
font17 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 17)
font18 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 18)
font19 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 19)
font20 = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-Regular.ttf'), 20)

font10_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 10)
font11_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 11)
font12_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 12)
font13_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 13)
font14_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 14)
font15_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 15)
font16_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 16)
font17_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 17)
font18_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 18)
font19_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 19)
font20_bold = ImageFont.truetype(os.path.join(fontdir, 'BalooPaaji2-SemiBold.ttf'), 20)


# Drawing on the Horizontal image
logging.info("1.Drawing on the Horizontal image...")
Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)

draw.text((90, 5), "Hallo Euckenstraße 17")

"""draw.text((5, 0), 'Last Cycle:    {}'.format(time.strftime('%I:%M %p')), font = font12, fill = 0)
draw.text((152, 0), '{}    {}'.format(time.strftime('%a, %e. %B'), time.strftime('%I:%M %p')), font = font12, fill = 0)
draw.text((150, 20), "NEW TEST", font = font12, fill = 0)
draw.text((150, 30), "Humidity", font = font12, fill = 0)
draw.text((150, 40), "Rain", font = font12, fill = 0)
draw.text((150, 50), "Fan Status", font = font12, fill =0)"""


draw.line((5, 20, 291, 20), fill = 0)
draw.line((148, 25, 148, 103), fill = 0)

#bottom Text
draw.line((5, 108, 291, 108), fill = 0)
draw.text((63, 112), "Rezept des Tages: {}".format(time.strftime('%d.%m.%Y')))

#draw.text((5, 108), 'Next Cycle:    {}'.format(time.strftime('%I:%M %p')), font = font12, fill = 0)

epd.display(epd.getbuffer(Himage))
#time.sleep(5)

bmp = Image.open(os.path.join(qrdir, 'ID_661758_Date_2022_05_13.png'))
bmp = bmp.resize((75, 75))

Himage.paste(bmp, (15, 26))
epd.display(epd.getbuffer(Himage))
time.sleep(2)
print("Done")


