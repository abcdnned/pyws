import collection.mutable.ArrayBuffer

abstract class Item{
  def price:Double
  def description:String
}
class SimpleItem(val price:Double,val description:String) extends Item{
  SimpleItem.allitems+=this
  override def toString()={
    description+" worth "+price
  }
}
object SimpleItem{
  val allitems=new ArrayBuffer[SimpleItem]
}
val wood=new SimpleItem(10,"wood")

val gold=new SimpleItem(100,"gold")

class Bundle{
  private val items=new ArrayBuffer[SimpleItem]
  def pack(item:SimpleItem){
    items+=item
  }
  override def toString()={
    var sum:Double=0
    for(i<-0 until items.length) sum+=items(i).price
    "items: %s || sum values: %f".format(items.map(i=>i.description).mkString(" "),sum)
  }
}

val bundle=new Bundle

for(i<-0 until SimpleItem.allitems.length) bundle.pack(SimpleItem.allitems(i))

println(bundle)
