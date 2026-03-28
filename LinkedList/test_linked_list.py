from LinkedListIMP import LinkedList

def test_insert():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    assert ll.len == 2
    assert ll.head.val == 10

def test_delete_first():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.delete_first()
    assert ll.head.val == 20
    assert ll.len == 1

def test_delete_last():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.delete_last()
    assert ll.last.val == 10
    assert ll.len == 1

def test_delete_at_position():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.delete_at_position(2)
    assert ll.head.next.val == 30