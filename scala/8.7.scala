import java.awt.Rectangle
class Square(x:Int,y:Int,length:Int)extends Rectangle(x,y,length,length){
  def this(len:Int)=this(0,0,len)
  def this()=this(0)
  override def toString()="%d %d %d".format(x,y,length)
}

val sq3=new Square(3,2,1)
println(sq3)

