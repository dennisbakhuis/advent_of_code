const INPUT_DATA: &str = include_str!("../../../data/15_lens_library.txt");
// const INPUT_DATA: &str = "\
// rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
// ";

const MULTIPLIER: usize = 17;

fn hash_algorithm(input: &str) -> u8 {
    let mut current_value: usize = 0;

    for c in input.chars() {
        let ascii_code = c as usize;
        current_value = (current_value + ascii_code) * MULTIPLIER;
        current_value %= 256;
    }

    current_value as u8
}

fn main() {
    // split INPUT_DATA into a vector of strings by comma and remove the new line character
    let list_of_strings: Vec<String> = INPUT_DATA
        .replace('\n', "")
        .split(',')
        .map(String::from)
        .collect();

    let mut total_sum = 0;

    for s in list_of_strings {
        let value = hash_algorithm(&s);
        println!("{} --> {}", s, value);

        total_sum += value as usize;
    }

    println!("Total sum: {}", total_sum);
}
