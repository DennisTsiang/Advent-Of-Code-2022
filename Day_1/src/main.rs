use std::error::Error;
use std::fs;
use std::process;

/* Input: list of numbers with a 0 in-between to separate each elf's inventory */
fn find_biggest_calorie_amount(input: &Vec<usize>) -> usize {
    let mut current = 0;
    let mut max = 0;
    for el in input.iter() {
        match el {
            0 => {
                if current > max {
                    max = current;
                }
                current = 0;
            }
            _ => {
                current += el;
            }
        }
    }
    if current > max {
        max = current;
    }
    max
}

fn sum_calorie_amounts(input: &Vec<usize>) -> Vec<usize> {
    let mut sums = Vec::new();
    let mut current = 0;
    for el in input.iter() {
        match el {
            0 => {
                sums.push(current);
                current = 0;
            }
            _ => {
                current += el;
            }
        }
    }
    sums.push(current);
    sums
}

fn find_sum_of_top_3_calorie_amount(input: &Vec<usize>) -> usize {
    let mut sums = sum_calorie_amounts(input);
    sums.sort();
    sums.reverse();
    sums[0..3].iter().sum()
}

fn main() -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string("input.txt")?;
    let input: Vec<usize> = contents
        .trim()
        .split('\n')
        .map(|x| {
            let el = x.trim();
            if el.is_empty() {
                return 0;
            } else {
                let parse_result = el.parse::<usize>();
                if !parse_result.is_ok() {
                    println!("Could not parse string {}", x);
                    process::exit(1);
                }
                return parse_result.unwrap();
            }
        })
        .collect();
    println!("{:?}", find_biggest_calorie_amount(&input));
    println!("{:?}", find_sum_of_top_3_calorie_amount(&input));
    Ok(())
}
