class DH:
    def __init__(self, size):
        self.size = size
        self.hash = [None]*size
        self.m = 7

    # hash fn
    def hash_fn(self, key):
        #       hash fn 1       hash fn 2
        return ((key%self.m)+self.i*(6 - key%6))%self.size


    # insert
    def insert(self, key, value):
        self.i = 0
        index = self.hash_fn(key)

        # check for None
        if self.hash[index]==None or self.hash[index]=='delete':
            self.hash[index]=[key, value]
            return

        # check for the altready present
        elif self.hash[index][0]==key:
            self.hash[index][1]=value
            return

        # else do double hash to find the index
        else:
            i = index
            self.i+=1
            index = self.hash_fn(key)

            while(i!=index):
                # check for the null
                if self.hash[index]==None or self.hash[index]=='delete':
                    self.hash[index]  = [key, value]
                    return
                # if already present
                elif self.hash[index][0]==key:
                    self.hash[index][1]=value
                    return

                self.i+=1
                index = self.hash_fn(key)

            
    # search
    def search(self, key):
        self.i=0
        index = self.hash_fn(key)

        # check for the none
        if self.hash[index]==None:
            print('key is not present')
            return
        # check for the key
        elif self.hash[index][0]==key:
            print(self.hash[index][1])
            return
        else:
            # do double hash
            i = index
            self.i+=1
            index = self.hash_fn(key)
            while(i!=index):
                # check for the null
                if self.hash[index]==None:
                    print('key is not present')
                    return
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

        # chek for  None
        if self.hash[index]==None:
            print('key is not present')
            return
        # if key present then delete 
        elif self.hash[index][0]==key:
            self.hash[index]='delete'
            return

        else:
            # do double hashing
            i  = index
            self.i+=1
            index  = self.hash_fn(key)

            while(i!=index):
                # if None
                if self.hash[index]==None:
                    print('key not present')
                    return
                elif self.hash[index][0]==key:
                    self.hash[index]='delete'
                    return

                self.i+=1
                index = self.hash_fn(key)
            print('key is not present')


    # print
    def pp(self):
        for x in self.hash:
            if x ==None:
                print(x)
            elif x=='delete':
                print(x)
            else:
                print(x[0], '\t-->\t', x[1])

if __name__=='__main__':
    hh =  DH(int(input('size-->\t')))
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


            
