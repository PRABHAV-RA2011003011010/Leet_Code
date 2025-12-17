class ListNode:
    def __init__(self, prev=None, key=0, val=0, next=None):
        self.prev = prev
        self.key=key
        self.val = val
        self.next = next
       

class LRUCache:

    def __init__(self, capacity: int):

        self.head=ListNode()
        self.tail=ListNode()

        self.head.next=self.tail
        self.tail.prev=self.head

        self.capacity=capacity
        self.cache={}

    def remove_node(self, node):

        prev_node=node.prev
        next_node=node.next

        prev_node.next=next_node
        next_node.prev=prev_node
    
    def insert_at_front(self, node):

        node.prev=self.head
        node.next=self.head.next

        self.head.next.prev=node
        self.head.next=node


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        else:
            cur=self.cache[key]
            self.remove_node(cur)
            self.insert_at_front(cur)

            return cur.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:

            cur=self.cache[key]
            cur.val=value
            self.remove_node(cur)
            self.insert_at_front(cur)
     
            

        else:
            if len(self.cache)==self.capacity:
                lru=self.tail.prev
                self.remove_node(lru)
                del self.cache[lru.key]

            new_node=ListNode(key=key,val=value)
            self.insert_at_front(new_node)
            self.cache[key]=new_node
            


            


               
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)