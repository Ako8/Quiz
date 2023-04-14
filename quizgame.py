KITXVEBI = {
    1: "Which animal is known as the 'Ship of the Desert'?",
    2: "How many days are there in a week?",
    3: "How many letters are there in the English alphabet?",
    4: "Rainbow consist of how many colours?",
    5: "Name the biggest continent in the world?",
    6: "ramdenia 5 x 5"
}

PASUXEBI = {
    1: {
        "A": {"Camel": True},
        "B": {"Lion": False},
        "Score": 0
    },
    2: {
        "A": {"7": True},
        "B": {"5": False},
        "Score": 0
    },
    3: {
        "A": {"26": True},
        "B": {"31": False},
        "Score": 0
    },
    4: {
        "A": {"7": True},
        "B": {"14": False},
        "Score": 0
    },
    5: {
        "A": {"Asia": True},
        "B": {"America": False},
        "Score": 0
    },
    6: {
        "A": {"25": True},
        "B": {"20": False},
        "Score": 0
    }

}


def damushaveba(pasuxebi, kitxva, pasuxi):
    savaraudoebi = pasuxebi[kitxva]
    a = str(savaraudoebi[pasuxi].keys())
    a = a[a.index('[') + 2:a.index(']') - 1]
    return a


def kitxvebis_chamowera(kitxvebi, pasuxebi, kitxva):
    print(f"{kitxva}: {kitxvebi[kitxva]}")
    savaraudoebi = pasuxebi[kitxva]
    a = str(savaraudoebi["A"].keys())
    b = str(savaraudoebi["B"].keys())


    print(f"A){a[a.index('[') + 2:a.index(']') - 1]}\nB){b[b.index('[') + 2:b.index(']') - 1]}")


def pasuxis_shemowmeba(kitxva, pasuxebi, pasuxi):
    savaraudoebi = pasuxebi[kitxva]
    if savaraudoebi[pasuxi]:
        savaraudoebi["Score"] = 2
    else:
        savaraudoebi["Score"] = 0


def main():
    it = 0
    score = 0
    kitxvis_nomeri = None
    while kitxvis_nomeri != 0:
        kitxvis_nomeri = input("Question ID (Quit: 0): ")
        if kitxvis_nomeri == '0':
            break
        elif kitxvis_nomeri.isdigit():
            if len(KITXVEBI) >= int(kitxvis_nomeri) > 0:
                kitxvebis_chamowera(KITXVEBI, PASUXEBI, int(kitxvis_nomeri))
                kitxvis_pasuxi = input("Answer(A/B): ").upper()
                if kitxvis_pasuxi != 'A' and kitxvis_pasuxi != 'B':
                    continue
                else:
                    it += 1
                    pasuxebis = damushaveba(PASUXEBI, int(kitxvis_nomeri), kitxvis_pasuxi)
                    print(f"{pasuxebis}")
                    pasuxis_shemowmeba(int(kitxvis_nomeri), PASUXEBI, kitxvis_pasuxi)
        else:
            continue
    for i in PASUXEBI:
        pas = PASUXEBI[i]
        score += pas["Score"]
    print(f"Score: {score}/{it*2}")

main()
