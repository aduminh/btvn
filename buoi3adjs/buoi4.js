var number=[10,12,8,16,35]
var max = 0;

for ( i = 0; i < number.length; i++) {
    if (max < number[i] ) {
        max = number[i];
    }
}
console.log(max);