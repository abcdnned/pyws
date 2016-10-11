var m = scala.collection.immutable.SortedMap[String,Int]()
val in = new java.util.Scanner(new java.io.File("testfile.java"))
while (in.hasNext()){
    val token=in.next()
    val s= if(m.contains(token)) (token,m(token)+1) else (token,1)
    m+=s
}
println(m)
