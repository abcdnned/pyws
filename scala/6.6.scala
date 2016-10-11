object Pork extends Enumeration{
  val Black,Flower,Square=Value
  override def toString()={
    "heart,black,Flower,Square"
  }
  val Heart=Value("hh")
}

println(Pork.toString())
println(Pork.Heart)
println(Pork.Heart.id)
