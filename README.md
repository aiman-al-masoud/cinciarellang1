# Cinciarellang

A simple, dinamically typed, c-like, functional programming language.


<img src="docs/res/cinciarella.jpg" width="500" />

## Parser

This is the very first time I try implementing a parser for a "real McCoy" programming language, with a technique known as <a href="https://en.wikipedia.org/wiki/Recursive_descent_parser">Recursive Descent</a>; where the goal is to write a bunch of <a href="https://en.wikipedia.org/wiki/Mutual_recursion">mutually recursive</a> functions that repeatedly call each other in a loop (eg: A calls B, B calls C, and C calls back A etc...). The loop eventually terminates, because function C eventually returns a base value, and stops calling A.



### Eg:

Take mathematical expressions as an example, 

1. An **Expression** is the topmost structure in the hierarchy, and it is defined as the sum of one or more **Terms**.
2. A **Term** is defined as the product of one or more **Factors**
3. And a **Factor** is a number, a variable, a bracketed **Expression**, or a negated **Factor**. 

More concisely:

```
E -> E+T | E-T
T -> T*F | T/F
F -> num | var | (E) | -F
```
*(these are known as "production rules").*

So the mutually recursive trio will behave like this (where arrows indicate function calls):
```
parseExp() -> parseTerm() -> parseFactor() ->
    <----------------------------------
```

Note how + and - are the weakest operators (think PEMDAS) so they're used to build up the topmost and most "fragile" structure: the **Expression**; while * and / are stronger, so they're used to build up the **Term** structure down in the hierarchy. To implement a full programming language you basically need to extend this simple hierarchy to include operators like: ==, !=, 

### Sources:
* https://www.youtube.com/watch?v=SToUyjAsaFk
* https://lisperator.net/pltut/







