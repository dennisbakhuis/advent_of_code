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

#[derive(Debug)]
struct Cell {
    x: usize,
    y: usize,
    value: char,
    energized: bool,
}

#[derive(Debug)]
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

fn main() {
    let mut contraption = Contraption::new(INPUT_DATA);

    let laser_beam = LaserBeam {
        x: 0,
        y: 0,
        direction: Direction::Right,
    };

    let mut laser_beams: Vec<LaserBeam> = vec![laser_beam];
    let mut already_added: Vec<LaserBeam> = vec![];

    loop {
        if laser_beams.is_empty() {
            break;
        }

        println!("New laser beam");
        let mut current_laser_beam = laser_beams.pop().unwrap();
        loop {
            println!(
                "x: {}, y: {}, direction: {:?}",
                current_laser_beam.x, current_laser_beam.y, current_laser_beam.direction,
            );

            // check if laser_beam is out of bounds
            if current_laser_beam.x >= (contraption.width as isize)
                || current_laser_beam.y >= (contraption.height as isize)
                || current_laser_beam.x < 0
                || current_laser_beam.y < 0
            {
                println!("Out of bounds");
                break;
            }

            let (cx, cy) = (current_laser_beam.x as usize, current_laser_beam.y as usize);
            contraption.cells[cy][cx].energized = true;
            let cell_char = contraption.cells[cy][cx].value;
            println!("cell_char: {}", cell_char);

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

    let energized_count = contraption.count_energized();
    println!("Energized count: {}", energized_count);
}
