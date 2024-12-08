const INPUT_DATA: &str = include_str!("../../../data/16_floor_is_lava.txt");

// const INPUT_DATA: &str = r#".|...\....
// |.-.\.....
// .....|-...
// ........|.
// ..........
// .........\
// ..../.\\..
// .-.-/..|..
// .|....-|.\
// ..//.|....
// "#;

#[derive(Debug, Clone)]
struct Cell {
    x: usize,
    y: usize,
    value: char,
    energized: bool,
}

#[derive(Debug, Clone)]
struct Contraption {
    cells: Vec<Vec<Cell>>,
    width: usize,
    height: usize,
}

impl Contraption {
    fn new(input_data: &str) -> Self {
        let mut cells: Vec<Vec<Cell>> = vec![];
        let mut width = 0;
        let mut height = 0;
        for (y, line) in input_data.lines().enumerate() {
            let mut row: Vec<Cell> = vec![];
            for (x, value) in line.chars().enumerate() {
                row.push(Cell {
                    x,
                    y,
                    value,
                    energized: false,
                });
            }
            cells.push(row);
            height += 1;
        }
        width = cells[0].len();
        Self {
            cells,
            width,
            height,
        }
    }

    fn print(&self) {
        for row in &self.cells {
            for cell in row {
                print!("{}", cell.value);
            }
            println!();
        }
    }

    fn count_energized(&self) -> usize {
        let mut count = 0;
        for row in &self.cells {
            for cell in row {
                if cell.energized {
                    count += 1;
                }
            }
        }
        count
    }
}

#[derive(Debug, PartialEq, Clone, Copy)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

#[derive(Debug, PartialEq, Clone, Copy)]
struct LaserBeam {
    x: isize,
    y: isize,
    direction: Direction,
}

fn get_number_energized_cells(
    input_contraption: &Contraption,
    input_laser_beam: &LaserBeam,
) -> usize {
    let mut contraption = input_contraption.clone();

    let mut laser_beams: Vec<LaserBeam> = vec![input_laser_beam.clone()];
    let mut already_added: Vec<LaserBeam> = vec![];

    loop {
        if laser_beams.is_empty() {
            break;
        }

        let mut current_laser_beam = laser_beams.pop().unwrap();
        let mut already_on_path: Vec<LaserBeam> = vec![];

        loop {
            // check if laser_beam is out of bounds
            if current_laser_beam.x >= (contraption.width as isize)
                || current_laser_beam.y >= (contraption.height as isize)
                || current_laser_beam.x < 0
                || current_laser_beam.y < 0
            {
                break;
            }

            // check if laser_beam was already on path
            if already_on_path.contains(&current_laser_beam) {
                break;
            }
            already_on_path.push(current_laser_beam);

            let (cx, cy) = (current_laser_beam.x as usize, current_laser_beam.y as usize);
            contraption.cells[cy][cx].energized = true;
            let cell_char = contraption.cells[cy][cx].value;

            match current_laser_beam.direction {
                Direction::Up => {
                    if cell_char == '|' || cell_char == '.' {
                        current_laser_beam.y -= 1;
                    } else if cell_char == '-' {
                        let new_beam = LaserBeam {
                            x: current_laser_beam.x + 1,
                            y: current_laser_beam.y,
                            direction: Direction::Right,
                        };
                        if !already_added.contains(&new_beam) {
                            laser_beams.push(new_beam);
                            already_added.push(new_beam);
                        }
                        current_laser_beam.x -= 1;
                        current_laser_beam.direction = Direction::Left;
                    } else if cell_char == '\\' {
                        current_laser_beam.x -= 1;
                        current_laser_beam.direction = Direction::Left;
                    } else if cell_char == '/' {
                        current_laser_beam.x += 1;
                        current_laser_beam.direction = Direction::Right;
                    }
                }
                Direction::Down => {
                    if cell_char == '|' || cell_char == '.' {
                        current_laser_beam.y += 1;
                    } else if cell_char == '-' {
                        let new_beam = LaserBeam {
                            x: current_laser_beam.x - 1,
                            y: current_laser_beam.y,
                            direction: Direction::Left,
                        };
                        if !already_added.contains(&new_beam) {
                            laser_beams.push(new_beam);
                            already_added.push(new_beam);
                        }
                        current_laser_beam.x += 1;
                        current_laser_beam.direction = Direction::Right;
                    } else if cell_char == '\\' {
                        current_laser_beam.x += 1;
                        current_laser_beam.direction = Direction::Right;
                    } else if cell_char == '/' {
                        current_laser_beam.x -= 1;
                        current_laser_beam.direction = Direction::Left;
                    }
                }
                Direction::Left => {
                    if cell_char == '|' {
                        let new_beam = LaserBeam {
                            x: current_laser_beam.x,
                            y: current_laser_beam.y + 1,
                            direction: Direction::Down,
                        };
                        if !already_added.contains(&new_beam) {
                            laser_beams.push(new_beam);
                            already_added.push(new_beam);
                        }
                        current_laser_beam.y -= 1;
                        current_laser_beam.direction = Direction::Up;
                    } else if cell_char == '-' || cell_char == '.' {
                        current_laser_beam.x -= 1;
                    } else if cell_char == '\\' {
                        current_laser_beam.y -= 1;
                        current_laser_beam.direction = Direction::Up;
                    } else if cell_char == '/' {
                        current_laser_beam.y += 1;
                        current_laser_beam.direction = Direction::Down;
                    }
                }
                Direction::Right => {
                    if cell_char == '|' {
                        let new_beam = LaserBeam {
                            x: current_laser_beam.x,
                            y: current_laser_beam.y + 1,
                            direction: Direction::Down,
                        };
                        if !already_added.contains(&new_beam) {
                            laser_beams.push(new_beam);
                            already_added.push(new_beam);
                        }
                        current_laser_beam.y -= 1;
                        current_laser_beam.direction = Direction::Up;
                    } else if cell_char == '-' || cell_char == '.' {
                        current_laser_beam.x += 1;
                    } else if cell_char == '\\' {
                        current_laser_beam.y += 1;
                        current_laser_beam.direction = Direction::Down;
                    } else if cell_char == '/' {
                        current_laser_beam.y -= 1;
                        current_laser_beam.direction = Direction::Up;
                    }
                }
            }
        }
    }

    contraption.count_energized()
}

fn main() {
    let mut contraption = Contraption::new(INPUT_DATA);

    // create vector of laser beams to test, from all boundaries of the contraption
    let mut laser_beams: Vec<LaserBeam> = vec![];
    for x in 0..contraption.width {
        laser_beams.push(LaserBeam {
            x: x as isize,
            y: 0,
            direction: Direction::Down,
        });
        laser_beams.push(LaserBeam {
            x: x as isize,
            y: (contraption.height - 1) as isize,
            direction: Direction::Up,
        });
    }
    for y in 0..contraption.height {
        laser_beams.push(LaserBeam {
            x: 0,
            y: y as isize,
            direction: Direction::Right,
        });
        laser_beams.push(LaserBeam {
            x: (contraption.width - 1) as isize,
            y: y as isize,
            direction: Direction::Left,
        });
    }

    let energized_count: Vec<usize> = laser_beams
        .iter()
        .map(|laser_beam| get_number_energized_cells(&contraption, &laser_beam))
        .collect();

    let max_energized_count = energized_count.iter().max().unwrap();
    println!("Max energized count: {}", max_energized_count);
}
