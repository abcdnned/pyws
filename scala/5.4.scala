import beans.BeanProperty

class Student{
  @BeanProperty var name:String ="no name"
  @BeanProperty var id:Long = 0
}
val s1=new Student
print(s1.name)
print(s1.id)
s1.id=2
print(s1.id)
print(s1.getName)
