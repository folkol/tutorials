static FOO: [&str; 2] = ["Hello", "world!"];

pub fn candidate() -> bool {
    // let mut buf = String::new();
    // File::open("numbers.dat").unwrap().read_to_string(&mut buf).unwrap();
    let mut found = false;
    for word in std::hint::black_box(FOO) {
        if word == "Wat?" {
            found = true;
        }
    }
    found
}

pub fn doohickey(n: i32) -> bool {
    // let mut buf = String::new();
    // File::open("numbers.dat").unwrap().read_to_string(&mut buf).unwrap();
    for _ in 0..(n * n) {
        std::hint::black_box(&FOO).contains(&"Wat?")
    }
    std::hint::black_box(&FOO).contains(&"Wat?")
}

