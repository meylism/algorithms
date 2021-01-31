# Data Structures

## Contents

- [Data Structures](#data-structures)
  - [Contents](#contents)
  - [Contiguous and Linked Structures](#contiguous-and-linked-structures)
    - [Arrays](#arrays)
    - [Linked Structures](#linked-structures)
    - [Comparison](#comparison)

**Data structures** is way to organize and store data in such a way that provides efficient retrieval and modification.

**Abstract data type** is a logical representation of data from the user point of view. ADTs are defined by possible values and operations on them.

> DS vs ADT: DSs serve as a basis for ADTs. ADTs define the logical form of the data type while DSs implement the physical form the data type.

## Contiguous and Linked Structures

Contiguous structures: arrays, matrices, heaps, and hash tables.

Linked structures: lists, trees, graph adjacency lists.

### Arrays

Some properties:

- Constant time access.
- Space efficiency. Unlike linked structures, there is no waste of memory for links.
- Memory locality. Most of the time, we iterate through all the elements of a data structure. Since arrays elements are stored contiguously, they exhibit excellent memory locality. Because there is no need to jump from pointer to pointer, arrays allow for good cache perfomance.

The downside of arrays is *resizing*. This can be compensated by allocating large arrays, but, of course, this is not a solution. One way to achieve relatively efficient resizings in array is to use the concept of **dynamic arrays**. The idea is to create a new array with twofold increase in size when an overflow occurs, and then copying the elements of the old array to the new one.

### Linked Structures

Uses pointers to refer to the next linked node. **Doubly-linked lists** simplify certain operation at a cost of an extra pointer per node.

### Comparison

| Static array                                     | Linked list                                          |
| :----------------------------------------------- | :--------------------------------------------------- |
| Better at *searching*                            | Better at *insertion* and *deletion*                 |
| Has better memory locality and cache performance | No overflow occurs unless the memory is actully full |