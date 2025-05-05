# 🧩 Doubly Linked Lists

Welcome to the **Doubly Linked List** Folder! This project explains and demonstrates how a **doubly linked list** works in computer science, using clear code examples and visualizations.

---




## 📚 What is a Doubly Linked List?

A **Doubly Linked List (DLL)** is a type of linked data structure where each node contains **three components**:

1. **Data** – The value stored in the node.
2. **Next Pointer** – A reference to the **next** node in the sequence.
3. **Previous Pointer** – A reference to the **previous** node in the sequence.

This allows **bi-directional traversal**, unlike a singly linked list which only moves forward.

---

## 🔗 How I learned Doubly Linked Lists

  Consider a web browser. WHen you hit the back arrow to go to the previous page it is able to do so because the current page holds a reference to the page previously visited. Because there are references to the the previous and next page, it is possible to navigate forwards and backwards because the chain is linked both directions
  Head -> [Prev Page: None | Page DATA A| Next Page: B] <-> [Prev Page: A | Page DATA B | Next Page: C] <-> [Prev Page: B | Page DATA  C | Next Page: D]





---

## 🔗 Visual Structure


Each node links to both its previous and next neighbors, forming a chain that can be navigated in **both directions**.

---

## 🛠️ Key Operations

| Operation            | Description                                     |
|----------------------|-------------------------------------------------|
| `insertFront()`      | Adds a node to the front of the list            |
| `insertEnd()`        | Adds a node to the end of the list              |
| `deleteNode()`       | Deletes a given node from the list              |
| `traverseForward()`  | Prints all elements from head to tail           |
| `traverseBackward()` | Prints all elements from tail to head           |

---

## ⏱️ Time Complexity

| Operation              | Time Complexity |
|------------------------|-----------------|
| Insertion at Front     | O(1)            |
| Insertion at End       | O(1)\*          |
| Deletion of a Node     | O(1)\*\*        |
| Search for a Value     | O(n)            |
| Forward Traversal      | O(n)            |
| Backward Traversal     | O(n)            |

> \* If you maintain a tail pointer. Otherwise, it’s O(n).  
> \*\* If the node pointer is known. Otherwise, searching is O(n).

---

## ⏱️ Example Leetcode Problems

  - [Easy: Reversed Linked Lists #206](https://leetcode.com/problems/reverse-linked-list/description/)
  
  - [Medium: Remove Node From End of Linked List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
    
  - [Hard: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

  
