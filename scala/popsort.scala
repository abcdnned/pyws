
var array=Array(3,1,2,4,7,5,6)

for(i<-0 until array.length-1;j<-0 until array.length-1-i){
    if(array(j)<array(j+1)){
        val t=array(j)
        array(j)=array(j+1)
        array(j+1)=t
    }
}
for(i<-array) print(i)
