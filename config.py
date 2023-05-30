import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '31035026e0011054f7ae111b72d20a23aae72807e6fcdf7f3d293b5fc8a032e6'