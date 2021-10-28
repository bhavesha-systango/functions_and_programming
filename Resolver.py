class Resolver:
    def __init__(self):
        print("init")

    def __call__(self, name):
        print("this is call",name)

resolve = Resolver()
resolve("sixty-north")
    