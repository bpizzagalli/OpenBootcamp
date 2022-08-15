function factorial(n){
    var total = 1;
    while (n>1){
        total *= n;
        n--;
    }
    console.log(total);
}

factorial(10);