# Projekti nga lënda Siguria e të Dhënave

# Crypto Tool - Vernam & ROT13

Ky është një program në Python që funksionon në terminal. Ai i lejon përdoruesit të enkriptojnë (kriptojnë) dhe dekriptojnë (zbulojnë) mesazhe duke përdorur dy algoritme të njohura kriptografike: **Vernam Cipher** dhe **ROT13**.

## 📌 Përshkrimi i Algoritmeve

### 1. Vernam Cipher (One-Time Pad)
Algoritmi Vernam është një metodë ku çdo shkronjë e mesazhit kombinohet matematikisht me një shkronjë të një çelësi të gjeneruar rastësisht.
* **Enkriptimi:** Mblidhen vlerat e shkronjave të mesazhit dhe çelësit.
* **Dekriptimi:** Zbritet vlera e çelësit nga shkronja e kriptuar për t'u kthyer tek mesazhi origjinal.
* **Rregulli Kryesor:** Çelësi duhet të jetë të paktën i njëjtë në gjatësi me tekstin që po kriptohet. Programi ynë e gjeneron këtë çelës automatikisht për ty.

### 2. ROT13 (Rotate by 13 places)
ROT13 është një variant i thjeshtë i Shifrës së Çezarit. Ky algoritëm e zëvendëson çdo shkronjë me shkronjën që ndodhet 13 pozicione më vonë në alfabetin anglez. 
* Meqenëse alfabeti ka 26 shkronja, zhvendosja me 13 pozicione dy herë të kthen aty ku ishe. Prandaj, i njëjti funksion përdoret si për të enkriptuar ashtu edhe për të dekriptuar.

---

## 🚀 Udhëzimet e Ekzekutimit

Për ta përdorur këtë program, duhet të keni të instaluar **Python 3** në kompjuterin tuaj. Sigurohuni që skedarët (`main.py`, `vernam_encrypt.py`, `vernam_decrypt.py`, `rot13.py`) të jenë të gjithë në të njëjtën dosje.

1. Hapni **Terminalin** (në Mac/Linux) ose **Command Prompt** (në Windows).
2. Shkoni te dosja ku ndodhet projekti duke përdorur komandën `cd`. Për shembull:
   ```bash
   cd Desktop/Projekti_Kriptografi

## Shembuj te rrezulltateve
## Shembull 1 per Veram Cypher

========== CRYPTO TOOL ==========
1. Vernam Cipher
2. ROT13
0. EXIT
Enter your choice: 1
1. Encrypt
2. Decrypt
Select: 1
Enter plaintext: HELLO WORLD
Processing...
Ciphertext: EQNVZ XMCKL
Key: XMCKL EQNVZ

## Kur Dekriptojm me duke perdorur qelsin e lartcekur

Select: 2
Enter ciphertext: EQNVZ XMCKL
Enter key: XMCKL EQNVZ
Decrypting...
Decrypted: HELLO WORLD

## Shembull 2 per Rot13

========== CRYPTO TOOL ==========
1. Vernam Cipher
2. ROT13
0. EXIT
Enter your choice: 2
1. Encrypt
2. Decrypt
Select: 1
Enter plaintext: Kriptografia eshte e bukur!
Encrypting...
Encrypted: Xevcgbtensvn rfugr r ohxhe!

