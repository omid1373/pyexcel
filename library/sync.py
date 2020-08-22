from library.PandasNumpy import pop

class Sync:
    path = 'C:\\Users\\stillomid\\Desktop\\omid'
    total = []
    files = []

    def initialize(dir = path , files = None):
        Sync.total = pop.openExcel(dir+ '\\total.xlsx')
        Sync.files = files
        
    # def syncAction(arr):


