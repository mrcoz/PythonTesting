'''
Created on Aug 27, 2014

@author: markc
'''
import os
from pathlib import Path

#CadPendDir = '//ATC-FS01/Master/Frames - standard/VS1/PEND/RAV/'
CadPendDir = '\\\\ATC-FS01\\Master\\Frames - standard\\VS1\\PEND\\RAV\\'

PDFRelDir = '//ATC-FS01/Master/Frames - standard/VS1/REL/RAV/PDF/'
SLDRelDir = '//ATC-FS01/Master/Frames - standard/VS1/REL/RAV/SLD/'
ProductionPDFReleaseDir = '//ATC-FS01/mDriveData/VS1/Production Drawing/Hendrix_StockPDFs/'
ProductionJPGReleaseDir = '//ATC-FS01/mDriveData/VS1/Production Drawing/Hendrix_StockJPGs/'
TempHoldDir = '//ATC-FS01/mDriveData/VS1/Production Drawing/del/'

p = Path(CadPendDir)
RelPdfDir = Path(PDFRelDir)
t = Path(TempHoldDir)
print(t.exists())
q = list(p.glob('*.pdf'))
# q = list(p.glob('**/*.pdf'))
# "**" Pattern means this directory and all sub-directories, recursively

for b in q:
    #print(b)
    a = b.suffix
    #print(a)
    c = b.name
    #print(c)
    RelDirFile = list(RelPdfDir.glob(c))
    #print(RelDirFile)
    for RelFileList in RelDirFile:
#        print(RelFileList.is_file())
        #print(RelFileList.drive)
        #print(RelFileList.root)
        #print(RelFileList.anchor)
        #print(RelFileList.parent)
        a = str(RelFileList.parent).upper()
        b = str(RelFileList.name).upper()   
        c = a+b
        d = a + '\\' + b
        # e = TempHoldDir + 
        print(d)    
        #print(a)
        #print(b)
        #print(c)
        
        #print(a + "Testing")
        os.system("copy \"%s\" \"%s\"" % (RelFileList, TempHoldDir))
        #print(RelFileList.suffix)
        #print(RelFileList.name)
        
if __name__ == '__main__':
    pass


# Renaming and Moving files
# import os
# os.rename(PreviousName, NewName)
# os.rename(PreviousName, Path/NewName)
# Path.rename() - Moving files
