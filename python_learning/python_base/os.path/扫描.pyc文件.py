import os


def pick(obj):
    if obj.endswith(".xml"):
        print(obj)


def scan_path(ph):
    file_list = os.listdir(ph)
    for obj in file_list:
        chid_ph = os.path.join(ph,obj)
        if os.path.isfile(chid_ph):
            pick(obj)
        if os.path.isdir(chid_ph):
            scan_path(chid_ph)


if __name__ == '__main__':
    path = "/home/oldeleven/PycharmProjects/about_python/"
    scan_path(path)