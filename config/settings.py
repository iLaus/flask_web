import os



BASE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT = os.path.dirname(BASE_ROOT)



class Settings(object):
    BASE_ROOT = BASE_ROOT
    STATIC_ROOT = STATIC_ROOT


settings = Settings()
