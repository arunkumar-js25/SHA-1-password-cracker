import hashlib

def crack_sha1_hash(hash,use_salts=False):
  file = open('top-10000-passwords.txt', 'r')
  Lines = file.readlines()
  for line in Lines:
      str = line.replace("\n", "")
      if(use_salts):
        saltsfile = open('known-salts.txt', 'r')
        salts = saltsfile.readlines()
        for salt in salts:
          str = salt.replace("\n", "") + line.replace("\n", "") + salt.replace("\n", "")
          if(hashlib.sha1(str.encode()).hexdigest() == hash):
            return line.replace("\n", "")
      else:
        if(hashlib.sha1(str.encode()).hexdigest() == hash):
          return str

  return "PASSWORD NOT IN DATABASE"
