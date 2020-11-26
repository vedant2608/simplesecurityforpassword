import random
change_dict={
      'a':'z',
      'b':'y',
      'c':'x',
      'd':'w',
      'e':'v',
      'f':'u',
      'g':'t',
      'h':'s',
      'i':'r',
      'j':'q',
      'k':'p',
      'l':'o',
      'm':'n',
      'n':'m',
      'o':'l',
      'p':'k',
      'q':'j',
      'r':'i',
      's':'h',
      't':'g',
      'u':'f',
      'v':'e',
      'w':'d',
      'x':'c',
      'y':'b',
      'z':'a',
      ' ':'1010'
    }
######Encoding the text###############
def Encode():
    lst=[]
    sentence=input("Enter the Text to Encode:")
    for i in sentence:
        for j in i.lower():
            try:
                z=j.replace(j,change_dict[j])
                lst.append(z.upper())
                lst.append(str(random.randint(0,100)))
            except KeyError:
                lst.append(j.replace(j,""))
    print("".join(lst))
#######Decoding the text#################
def Decode():
    lst=[]
    sentence=input("Enter the Encoded text : ")
    for i in sentence:
        for j in i.lower():
             try:
                 z=j.replace(j,change_dict[j])
                 lst.append(z.lower())
             except KeyError:
                 z=j.replace(j,"")
                 lst.append(z)
    print("".join(lst))

Decode()
