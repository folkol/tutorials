#[inline(never)]
fn doohickey() -> usize {
    std::hint::black_box(1337)
}

fn main() {
    let begin = std::time::Instant::now();
    doohickey();
    let elapsed = begin.elapsed().as_nanos();
    println!("doohickey {elapsed}");
}