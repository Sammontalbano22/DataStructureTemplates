# Array Lists

Welcome to the Array List Folder! This project explains and demonstrates how an **array list** works in computer science, using clear code examples and visualizations.

---

## What is an Array List?

An **Array List** is a **resizable, indexed collection** of elements. Unlike regular arrays that have a fixed size, array lists automatically resize themselves when more elements are added or removed.

Each element is stored **contiguously in memory** and can be accessed using an index, making random access very fast.

---

## How I Learned Array Lists

Imagine you're managing a list of tasks in a to-do app. You want to:

- Quickly view your 3rd or 5th task — use array indexing  
- Add new tasks to the end — append  
- Remove a completed task from anywhere in the list — remove by index  

The array list is like a flexible array that expands or contracts as needed.




Time Complexity
Operation	Time Complexity
Access (by index)	O(1),
Append (amortized)	O(1),
Insert/Delete (mid)	O(n),
Search	O(n)


Example:
```python
tasks = ["Email", "Meeting", "Code", "Lunch"]
tasks.append("Debug")       # Add at end
tasks.pop(1)                # Remove "Meeting"
print(tasks[2])             # Access "Lunch"
```
## Array List LeetCode Problems
- Contains Duplicate   	
- Valid Anagram   	
- Two Sum   	
- Group Anagrams   	
- Top K Frequent Elements   	
- Encode and Decode Strings   	
- Product of Array Except Self   	
- Valid Sudoku   	
- Longest Consecutive Sequence   	



