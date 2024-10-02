fn doohickey() -> usize {
    1337
}

fn main() {
    let begin = std::time::Instant::now();
    std::hint::black_box(doohickey());
    let elapsed = begin.elapsed().as_nanos();
    println!("doohickey {elapsed}");
}