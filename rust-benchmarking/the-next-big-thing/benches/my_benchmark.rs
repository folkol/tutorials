use criterion::{criterion_group, criterion_main, Criterion};
use the_next_big_thing::{candidate, doohickey};

fn benches(criterion: &mut Criterion) {
    let mut group = criterion.benchmark_group("doohickey");
    group.bench_function("old", |bencher| bencher.iter(doohickey));
    group.bench_function("new", |bencher| bencher.iter(candidate));
    group.finish()
}

criterion_group!(my_config_group, benches);
criterion_main!(my_config_group);

