reverse_dict = []
with open("./flypy_reverse.dict.yaml") as f:
    reverse_dict = [(c.split("\t")[0],c.split("\t")[1]) for c in f.read().split("\n")]

def get_code(s: str, num: int):
    ss = ""
    for i in range(4):
        if num < 2 ** i:
            ss =s[len(s)-1-i]+ss
        else:
            num -= 2**i
            ss="`"+ss
    return ss
for i in range(1,16):
    first = '`'
    for char, code in reverse_dict:
        print(f"{char}\t{get_code(code,i)}")