s = ''
strings = set()
def password_cracker(string, length):
   if length == 5:
      strings.add(string)
      return

   for i in range(97, 123):
      password_cracker(string + chr(i), length +1)


password_cracker('', 0)

