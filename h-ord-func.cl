maprint3 = fun(a, b, c, f){
    print(f(a), f(b), f(c));
};

maprint3(1,2,3, fun(x){2*x;});


redl3 = fun(a, b, c, f){
    f(f(a,b), c);
};


print(redl3(1,2,3, fun(a,b){
    a+b;
}));


print(redl3(1,2,3, fun(a,b){
    a-b;
}));
