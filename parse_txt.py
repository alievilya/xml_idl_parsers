import re

def find_center(coords, width=640, height=480):
    x0, y0, x1, y1 = [float(n) for n in coords]
    x = round((x0 + x1)/2/width, 3)
    y = round((y0 + y1)/2/height, 3)
    w = round((x1 - x0) /width, 3)
    h = round((y1 - y0)/height, 3)

    return "{} {} {} {} {}".format(0, x, y, w, h)

with open ('brainwash_train.txt', 'r') as file:
    data = file.readlines()

names = []

for line in data:
    # print(line[29:49])
    # print(line[45:49])
    if line[:-4] != '.png':
        names.append('data/obj/' + line[29:49]+'\n')
    # coorrdinates.append(line[54:])
#
# with open('train2.txt', 'w') as wr:
#     wr.writelines(names)

# boxes = []
# for i, name in enumerate(names):
#     with open('train/'+name[:-4]+'txt', 'w') as f:
#         ke = re.findall(r'\w+.0', str(data[i][51:-2]))
#         hui = ke.copy()
#         for h in range(0, len(hui), 4):
#             coordinates = find_center(hui[h:h + 4])
#             f.write(coordinates+'\n')
#             boxes.append(coordinates)
#         # print(boxes)
