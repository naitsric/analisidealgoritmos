A = [6,5,3,1,8,7,2,4]

debugger;
for (var i = 1; i < A.length; i++) {
	temp = A[i]
	for (var j = i - 1; j >= 0 && A[j]>temp; j--) {
		A[j+1] = A[j];
	};
	A[j+1] = temp;
};
