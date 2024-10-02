static mut COUNTER: usize = 0;

fn doohickey() {
    unsafe { COUNTER += 1; }
}

fn main() {
    let mut total_time = 0;
    for _ in 0..640_000 {
        let begin = std::time::Instant::now();
        doohickey();
        let elapsed = begin.elapsed().as_nanos();
        total_time += elapsed;
    }
    println!("{total_time}");
}