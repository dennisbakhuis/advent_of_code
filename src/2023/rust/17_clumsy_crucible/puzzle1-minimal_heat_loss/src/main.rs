// const INPUT_DATA: &str = include_str!("../../../data/17_clumsy_crucible.txt");

const INPUT_DATA: &str = "\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
";

fn create_vector_map_from_input(input_data: &str) -> Vec<Vec<usize>> {
    let mut cells: Vec<Vec<usize>> = vec![];
    for line in input_data.lines() {
        let mut row: Vec<usize> = vec![];
        for character in line.chars() {
            let number = character.to_digit(10).unwrap() as usize;
            row.push(number);
        }
        cells.push(row);
    }
    cells
}

fn print_vector_map(vector_map: &Vec<Vec<usize>>) {
    for row in vector_map {
        for cell in row {
            print!("{}", cell);
        }
        println!();
    }
}

fn test_last_elements(elements: &Vec<char>, character: char) -> bool {
    elements.len() >= 3 && elements[elements.len() - 3..].iter().all(|&c| c == character)
}


fn main() {
    let heat_map = create_vector_map_from_input(INPUT_DATA);
    let (rows, columns) = (heat_map.len(), heat_map[0].len());
    println!("rows: {}, columns: {}", rows, columns);
    print_vector_map(&heat_map);
    println!();

    let mut visited = vec![vec![false; columns]; rows];
    let mut distance = vec![vec![usize::MAX; columns]; rows];
    distance[0][0] = 0;

    let (mut current_row, mut current_column) = (0, 0);

    while (current_row, current_column) != (rows - 1, columns - 1) {
        // check left
        if current_column > 0 && !visited[current_row][current_column - 1] {
            let new_distance = distance[current_row][current_column]
                + heat_map[current_row][current_column - 1];

            if new_distance < distance[current_row][current_column - 1] {
                distance[current_row][current_column - 1] = new_distance;
            }
        }

        // check right
        if current_column < columns - 1 && !visited[current_row][current_column + 1] {
            let new_distance = distance[current_row][current_column]
                + heat_map[current_row][current_column + 1];
            if new_distance < distance[current_row][current_column + 1] {
                distance[current_row][current_column + 1] = new_distance;
            }
        }

        // check up
        if current_row > 0 && !visited[current_row - 1][current_column] {
            let new_distance = distance[current_row][current_column]
                + heat_map[current_row - 1][current_column];
            if new_distance < distance[current_row - 1][current_column] {
                distance[current_row - 1][current_column] = new_distance;
            }
        }

        // check down
        if current_row < rows - 1 && !visited[current_row + 1][current_column] {
            let new_distance = distance[current_row][current_column]
                + heat_map[current_row + 1][current_column];
            if new_distance < distance[current_row + 1][current_column] {
                distance[current_row + 1][current_column] = new_distance;
            }
        }

        visited[current_row][current_column] = true;

        // find coordinates of non-visited cell with the smallest distance
        let mut min_distance = usize::MAX;
        for row in 0..rows {
            for column in 0..columns {
                if !visited[row][column] && distance[row][column] < min_distance {
                    min_distance = distance[row][column];
                    current_row = row;
                    current_column = column;
                }
            }
        }
    }

    // back track to find the path
    let mut path = vec![];
    let (mut current_row, mut current_column) = (rows - 1, columns - 1);
    path.push((current_row, current_column));
    let mut elements: Vec<char> = vec![];

    while (current_row, current_column) != (0, 0) {
        let current_distance = distance[current_row][current_column];
        // check left
        if current_column > 0 && distance[current_row][current_column - 1] < current_distance && !test_last_elements(&elements, 'L') {
            current_column -= 1;
            elements.push('L');
        }
        // check right
        else if current_column < columns - 1
            && distance[current_row][current_column + 1] < current_distance && !test_last_elements(&elements, 'R')
        {
            current_column += 1;
            elements.push('R');
        }
        // check up
        else if current_row > 0 && distance[current_row - 1][current_column] < current_distance && !test_last_elements(&elements, 'U') {
            current_row -= 1;
            elements.push('U');
        }
        // check down
        else if current_row < rows - 1
            && distance[current_row + 1][current_column] < current_distance && !test_last_elements(&elements, 'D')
        {
            current_row += 1;
            elements.push('D');
        }
        path.push((current_row, current_column));
    }

    // Draw map and calculate heat loss
    let mut heat_loss = 0;
    let mut new_heat_str = INPUT_DATA.to_string();
    for (row, column) in path.iter().rev() {
        new_heat_str.replace_range(
            row * (columns + 1) + column..row * (columns + 1) + column + 1,
            "X",
        );
        heat_loss += heat_map[*row][*column];
    }
    println!("{}", new_heat_str);

    println!("Heat loss: {}", heat_loss);
}
