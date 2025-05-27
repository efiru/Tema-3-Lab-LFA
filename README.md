# Tema 3 – Limbaje Formale și Automate

Acest proiect oferă trei funcționalități pentru CFG

G = (V, Σ, P, S), unde:
  V = { S }
  Σ = { a, b }
  P:
    S → a S b
    S → ε
  S: simbol de start

L(G) = { a^n b^n | n ≥ 0 }

---

## Conținut

- **`generate_strings(max_strings, max_length)`**  
  Generează aleatoriu până la `max_strings` șiruri din \(L(G)\), cu lungime maximă `max_length`.

- **`derive(target)`**  
  Găsește și returnează secvența de forme sentențiale (derivarea) de la simbolul de start `S` la șirul terminal `target`, sau lista goală dacă nu se poate deriva.

- **`recognize(s)`**  
  Verifică dacă șirul `s` aparține limbajului \(\{a^n b^n \mid n\ge0\}\) (True/False).

---

## Cerințe

- Python 3.x

---

## Instalare și rulare

1. Clonează proiectul:
   ```bash
   git clone https://github.com/efiru/Tema-3-Lab-LFA.git
   cd Tema-3-Lab-LFA
