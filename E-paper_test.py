#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os


imagedir = '/home/pi/Desktop/Raspberry_Pi/Images'
qrdir = '/home/pi/Desktop/Raspberry_Pi/Recipe_QRs'
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in9
import time
from PIL import Image,ImageDraw
from epaperutil import EPaperUtil


print('imports successful')

# Frame Setup
epd = epd2in9.EPD()
logging.info("init and Clear")
epd.init(epd.lut_full_update)
epd.Clear(0xFF)

# Clear the frame
Himage = Image.new('1', (epd.height, epd.width), 255)
draw = ImageDraw.Draw(Himage)

### Drawing of Screen, Top to Bottom, Left to Right

# Header Text
draw.text((85, 0), "Hallo Euckenstraße 17", font=EPaperUtil.font14)

# Header Horizontal Divider
draw.line((5, 20, 291, 20), fill=0)

# QR Code 1
qr_code = Image.open(os.path.join(qrdir, 'ID_661758_Date_2022_05_13.png'))
qr_code = qr_code.resize((75, 75))
Himage.paste(qr_code, (15, 26))

# Vertical Divider
draw.line((105, 25, 105, 103), fill=0)

# Recipe Information
### ///////////////////////////###

# Footnote Horizontal Divider
draw.line((5, 108, 291, 108), fill=0)

# Footnote Text
draw.text((63, 112), "Rezept des Tages: {}".format(time.strftime('%d.%m.%Y')))

# Rendering
epd.display(epd.getbuffer(Himage))
time.sleep(2)
print("Done")


