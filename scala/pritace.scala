var r=util.Random
def generate(n:Int)={
    val result=new Array[Int](n)
    for(i<-0 until n){
        result(i)=r.nextInt(n)
    }
    result
}

val array=generate(10)
for(i<-0 until array.length)
    println(array(i))
    
