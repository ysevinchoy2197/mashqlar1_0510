class Patient:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def info(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"


class Hospital:
    def __init__(self, nomi):
        self.nomi = nomi
        self.bemorlar = []

    def bemor_qoshish(self, bemor):
        self.bemorlar.append(bemor)

    def shifoxona_info(self):
        print(f"Shifoxona nomi: {self.nomi}")
        for bemor in self.bemorlar:
            print(bemor.info())


bemor1 = Patient("Akbar", 35)
bemor2 = Patient("Zulfiya", 28)
bemor3 = Patient("Hamid", 40)

shifoxona = Hospital("Ibn Sino")

shifoxona.bemor_qoshish(bemor1)
shifoxona.bemor_qoshish(bemor2)

shifoxona.shifoxona_info()

shifoxona.bemor_qoshish(bemor3)
