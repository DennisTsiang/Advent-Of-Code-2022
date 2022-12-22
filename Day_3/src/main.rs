use std::error::Error;
use std::fs;

fn find_common_item_in_rucksack(rucksack: &str) -> &str {
    let first_compartment = &rucksack[0..(rucksack.len() / 2)];
    let second_compartment = &rucksack[(rucksack.len() / 2)..];

    let mut i = 0;
    while i < first_compartment.len() {
        if second_compartment
            .find(&first_compartment[i..i + 1])
            .is_some()
        {
            return &first_compartment[i..i + 1];
        }
        i += 1;
    }

    println!("Could not find comment item in rucksack {}", rucksack);
    return "";
}

fn find_sum_of_priorities_of_duped_items(rucksacks: &Vec<&str>) -> u32 {
    let mut sum = 0;
    for rucksack in rucksacks {
        let common_item = find_common_item_in_rucksack(rucksack);
        let character = common_item
            .chars()
            .next()
            .expect(&format!("Unable to convert item to a char {}", common_item));
        let mut priority = character.to_digit(36).unwrap() - 'a'.to_digit(36).unwrap() + 1;
        if character.is_ascii_uppercase() {
            priority += 26;
        }
        sum += priority;
    }
    sum
}

fn find_common_item_between_rucksack_groups<'a>(rucksacks: &[&'a str]) -> &'a str {
    let mut i = 0;
    while i < rucksacks[0].len() {
        let mut common = true;
        for rucksack in rucksacks {
            if rucksack.find(&rucksacks[0][i..i + 1]).is_none() {
                common = false;
                break;
            }
        }
        if common {
            return &rucksacks[0][i..i + 1];
        }
        i += 1;
    }

    println!("Could not find badge in rucksack group");
    return "";
}

fn find_sum_of_priorities_of_duped_items2(rucksacks: &Vec<&str>) -> u32 {
    let mut sum = 0;
    let mut i = 0;
    while i < rucksacks.len() {
        let common_item = find_common_item_between_rucksack_groups(&rucksacks[i..i + 3]);
        let character = common_item
            .chars()
            .next()
            .expect(&format!("Unable to convert item to a char {}", common_item));
        let mut priority = character.to_digit(36).unwrap() - 'a'.to_digit(36).unwrap() + 1;
        if character.is_ascii_uppercase() {
            priority += 26;
        }
        sum += priority;
        i += 3;
    }
    sum
}

fn main() -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string("input.txt")?;
    let input: Vec<&str> = contents.trim().split('\n').collect();
    println!("{:?}", find_sum_of_priorities_of_duped_items(&input));
    println!("{:?}", find_sum_of_priorities_of_duped_items2(&input));
    Ok(())
}
