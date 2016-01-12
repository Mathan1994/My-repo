

object Pattern1 {
   def main(args: Array[String]) {
   	val alice = new Person("Alice", 25)
	   val bob = new Person("Bob", 32)
   	val charlie = new Person("Charlie", 32)
   
      for (person <- List(alice, bob, charlie)) {
         person match {
            case Person("Alice", 25) => println("Hi Alice!")
            case Person(name, age) =>
               println("Age: " + age + " year, name: " + name + "?")
         }
      }
   }
   // case class, empty one.
   case class Person(name: String, age: Int)
}
