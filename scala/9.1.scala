import scala.io.Source
import java.io.PrintWriter
val source=Source.fromFile("9.1.txt")
val lines = source.getLines.toArray[String].reverse
val out=new PrintWriter("9.1.txt")
for(i<-0 until lines.length) out.println(lines(i))
out.flush
