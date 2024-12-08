const INPUT_DATA: &str = include_str!("../../../data/14_parabolic_dish.txt");
// const INPUT_DATA: &str = "\
// O....#....
// O.OO#....#
// .....##...
// OO.#O....O
// .O.....O#.
// O.#..O.#.#
// ..O..#O..O
// .......O..
// #....###..
// #OO..#....
// ";

const NUMBER_OF_CYCLES: usize = 1_000_000_000;

#[derive(Debug, PartialEq, Clone, Copy)]
enum CellState {
    Empty,
    Stone,
    Wall,
}

#[allow(dead_code)]
#[derive(Debug, PartialEq)]
enum Direction {
    North,
    East,
    South,
    West,
}

#[allow(dead_code)]
#[derive(Debug, PartialEq, Clone, Copy)]
struct Cell {
    x: usize,
    y: usize,
    state: CellState,
}

#[allow(dead_code)]
impl Cell {
    fn new(x: usize, y: usize, state: CellState) -> Self {
        Cell { x, y, state }
    }

    fn from_char(x: usize, y: usize, c: char) -> Self {
        let state = match c {
            'O' => CellState::Stone,
            '#' => CellState::Wall,
            _ => CellState::Empty,
        };
        Cell::new(x, y, state)
    }

    fn get_char(&self) -> char {
        match self.state {
            CellState::Empty => '.',
            CellState::Stone => 'O',
            CellState::Wall => '#',
        }
    }
}

struct Grid {
    cells: Vec<Vec<Cell>>,
    width: usize,
    height: usize,
}

#[allow(dead_code)]
impl Grid {
    fn from_input(input: &str) -> Self {
        let lines: Vec<&str> = input.trim().split('\n').collect();
        let height = lines.len();
        let width = lines[0].len();
        let mut cells = Vec::with_capacity(height);

        for (y, line) in lines.iter().enumerate() {
            let mut row = Vec::with_capacity(width);
            for (x, c) in line.chars().enumerate() {
                row.push(Cell::from_char(x, y, c));
            }
            cells.push(row);
        }

        Grid {
            cells,
            width,
            height,
        }
    }

    fn print_grid(&self) {
        for row in &self.cells {
            for cell in row {
                print!("{}", cell.get_char());
            }
            println!();
        }
    }

    fn tilt_grid(&mut self, direction: Direction) {
        // First need to determine the order of cells to move
        match direction {
            Direction::North => {
                for x in 0..self.width {
                    for y in 1..self.height {
                        self.move_cell(x, y, &direction);
                    }
                }
            }
            Direction::South => {
                for x in 0..self.width {
                    for y in (0..self.height - 1).rev() {
                        self.move_cell(x, y, &direction);
                    }
                }
            }
            Direction::East => {
                for y in 0..self.height {
                    for x in (0..self.width - 1).rev() {
                        self.move_cell(x, y, &direction);
                    }
                }
            }
            Direction::West => {
                for y in 0..self.height {
                    for x in 1..self.width {
                        self.move_cell(x, y, &direction);
                    }
                }
            }
        }
    }

    fn move_cell(&mut self, x: usize, y: usize, direction: &Direction) {
        // Move stone in the given direction
        let (mut next_x, mut next_y) = (x, y);
        match direction {
            Direction::North => {
                while next_y > 0 && self.cells[next_y - 1][next_x].state == CellState::Empty {
                    next_y -= 1;
                }
            }
            Direction::South => {
                while next_y < self.height - 1
                    && self.cells[next_y + 1][next_x].state == CellState::Empty
                {
                    next_y += 1;
                }
            }
            Direction::East => {
                while next_x < self.width - 1
                    && self.cells[next_y][next_x + 1].state == CellState::Empty
                {
                    next_x += 1;
                }
            }
            Direction::West => {
                while next_x > 0 && self.cells[next_y][next_x - 1].state == CellState::Empty {
                    next_x -= 1;
                }
            }
        }
        if (next_x, next_y) != (x, y) && self.cells[y][x].state == CellState::Stone {
            self.cells[next_y][next_x].state = CellState::Stone;
            self.cells[y][x].state = CellState::Empty;
        }
    }

    fn calculate_load(&self) -> usize {
        let stones_per_row = self
            .cells
            .iter()
            .map(|row| {
                row.iter()
                    .filter(|cell| cell.state == CellState::Stone)
                    .count()
            })
            .collect::<Vec<usize>>();

        let score = stones_per_row
            .iter()
            .enumerate()
            .map(|(i, count)| (self.height - i) * count)
            .sum();

        score
    }

    fn cycle(&mut self) {
        self.tilt_grid(Direction::North);
        self.tilt_grid(Direction::West);
        self.tilt_grid(Direction::South);
        self.tilt_grid(Direction::East);
    }

    fn perform_n_cycles(&mut self, number_of_cycles: usize) {
        // doing all cylces is impossible, probably need to find a cycle pattern
        let mut patterns = vec![self.cells.clone()];
        let mut final_index = 0;

        for _ in 0..number_of_cycles {
            self.cycle();

            if let Some(index) = patterns.iter().position(|x| x == &self.cells) {
                let length_of_cycle = patterns.len() - index;
                final_index = index + (number_of_cycles - index) % length_of_cycle;
                break;
            }

            patterns.push(self.cells.clone());
        }

        self.cells = patterns[final_index].clone();
    }
}

fn main() {
    let mut grid = Grid::from_input(INPUT_DATA);
    // grid.print_grid();
    // println!();

    grid.perform_n_cycles(NUMBER_OF_CYCLES);

    // println!();
    // grid.print_grid();
    // println!();

    let score = grid.calculate_load();
    println!("score: {:?}", score);
}
