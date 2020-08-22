import pandas as pd
class Saver:

    path = 'C:\\Users\\stillomid\\Desktop'
    def excelBuilder(dataFrame = None, dir = path ,excelName = 'omid' , sheetName = 'sheetOmid'):
        writer = pd.ExcelWriter(dir + '\\' +excelName +'.xlsx', engine='xlsxwriter')
        dataFrame.to_excel(writer, sheet_name=sheetName ,index=False)
        worksheet = writer.sheets[sheetName]
        worksheet.right_to_left()
        writer.save()
        print('Excel file '+excelName+' with SheetName '+sheetName+ 'created in: \n' + dir)
