import("./list.cl");

map = fun(li, fx, n){

    if n == 0{
        newLi = list();
    }

    if n < get(li, "size") {
        chirp(fx(get(li, n)));
        chirp(newLi, add);
        
        #add(newLi, fx(get(li, n)));
        map(li, fx, n+1);
    }

    newLi;
};


li = list();
add(li, 1);
add(li, 2);
add(li, 3);
chirp(li);


s = map(li, fun(x){x+1;}, 0);
chirp(s);










