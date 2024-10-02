fn candidate() -> u32 {
    1337 + 1
}

fn doohickey() -> u32 {
    1337
}

type F = fn() -> u32;

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
    assert_eq!(doohickey(), candidate());
    bench_function("old", doohickey);
    bench_function("new", candidate);
}