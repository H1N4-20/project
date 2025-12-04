class Stack:
    """
    A simple implementation of a Stack (LIFO - Last In, First Out).
    
    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item from the stack.
        peek(): Return the top item without removing it.
        is_empty(): Check if the stack is empty.
        size(): Return the number of items in the stack.
    """
    
    def __init__(self):
        """Initialize an empty stack using a Python list."""
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item. Returns None if stack is empty."""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Return the top item without removing it. Returns None if stack is empty."""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

class Queue:
    """
    A simple implementation of a Queue (FIFO - First In, First Out).
    
    Methods:
        enqueue(item): Add an item to the back of the queue.
        dequeue(): Remove and return the front item from the queue.
        peek(): Return the front item without removing it.
        is_empty(): Check if the queue is empty.
        size(): Return the number of items in the queue.
    """
    
    def __init__(self):
        """Initialize an empty queue using a Python list."""
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item. Returns None if queue is empty."""
        if not self.is_empty():
            return self.items.pop(0)  # Remove first element
        return None
    
    def peek(self):
        """Return the front item without removing it. Returns None if queue is empty."""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

# --- Testing Stack ---
stack = Stack()
stack.push("Math")
stack.push("English")
stack.push("History")

print("Stack size:", stack.size())       # Expected: 3
print("Top of stack:", stack.peek())     # Expected: "History"
print("Pop:", stack.pop())               # Expected: "History"
print("Stack after pop:", stack.items)   # Expected: ["Math", "English"]

# --- Testing Queue ---
queue = Queue()
queue.enqueue("Flashcard 1")
queue.enqueue("Flashcard 2")
queue.enqueue("Flashcard 3")

print("Queue size:", queue.size())       # Expected: 3
print("Front of queue:", queue.peek())   # Expected: "Flashcard 1"
print("Dequeue:", queue.dequeue())       # Expected: "Flashcard 1"
print("Queue after dequeue:", queue.items)  # Expected: ["Flashcard 2", "Flashcard 3"]
