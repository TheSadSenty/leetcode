#[cfg(test)]
mod tests {
    use std::str::FromStr;

    use crate::*;
    #[test]
    fn test_9() {
        assert_eq!(problem_9::is_palindrome(121), true);
        assert_eq!(problem_9::is_palindrome(-121), false);
        assert_eq!(problem_9::is_palindrome(10), false);
    }
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
fn main() {
    println!("Hello");
}
mod problem_9 {
    pub fn is_palindrome(x: i32) -> bool {
        let result = recursive(x, x, 0);
        result
    }
    fn recursive(mut n: i32, tmp: i32, mut rev: i32) -> bool {
        if n < 0 {
            return false;
        }
        if n == 0 {
            if tmp == rev {
                return true;
            } else {
                return false;
            }
        } else {
            let dig = n % 10;
            rev = rev * 10 + dig;
            n = n / 10;
            return recursive(n, tmp, rev);
        }
    }
}
mod problem_13 {
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
}
