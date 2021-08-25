class Chain:
    def __init__(self):
        self.hash = [[] for x in range(7)]
        self.m = 7

    # insert
    def insert(self, key, value):
        index = key%self.m

        # check whether the key is present or not
        for x, y in enumerate(self.hash[index]):

            if y[0]==key:
                self.hash[index][x][1]=value
                print('key already present')
                return

        self.hash[index].append([key, value])

    # delete
    def delete(self, key):
        index = key%self.m

        for x in range(len(self.hash[index])):
            k, v = self.hash[index][x]

            if k==key:
                self.hash[index].pop(x)
                return

        print('key not present')

    # search
    def search(self, key):
        index  =key%self.m

        for x in range(len(self.hash[index])):
            # print(self.hash[index][x])
            k, v = self.hash[index][x]

            if k==key:
                print(v)
                return

        print('key is not present')

    def pp(self):
        for x,ll in enumerate(self.hash):
            print(x ,'\t-->\t', *ll)


if __name__=='__main__':
    hh = Chain()
    while(True):
        print('1 --> insert')
        print('2 --> delete')
        print('3 --> search')
        print('4 --> print')
        print('0 --> exit')

        user = int(input(' choose from above --> \t'))

        if user==1:
            hh.insert(int(input('key -->\t')), int(input('value --> \t')))
        elif user==2:
            hh.delete(int(input('key -->\t')))
        elif user==3:
            hh.search(int(input('key -->\t')))
        elif user==4:
            hh.pp()
        elif user==0:
            break
        else:
            pass
            
