import yaml
class Membership():
    # static attribute
    
    def __init__(self, name):
        self.name = name
        self.discount = 0
        self.check()
        pass
    
    def check(self):
        with open("members.yml") as f:
            members = yaml.load_all(f, Loader=yaml.FullLoader)
            for x in members:
                #print(type((x["name"])))
                if self.name == x["name"]:
                    print("Khach hang than thiet")
                    self.discount = x["intimacy_point"]
                    break
            