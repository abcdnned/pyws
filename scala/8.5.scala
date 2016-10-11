class Point(val x:Double,val y:Double)

class LabeledPoint(x:Double,y:Double,val label:String)extends Point(x,y){
  override def toString()="%s position: (%f,%f)".format(label,x,y)
}

val lp=new LabeledPoint(100,200,"china")
println(lp)

