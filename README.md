# Projekti nga lënda Siguria e të Dhënave

## Tema e projektit
Ky projekt implementon dy algoritme klasike të kriptimit:

- **Vernam Cipher**
- **ROT13**

Programi është ndërtuar në gjuhën **Python** dhe ofron mundësi për:
- enkriptim
- dekriptim
- gjenerim automatik të çelësit për Vernam Cipher
- ndërfaqe të thjeshtë në terminal

---

## Përmbajtja e projektit

Projekti përbëhet nga këto fajlla:

- `main.py` – fajlli kryesor për ekzekutimin e programit
- `vernam_encrypt.py` – përmban funksionin për enkriptim me Vernam Cipher dhe gjenerimin e çelësit
- `vernam_decrypt.py` – përmban funksionin për dekriptim me Vernam Cipher
- `rot13.py` – përmban funksionet për enkriptim dhe dekriptim me ROT13

---

## Përshkrimi i algoritmeve

### 1. Vernam Cipher
Vernam Cipher është një metodë kriptimi simetrik ku çdo shkronjë e plaintext-it kombinohet me një shkronjë të çelësit.  
Në këtë projekt:
- teksti kthehet në shkronja të mëdha
- çelësi gjenerohet automatikisht sipas numrit të shkronjave
- karakteret jo alfabetike ruhen pa ndryshim
- për dekriptim përdoret i njëjti çelës

**Formula e enkriptimit:**
C = (P + K) mod 26

**Formula e dekriptimit:**
P = (C - K) mod 26

Ku:
- `P` = plaintext
- `K` = key
- `C` = ciphertext

---

### 2. ROT13
ROT13 është një variant i Caesar Cipher, ku çdo shkronjë zhvendoset për **13 pozita** në alfabet.

Karakteristikat e ROT13:
- përdor të njëjtin funksion si për enkriptim ashtu edhe për dekriptim
- shkronjat e mëdha dhe të vogla ruhen sipas formës
- karakteret speciale dhe hapësirat nuk ndryshohen

Shembull:
- `A` bëhet `N`
- `B` bëhet `O`
- `HELLO` bëhet `URYYB`
