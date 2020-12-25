
count = 0
with open('train2.txt', 'r') as d:
    strr = d.readlines()
    with open('valid.txt', 'w+') as w:
        with open('full.txt', 'w+') as o:
            for i in strr:
                if count % 7 == 0:
                    w.write(i)
                else:
                    o.write(i)
                count += 1