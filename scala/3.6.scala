import collection.mutable.ArrayBuffer

val a=Array(1,2,7,4,5,6)

for(i <- 0 until a.length-1;j<- a.length-1 until i by -1){
    var t=a(j)
    a(j)=a(j-1)
    a(j-1)=t
}
println(a.mkString(","))

val b=ArrayBuffer[Int](1,2,3,4,5,6)
for(i<-0 until a.length-1){
    var v=b.remove(b.length-1)
    b.insert(i,v)
}

println(b.mkString(","))
