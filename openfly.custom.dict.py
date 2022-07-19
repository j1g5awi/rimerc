# 彳（双人旁） 绑定声母：i -> r

chaizi = {}
with open("./chaizi-jt.txt", "r") as f:
    chaizi = {
        line.split("\t", 1)[0]: line.split("\t")[1:] for line in f.read().split("\n")
    }


def 有偏旁(字: str, 偏旁: str):
    if 字 not in chaizi:
        # print(字)
        return False
    for 拆字 in chaizi[字]:
        if 偏旁 == 拆字[0]:
            return True
    return False


def 替换(偏旁: str, 旧声母: str, 新声母: str):
    for 词典 in (
        "./openfly_reverse.dict.yaml",
        "openfly.off-table.dict.yaml",
        "openfly.primary.dict.yaml",
        "openfly.secondary.dict.yaml",
        "openfly.uncommon.dict.yaml",
        "./flypy.dict.yaml",
    ):
        dict = []
        output = ""
        with open(词典, "r") as f:
            raw = f.read()
            output += raw[: raw.find("...") + 4]
            raw = raw[raw.find("...") + 4 : -1]
            dict = [
                (line.split("\t", 1)[0], line.split("\t", 1)[1])
                for line in raw.split("\n")
            ]
        for char, code in dict:
            if 有偏旁(char, 偏旁) and len(code) > 2 and code[2] == 旧声母:
                output += f"{char}\t{code[:2]}{新声母}{code[3:]}\n"
            else:
                output += f"{char}\t{code}\n"
        with open(词典, "w") as f:
            f.write(output)


替换("彳", "i", "r")
