use std::fs;

fn main() {
    let turns = parse_file();

    // part_one(turns);
    part_two(turns);
}

fn parse_file() -> Vec<String> {
    let file_path = "input.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let split: Vec<String> = contents
                                    .lines()
                                    .map(|s| s.to_string()) // Convert each &str to String
                                    .collect();
    return split;
}

fn part_one(turns: Vec<String>) {
    let mut curr: i32 = 50;

    let mut ans = 0;

    for turn in turns {
        let (direction, number) = turn.split_at(1);

        let number: i32 = number.parse().expect("not a number :(");

        // mod by 100 to see how many we need to add / subtract by 
        let number = number % 100;

        if direction == "R" {
            curr += number;
            if curr >= 100 {
                curr -= 100;
            }
        }
        else {
            curr = curr - number;
            if curr < 0 {
                curr += 100;
            }
            curr = curr.abs()
        }    

        if curr == 0 {
            ans += 1;
        }
    }
    println!("{ans}");
}

fn part_two(turns: Vec<String>) {
    let mut curr = 50;
    let mut ans = 0;

    for turn in turns {
        let (direction, number) = turn.split_at(1);

        let number: i32 = number.parse().expect("not a number :(");
        // check how many times we rotate by 100 (so back to the same num)
        let times_through = number / 100;
        let number = number % 100;

        ans += times_through;

        // flag ensures we don't increment extra if we start at 0 and move left
        let mut flag = true;
        if curr == 0 {
            flag = false;
        }

        curr = match direction {
            "R" => curr + number,
            "L" => curr - number,
            _ => panic!("at the disco")
        };

        if curr >= 100 {
            curr -= 100;
            ans += 1;
        } 
        else if curr == 0 && number != 0 {
            ans += 1;
        } else if curr < 0 {
            curr += 100;
            if flag {
                ans += 1;
            }
        }
    }
    println!("{ans}");
}