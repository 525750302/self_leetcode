import random
class node(object):
    def __init__(self,num):
        self.val = num
        self.next = None
        self.before = None
        self.down_state = None
        self.up_state = None

class Skiplist(object):

    def __init__(self):
        self.head1 = node(-1)
        self.head2 = node(-1)
        self.head3 = node(-1)
        self.head4 = node(-1)
        self.head1.up_state = self.head2
        self.head2.up_state = self.head3
        self.head3.up_state = self.head4
        self.head2.down_state = self.head1
        self.head3.down_state = self.head2
        self.head4.down_state = self.head3

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        head = self.head1
        findposition = self.find_position(target,head)
        if findposition.val< target:
            print("search",target,"False")
            return False
        elif findposition.val == target:
            print("search",target,"True")
            return True


    def find_position(self, target, head):
        while head.next!=None and head.next.val <= target:
            head = head.next
        if head.next == None:
            if head.up_state == None:
                return head
            return self.find_position(target,head.up_state)
        else:
            if head.up_state == None:
                return head
            return self.find_position(target,head.up_state)


    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        head = self.head1
        self.add_node(num,head)
        print("add",num,"Null")
    
    def add_node(self,num,head):
        while head.next!=None and head.next.val <= num:
            head = head.next
        if head.up_state == None:
            new_node = node(num)
            new_node.next = head.next
            head.next = new_node
            if new_node.next!= None:
                new_node.next.before = new_node
            new_node.before = head
            return new_node
        if head.up_state != None:
            new_head = self.add_node(num,head.up_state)
            if new_head != False:
                if random.random()<0.5:
                    new_node = node(num)
                    new_node.up_state = new_head
                    new_head.down_state = new_node
                    new_node.next = head.next
                    head.next = new_node
                    if new_node.next!= None:
                        new_node.next.before = new_node
                    new_node.before = head
                    return new_node
                else:
                    return False

            return new_head

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        head = self.head1
        findposition = self.find_position(num,head)
        if findposition.val!= num:
            print("erase",num,"False")
            return False
        elif findposition.val == num:
            next_traget = findposition.down_state
            findposition.before.next = findposition.next
            if findposition.next!= None:
                findposition.next.before = findposition.before
            del findposition
            findposition = next_traget
            while findposition!= None:
                next_traget = findposition.down_state
                findposition.before.next = findposition.next
                if findposition.next!= None:
                    findposition.next.before = findposition.before
                del findposition
                findposition = next_traget
            print("erase",num,"TRUE")
            return True
                
   

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)