
count = 0
with open('full.txt', 'r') as d:
    strr = d.readlines()
    with open('valid.txt', 'w+') as w:
        with open('train.txt', 'w+') as o:
            for i in strr:
                if count % 7 == 0:
                    w.write(i)
                else:
                    o.write(i)
                count += 12