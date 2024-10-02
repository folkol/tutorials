use std::fs::File;
use std::io::Read;

fn candidate() {
    for _ in 0..4 {
        let mut buf = String::new();
        File::open("numbers.dat").unwrap().read_to_string(&mut buf).unwrap();
    }
}

fn doohickey() {
    for _ in 0..4 {
        let mut buf = String::new();
        File::open("numbers.dat").unwrap().read_to_string(&mut buf).unwrap();
    }
}

type F = fn();

const N: u128 = 1000;

fn bench_function(name: &str, f: F) {
    for _ in 0..N {
        std::hint::black_box(f());
    }
    let begin = std::time::Instant::now();
    for _ in 0..N {
        std::hint::black_box(f());
    }
    let elapsed = begin.elapsed().as_nanos();
    let average_time = elapsed / N;
    println!("{name} {average_time}");
}

fn main() {
    bench_function("old", doohickey);
    bench_function("new", candidate);
}