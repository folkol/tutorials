use std::time::Instant;

fn timeit(f: fn() -> ()) -> u128 {
    let begin = Instant::now();
    f();
    begin.elapsed().as_nanos()
}

fn main() {
    eprintln!("old: {}", timeit(old_func));
    eprintln!("new: {}", timeit(new_func));
}

fn new_func() {
    println!("Hello, world!");
}

fn old_func() {
    println!("Hello, world!");
}

