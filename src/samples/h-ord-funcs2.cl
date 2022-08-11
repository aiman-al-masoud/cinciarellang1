import("./list.cl");

map = fun(li, fx, n){

    if !n {
        newLi = list();
        n = 0;
    }

    if n < get(li, "size") {

        e = get(li, n);
        #chirp(fx(e));
        #chirp(newLi, add);
        add(newLi, fx(e));
        map(li, fx, n+1);
    }

    newLi;
};


li = list();
add(li, 1);
add(li, 2);
add(li, 3);
chirp(li);


s = map(li, fun(x){x+1;});
chirp(s);










