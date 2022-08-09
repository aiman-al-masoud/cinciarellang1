stack = fun(){
    set(set(obj(), "type", "stack"), "index", 0);
};

error = fun(fName){
    fName+"() called on non-stack!";
};

push = fun(s, v){
    
    t = get(s, "type");
    chirp(t);

    if false{
        ret = error("push");
    }else{
        i = get(s, "index") +1;
        set(s, i, v);
        set(s, "index", i);
        ret = s;
    }

    ret;
};

pop = fun(s){
    
    t = get(s, "type");

    if t != "stack"{
        ret = error("pop");
    }else{
        i = get(s, "index");
        ret = get(s, i);
        set(s, "index", i-1);
    }

    ret;
};


x  = stack();

e  = push(x, "crap");
chirp(e);


chirp(x);


