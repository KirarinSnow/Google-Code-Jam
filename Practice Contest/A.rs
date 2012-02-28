// Problem: Old Magician
// Language: Rust
// Author: KirarinSnow
// Usage: rustc thisfile.rs -o executable && ./executable <input.in >output.out


use std;
import std::io;
import std::io::reader_util;

fn main() {
  let s = io::stdin();
  let t = int::from_str(s.read_line());
  let i = 0;
  while i < t {
    i = i + 1;
    let b = int::from_str(str::split_str(s.read_line(), " ")[1]);
    let out;
    if b % 2 == 1 {out = "BLACK"} else {out = "WHITE"}
    std::io::println(#fmt("Case #%d: %s", i, out));
  }
}
