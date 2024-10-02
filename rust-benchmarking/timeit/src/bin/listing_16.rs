use criterion::{criterion_group, criterion_main, Criterion};
use timeit::{candidate, doohickey};

fn benches(criterion: &mut Criterion) {
    let mut group = criterion.benchmark_group("doohickey");
    group.bench_function("old", |bencher| bencher.iter(doohickey));
    group.bench_function("new", |bencher| bencher.iter(candidate));
    group.finish()
}

criterion_group! {
    name = my_config_group;
    config = Criterion::default();
    targets = benches
}
criterion_main!(my_config_group);
