val a= Array(1.2,1.3,1.4)
println(a.mkString(","))

def doubleAverage(a:Array[Double])={
    var sum:Double=0
    for(i<-a)
        sum+=i
    sum/a.length
}

println(doubleAverage(a))
