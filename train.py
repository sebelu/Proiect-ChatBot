from nltk.classify import NaiveBayesClassifier

############ DATE DE ANTRENARE ##################

training_data = [

    #  ("ex de intrebare","clasa/eticheta")

    #personalitate
    ("Sunt pisicile prietenoase ?","personalitate"),
    ("Sunt pisicile dragute ?","personalitate"),
    ("Sunt pisicile inteligente ?","personalitate"),
    ("Sunt pisicile lenese ?","personalitate"),
    ("Sunt pisicile agresive ?","personalitate"),

    #mancare
    ("Ce mananca pisicile ?","mancare"),
    ("Mananca pisicile peste ?","mancare"),
    ("Mananca pisicile fructe ?","mancare"),
    ("Cu ce se hranesc pisicile ?","mancare"),
    ("Se hranesc pisicile cu soareci ?","mancare"),


    #somn
    ("Cat dorm pisicile ?","somn"),
    ("Cate ore dorm pisicile ?","somn"),
    ("Se odihnesc mult pisicile ?","somn"),
    ("Cat timp nu sunt active pisicile ?","somn"),
    ("Dorm mult pisicile ?","somn")


]

############ PROCESARE TEXT ##################

def split_words(text):
    words = text.lower().split()
    return {word: True for word in words}

training_set = [
    (split_words(text), label)
    for text, label in training_data
]

############ MODEL AI ##################

classifier = NaiveBayesClassifier.train(training_set)

############ CHATBOT ##################

print("Salut! Intreaba-ma despre pisici.")

while True:

    mesaj = input("> ")
    if mesaj.strip().lower() == "bye":
        break

    rezultat = classifier.classify(split_words(mesaj))

    if rezultat == "personalitate":
        print("Răspuns: Pisicile pot fi prietenoase, drăguțe, inteligente, leneșe sau agresive.")
    elif rezultat == "mancare":
        print("Răspuns: Pisicile se hrănesc cu pește, fructe și alte alimente specifice.")
    elif rezultat == "somn":
        print("Răspuns: Pisicile dorm în medie între 12 și 16 ore pe zi.")
