
class LP:
    def __init__(self, size):
        self.hash = [None]*size
        self.m = size

    # insert
    def insert(self, key, value):
        index = key%self.m

        # check and then insert in the hash
        if self.hash[index]==None or self.hash[index]=='delete':
            self.hash[index]=[key, value]
        # if already present then pdate the value
        elif self.hash[index][0]==key:
            self.hash[index][1]=value
            return

        else:
            # traverse till we find the empty slot
            i = index
            index+=1
            while(i!=index):
                # update the index
                index = index%self.m

                if self.hash[index]==None or self.hash[index]=='delete':
                    self.hash[index]=[key, value]
                    return
                elif self.hash[index][0]==key:
                    self.hash[index][1]=value
                    return

                index+=1
                
            print('hash is full')

    # search
    def search(self, key):
        index = key%self.m

        if self.hash[index] and self.hash[index][0]==key:
            print(self.hash[index][1])
            return
        elif self.hash[index]==None:
            print('key is not present')
            return

        else:
            # do linear probe
            i = index
            index+=1
            while(i!=index):
                index=index%self.m

                # for the case when the key is not present
                if self.hash[index]==None:
                    print('key is not present')
                    return
                elif self.hash[index][0]==key:
                    print(self.hash[index][1])
                    return

                index+=1
            print('key is not present')

    # delete
    def delete(self, key):
        index = key%self.m

        if self.hash[index]==None:
            return
        elif self.hash[index][0]==key:
            self.hash[index]='delete'
        else:
            # do linear probe and then delete
            i = index
            index+=1

            while(i!=index):
                index = index%self.m

                if self.hash[index]==None:
                    return 
                elif self.hash[index][0]==key:
                    self.hash[index]='delete'
                    return

                index+=1

    # print
    def pp(self):
        for x in self.hash:
            if x:
                print(x[0],'\t-->\t', x[1])
            else:
                print(None)


if __name__=='__main__':
    hh = LP(int(input('size -->\t')))
    while(True):
        print('1 --> insert')
        print('2 --> search')
        print('3 --> delete')
        print('4 --> print')
        print('0 --> EXIT')

        user = int(input('select from above --> \t'))

        if user==1:
            hh.insert(int(input('key --> \t')), int(input('value --> \t')))
        elif user==2:
            hh.search(int(input('key -->\t')))
        elif user==3:
            hh.delete(int(input('key -->\t')))
        elif user==4:
            hh.pp()
        elif user==0:
            break
        else:
            pass
