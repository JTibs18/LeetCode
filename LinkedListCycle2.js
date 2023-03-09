// Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
// Note that pos is not passed as a parameter.
// Notice that you should not modify the linked list.

function ListNode(val) {
    this.val = val;
    this.next = null;
}

function detectCycle(head){
    let nodes = new Set();

    if (head == null){
        return null;  
    }
    
    var cur = head;
    nodes.add(cur);

    while(cur.next){
        cur = cur.next;
        if (!nodes.has(cur)){
            nodes.add(cur);
        }else{
            return cur;
        }
    }
    return null;
}

// Test cases
var head = new ListNode(3)
var node1 = new ListNode(2)
var node2 = new ListNode(0)
var node3 = new ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1
console.log(detectCycle(head))

var head = new ListNode(1)
var node1 = new ListNode(2)
head.next = node1
node1.next = head
console.log(detectCycle(head))

var head = new ListNode(1)
console.log(detectCycle(head))