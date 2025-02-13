import configparser
import os

config = configparser.ConfigParser()
config.read("./config/config.ini")

PATH_CV = config["Paths"]["path_cv"]
PATH_PHOTO = config["Paths"]["path_photo"]