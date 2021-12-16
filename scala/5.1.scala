class Counter{
    private var value=Int.MaxValue
    def increment(){
    if(value!=Int.MaxValue){
    value+=1}}
    def current = value
}
val counter=new Counter
print(counter.current)
counter.increment()
print(counter.current)
