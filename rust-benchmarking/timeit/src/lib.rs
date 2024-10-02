static FOO: [&str; 2] = ["Hello", "world!"];

pub fn candidate(input: i32) -> bool {
    // let mut buf = String::new();
    // File::open("numbers.dat").unwrap().read_to_string(&mut buf).unwrap();
    let mut ans = false;
    for _ in 0..(10 * 10) {
        ans |= std::hint::black_box(&FOO).contains(&"Wat?");
    }
    ans
}

pub fn doohickey(input: i32) -> bool {
    // let mut buf = String::new();
    // File::open("numbers.dat").unwrap().read_to_string(&mut buf).unwrap();
    let mut ans = false;
    for _ in 0..10 {
        ans |= std::hint::black_box(&FOO).contains(&"Wat?");
        ans |= std::hint::black_box(&FOO).contains(&"Wat?");
        ans |= std::hint::black_box(&FOO).contains(&"Wat?");
    }
    ans
}

