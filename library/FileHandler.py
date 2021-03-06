import pandas as pd
import os
import glob
import requests as req
import mimetypes
from library.PandasNumpy import pop
from library.ExcelSaver import Saver as save
from library.HTMLParser import Parse as parse
import numpy as np

class File:

    path = 'C:\\Users\\stillomid\\Desktop\\omid'
    arr = []
    names = []
    total = []
    header = ['ردیف', 'نام و نام خانوادگی' ,'شماره همراه' ,'استان' ,'کدملی']

    def readFiles():
        readArray = []
        fileNames = []
        for file in glob.glob(os.path.join(File.path, '*.csv')):
            fileName = file.replace('.csv', '').replace(File.path+"\\", '')
            readArray.append(pop.openCSV(file))
            fileNames.append(fileName)
        File.arr = readArray
        File.names = fileNames
        File.total = pop.openExcel(File.path + '\\total.xlsx')
        # return (File.arr[1][0][14] , File.names[0])

    def requestPics():
        a = File.arr
        url = ''
        for i in range(len(a)):
            for b in a[i]:
                if str(b[10]).find('https') >= 0 :
                    url = parse.getDownload(b[10])
                    File.requestSender(url, File.names[i], b[1] , 1)
                if str(b[11]).find('https') >= 0 :
                    url = parse.getDownload(b[11])
                    File.requestSender(url, File.names[i], b[1] , 2)
                if len(b) > 18:
                    if str(b[12]).find('https') >= 0 :
                        url = parse.getDownload(b[12])
                        File.requestSender(url, File.names[i], b[1], 3)
                    if str(b[13]).find('https') >= 0 :
                        url = parse.getDownload(b[13])
                        File.requestSender(url, File.names[i], b[1], 4)

    def requestSender(url, folder='Folder', name='test', index=0):
        index = str(index)
        name = str(name)
        folder = str(folder)
        try:
            if (type(url) is not str) or (type(folder) is not str)  or (type(name) is not str):
                return
            r = req.get(url , timeout=30, allow_redirects=True)
            if r.status_code != 200 : return
            path = os.path.join(File.path, folder)
            if not os.path.isdir(path):
                os.mkdir(path)
            fileURL = path +'\\'+ str(name) +'__'+ str(index) + File.getExtension(url)
            open(fileURL, 'wb').write(r.content)
            print('response', r)
        except TypeError:
            return

    def getExtension(url):
        extensions = ['.doc' , '.docx' , '.pdf' , '.jpg' , '.jpeg' , '.png']
        for ext in extensions:
            if url.find(ext) > 0:
                return str(ext)

    def mainAlgorithm():
        plus = 0
        total = File.total
        header = File.header
        for i in range(len(File.names)):
            for row in File.arr[i]:
                flag = False
                for j in range(len(total)):
                    if float(row[1]) == float(total[j][4]):
                        flag = True
                buffer = [['Unknown'] * 4 + [row[1]] + ['Null'] * (len(total[1]) - 5)]
                if not flag:
                    total = np.append(total, buffer, axis=0)
        # ------------------------------------------------------------------------
        for i in range(len(File.names)):
            N = len(total)
            total = np.c_[total, np.zeros(N)]
            header.append(File.names[i])
            s = {True: 4, False:2}[len(File.arr[i][1]) > 18]
            for k in range(s):
                N = len(total)
                empty = ['Null'] * N
                total = np.c_[total, empty]
                header.append(File.names[i] + '__Link'+str(k))

            if len(File.arr[i][1]) > 18 : plus += 2
            for row in File.arr[i]:
                for j in range(len(total)):
                    if float(row[1]) == float(total[j][4]):
                        if len(row) > 18:
                            total[j][3 * i + 5] = row[14]
                            total[j][3 * i + 6] = row[10]
                            total[j][3 * i + 7] = row[11]
                            total[j][3 * i + 8] = row[12]
                            total[j][3 * i + 9] = row[13]
                        # elif row[1] in total:
                        #     print(row[1])
                        #     buffer = [['Unknown'] * 4 + [row[1]] + ['Null'] * (len(total[1]) - 5)]
                        #     total = np.append(total, buffer, axis=0)
                        #     print(total)
                        #     return
                        else:
                            total[j][3 * i + 5 + plus] = row[12]
                            total[j][3 * i + 6 + plus] = row[10]
                            total[j][3 * i + 7 + plus] = row[11]
                        continue

        dataFrame = pd.DataFrame(total , index = None , columns= header)
        save.excelBuilder(dataFrame)
        return dataFrame