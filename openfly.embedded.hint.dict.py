import code


dict = {}
new_dict = []

with open("./openfly.primary.dict.yaml", "r", encoding="utf-8") as f:
    dict = {
        c.split("\t")[1]: c.split("\t")[0]
        for c in f.read().split("\n")[12:-1]
        if len(c.split("\t")[1])
    }
    for i in range(4):
        new_dict.append({k: v for k, v in dict.items() if len(k) == i + 1})

s = ""
code423 = {}
for k, v in new_dict[3].items():
    if k[:-1] not in code423:
        code423[k[:-1]] = f"{v}`{k[-1]}"

for i in range(ord("a"), ord("z") + 1):
    for j in range(ord("a"), ord("z") + 1):
        for k in range(ord("a"), ord("z") + 1):
            code = chr(i) + chr(j) + chr(k)
            if code not in new_dict[2] and code in code423:
                s += f"{code423[code]}\t{code}\n"
with open("new.openfly.embedded.hint.dict.yaml", "w", encoding="utf-8") as f:
    f.write(s)
