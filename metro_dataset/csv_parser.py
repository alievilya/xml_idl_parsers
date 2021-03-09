import csv

written = []
with open('src/B_No_d800mm_R2-Filt.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    # with open(filename, 'w') as file:

    with open('new_ds/b7.txt', 'a') as trainfile:
        for row in reader:

            number = int(row[0])
            chislo = str(number).zfill(5)
            filename = "B_No_d800mm_R2_" + chislo

            x1 = row[3]
            y1 = row[4]
            wid = row[5]
            hei = row[6]
            x2 = int(row[3]) + int(wid)
            y2 = int(row[4]) + int(hei)
            xc = round((int(x2) + int(x1)) / 2 / 352, 4)
            yc = round((int(y2) + int(y1)) / 2 / 288, 4)
            width = round(int(wid) / 352, 3)
            height = round(int(hei) / 2 / 288, 3)
            res = "{} {} {} {} {}".format(0, xc, yc, width, height)
            with open("new_ds/b7/" + filename + ".txt", 'a') as writer:
                writer.write(res + '\n')
            print(res)

            if filename not in written:
                trainfile.write('data/obj/' + filename + ".jpg" + '\n')
                written.append(filename)
