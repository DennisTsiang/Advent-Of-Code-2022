use std::error::Error;
use std::fs;

struct RpsPair {
    opponent: char,
    player: char,
}

/*
 * Opponent: A = Rock, B = Paper, C = Scissors
 * Me: X = Rock, Y = Paper, Z = Scissors
 */
fn find_my_total_score(input: &Vec<RpsPair>) -> usize {
    let mut my_score = 0;
    for pair in input.iter() {
        match pair.player {
            'X' => my_score += 1,
            'Y' => my_score += 2,
            'Z' => my_score += 3,
            _ => (),
        }
        if (pair.opponent == 'A' && pair.player == 'Y')
            || (pair.opponent == 'B' && pair.player == 'Z')
            || (pair.opponent == 'C' && pair.player == 'X')
        {
            my_score += 6;
        } else if (pair.opponent == 'A' && pair.player == 'X')
            || (pair.opponent == 'B' && pair.player == 'Y')
            || (pair.opponent == 'C' && pair.player == 'Z')
        {
            my_score += 3;
        }
    }
    my_score
}

/*
 * Opponent: A = Rock, B = Paper, C = Scissors
 * Me: X = Lose, Y = Draw, Z = Win
 */
fn find_my_total_score_2(input: &Vec<RpsPair>) -> usize {
    let mut my_score = 0;
    for pair in input.iter() {
        /* For player choices lay out the score calculation as (choice + outcome) */
        match pair.opponent {
            'A' => match pair.player {
                'X' => my_score += 3 + 0,
                'Y' => my_score += 1 + 3,
                'Z' => my_score += 2 + 6,
                _ => (),
            },
            'B' => match pair.player {
                'X' => my_score += 1 + 0,
                'Y' => my_score += 2 + 3,
                'Z' => my_score += 3 + 6,
                _ => (),
            },
            'C' => match pair.player {
                'X' => my_score += 2 + 0,
                'Y' => my_score += 3 + 3,
                'Z' => my_score += 1 + 6,
                _ => (),
            },
            _ => (),
        }
    }
    my_score
}

fn main() -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string("input.txt")?;
    let input: Vec<RpsPair> = contents
        .trim()
        .split('\n')
        .map(|x| {
            let el = x.trim();
            let mut choices = el.split_ascii_whitespace();

            let opponent_choice = choices
                .next()
                .expect(&format!("Did not find opponent choice in the line {}", el))
                .parse::<char>()
                .expect(&format!("Could not parse opponent choice"));
            let my_choice = choices
                .next()
                .expect(&format!("Did not find my choice in the line {}", el))
                .parse::<char>()
                .expect(&format!("Could not parse my choice"));
            return RpsPair {
                opponent: opponent_choice,
                player: my_choice,
            };
        })
        .collect();
    println!("{:?}", find_my_total_score(&input));
    println!("{:?}", find_my_total_score_2(&input));
    Ok(())
}
