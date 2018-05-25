import csv, json

reader = csv.DictReader(open('orders111.csv', 'r', encoding='utf-8'))

dict_list = []

id = 1



for line in reader:
    # dict_list.append(line)
    # create your own dic
    if id < 139795:
        dict = {"index":{"_index":"busdb","_type":"bus","_id":id}}

        # convert to json
        json_1 = json.dumps(dict)
        json_2 = json.dumps(line)

        f = open("firstBus.json", "a")
        f.write(json_1)
        f.write("\n")
        f.write(json_2)
        f.write("\n")

        f.close()

        id = id + 1
    # here id = 559181
    # write it to another file.
    # seperate into two files:
    # each will contain 559180, 559182.
    elif id < 279591:
        dict = {"index": {"_index": "busdb", "_type": "bus", "_id": id}}

        # convert to json
        json_1 = json.dumps(dict)
        json_2 = json.dumps(line)

        f = open("secondBus.json", "a")
        f.write(json_1)
        f.write("\n")
        f.write(json_2)
        f.write("\n")

        f.close()

        id = id + 1

    elif id < 409381:
        dict = {"index": {"_index": "busdb", "_type": "bus", "_id": id}}

        # convert to json
        json_1 = json.dumps(dict)
        json_2 = json.dumps(line)

        f = open("thirdBus.json", "a")
        f.write(json_1)
        f.write("\n")
        f.write(json_2)
        f.write("\n")

        f.close()

        id = id + 1


    else:
        dict = {"index": {"_index": "busdb", "_type": "bus", "_id": id}}

        # convert to json
        json_1 = json.dumps(dict)
        json_2 = json.dumps(line)

        f = open("fourthBus.json", "a")
        f.write(json_1)
        f.write("\n")
        f.write(json_2)
        f.write("\n")

        f.close()

        id = id + 1







