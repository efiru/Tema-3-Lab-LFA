# Tema 3 – Limbaje Formale și Automate

Acest proiect oferă trei funcționalități pentru gramatica liberă de context  
\[
G = (\{S\}, \{a,b\}, P, S),
\quad
P: S \to aSb \mid \varepsilon
\]
care generează limbajul \(L = \{\,a^n b^n \mid n \ge 0\}\).

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
