import("./list.cl");

map = fun(li, fx){

    size = get(li, "size");
    
    if size -1 > -1 {
        e = get(li, size-1);
        set(li, "size", size-1);
        chirp(fx(e));
        map(li, fx);
    }

};


li = list();
add(li, 1);
add(li, 2);
add(li, 3);
chirp(li);


map(li, fun(x){x+1;});











