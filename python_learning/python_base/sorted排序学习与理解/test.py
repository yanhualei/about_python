
import json
groups_info={
    'id1':{
        'name':'name1',
        'desc':'desc'
    },
    'id2':{
        'name':'name2',
        'desc':'desc'
    },
    'id3': {
        'name': 'name3',
        'desc': 'desc'
    },
    'id4': {
        'name': 'name4',
        'desc': 'desc'
    }
}
def name(t):
    # print(t)
    return t[1]["name"]



groups_info = sorted(groups_info.items(),key=name,reverse=True)
print("按照成绩排序，由大到小：",groups_info)
# groups_info = dict(groups_info)
# print("按照成绩排序，由大到小：",groups_info)
# items = {}
# for i in groups_info:
#     print(i)
#     items[i[0]] = i[1]
#
# print(items)



