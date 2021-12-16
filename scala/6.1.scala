object Conversions{
  println("init object Conversions")
  def inchesToCentimeters(n:Int)={
    n*30
  }
  def gallonsToLiters(n:Int)={
    n*4
  }
  def milesToKilometers(n:Int)={
    n*2
  }
}

println(Conversions.inchesToCentimeters(3))
println(Conversions.gallonsToLiters(3))
println(Conversions.milesToKilometers(3))

