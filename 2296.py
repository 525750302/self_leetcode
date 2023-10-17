class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.before = None

class TextEditor:

    def __init__(self):
        self.head = node("")
        self.now_cursor = self.head


    def addText(self, text: str) -> None:
        for i in range(len(text)):
            new_node = node(text[i])
            if i == 0:
                head = new_node
                now_node = new_node
            new_node.before = self.now_cursor
            if self.now_cursor!= None:
                if self.now_cursor.next!= None:
                    self.now_cursor.next.before = new_node
                new_node.next = self.now_cursor.next
                self.now_cursor.next = new_node
            self.now_cursor = new_node

    def deleteText(self, k: int) -> int:
        result = 0
        while self.now_cursor!= None and k > 0:
            if self.now_cursor == self.head:
                break
            before = self.now_cursor.before
            before.next = self.now_cursor.next
            if self.now_cursor.next!= None:
                self.now_cursor.next.before = before
            self.now_cursor.before = None
            self.now_cursor.next = None
            del self.now_cursor
            if before != None:
                self.now_cursor = before
            k -= 1
            result += 1
        return result


    def cursorLeft(self, k: int) -> str:
        if self.now_cursor == None:
            return ""
        for i in range(k):
            if self.now_cursor.before!= None:
                self.now_cursor = self.now_cursor.before
        output_str = ""
        count = 0
        point = self.now_cursor
        while count<10 and point!=None:
            output_str = point.val + output_str
            point = point.before
            count = count + 1
        
        return output_str

    def cursorRight(self, k: int) -> str:
        if self.now_cursor == None:
            return ""
        for i in range(k):
            if self.now_cursor.next!= None:
                self.now_cursor = self.now_cursor.next
        output_str = ""
        count = 0
        point = self.now_cursor
        while count<10 and point!=None:
            output_str = point.val + output_str
            point = point.before
            count = count + 1
        
        return output_str



# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)