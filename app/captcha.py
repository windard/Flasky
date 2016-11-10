# coding=utf-8

from wheezy.captcha.image import captcha

from wheezy.captcha.image import background
from wheezy.captcha.image import curve
from wheezy.captcha.image import noise
from wheezy.captcha.image import smooth
from wheezy.captcha.image import text

from wheezy.captcha.image import offset
from wheezy.captcha.image import rotate
from wheezy.captcha.image import warp

import random
from os import path

chars = 'ABCDEFGHJKLMNPRTUVWXY346789'

class Captcha(object):
    """docstring for Captcha"""
    def __init__(self, code, count=4, width=200, height=75, fonts_dir='static/fonts', captcha_type='png'):
        super(Captcha, self).__init__()
        self.code = code
        self.count = count
        self.width = width
        self.height = height
        self.fonts_dir = fonts_dir
        self.captcha_type = captcha_type
        self.captcha_image = captcha(drawings=[
            background(),
            text(fonts=[
                path.join(fonts_dir,'78640___.TTF'),
                path.join(fonts_dir,'46152___.TTF')],
                drawings=[
                    warp(),
                    rotate(),
                    offset()
                ]),
            curve(),
            noise(),
            smooth()
        ])

    def get_captcha(self):
        self.image = self.captcha_image(self.code)
        return self.image

    def save_captcha(self, name="test"):
        self.image.save(name+'.'+self.captcha_type, self.captcha_type, quality=75)

    @staticmethod
    def get_chars(length=4):
        return random.sample(chars, length)

if __name__ == '__main__':
    chars = random.sample(chars,4)
    captchas = Captcha(chars)
    captchas.save_captcha()