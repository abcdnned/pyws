class Time(private var hours:Int ,private var minute:Int){
    hours=hours min 24
    minute=minute min 60
    private var time=hours*60+minute
    def hrs=time/60
    def min=time%60
    def before(other:Time)=time<other.time
}
val morning=new Time(24,0)
val evening=new Time(25,10)
println(evening.hrs)
println(morning.before(evening))
