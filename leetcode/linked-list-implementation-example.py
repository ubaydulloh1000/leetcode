

class MyLinkedList:

    def __init__(self, val=None, next=None):
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        i = 0
        node = self

        while node:
            if index == i:
            	print("OBJ ID G: ", id(node))
            	return node.val
            node = node.next
            i+=1
        return -1


    def addAtHead(self, val: int) -> None:
    	self.next = self.__class__(val=self.val, next=self.next)
    	self.val = val


    def addAtTail(self, val: int) -> None:
        node = self
        
        while node.next:
            node = node.next

        print("VALLL: ", val)
        node.next = self.__class__(val=val)
        print("OBJ ID T: ", id(node.next))
        print("OBJ VAL T: ", node.next.val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        node = self
        if index == i:
            self.next = self
            self.val = val
        
        while node.next:
            i += 1
            if index == i:
                temp = node.next
                node.next = self.__class__(val=val)
                node.next.next = temp
                return
            node = node.next

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        node = self
        
        if index == i:
            if self.next:
                self = self.next
            else:
                self = None
        
        while node.next:
            i += 1
            if index == i:
                node.next = node.next.next
                return
            node = node.next

    def __repr__(self):
    	return f"List val={self.val} next={self.next}"


def main():
	obj = MyLinkedList()
	param_1 = obj.get(0)

	obj.addAtHead(val=10)
	obj.addAtTail(val=99)
	
	param_2 = obj.get(1)
	param_3 = obj.get(2)
	print("PARAM 2: ", param_2)
	print("PARAM 3: ", param_3)


if __name__ == '__main__':
	main()
