#[cfg(test)]
mod tests {
    use crate::*;
    #[test]
    fn test_9() {
        assert_eq!(problem_9::is_palindrome(121), true);
        assert_eq!(problem_9::is_palindrome(-121), false);
        assert_eq!(problem_9::is_palindrome(10), false);
    }
}
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
