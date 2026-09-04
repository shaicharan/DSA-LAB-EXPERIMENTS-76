class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class CSLL:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def add(self, val):
        if self.empty():
            self.head = Node(val)
            self.head.next = self.head
            print("Head value created")
            return

        opt = int(input(
            "Enter 1 to add a Node at the beginning\n"
            "Enter 2 to add a Node at the end\n"
            "Enter 3 to add a Node in the middle:: "
        ))

        if opt == 1:
            a = Node(val)
            n = self.head
            while n.next != self.head:
                n = n.next
            a.next = self.head
            n.next = a
            self.head = a

        elif opt == 2:
            i = self.head
            while i.next != self.head:
                i = i.next
            new_node = Node(val)
            i.next = new_node
            new_node.next = self.head

        elif opt == 3:
            pos = int(input("Enter the position (1-based index):: "))
            
            if pos == 1:
                a = Node(val)
                n = self.head
                while n.next != self.head:
                    n = n.next
                a.next = self.head
                n.next = a
                self.head = a
                return

            i = 1
            n = self.head
            while i < pos - 1 and n.next != self.head:
                n = n.next
                i += 1

            if i == pos - 1:
                new_node = Node(val)
                new_node.next = n.next
                n.next = new_node
            else:
                print("Position out of bounds")

    def delete(self):
        if self.empty():
            print("Linked List empty")
            return

        if self.head.next == self.head:
            self.head = None
            print("Single node removed. List is now empty.")
            return

        opt = int(input(
            "Enter 1 to delete the beginning element\n"
            "Enter 2 to delete the last element\n"
            "Enter 3 to delete elements in between :: "
        ))

        if opt == 1:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = self.head.next
            self.head = self.head.next

        elif opt == 2:
            n = self.head
            while n.next.next != self.head:
                n = n.next
            n.next = self.head

        elif opt == 3:
            op = int(input(
                "Enter 1 to delete by position\n"
                "Enter 2 to delete by value :: "
            ))

            if op == 1:
                pos = int(input("Enter the position :: "))
                if pos == 1:
                    n = self.head
                    while n.next != self.head:
                        n = n.next
                    n.next = self.head.next
                    self.head = self.head.next
                    return

                i = 1
                n = self.head
                while i < pos - 1 and n.next != self.head:
                    n = n.next
                    i += 1

                if n.next != self.head and i == pos - 1:
                    n.next = n.next.next
                else:
                    print("Position not found")

            elif op == 2:
                val = int(input("Enter the value you want to delete :: "))
                
                if self.head.value == val:
                    n = self.head
                    while n.next != self.head:
                        n = n.next
                    n.next = self.head.next
                    self.head = self.head.next
                    return

                n = self.head
                found = False
                while n.next != self.head:
                    if n.next.value == val:
                        found = True
                        break
                    n = n.next

                if found:
                    n.next = n.next.next
                else:
                    print("Value not found")

    def clear(self):
        self.head = None
        print("Linked List cleared")

    def display(self):
        if self.empty():
            print("Linked List empty")
            return

        print("\n--- THE LINKED LIST ---")
        print(self.head.value, "<== HEAD")

        n = self.head.next
        while n != self.head:
            print(n.value)
            n = n.next
        print("--- Linked List ends ---\n")


obj = CSLL()

while True:
    try:
        option = int(input(
            "Enter 1 to add an element\n"
            "Enter 2 to delete an element\n"
            "Enter 3 to clear the Linked List\n"
            "Enter 4 to display the Linked List\n"
            "Enter 5 to exit :: "
        ))

        if option == 1:
            value = int(input("Enter the value you want to add :: "))
            obj.add(value)
        elif option == 2:
            obj.delete()
        elif option == 3:
            obj.clear()
        elif option == 4:
            obj.display()
        elif option == 5:
            print("Goodbye")
            break
        elif option == 6:
            print("Empty state:", obj.empty())
        else:
            print("Wrong option")
    except ValueError:
        print("Please enter a valid integer.")
