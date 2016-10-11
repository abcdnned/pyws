import collection.mutable.ArrayBuffer
import java.io._

class Person(val name:String) extends Serializable{
    val friends:ArrayBuffer[Person] = new ArrayBuffer[Person]

    def makeFriendsWith(person:Person) = friends += person
    
    override def toString() = "%s {%s}".format(name,friends.map(_.name).mkString(","))
}

object Main extends App{
    val tom = new Person("tom")
    val frank = new Person("frank")
    val jerry = new Person("jerry")

    tom makeFriendsWith frank
    tom makeFriendsWith jerry
    frank makeFriendsWith tom
    frank makeFriendsWith jerry
    jerry makeFriendsWith tom
    jerry makeFriendsWith frank

    val all = Array(tom,jerry,frank)
    all.foreach(print _)
    println()

    val out = new ObjectOutputStream(new FileOutputStream("9.10.txt"))
    out.writeObject(all)
    out.flush()
    out.close()
    val in = new ObjectInputStream(new FileInputStream("9.10.txt"))
    val saved = in.readObject().asInstanceOf[Array[Person]]
    saved.foreach(print _)
}
