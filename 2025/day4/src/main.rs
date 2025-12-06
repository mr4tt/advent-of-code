use std::fs;

fn main() {
    let rolls = parse_file();

    println!("{:?}", rolls);
    // part_one(rolls);
    part_two(rolls);
}

fn parse_file() -> Vec<Vec<char>> {
    let file_path = "input.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let grid = contents
                                    .lines()
                                    .map(|line| {
                                        line.chars().collect()
                                    })
                                    .collect();

    return grid;
}

fn part_one(rolls: Vec<Vec<char>>) {
    let mut ans = 0;
    let rows = rolls.len() as i32;
    let cols = rolls[0].len() as i32;

    // check if is 1) in bounds and 2) contains a roll of paper
    let is_valid = |x: i32, y: i32| -> bool {
        x < rows && x >= 0 && y < cols && y >= 0 && rolls[x as usize][y as usize] == '@'
    };

    // up, down, right, left
    // right down, right up, left down, left up
    let directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [1, 1], [-1, -1], [-1, 1]];
    for x in 0..rows {
        'inner: for y in 0..cols as i32 {
            if rolls[x as usize][y as usize] != '@' {
                continue
            }

            let curr = [x, y];
            let mut accessible = 0;

            for direction in directions {
                let new_x: i32 = curr[0] + direction[0];
                let new_y: i32 = curr[1] + direction[1];

                if is_valid(new_x, new_y) {
                    accessible += 1;
                }

                if accessible >= 4 {
                    continue 'inner
                }
            }

            ans += 1;
        }
    }

    println!("{ans}");
}

fn part_two(mut rolls: Vec<Vec<char>>) {
    let mut ans = 0;
    let mut edited;

    // keep removing rolls until you can't 
    loop {
        (rolls, edited) = check_rolls(&rolls);
        ans += edited;
        if edited == 0 {
            break
        }
    }

    println!("{ans}");

    // remove accessible paper rolls
    // return a rolls vector that include removed rolls and # of removed rolls
    fn check_rolls (rolls: &Vec<Vec<char>>) -> (Vec<Vec<char>>, i32) {
        let mut removed = 0;
        let rows = rolls.len() as i32;
        let cols = rolls[0].len() as i32;

        let mut new_rolls = rolls.clone();

        // check if is 1) in bounds and 2) contains a roll of paper
        let is_valid = |x: i32, y: i32| -> bool {
            x < rows && x >= 0 && y < cols && y >= 0 && rolls[x as usize][y as usize] == '@'
        };

        // up, down, right, left
        // right down, right up, left down, left up
        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [1, 1], [-1, -1], [-1, 1]];
        for x in 0..rows {
            'inner: for y in 0..cols {
                if rolls[x as usize][y as usize] != '@' {
                    continue
                }

                let curr = [x, y];
                let mut accessible = 0;

                for direction in directions {
                    let new_x: i32 = curr[0] + direction[0];
                    let new_y: i32 = curr[1] + direction[1];

                    if is_valid(new_x, new_y) {
                        accessible += 1;
                    }

                    if accessible >= 4 {
                        continue 'inner
                    }
                }
                // edit map to remove rolls
                new_rolls[x as usize][y as usize] = '.';
                removed += 1;
            }
        }

        (new_rolls, removed)
    }
}