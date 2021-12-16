class BankAccount{
    private var balance=0
    def current=balance
    def deposit(ammount:Int){
        balance+=ammount
    }
    def withdraw(ammount:Int):Int={
        var r=0
        if(balance>=ammount){
            balance-=ammount
            r=ammount
            return r
        }
        r
    }
}

val account=new BankAccount
print(account.current)
account.deposit(100)
print(account.current)
print(account.withdraw(50))
print(account.current)

var a=1
a="fdsafdsafa"
println(a)
