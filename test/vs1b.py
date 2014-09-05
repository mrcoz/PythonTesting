'''
Created on Aug 28, 2014

@author: markc
'''

if __name__ == '__main__':
    pass
#import pathlib
from pathlib import Path
import os
print(os.getcwd())
#print(dir(os))
#print(dir(pathlib))
#print(dir(Path))
#print(help(os))

CadPendDir = '//ATC-FS01/Master/Frames - standard/VS1/PEND/RAV/'
PDFRelDir = '//ATC-FS01/Master/Frames - standard/VS1/REL/RAV/PDF/'
SLDRelDir = '//ATC-FS01/Master/Frames - standard/VS1/REL/RAV/SLD/'
ProdPDFRelDir = '//ATC-FS01/mDriveData/VS1/Production Drawing/Hendrix_StockPDFs/'
ProdJPGRelDir = '//ATC-FS01/mDriveData/VS1/Production Drawing/Hendrix_StockJPGs/'
TempHoldDir = '//ATC-FS01/mDriveData/VS1/Production Drawing/del/'

p = Path(CadPendDir)
RelPdfDir = Path(PDFRelDir)
t = Path(TempHoldDir)
# Only Operate on the PDF files
q = list(p.glob('*.pdf'))
for b in q:
    a = b.suffix
    c = b.name
    d = b.stem
    print(d)
    RelDirFile = list(RelPdfDir.glob(c))
    for RelFileList in RelDirFile:
        # Copy Release Files to Holding Directory - Manually Moved to Superceded Directory
        
        #os.system("copy \"%s\" \"%s\"" % (RelFileList, TempHoldDir))
        
        PendFile = str(CadPendDir + RelFileList.name)
        print(PendFile.upper())