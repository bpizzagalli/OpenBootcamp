function factorial(n){
    var total = 1;
    while (n>1){
        total *= n;
        n--;
        if (n<=1){
            break;
        }

    }
    console.log(total);
}

factorial(10);
