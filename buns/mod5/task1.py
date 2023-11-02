class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        current = self.end
        end = 0
        while current:
            end = current.data
            current = current.pref
        print(end)
        
        if not self.end:
            return None
        if not self.end.pref:
            data = self.end.data
            self.end = None 
            return data
        current = self.end
        while current.pref.pref:
            current = current.pref
        data = current.pref.data
        current.pref = None
        return data

    def push(self, val):
        new_node = Node(val)
        if not self.end:
            self.end = new_node
        else:
            current = self.end
            while current.pref:
                current = current.pref
            current.pref = new_node
            
        """
        добавление элемента val в конец списка
        """
    def print(self):
        current = self.end
        while current:
            print(current.data, end=" ")
            current = current.pref
        print("none")
        
        """
        вывод на печать содержимого стека
        """

stack = Stack()
stack.push(1)
stack.push(33)
stack.push(100)
stack.print()
stack.pop()
stack.print()


