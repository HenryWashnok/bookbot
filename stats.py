def word_count(text):
    return len(text.split())

def char_count (text):
    ltext=text.lower()
    char_c = {}
    for i in ltext:
        if i in char_c:
            char_c[i]= char_c[i]+1
        else:
            char_c[i]=1
    return char_c

def sort_dic (dic):
    dic_list =[]
    for i in dic:
        charlist={}
        charlist["char"]=i
        charlist["num"]=dic[i]
        dic_list.append(charlist)
    
    dic_list.sort(reverse=True,key=sort_on)
    return dic_list

def sort_on(d):
    return d["num"]

def report(path,wc,ch):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for i in ch:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
        else:
            pass
    print("============= END ===============")

