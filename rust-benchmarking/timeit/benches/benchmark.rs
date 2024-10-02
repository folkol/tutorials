use criterion::{BenchmarkId, Criterion};
use timeit::doohickey;

fn main() {
    let mut criterion = Criterion::default();
    for i in 1..10 {
        criterion.bench_with_input(
            BenchmarkId::new("doohickey", i),
            &i,
            |bencher, &input| bencher.iter(|| doohickey(input)),
        );
    }
    criterion.final_summary();
}