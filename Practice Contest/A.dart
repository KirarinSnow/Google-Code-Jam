// Problem: Old Magician
// Language: Dart
// Author: KirarinSnow
// Usage: dart thisfile.dart <input.in >output.out


#import('dart:io');

void main() {
  var stream = new StringInputStream(stdin);  
  stream.lineHandler = () {
    var line = stream.readLine();
    var t = Math.parseInt(line);
    for (var i = 1; i <= t; i++) {
      var b = Math.parseInt(stream.readLine().split(" ")[1]);
      print("Case #${i}: ${(b%2 == 0)?'WHITE':'BLACK'}");
    }
  };
}
