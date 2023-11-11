def generateKey(string, kunci):
  kunci = list(kunci)
  if len(string) == len(kunci):
    return(kunci)
  else:
    for i in range(len(string) -len(kunci)):
      kunci.append(kunci[i % len(kunci)])
  return("" . join(kunci))

def encryption(string, kunci):
  encrypt_tulisan = []
  for i in range(len(string)):
    x = (ord(string[i]) +ord(kunci[i])) % 26
    x += ord('A')
    encrypt_tulisan.append(chr(x))
  return("" . join(encrypt_tulisan))

def decryption(encrypt_tulisan, kunci):
  orig_text = []
  for i in range(len(encrypt_tulisan)):
    x = (ord(encrypt_tulisan[i]) -ord(kunci[i]) + 26) % 26
    x += ord('A')
    orig_text.append(chr(x))
  return("" . join(orig_text))

if __name__ == "__main__":
  string = input("Masukkan pesannya: ")
  keyword = input("Masukkan kata kunci: ")
  kunci = generateKey(string, keyword)
  encrypt_tulisan = encryption(string,kunci)
  print("Pesan terenkripsi:", encrypt_tulisan)
  print("Pesan yang didekripsi:", decryption(encrypt_tulisan, kunci))
