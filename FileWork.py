class name():
    l = '1'

    def du(self):
        self.chan()
        self.pri()

    def chan(self):
        self.l = '2'

    def pri(self):
        print(self.l)


if __name__ == "__main__":
    na = name()
    na.du()