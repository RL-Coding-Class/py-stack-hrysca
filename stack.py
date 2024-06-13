class Stack:
    """Provides stack container"""
    def init(self, _stack_type = None, _items = None):
        self._items = _items if _items is not None else []
        self._stack_type = _stack_type

    def push(self, data) -> None:
        self._items.append(data)
    
    def pop(self):
        if self._items == None:
            return None
        temp = self._items[-1]    
        del self._items[-1]
        return temp
    
    def get(self):
        if self._items == None:
            return None
        return self._items[-1]
    
    def length(self) -> int:
        return len(self._items)

    def str(self):
        return str(self._items)

    def repr(self):
        return f"Stack(_stack_type = {repr(self._stack_type)!r}, _items = {self._items})"
