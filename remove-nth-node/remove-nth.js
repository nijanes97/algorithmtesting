function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

var removeNthFromEnd = function(head, n) {
    copy = new ListNode(0, head)
    pointer1 = copy
    pointer2 = copy
    
    for (i = 0; i <= n; i++){
        pointer1 = pointer1.next
    }
    while (pointer1 != null){
        pointer2 = pointer2.next
        pointer1 = pointer1.next
    }
    
    pointer2.next = pointer2.next.next
    return copy.next
    
//     counter = 0
    
//     while(pointer1.next != null){
//         pointer1 = pointer1.next
//         if(counter === n){
//             pointer2 = pointer2.next
//         } else {
//             counter += 1
//         }
//     }
    
//     if(pointer2.next === pointer1 && n === 2){
//         return pointer1
//     }
//     if(pointer2 === head && n > 2 && counter != n){
//         return pointer2.next
//     }
//     if(counter != n){
//         return head
//     }
//     pointer2.next = pointer2.next.next
    
//     return head
};

tester = new ListNode(0, null);
pointer = tester
for(i = 1; i < 10; i++){
    temp = new ListNode(i, null)
    pointer.next = temp
    pointer = temp
}

printer = removeNthFromEnd(tester, 3);


while(printer != null){
    console.log(printer.val)
    printer = printer.next
}