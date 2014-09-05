'''
Created on Aug 27, 2014

@author: markc
'''

import os
from pathlib import Path

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
    RelDirFile = list(RelPdfDir.glob(c))
    for RelFileList in RelDirFile:
        # Copy Release Files to Holding Directory - Manually Moved to Superceded Directory
        
        #os.system("copy \"%s\" \"%s\"" % (RelFileList, TempHoldDir))
        
        PendFile = str(CadPendDir + RelFileList.name)
        #print(PendFile.upper())
        jjj = Path(PendFile).exists()
        #print(jjj)
        jj1 = Path(PendFile)
        #print(jj1)
         
        # Copy Pending Files to VS1 Production Drawings Directory
        #os.system("copy \"%s\" \"%s\"" % (jj1, ProdPDFRelDir))
        
        # Move Pending Files to Release Directory
        
        #os.system("move \"%s\" \"%s\"" % (CadPendDir, PDFRelDir))
        
        # Convert pdf to jpg files
        # file size 120kb, using as standard starting out.
        
        PDFFileStr = str(ProdPDFRelDir + d + ".pdf")
        JPGFileStr = str(ProdJPGRelDir + d + ".jpg")
        #print(JPGFile)
        PDFFile = Path(PDFFileStr)
        JPGFile = Path(JPGFileStr)
        print(PDFFile)
        print(JPGFile)
        
        #os.system("convert -verbose -monochrome -resize 2500 -interlace none -rotate 90 -density 300 -threshold 80% -quality 80 \"%s\" \"%s\"" % (PDFFile, JPGFile))
        os.system("convert -monochrome -resize 2500 -interlace none -rotate 90 -density 300 -quality 80 \"%s\" \"%s\"" % (PDFFile, JPGFile))

