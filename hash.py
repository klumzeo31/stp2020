class Entry:
    """
        holds key, value pairs
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.is_deleted = False

class Map(object):
    """
        a basic, minimal implementation of a hash map
    """
    def __init__(self):
        """
            constructs a new Map
        """
        self.table = [None] * 10
        self.load_factor = .75
        self.current_size = 0

    def __setitem__(self, key, item):
        """
            stores the key value combo in the table
            implements open addressing collision resolution
        """
        entry = Entry(key, item)
        for i in range(len(self.table)):
            index = self.__get_hash_code(key, i)

            if self.table[index] is None or self.table[index].is_deleted:
                self.table[index] = entry 
                self.current_size += 1
                if float(self.current_size)/len(self.table) >= self.load_factor:
                    self.__resize_table()
                break

    def __getitem__(self, key):
        """
            gets the value associated with the key
        """
        for i in range(len(self.table)):
            index = self.__get_hash_code(key, i)

            if self.table[index] is not None:
                if self.table[index].key == key:
                    if self.table[index].is_deleted:
                        raise KeyError('Key is not in the map')
                    else:
                        return self.table[index].value

            elif self.table[index] is None:
                raise KeyError('Key is not in the map')

        raise KeyError('Hmm something has gone wrong here')

    def __get_hash_code(self, key, value):
        return (hash(key) + value) % len(self.table) 

    def __resize_table(self):
        new_table = [None] * (len(self.table) * 2)
        for i in range(len(self.table)):
            new_table[i] = self.table[i]

        self.table = new_table

    def delete(self, key):
        """
            deletes a value from the hash table
        """
        for i in range(len(self.table)):
            index = self.__get_hash_code(key, i)

            if self.table[index] is not None:
                if self.table[index].key == key:
                    if self.table[index].is_deleted:
                        raise KeyError('Key is not in the map')
                    else:
                        self.table[index].is_deleted = True
                        self.current_size -= 1
                        break

a=Map()
a.__setitem__('a', 1)
print(a.__getitem__('a'))