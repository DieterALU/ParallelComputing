//=========== Average grade per course ===============

// write code here

var mapFunc = function(){
	emit(this.course, this.grade);
};

var reduceFunc = function(key,values){
	return Array.avg(values);
};


db.runCommand({
mapReduce: 'marks',
map: mapFunc,
reduce: reduceFunc,
out: {
inline:1
}
});
