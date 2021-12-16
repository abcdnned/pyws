class BankAccount(initialBalance: Double) {
	private var balance = initialBalance
	def deposit(amount: Double) = { balance += amount; balance }
	def withdraw(amount: Double) = { balance -= amount; balance }
}
class Fee (initialBalance:Double) extends BankAccount(initialBalance){
  override def deposit(amount:Double)=super.deposit(amount-1)
  override def withdraw(amount:Double)=super.withdraw(amount+1)
} 

val fee=new Fee(100)
println(fee.withdraw(10))
println(fee.deposit(10))

class SavingsAccount(initialBalance:Double) extends Fee(initialBalance){
  private var freetime:Int=3
  override def deposit(amount:Double)={
    if(freetime>0){
      freetime-=1
      super.deposit(amount+1)
    }else{
      super.deposit(amount)
    }
  }
  override def withdraw(amount:Double)={
    if(freetime>0){
      freetime-=1
      super.withdraw(amount-1)
    }else{
      super.withdraw(amount)
    }
  }
    
  def earnMonthlyInterest()={
    freetime=3
    super.deposit(2)
  }
}

val savings=new SavingsAccount(100)
println(savings.deposit(10))
println(savings.withdraw(10))
println(savings.deposit(10))
println(savings.withdraw(10))
println(savings.earnMonthlyInterest())
println(savings.deposit(10))
println(savings.withdraw(10))
println(savings.deposit(10))

