use std::fs;

fn main() {
    let batteries = parse_file();

    // part_one(batteries);
    part_two(batteries);
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

fn part_one(batteries: Vec<String>) {
    let mut ans = 0;
    for battery in batteries {
        let battery_chars = battery.chars();

        // get biggest number barring the last one
        let tens_digit = battery_chars.take(battery.len() - 1).max().unwrap();

        // get the index of the tens digit
        let tens_index = battery.find(tens_digit).unwrap();

        // get biggest ones digit (need to look for ones digit after the tens)
        let ones_digit = battery.chars().skip(tens_index + 1).max().unwrap();

        // the second value needs to be a slice for some reason
        let joltage: i32 = (tens_digit.to_string() + &ones_digit.to_string()).parse().unwrap();

        ans += joltage;
    }
    print!("{ans}");
}

fn part_two(batteries: Vec<String>) {
    let mut ans = 0;

    for battery in batteries {
        let mut joltage: Vec<char> = Vec::new();
        let battery_len = battery.len();
        
        let mut next_index = 0; // index to start the search from
        let mut chars_needed = 12;

        while chars_needed > 0 {
            // valid window size
            let remaining_len = battery_len - next_index;

            // window must be large enough to pick all remaining chars_needed from it
            let window_limit = remaining_len - chars_needed + 1;

            let mut max_char = '\x00'; //smallest char
            let mut max_abs_index = next_index;

            // iterate over current window
            for (relative_index, current_c) in battery.chars()
                                                      .skip(next_index)
                                                      .take(window_limit)
                                                      .enumerate() {
                // update if the character is greater (not equals), as using max_by grabs the last digit if there's multiple max digits
                // if current_c == max_char, the loop continues, keeping the first index found
                if current_c > max_char {
                    max_char = current_c;
                    max_abs_index = next_index + relative_index; // find index inside entire battery
                }
            }

            joltage.push(max_char);
            chars_needed -= 1;
            
            // next search will start the chosen digit
            next_index = max_abs_index + 1; 

            println!("got '{}' at index {}, {} chars left", max_char, max_abs_index, chars_needed);
        }

        let joltage_combined: u64 = joltage.into_iter().collect::<String>().parse().unwrap();
        
        ans += joltage_combined;
    }
    println!("answer is {ans}");
}