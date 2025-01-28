
file = open("competitive_programming/input.txt", "r")
cont = file.read().split("\n")

n = int(cont[0])

alph = "abcdefghijklmnopqrstuvwxyz"
rot_dict = {
    "a": "e",
    "e": "a",
    "b": "q",
    "q": "b",
    "d": "p",
    "p": "d",
    "h": "y",
    "y": "h",
    "m": "w",
    "w": "m",
    "u": "n",
    "n": "u"
}

comp = {
    "o",
    "s",
    "x",
    "z"
}


def solve(i):
    line = cont[1+i].lower()
    
    chars = []
    for char in line:
        if char not in alph: continue
        if char not in rot_dict and char not in comp: return False
        chars.append(char)

    
    base = list(reversed(chars.copy()))
    for i in range(len(base)):
        if base[i] in comp: continue
        base[i] = rot_dict[base[i]]


    return line + f" ({"is" if base==chars else "not"}) "


for i in range(n):
    print(solve(i))