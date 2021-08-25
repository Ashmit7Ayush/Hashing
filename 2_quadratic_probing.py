class Quad:
    def __init__(self, size):
        self.hash = [None]*size
        self.m = 7
        self.size=size

    def hash_fn(self, index):
        return ((index)%self.m + self.i*self.i)%self.size


    # insert
    def insert(self, key, value):
        self.i=0
        index = self.hash_fn(key)

        if self.hash[index]==None or self.hash[index]=='delete':
            self.hash[index]=[key, value]
            return
        elif self.hash[index][0]==key:# update in this case
            self.hash[index][1]=value
            return
        else:
            # do quad probing
            i=index
            self.i+=1
            index = self.hash_fn(key)
            while(i!=index):
                # found delete or none
                if self.hash[index]==None or self.hash[index]=='delete':
                    self.hash[index] = [key, value]
                    return
                # if te key is already present
                elif self.hash[index][0]==key:
                    self.hash[index][1]=value
                    return

                # for the next iteration
                self.i+=1
                index = self.hash_fn(key)

    
    # search
    def search(self, key):
        self.i = 0
        index = self.hash_fn(key)

        # if not present
        if self.hash[index]==None:
            print('key is not present')
            return
        # if key is present
        elif self.hash[index][0]==key:
            print(self.hash[index][1])
            return
        else:
            # do quad probing
            i = index
            self.i+=1
            index = self.hash_fn(key)

            while(i!=index):
                # if null then return
                if self.hash[index]==None:
                    print('key is not present')
                    return
                # if present
                elif self.hash[index][0]==key:
                    print(self.hash[index][1])
                    return
                
                self.i+=1
                index = self.hash_fn(key)

            print('key is not present')

    
    # delete
    def delete(self, key):
        self.i = 0
        index = self.hash_fn(key)

        if self.hash[index]==None:
            print('key is not present')
            return
        elif self.hash[index][0]==key:
            self.hash[index]='delete'
            return
        else:
            # do quad probing
            i = index
            self.i+=1
            index = self.hash_fn(key)
            while(i!=index):
                if self.hash[index]==None:
                    print('key is not present')
                    return
                elif self.hash[index][0]==key:
                    self.hash[index]='delete'
                    return

                self.i+=1
                index = self.hash_fn(key)

            print('key is not present')

    def pp(self):
        for x in self.hash:
            if not x:
                print(x)
            elif x=='delete':
                print(x)
            else:
                print(x[0], '\t-->\t', x[1])

if __name__=='__main__':
    hh = Quad(int(input('size -->')))
    while(True):
        print('1 --> insert')
        print('2 --> search')
        print('3 --> delete')
        print('4 --> print')
        print('0 --> EXIT')

        user = int(input('select from above -->\t'))

        if user==1:
            hh.insert(int(input('key -->')), int(input('value -->\t')))
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

                
