package com{
  package horstmann{
    object Utils{
      def add(a:Int,b:Int)=a+b
    }
    package impatient{
      object Useage{
        def use(a:Int,b:Int)=Utils.add(a,b)
      }
    }
  }
}

package com.horstmann{
  package impatient{
    object Failure{
      def failuse(a:Int,b:Int)=Utils.add(a,b)
    }
  }
}

import com.horstmann.impatient._

object Q71 extends App{
  println(Useage.use(1,1))
  println(Failure.failuse(1,1))
}

