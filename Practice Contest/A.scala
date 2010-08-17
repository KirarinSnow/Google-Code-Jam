// Problem: Old Magician
// Language: Scala
// Author: KirarinSnow
// Usage: scala thisfile.scala <input.in >output.out


def compute() =
    if (readLine.split(" ").apply(1).toInt % 2 == 1) {"BLACK"} else {"WHITE"}

for (i <- 1 to readInt) {
    println("Case #" + i + ": " + compute)
}
