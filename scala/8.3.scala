abstract class animal{
  def say
}
class dog extends animal{
  def say(){
    println("wang")
  }
}
class cat extends animal{
  def say(){
    println("miao")
  }
}
val frank=new dog
frank.say
val tom=new cat
tom.say
