
count = 0
with open('new_ds/full.txt', 'r') as d:
    stroka = d.readlines()
    with open('new_ds/valid.txt', 'a') as w:
        with open('new_ds/train.txt', 'a') as o:
            for i in stroka:
                if count % 7 == 0:
                    w.write(i)
                else:
                    o.write(i)
                count += 1
