# Cinciarellang

A simple dinamically typed, c-like functional programming language.


<img src="docs/res/cinciarella.jpg" width="500" />


This is the very first time I try implementing a parser for a "real McCoy" programming language, the technique that I used is called <a href="https://en.wikipedia.org/wiki/Recursive_descent_parser">Recursive Descent</a>; where the goal is to write a bunch of mutually recursive functions that end up calling themselves in a loop, which eventually terminates because some function returns a base value and stops calling the others.

