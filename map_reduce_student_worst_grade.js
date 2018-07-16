
// ==========  5 student with the worst grade  in maths and history only. Formating the final grade as a percentage eg. 87%===============

// write code here
var mapperFunc = function(){
	var key = this.course;
	var value = {name:this.name,grade:this.grade};
	emit(key,value);
};

var reducerFunc = function(key,values){
	reducedVal = [];
	values.forEach(function(val){
	
	reducedVal.push([val.name,val.grade]);
	}
	);
	reducedVal.sort(function(a,b){return a[1]>b[1];});
	top = String(reducedVal[1][0]+" : "+reducedVal[1][1]+"  ,"+
		     reducedVal[2][0]+" : "+reducedVal[2][1]+"  ,"+
		     reducedVal[3][0]+" : "+reducedVal[3][1]+"  ,"+
		     reducedVal[4][0]+" : "+reducedVal[4][1]+"  ,"+
		     reducedVal[5][0]+" : "+reducedVal[5][1]
		    );
    return top
};

db.runCommand({
mapReduce: 'marks',
map: mapperFunc,
reduce: reducerFunc,
out: {inline:1}
});


