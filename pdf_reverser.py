#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyPDF2


def rotatePDF(filePath, degrees, whichPageStart):
    pdfObj = open(filePath, 'rb')

    fileNameSplit = filePath.split('.pdf');
    outputName = fileNameSplit[0] +"_rot_"+str(degrees)+".pdf";
    print outputName;

    resultPdfFile = open(outputName, 'wb')

    pdfReader = PyPDF2.PdfFileReader(pdfObj)
    pdfWriter = PyPDF2.PdfFileWriter()

    pagesAmount = pdfReader.getNumPages();

    for i in range(pagesAmount):
        pageObj = pdfReader.getPage(i)
        if(i%whichPageStart == 0 and i!=0 ):
            pageObj.rotateClockwise(90)

        pdfWriter.addPage(pageObj);

    pdfWriter.write(resultPdfFile);
    pdfObj.close();
    resultPdfFile.close();






def test():
    rotatePDF("name.pdf", 90, 2);















