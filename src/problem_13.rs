#[cfg(test)]
mod tests {
    use crate::*;
    use std::str::FromStr;
    #[test]
    fn test_13() {
        assert_eq!(
            problem_13::roman_to_int(String::from_str("III").unwrap()),
            3
        );
        assert_eq!(
            problem_13::roman_to_int(String::from_str("LVIII").unwrap()),
            58
        );
        assert_eq!(
            problem_13::roman_to_int(String::from_str("MCMXCIV").unwrap()),
            1994
        );
    }
}
pub fn roman_to_int(s: String) -> i32 {
    let mut result = 0;
    let mut prev_num = ' ';
    for i in s.chars() {
        match i {
            'I' => {
                prev_num = 'I';
                result += 1;
            }
            'V' => {
                if prev_num == 'I' {
                    result += 3;
                } else {
                    result += 5;
                }
                prev_num = 'V';
            }
            'X' => {
                if prev_num == 'I' {
                    result += 8;
                } else {
                    result += 10;
                }
                prev_num = 'X';
            }
            'L' => {
                if prev_num == 'X' {
                    result += 30;
                } else {
                    result += 50;
                }
                prev_num = 'L';
            }
            'C' => {
                if prev_num == 'X' {
                    result += 80;
                } else {
                    result += 100;
                }
                prev_num = 'C';
            }
            'D' => {
                if prev_num == 'C' {
                    result += 300;
                } else {
                    result += 500;
                }
                prev_num = 'D';
            }
            'M' => {
                if prev_num == 'C' {
                    result += 800;
                } else {
                    result += 1000;
                }
                prev_num = 'M';
            }
            _ => {
                panic!();
            }
        }
    }
    return result;
}
