from lxml import etree
import os
from os.path import isfile, join

def find_center(coords, width=640, height=480):
    x0, y0, x1, y1 = [float(n) for n in coords]
    x = round((x0 + x1)/2/width, 3)
    y = round((y0 + y1)/2/height, 3)
    w = round((x1 - x0) /width, 3)
    h = round((y1 - y0)/height, 3)

    return "{} {} {} {} {}".format(0, x, y, w, h)

def parseXML(xmlFile, writepath, counter_fire, counter_smoke):
    full = []
    width = 0
    height = 0
    global cnt
    with open(xmlFile) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)
    for appt in root.getchildren():
        if appt.tag == "size":
            for elem in appt.getchildren():
                if elem.tag == 'width':
                    if elem.text != '0':
                        width = int(elem.text)
                    else: cnt+=1
                if elem.tag == 'height':
                    if elem.text != '0':
                        height = int(elem.text)
                    else: cnt += 1

        for elem in appt.getchildren():

            coord = []
            if elem.tag == 'bndbox':
                for el in elem.getchildren():
                    coord.append(int(el.text))
            if width == 0 or height == 0:
                continue

            if coord:
                # coord.insert(0, objclass)
                print(coord)
                str_bbox = find_center(coord, width=width, height=height)
                full.append(str_bbox)
    if width != 0 or height != 0:
        with open(writepath, 'w') as writer:
            for stroka in full:
                writer.write(stroka+'\n')



    return counter_fire, counter_smoke

if __name__ == "__main__":
    pathIn = 'JPEGImages/'
    XmlPath = 'Annotations/'
    TxtPath = 'TxtPath/'
    ImagePath = pathIn
    files = [f for f in os.listdir(ImagePath) if isfile(join(ImagePath, f))]
    cntr_fire = 0
    cntr_smoke = 0
    cnt = 0
    for p in range(0, len(files)):
        filename = ImagePath + files[p]
        xmlpath = XmlPath + files[p]
        txtpath = TxtPath + files[p]
        xmlfile = xmlpath[0:-4] + ".xml"
        txtfile = txtpath[0:-4] + ".txt"
        print(txtfile)

        cntr_fire, cntr_smoke = parseXML(xmlfile, txtfile, cntr_fire, cntr_smoke)

    print("examples: {}".format(cnt))

    files_tr = os.listdir('TxtPath')
    with open ('full.txt', 'w') as wr:
        for line in files_tr:
            wr.write('data/obj/' + line[0:-4] + '.jpg' + '\n')
