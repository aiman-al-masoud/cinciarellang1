list = fun(){ set(obj(), "size", 0); };

add = fun(li, e){
    size = get(li, "size");
    set(li, size, e);
    set(li, "size", size+1);
};


li = list();
add(li, 1);
add(li, 2);
#chirp(get(li, 1));
#chirp(li);


