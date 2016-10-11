import java.util.{HashMap => JavaHashMap, Map => JavaMap}
import scala.collection.mutable.HashMap
import collection.JavaConversions.mapAsScalaMap

val map=new JavaHashMap[Int,Int]

map.put(1,1)
map.put(2,2)

val smap=new HashMap[Int,Int]

map.foreach(kv=>smap.put(kv._1,kv._2))
println(smap)
