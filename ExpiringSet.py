import time

class ExpiringSet: 
    """Set in which items (may) expire after a specified number of seconds."""
    
    def __init__(self, ttl=60):
        self._set = {} # actually stored as a dict where values are ttls
        self._ttl = ttl # default time to live for items


    def __contains__(self, item):
        """Needs to be here and also not be expired."""
        
        if ttl := self._set.get(item): # it's here, grab the ttl
            match ttl:
                case n if n > time.time(): # valid
                    return True
                case _: # expired, so clean it up
                    del self._set[item]

        # not here, or expired and deleted above...
        return False


    def __eq__(self, other):
        """Two ExpiringSets are equal if their keys are equal..."""
        self._cleanup() # delete any expired entries
        other._cleanup() # ditto...,
        return self._set.keys() == other._set.keys()

        
    def __len__(self):
        """Compute len, which may mean removing expired items."""
        self._cleanup()
        
        return len(self._set)


    def __repr__(self):
        """Human readable version. We could just ignore expired items,
        but we might as well clean them up here.
        """
        self._cleanup()

        return f'/{', '.join(self._set.keys())}/'
        
        
    def _cleanup(self):
        """Delete expired keys."""
        timestamp = time.time() # get current time
        keys_to_del = [] # make a list of keys to del
        
        for item in self._set: # for each key...
            # ...if it has expired
            if self._set[item] < timestamp:
                keys_to_del.append(item)

        # we need to do this in a separate loop cuz we can't modify a
        # dict while iterating over it...
        for key in keys_to_del:
            del self._set[key]

            
    def add(self, item, ttl=None):
        """Add an item to the ExpiringSet if it's not already here."""
        
        if item in self._set: # already here, nothing to do
            return

        # if ttl is specified here, use it
        # if not, use default ttl
        expires = ttl or self._ttl
        
        if expires:
            expires += int(time.time())
        
        self._set[item] = expires
