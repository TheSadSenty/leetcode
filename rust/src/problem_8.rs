#[cfg(test)]
mod tests {
    use crate::*;
    #[test]
    fn test_8() {
        assert_eq!(problem_8::my_atoi(String::from("42")), 42);
        assert_eq!(problem_8::my_atoi(String::from("   -42")), -42);
        assert_eq!(problem_8::my_atoi(String::from("4193 with words")), 4193);
    }
}
pub fn my_atoi(s: String) -> i32 {
    let mut sign = 1;
    let mut result = 0;
    for i in s.chars() {
        if i == ' ' {
            continue;
        }
        if i == '-' {
            sign = -1;
        }
        if (i as i32 - '0' as i32) >= 0 && (i as i32 - '0' as i32) <= 9 {
            result = result * 10 + (i as i32 - '0' as i32);
        }
    }
    sign * result
}
