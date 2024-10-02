use criterion::Criterion;
use timeit::{candidate, doohickey};

fn main() {
    let mut criterion = Criterion::default().configure_from_args();
    let mut group = criterion.benchmark_group("doohickey");
    group.bench_function("old", |bencher| bencher.iter(doohickey));
    group.bench_function("new", |bencher| bencher.iter(candidate));
    group.finish();
}

fn make_input() {}