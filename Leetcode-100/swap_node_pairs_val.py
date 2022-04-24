def pairWiseSwap(head):
    # There must be at-least two nodes in the list
    if (head != None and head.next != None):
        # Swap the node's data with data of next node
        swap(head.data, head.next.data);

        # Call pairWiseSwap() for rest of the list
        pairWiseSwap(head.next.next);