# 题目是合并两个有序列表，合并之后仍然是有序列表，不能使用+或者extend

def sort_list(left,right):
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    return result

if __name__ == '__main__':

    a = [1, 2, 3, 5, 9]
    b = [2, 4, 6, 7, 8, 9]
    result = sort_list(a,b)
    print(result)



