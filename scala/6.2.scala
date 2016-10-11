abstract class UnitConversion{
  def convert(n:Int):Int
}
object InchesToCentimeters extends UnitConversion {
  override def convert(n:Int)={
    n*30
  }
}
object GallonsToLiters extends UnitConversion{
  override def convert(n:Int)={
    n*4
  }
}
object MilesToKilometers extends UnitConversion{
  override def convert(n:Int)={
    n*3
  }
}

println(InchesToCentimeters.convert(3))
println(GallonsToLiters.convert(3))
println(MilesToKilometers.convert(3))
