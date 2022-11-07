class clock:

    def __init__(self, jam, menit, detik):
        self.jam = jam 
        self.menit = menit
        self.detik = detik

    def term(self):
        if 0 <= self.jam <= 24 and 0 <= self.menit <= 59 and 0 <= self.detik <= 59:
            print(self.jam, ":", self.menit, ":", self.detik)
        else:
            print("error")

jam = clock(int(input("jam:")), int(input("menit:")), int(input("detik:")))
jam.term()