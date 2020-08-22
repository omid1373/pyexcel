import pandas as pd
from library.PandasNumpy import pop as c
from library.FileHandler import File as file
from library.HTMLParser import Parse as parse
from library.sync import Sync
import mimetypes

url_csv1 = "C:\\Users\\stillomid\\Desktop\\omid\\آزمون حقوق تجارت (اختبار).csv"
url = "https://dcs.dunkel.de/porsline-file-upload/iD5353i/22720768/2559806-FE87B07A_58F3_4EEF_A961_7BCA05EFF6AB.jpeg?Signature=w8RqY0Okkbv4zlXRRl7cUvxbyB8%3D&AWSAccessKeyId=JEVKSTQU0NRSTVLNXRPR&Expires=1598193332"
name = 'Essi'
folder = 'pic'
# res = file.requestSender(url, name, folder, 0)
# type = mimetypes.MimeTypes().guess_type(file.requestSender(url, name, 'Pics', 0))
# print(type)
file.readFiles()
file.mainAlgorithm()
# file.requestPics()
# url = 'https://survey.porsline.ir/file/1b9daaa159f92b92-pXjMjcl/22939227/2571048-BDD7E8C5_4D99_49DE_BE64_F3A3B49E0F38.jpeg/download'
# new_link = parse.getDownload(url)
# file.requestSender(new_link, 'SS', 'name')
# # link = parse.getLink(url)
