val a=Array(1,2,3,4,5,6,7)
val a2=Array(1,2,3,4,5,6)

def swap(arr:Array[Int])={
    for(i <- 0 until arr.length) yield {
        if(i!=arr.length-1 && i % 2==0)
            arr(i+1)
        else
            arr(i-1)
        
    }
}


val b=swap(a)
val b2=swap(a2)
println(a.mkString(","))
println(a2.mkString(","))
println(b.mkString(","))
println(b2.mkString(","))
