#!/usr/bin/node
// Computes and prints a factorial recursively

const num = parseInt(process.argv[2]);

function factorial(x) {
	if (x === 0){
		return 1;
	}
	return x * factorial(x-1);
}

console.log(factorial(num));
