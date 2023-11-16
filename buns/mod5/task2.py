#Создать класс. Очередь на структуре данных двусвязный список. 
class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди
    
    def is_empty(self):
        return self.start is None

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.is_empty():
            return None
        
        data = self.start.data
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref
            self.start.nref = None
        return data

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_el = Node(val)
        if self.is_empty():
            self.start = new_el
            self.end = new_el
        else:
            new_el.next = self.start
            self.start.pref = new_el
            self.start = new_el
        

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)
        
        if n == 0:
            new_node.next = self.start 
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            index = 0
            while current and index < n - 1:
                current = current.next
                index += 1
            
            if current is None:
                self.enqueue(val)
            else:
                new_node.nref = current.nref
                new_node.pref = current
                if current.nref:
                    current.nref.pref = new_node
                current.next = new_node

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        cur = self.start
        while cur:
            print(cur.data, end=" ")
            cur = cur.nref
        print("None")

z = Queue()
z.push(1)
z.push(2)
z.insert(2,44)
z.push(3)
z.print()
z.pop()
z.print()
