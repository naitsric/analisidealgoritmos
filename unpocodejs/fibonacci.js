var fibo = {
	init: function(){
		console.time("t1");
		var ini = 0;
		var more = 1;
		var flag = true;
		var i = 0;
		while(flag){
			var tem = this.sum(ini,more);
			ini = more;
			more = tem;
			console.log(i+" "+tem);
			i++
			if(i>1475){
				flag = false;
			}
		}
		console.timeEnd("t1");
		alert(tem);
	},
	sum: function(ini,mor){
		return ini+mor;
	}
}
fibo.init();