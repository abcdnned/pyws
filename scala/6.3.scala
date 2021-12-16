import java.awt.Point

object Origin extends Point{
  def foo(){
    println("foo")
  }
}

Origin.foo()
println(Origin.getX())
println(Origin)
