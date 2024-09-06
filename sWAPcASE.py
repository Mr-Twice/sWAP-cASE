def swap_case(s):
     strs = ""
     for i in s:
        if i.islower():
            strs += i.upper()
        else:
             strs += i.lower()
       
     return strs

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
