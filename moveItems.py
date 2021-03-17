from zipfile import ZipFile
import shutil

def main():

    with ZipFile(r'C:\Users\bruno\Documents\kintera_otc\data.zip', 'r') as zipObj:
        listOfFileNames = zipObj.namelist()
        for fileName in listOfFileNames:
            if (fileName.endswith('.dat') or fileName.endswith('.spr')):
                zipObj.extract(fileName, r'C:\Users\bruno\Documents')

    destinations = ["otc_druid", "otc_paladin", "otc_money", "otc_fullafk", "otc_sorcerer", "otc_clientv8"]

    for destiny in destinations:
        shutil.copy(r'C:\Users\bruno\Documents\data\things\1100\Tibia.dat', r'C:\{}\data\things\1100'.format(destiny))
        shutil.copy(r'C:\Users\bruno\Documents\data\things\1100\Tibia.spr', r'C:\{}\data\things\1100'.format(destiny))

if __name__ == '__main__':
   main()