// Problem: Old Magician
// Language: Groovy
// Author: KirarinSnow
// Usage: groovy thisfile.groovy <input.in >output.out


reader = System.in.newReader()

def compute = {
    b = reader.readLine().split()[1].toInteger()
    b % 2 == 1 ? "BLACK" : "WHITE"    
}

(1..reader.readLine().toInteger()).each {
    println "Case #" + it + ": " + compute()
}
