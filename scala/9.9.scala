import java.io.File
def recursiveListFiles(f: File): Array[File] = {
  val these = f.listFiles
  these ++ these.filter(_.isDirectory).flatMap(recursiveListFiles)
}
val f=new File("D:/gitrepo/dcd/dcd-parser/target/classes/cn/com/netis/dcd/parser/huygens")
val files=recursiveListFiles(f)
print(files.count(_.getName.endsWith(".class")))
files.filter(_.getName.endsWith(".class")).foreach(print _)

