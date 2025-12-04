use std::fs;
use std::collections::HashSet;
use std::collections::HashMap;

fn main() {
    let codes = parse_file();

    println!("{:?}", codes);
    // part_one(codes);
    part_two(codes);

}

fn parse_file() -> Vec<String> {
    let file_path = "input.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let split: Vec<String> = contents
                                    .split(',')
                                    .map(|s| s.to_string()) // Convert each &str to String
                                    .collect();
    return split;
}

fn part_one(codes: Vec<String>) {
    let mut ans = 0;

    for code in codes {
        let (start, end) = code.split_once('-').unwrap();
        let start: u64 = start.parse().unwrap();
        let end: u64 = end.parse().unwrap();

        for num in start..end + 1 {
            let num_str = num.to_string();
            let length: usize = num_str.len();

            // if its not even, it can't be split into equal halves
            if length % 2 != 0 {
                continue
            }
            
            let (first_half, second_half) = num_str.split_at(length / 2);

            if first_half == second_half {
                ans = ans + num;
            }
        }
    }
    println!("{ans}");
}

fn part_two(codes: Vec<String>) {
    let mut ans = 0;
    let mut factors_map = HashMap::new();

    for code in codes {
        let (start, end) = code.split_once('-').unwrap();
        let start: u64 = start.parse().unwrap();
        let end: u64 = end.parse().unwrap();
        
        for num in start..end + 1 {
            let num_str = num.to_string();
            let length = num_str.len();

            // find all factors of the length to see how we can evenly divide the number
            let factors = factors_map.entry(length).or_insert(find_factors(length));

            for factor in  &mut factors.iter() {
                let chunks = split_into_chunks(&num_str, *factor);
                let first_element = &chunks[0];
                // if all chunks in the number are equal, then it's invalid
                if chunks.iter().all(|element| element == first_element) {
                    ans = ans + num;
                    break;
                }
            }
        }
    }
    println!("{ans}");

    fn find_factors (number: usize) -> HashSet<usize> {
        let mut factors: HashSet<usize> = HashSet::new();

        // don't use number + 1 as we don't need the number itself in the list
        for curr in 1..number {
            if number % curr == 0 {
                factors.insert(curr);
            }
        }
        factors
    }

    // given a string and a chunk size, split the string into chunks
    fn split_into_chunks (s: &str, size: usize) -> Vec<String> {
        let mut chars = s.chars();
        let mut result = Vec::new();
        loop {
            let chunk: String = chars.by_ref().take(size).collect();
            if chunk.is_empty() {
                break;
            }
            result.push(chunk);
        }
        result
    }
}

