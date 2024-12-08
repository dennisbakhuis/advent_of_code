use std::collections::HashMap;

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

#[derive(Debug, PartialEq)]
enum Command {
    Remove,
    Insert,
}

struct Lens {
    label: String,
    focal_length: u8,
}

fn main() {
    let list_of_strings: Vec<String> = INPUT_DATA
        .replace('\n', "")
        .split(',')
        .map(String::from)
        .collect();

    // create all 256 boxes
    let mut boxes: HashMap<u8, Vec<Lens>> = HashMap::new();
    for i in 0..255 {
        boxes.insert(i, Vec::new());
    }

    for string in list_of_strings {
        // split string on '-' or '='
        let (label, focal_length_string) = string.split_once(|c| c == '-' || c == '=').unwrap();

        let command = match focal_length_string.len() {
            0 => Command::Remove,
            _ => Command::Insert,
        };

        let box_number = hash_algorithm(label);

        if command == Command::Remove {
            // remove lens from box
            if let Some(lens_box) = boxes.get_mut(&box_number) {
                if let Some(index) = lens_box.iter().position(|l| l.label == label) {
                    lens_box.remove(index);
                }
            }
        } else {
            // insert lens into box
            let focal_length: u8 = focal_length_string.parse().unwrap();
            if let Some(lens_box) = boxes.get_mut(&box_number) {
                if let Some(index) = lens_box.iter().position(|l| l.label == label) {
                    if let Some(current_lens) = lens_box.get_mut(index) {
                        current_lens.focal_length = focal_length;
                    }
                } else {
                    lens_box.push(Lens {
                        label: label.to_string(),
                        focal_length,
                    });
                }
            }
        }
    }

    // calculate focussing power
    let mut focussing_power: usize = 0;

    for ix in 0..255 {
        if let Some(lens_box) = boxes.get(&ix) {
            for (slot_number, lens) in lens_box.iter().enumerate() {
                focussing_power +=
                    (ix as usize + 1) * (slot_number + 1) * lens.focal_length as usize;
            }
        }
    }

    println!("focussing power: {}", focussing_power);
}
