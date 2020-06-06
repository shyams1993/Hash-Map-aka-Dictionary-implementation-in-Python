from random import randint
class HashTable():
    '''
    Implementation of a Hash Table aka Dictonary.
    '''
    def __init__(self,arrsize):
        '''
        Constructor that initializes the hash table/dictionary based on user input of size.
        Also initializes the address counter to keep track of the index created randomly.
        '''
        self.newdict = ['None']*arrsize
        self.addrlist = []

    def __str__(self):
        return str(self.__dict__)

    def _hash(self):
        '''
        Simple hash function declared privately with "_" so that it's not used outside the class. This hash function is based on random library that returns a random number
        between 0 and 1-size of array. If the number is not in the address list, then it proceeds. Otherwise, gives a different random number.
        '''
        while True:
            x = randint(0,len(self.newdict)-1)
            if x not in self.addrlist:
                return x

    def set(self,key,value):
        '''
        Function to insert a key-value pair into the hash map.
        '''
        address = self._hash()
        self.newdict[address] = [key,value]
        self.addrlist.append(address)
        return self.newdict

    def get(self,key):
        '''
        Function to return the value based on key.
        '''
        for i in self.addrlist:
            if self.newdict[i][0] == key:
                return self.newdict[i][1]

    def keys(self):
        '''
        Function to retrieve all keys.
        '''
        key = []
        for i in self.addrlist:
            key.append(self.newdict[i][0])
        return key

    def values(self):
        '''
        Function to retrieve all values.
        '''
        val = []
        for i in self.addrlist:
            val.append(self.newdict[i][1])
        return val

    def length(self):
        '''
        Function to return the length of the hash map without the empty values.
        '''
        new =[]
        for x in self.newdict:
            if x != 'None':
                new.append(x)
        return len(new)

h = HashTable(30)
h.set("sanjuu",8056441715)
h.set("shyamm",9566293597)
h.set("shyam",9566293597)
h.set("divya",7259887722)
h.set("naushath",9940113955)
h.set("soumya",8903254554)
print(h.get("shyam"))
print(h.values())
print(h.length())