use std::cmp::min;

// const INPUT_DATA: &str = "\
// #.##..##.
// ..#.##.#.
// ##......#
// ##......#
// ..#.##.#.
// ..##..##.
// #.#.##.#.
//
// #...##..#
// #....#..#
// ..##..###
// #####.##.
// #####.##.
// ..##..###
// #....#..#
// ";

// const INPUT_DATA: &str = "\
// .#..#..####
// .#....#.###
// ...#####..#
// ##..#.#.###
// .####.###..
// .#.#..#####
// ##.##..##..
// ##.##..##..
// .#.#..#####
// ";

// const INPUT_DATA: &str = "\
// #..##...###
// #..##..#...
// #..##..#...
// #..##...###
// #####..#.##
// #.##..#####
// #..####.#.#
// .##.#.#.#..
// .....#####.
// ####..#####
// #..#.#.###.
// #..#.#..#.#
// #..#.##....
// ";

const INPUT_DATA: &str = include_str!("../../../data/13_mirrors.txt");

const NUMBER_OF_SMUDGES: usize = 1;

#[derive(Debug)]
struct Mirror {
    rows: Vec<String>,
    cols: Vec<String>,
}

impl Mirror {
    fn new(data: &str) -> Self {
        let rows: Vec<String> = data.lines().map(|s| s.to_string()).collect();
        let cols = (0..rows[0].len())
            .map(|i| rows.iter().map(|s| s.chars().nth(i).unwrap()).collect())
            .collect();
        Self { rows, cols }
    }
    fn rows(&self) -> &Vec<String> {
        &self.rows
    }
    fn cols(&self) -> &Vec<String> {
        &self.cols
    }
}

#[derive(Debug, PartialEq, Clone, Copy)]
enum Direction {
    Horizontal,
    Vertical,
}

#[derive(Debug, Clone, Copy)]
struct Reflection {
    first: usize,
    n_smudges: usize,
    direction: Direction,
}

impl Reflection {
    fn score(&self) -> usize {
        if self.direction == Direction::Horizontal {
            (self.first + 1) * 100
        } else {
            self.first + 1
        }
    }
}

fn is_one_char_diff(s1: &str, s2: &str) -> bool {
    if s1.len() != s2.len() {
        return false;
    }

    let mut differences = 0;

    for (c1, c2) in s1.chars().zip(s2.chars()) {
        if c1 != c2 {
            differences += 1;
            if differences > 1 {
                return false;
            }
        }
    }

    differences == 1
}

fn find_neighbors(
    lines: Vec<String>,
    number_of_smudges: usize,
    direction: Direction,
) -> Vec<Reflection> {
    let n = lines.len();
    let mut reflections: Vec<Reflection> = vec![];

    for ix in 0..n - 1 {
        if lines[ix] == lines[ix + 1] {
            let mut n_smudges = 0;
            let backwards_n = min(ix, n - ix - 2);
            let mut is_ok = true;

            for ix2 in 1..backwards_n + 1 {
                if lines[ix - ix2] != lines[ix + ix2 + 1] {
                    if n_smudges >= number_of_smudges {
                        is_ok = false;
                        break;
                    }

                    if !is_one_char_diff(&lines[ix - ix2], &lines[ix + ix2 + 1]) {
                        is_ok = false;
                        break;
                    }

                    n_smudges += 1;
                }
            }
            if is_ok {
                reflections.push(Reflection {
                    first: ix,
                    n_smudges,
                    direction,
                });
            }
        } else {
            if !is_one_char_diff(&lines[ix], &lines[ix + 1]) {
                continue;
            }

            let mut n_smudges = 1;
            let mut is_ok = true;

            // if n_smudges >= number_of_smudges {
            //     continue;
            // }
            //
            let backwards_n = min(ix, n - ix - 2);
            for ix2 in 1..backwards_n + 1 {
                if lines[ix - ix2] != lines[ix + ix2 + 1] {
                    if n_smudges >= number_of_smudges {
                        is_ok = false;
                        break;
                    }

                    if !is_one_char_diff(&lines[ix - ix2], &lines[ix + ix2 + 1]) {
                        is_ok = false;
                        break;
                    }

                    n_smudges += 1;
                }
            }
            if is_ok {
                reflections.push(Reflection {
                    first: ix,
                    n_smudges,
                    direction,
                });
            }
        }
    }
    reflections
}

fn find_reflection_with_smudges(mirror: &Mirror, smudged: bool) -> Vec<Reflection> {
    let number_of_smudges: usize = if smudged { NUMBER_OF_SMUDGES } else { 0 };

    println!(" set number of smudges: {:?}", number_of_smudges);

    let horizontal_reflections = find_neighbors(
        mirror.rows().to_vec(),
        number_of_smudges,
        Direction::Horizontal,
    );

    let vertical_reflections = find_neighbors(
        mirror.cols().to_vec(),
        number_of_smudges,
        Direction::Vertical,
    );

    let combined = [&horizontal_reflections[..], &vertical_reflections[..]].concat();

    println!("len: {:?}", combined.len());

    combined
}

fn find_reflection_in_mirror(mirror: &Mirror, smudged: bool) -> Reflection {
    // no_smudge is always a single reflection
    // let no_smudge = find_reflection_with_smudges(mirror, false)[0];
    let also_smudged = find_reflection_with_smudges(mirror, true);

    // if not smudged we are done
    if !smudged {
        let not_smudged = also_smudged.iter().find(|r| r.n_smudges == 0).unwrap();
        return not_smudged.clone();
    }

    let smudged = also_smudged.iter().find(|r| r.n_smudges > 0).unwrap();
    return smudged.clone();
}

fn main() {
    let mirrors: Vec<Mirror> = INPUT_DATA.split("\n\n").map(Mirror::new).collect();

    let reflections: Vec<Reflection> = mirrors
        .iter()
        .map(|x| find_reflection_in_mirror(x, false))
        .collect();

    let score = reflections.iter().map(|r| r.score()).sum::<usize>();

    println!("score: {:?}", score);

    println!("");
    println!("Smudged:");
    println!("");

    let smudged_reflections: Vec<Reflection> = mirrors
        .iter()
        .map(|x| find_reflection_in_mirror(x, true))
        .collect();

    let smudged_score = smudged_reflections.iter().map(|r| r.score()).sum::<usize>();

    println!("smudged_score: {:?}", smudged_score);
}
