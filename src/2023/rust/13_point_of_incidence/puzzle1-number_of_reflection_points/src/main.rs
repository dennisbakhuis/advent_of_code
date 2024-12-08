use std::cmp::min;

const INPUT_DATA: &str = include_str!("../../../data/13_mirrors.txt");
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

#[derive(Debug, PartialEq)]
enum Direction {
    Horizontal,
    Vertical,
}

#[derive(Debug)]
struct Reflection {
    first: usize,
    // second: usize,
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

fn find_neighbors(lines: Vec<String>) -> Option<(usize, usize)> {
    let n = lines.len();
    for ix in 0..n - 1 {
        if lines[ix] == lines[ix + 1] {
            let backwards_n = min(ix, n - ix - 2);
            let mut is_ok = true;

            for ix2 in 1..backwards_n + 1 {
                // boundaries are not inclusive
                if lines[ix - ix2] != lines[ix + ix2 + 1] {
                    is_ok = false;
                    break;
                }
            }
            if is_ok {
                return Some((ix, ix + 1));
            }
        }
    }
    None
}

fn find_reflection_in_mirror(mirror: &Mirror) -> Option<Reflection> {
    // first try to find a horizontal reflection
    if let Some((start, _)) = find_neighbors(mirror.rows().to_vec()) {
        return Some(Reflection {
            first: start,
            // second: end,
            direction: Direction::Horizontal,
        });
    }

    // then try to find a vertical reflection
    if let Some((start, _)) = find_neighbors(mirror.cols().to_vec()) {
        return Some(Reflection {
            first: start,
            // second: end,
            direction: Direction::Vertical,
        });
    }

    None
}

fn main() {
    let mirrors: Vec<Mirror> = INPUT_DATA.split("\n\n").map(Mirror::new).collect();

    let reflections: Vec<Reflection> = mirrors
        .iter()
        .filter_map(find_reflection_in_mirror)
        .collect();

    let score = reflections.iter().map(|r| r.score()).sum::<usize>();

    println!("score: {:?}", score);
}
