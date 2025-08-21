class SortedList(list):
    ''' Sub-class of list to maintain all items in ascending order '''
    def __init__(self, iterable=None):
        if iterable is None:
            super().__init__()
        else:
            super().__init__(sorted(iterable))

    def append(self, item):
        ''' Add a single item to the list '''
        super().append(item)
        list.sort(self)  # call base list.sort, bypassing overrides

    def extend(self, iterable):
        ''' Add multiple elements at once'''
        super().extend(iterable)
        list.sort(self)

    def insert(self, index, item):
        '''  '''
        super().append(item)  # ignore provided index
        list.sort(self)

    def __setitem__(self, index, value):
        # Temporarily call original setitem to avoid re-triggering sort
        super().__setitem__(index, value)
        list.sort(self)

    def __iadd__(self, other):
        super().__iadd__(other)
        list.sort(self)
        return self
