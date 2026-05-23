# Chatbot AI pentru Pisici (NLTK Naive Bayes)

Acest proiect implementează un chatbot simplu bazat pe Inteligență Artificială și Procesarea Limbajului Natural (NLP). Scriptul este capabil să clasifice intenția utilizatorului și să ofere răspunsuri dinamice despre comportamentul, alimentația și somnul pisicilor.

##  Cum funcționează?
Spre deosebire de un algoritm rigid bazat pe reguli stricte, acest chatbot folosește un model probabilistic:

1. **Procesarea Textului:** Mesajul primit este convertit în litere mici și transformat într-un format de tip *Bag-of-Words* (sac de cuvinte).
2. **Modelul AI:** Folosind clasificatorul **Naive Bayes** din biblioteca `nltk`, modelul calculează probabilitatea ca textul să aparțină uneia dintre cele trei categorii definite: `personalitate`, `mancare` sau `somn`.
3. **Răspunsul:** Odată identificată intenția, chatbot-ul selectează aleatoriu o replică dintr-o bază de date predefinită pentru a evita repetiția și a asigura o conversație naturală.

##  Tehnologii și Biblioteci
* **Python 3.x**
* **NLTK (Natural Language Toolkit)** – pentru clasificatorul IA și tokenizare.
* **Random** – pentru selecția dinamică a răspunsurilor.

##  Instalare și Rulare

1. Instalează biblioteca necesară:
```bash
   pip install nltk
