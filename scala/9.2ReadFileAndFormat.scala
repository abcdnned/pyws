import io.Source
import java.io.PrintWriter
val source=Source.fromFile("9.2.txt")
val out=new PrintWriter("9.2.out.txt")
val lines=source.getLines
for(line<-lines){
  val its=line.split(",")
  val sb=new StringBuilder()
  for(it<-its) sb.append(String.format("%10s",it))
  out.println(sb.toString())
}
out.flush
out.close
source.close

/**
import io.Source
//from file
val source=Source.fromFile("input")
//from string
val source=Source.fromString("hello world")
//read lines
val lines=Source.getLines
//to array
val arr=lines.toArray[String]
//iter char
for(c <- source) c match{
  case '\t' => ...
  case _ => ...
}
//peek next char
val iter=source.buffered
while(iter.hasNext) print(iter.head)
//read whole file to string
val content = source.mkString
**/
