import("./list.cl");

map = fun(li, fx){

    size = get(li, "size");
    
    if size -1 {
        e = get(li, size-1);
        set(li, "size", size-1);
        chirp(fx(e));
        map(li, fx);
    }

};


