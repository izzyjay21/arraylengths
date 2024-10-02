def recursivelength(list):
    if len(list)==0:
        return list
    else:
        return recursivelength (list[1:]) + list[0]
    
print(recursivelength("845678,7854,3453")) 