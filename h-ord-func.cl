maprint3 = fun(a, b, c, f){
    print(f(a), f(b), f(c));
};


g = fun(x){2*x;};

maprint3(1,2,3, (g));