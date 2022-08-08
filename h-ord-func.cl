maprint3 = fun(a, b, c, f){
    print(f(a), f(b), f(c));
};

maprint3(1,2,3, fun(x){2*x;});

redlprint3 = fun(a, b, c, f){
    print(f(f(a,b), c));
};

redlprint3(1,2,3, fun(a,b){a+b;};);