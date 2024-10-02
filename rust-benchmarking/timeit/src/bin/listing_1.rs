use std::fs::File;
use std::io::Read;

fn candidate() {
    let mut buf = String::new();
    File::open("numbers.dat").unwrap().read_to_string(&mut buf).unwrap();
}

fn doohickey() {
    let mut buf = String::new();
    File::open("numbers.dat").unwrap().read_to_string(&mut buf).unwrap();
}

type F = fn();

fn bench_function(name: &str, f: F) {
    let begin = std::time::Instant::now();
    f();
    let elapsed = begin.elapsed().as_nanos();
    println!("{name} {elapsed}");
}

fn main() {
    bench_function("old", doohickey);
    bench_function("new", candidate);
}