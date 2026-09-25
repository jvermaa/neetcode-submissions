class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Key:Node
        self.left_most = Node(-1, -1)
        self.right_most = Node(-1, -1)
        
        self.left_most.next = self.right_most
        self.right_most.prev = self.left_most #[left_most]<=>[right_most]

    def get(self, key: int) -> int:
        if key in self.cache:

            # [left_most]<=>[]<=>[key]<=[]=>[right_most]
            
            current = self.cache[key]
            current.next.prev = current.prev
            current.prev.next = current.next

            current.next = self.right_most
            self.right_most.prev.next = current
            current.prev = self.right_most.prev
            self.right_most.prev = current
            
            return self.cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            current = self.cache[key]
            current.val = value

            current.next.prev = current.prev
            current.prev.next = current.next

            current.next = self.right_most
            self.right_most.prev.next = current
            current.prev = self.right_most.prev
            self.right_most.prev = current
            return
        
        # Logic to insert

        new_node = Node(key, value)
        new_node.next = self.right_most
        self.right_most.prev.next = new_node
        new_node.prev = self.right_most.prev
        self.right_most.prev = new_node
        self.cache[key] = new_node


        if len(self.cache) > self.capacity:
            # remove the left most
            dispose = self.left_most.next
            self.left_most.next = dispose.next
            dispose.next.prev = self.left_most

            del self.cache[dispose.key]
        

        
