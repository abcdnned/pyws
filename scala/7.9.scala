import java.lang.System._
import io.StdIn.readLine

val user=getProperty("user.name")
val password=readLine
println(user)
println(password)

if(password!="secret")
  err.println("error")
else
  println("hello there")
