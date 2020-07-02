encoded="PKEWHNG PKNNG PKEWHNG UWHK PKEWHNG RUNU PKEWHNG PKAM".lower()
alphabet = "a, e, h, i, k, m, n, ng, o, p, r, t, u, w, wh".split(", ")
for a in alphabet:
   e=""
   w=False
   for i,c in enumerate(encoded):
      if c == "n" or c=="w":
         try:
            if encoded[i+1] =="h" or encoded[i+1]=="g":
               if encoded[i+1] =="h":
                  w =True
               continue
            else:
               e+=alphabet[alphabet.index(c)-1]
         except:
            e+=alphabet[alphabet.index(c)-1]
      elif c=="g":
         e+="n"
      elif c=="h" and w:
         e+="w"
         w=False
      elif c==" ":
         e+=" "
      else:
         e+=alphabet[alphabet.index(c)-1]
   print(e)
   encoded=e
      
