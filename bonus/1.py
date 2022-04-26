def recursive_bsearch(data, el):
    if len(data) == 0:
        print(False)
    else:
        mid = len(data)//2

        if data[mid] == el:
            print(True)
        elif el < data[mid]:
            recursive_bsearch(data[:mid], el)
        elif el > data[mid]:
            recursive_bsearch(data[mid:], el)

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31] 
recursive_bsearch(test_list, 27)