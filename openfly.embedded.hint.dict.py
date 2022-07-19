dict = {}
codes = []
with open("./flypy.dict.yaml", "r", encoding="utf-8") as f:
    raw = f.read()
    dict = {
        c.split("\t")[0]: c.split("\t")[1]
        for c in raw[raw.find("...") + 4 : -1].split("\n")
        if len(c.split("\t")[1]) > 2
    }
    for i in range(4):
        codes.append({v: k for k, v in dict.items() if len(v) == i + 1})

embedded_dict = ""
old_embedded_dict = {}
with open("./openfly.embedded.hint.dict.yaml", "r", encoding="utf-8") as f:
    raw = f.read()
    embedded_dict += raw[: raw.find("...") + 4]
    old_embedded_dict = {
        c.split("\t")[1]: c.split("\t")[0]
        for c in raw[raw.find("...") + 4 : -1].split("\n")
        if c.split("\t")[0][:-2] in dict
    }

code3 = {}
with open("./code3.txt", "r", encoding="utf-8") as f:
    code3 = {
        c.split("\t")[1]: c.split("\t")[0] + "`" + dict[c.split("\t")[0]][-1]
        for c in f.read().split("\n")
        if c.split("\t")[0] in dict
    }

code423 = {}
for k, v in codes[3].items():
    if len(v) > 1 and k[:-1] not in code423:
        code423[k[:-1]] = f"{v}`{k[-1]}"


for i in range(ord("a"), ord("z") + 1):
    for j in range(ord("a"), ord("z") + 1):
        for k in range(ord("a"), ord("z") + 1):
            code = chr(i) + chr(j) + chr(k)
            if code not in codes[2]:
                if code in code3:
                    embedded_dict += f"{code3[code]}\t{code}\n"
                elif code in old_embedded_dict:
                    embedded_dict += f"{old_embedded_dict[code]}\t{code}\n"
                elif code in code423:
                    print(f"{code423[code]}\t{code}")
with open("openfly.embedded.hint.dict.yaml", "w", encoding="utf-8") as f:
    f.write(embedded_dict)
