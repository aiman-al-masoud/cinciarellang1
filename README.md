# Cinciarellang

A simple, dinamically typed, c-like, functional programming language.


<img src="docs/res/cinciarella.jpg" width="500" />

## Parser

This is the very first time I try implementing a parser for a "real McCoy" programming language, the technique that I used is called <a href="https://en.wikipedia.org/wiki/Recursive_descent_parser">Recursive Descent</a>; where the goal is to write a bunch of mutually recursive functions that begin calling themselves in a loop (eg: A calls B, B calls C, and C calls back A). The loop eventually terminates, because C eventually returns a base value, and stops calling A.

### Eg:

Take mathematical expressions as an example, the **Expression** is the topmost structure in the hierarchy, and it is defined as the sum of one or more **Terms**; a **Term** is defined as the product of one or more **Factors**; and a **Factor** is a number, a variable, or a bracketed **Expression**, more concisely:

```
E -> E+T | E-T
T -> T*F | T/F
F -> num | var | (E)
```

This means that the mutually recursive trio is going to behave like this (where arrows indicate function calls):
```
parseExp() -> parseTerm() -> parseFactor() ->
    <----------------------------------
```


