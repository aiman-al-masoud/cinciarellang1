list = fun(){ set(obj(), "size", 0); };

add = fun(li, e){
    size = get(li, "size");
    set(li, size, e);
    set(li, "size", size+1);
};

getFromList = fun(li, index){
    get(li, index);
};


li = list();
add(li, 1);
add(li, 2);
chirp(getFromList(li, 1));
chirp(li);


