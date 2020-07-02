from hashlib import sha256

charactersArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                   "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "!", "@", "#", "$"]

salt = "uLep9JTiRmM1T9gr"
realHash = "2B3B2A6C7D2E18BF6BD44A63DA7A24A0F5FDE915907A8FEAAAF6F2F9DFBBDE85"
testHash = ""
boolBreak = False
i = 0
for a in charactersArray:
    for b in charactersArray:
        for c in charactersArray:
            for d in charactersArray:
                for e in charactersArray:
                    i += 1
                    password = "nat" + a + b + c + d + e
                    saltPassword = password + salt
                    testHash = sha256(str(saltPassword).encode('utf-8')).hexdigest().upper()
                    if testHash == realHash:
                        boolBreak = True
                        break
                if boolBreak == True:
                    break
            if boolBreak == True:
                break
        if boolBreak == True:
            break
    if boolBreak == True:
        break
    print(testHash)
print("\nPASSWORD FOUND!")
print("Nat's Password: " + password)
print("Nat's Hash: " + testHash)
