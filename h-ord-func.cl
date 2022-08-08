maprint3 = fun(a, b, c, f){
    print(f(a), f(b), f(c));
};

g = fun(x){2*x;};

maprint3(1,2,3, g);

redlprint3 = fun(a,b,c,f){
    print(f(f(a,b), c));
};

h = fun(a,b){a+b;};

redlprint3(1,2,3, fun(a,b){a+b;});