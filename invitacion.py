#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from ezodf import newdoc
import os
import zipfile
import tempfile
import xlrd

def updateZip(zipname, filename, data):
    # generate a temp file
    tmpfd, tmpname = tempfile.mkstemp(dir=os.path.dirname(zipname))
    os.close(tmpfd)

    # create a temp copy of the archive without filename
    with zipfile.ZipFile(zipname, 'r') as zin:
        with zipfile.ZipFile(tmpname, 'w') as zout:
            zout.comment = zin.comment # preserve the comment
            for item in zin.infolist():
                if item.filename != filename:
                    zout.writestr(item, zin.read(item.filename))

    # replace with the temp archive
    os.remove(zipname)
    os.rename(tmpname, zipname)

    # now add filename with its new data
    with zipfile.ZipFile(zipname, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(filename, data)

workbook = xlrd.open_workbook('./speakers/speakers.xls')
worksheet = workbook.sheet_by_name('Speakers')
for x in range(1,5,1):
    id = str(int(worksheet.cell(x,0).value))
    filen = './speakers/' + id + '.odt'
    name = ''
    for y in range(1,4,1):
        name += worksheet.cell(x, y).value
        name += ' '
    name.rstrip()
    org = worksheet.cell(x,4).value
    odt = newdoc(doctype='odt', filename=filen, template='invitacion.odt')
    odt.save()
    a = zipfile.ZipFile('invitacion.odt')
    content = a.read('content.xml')
    content = str(content.decode(encoding='utf8'))
    content = str.replace(content,"Nombre Completo", name)
    content = str.replace(content,"Organizacion", org)
    updateZip(filen, 'content.xml', content)
    cm = "unoconv -f pdf " + filen
    os.system(cm)
