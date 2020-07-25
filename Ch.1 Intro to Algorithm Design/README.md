# Introduction to Algorithm Design

## Subchapters

* [Reasoning for Correctness](#reasoning-for-correctness)
* [Modelling the Problems](#modelling-the-problems)
* [Exercises](#exercises)

## Reasoning for Correctness

Please take a look at the two examples author gives in the first two
subchapters of the chapter one. If you do, you come to notice that working
with algorithms is very subtle. We need tools to distinguish correct 
algorithms from the incorrect one. One of those tools is called **proof**.

We have to put efforts to show both algorithms' correctness and not 
incorrectness. We will develop tools from here on.

### Expressing Algorithms

We have 3 ways to accomplish that. They are:
* English
* Pseudocode
* Programming language

There are trade-offs should be made. E.g. when there are minor details,
programming languages your be your tool. The main thing with algorithms
is an **idea**. If you get an idea, you are done. Try to choose the way
which expresses you algorithm with clarity.

### Problems and Properties

Expressing your problem and its properties is as important as describing
the algorithm itself. Problem specification has 2 parts:

1. The set of allowed inputs.
2. The required properties of the algorithm's output.

This is very important. One has to put an effort to express their problem
with clarity. It is hard to prove poor-defined algorithms as well.

**Take-home lesson:** It is important in algorithm design techniques to
narrow down the allowed input instances until correct algorithm is found. E.g.
change the 2D array to 1D until you find a solution for the simpler form 
of the problem.

### Demonstrating incorrectness

The best way is to come up with counter examples. Followings are techniques
to develop to get better at finding counter examples.

* *Think small:* Try to go counter with simpler examples as they are easy
to verify
* *Seek extremes:* Many of the counter-examples are huge and tiny, left and right,
near and far...

## Modelling the Problems

"Modelling is the art of designing your application in terms of precisely
described, well-understood problems". Modelling is the key to apply
algorithmic design techniques to real-world problems. Proper modelling 
can eliminate the need to design or even implement algorithms, by relating
to what has been done before.

Real-world problems involve real-world objects. For example, for the problem
of finding the shortest path, you will be dealing with roads. However, most
algorithms are designed to work on defined abstract structures such as
permutations, graphs and sets. To exploit algorithms, you must learn to
describe your problem in terms of well-known fundamental structures.

### Combinatorial Objects

It is good that someone has already dealt with the problem you are searching
solution for, perhaps in a substantially different contexts. But, to find
solution from previous experiences, you have to express your problem using
common structures:

* Permutations: arrangements and orderings of items. They are in question
when the problem seeks "arrangement", "tour", "ordering" or "sequence".

* Subsets: selection from set of items. They are in question
when the problem seeks "cluster", "collection", "committee", "group" or "selection".

* Trees: hierarchical relationships between items. They are in question
when the problem seeks "hierarchy", "dominance", "relationship" or "taxonomy".

* Graphs: relationship between arbitrary pairs of objects. They are in question
when the problem seeks "network", "circuit", "web" or "relationship".

* Points: locations in some geometric space. They are in question
when the problem seeks "sites", "positions", "data records" or "locations".

* Polygons: regions in some geometric space. They are in question
when the problem seeks "shapes", "regions" or "boundaries".

* Strings: sequence of characters or patterns. They are in question
when the problem seeks "text", "characters", "patterns" or "labels".

**Take-home lesson:** Modelling your application in terms of well-defined
structures and algorithms is the most important step towards a solution.

## Exercises

### Interview Problems

1-28. [5] Write a function to perform integer division without using either the / or *
operators. Find a fast way to do it. [Solution.](src/com/meylis/algorithms/SpecialDivision.java)

1-29. [5] There are 25 horses. At most, 5 horses can race together at a time. You must
determine the fastest, second fastest, and third fastest horses. Find the minimum
number of races in which this can be done.

### Programming Challenges

These programming challenge problems with robot judging are available at
http://www.programming-challenges.com or http://online-judge.uva.es.

1-1. “The 3n + 1 Problem” – Programming Challenges 110101, UVA Judge 100. [Solution.](src/com/meylis/algorithms/ThreeNPlusOne.java)

1-2. “The Trip” – Programming Challenges 110103, UVA Judge 10137.

1-3. “Australian Voting” – Programming Challenges 110108, UVA Judge 10142.



 

 
