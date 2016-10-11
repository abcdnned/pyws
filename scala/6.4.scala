class Point(val x:Int,val y:Int)
object Point{
  def apply(x:Int,y:Int)=new Point(x,y)
}

val p=Point(1,2)
println(p.x)
println(p.y)
