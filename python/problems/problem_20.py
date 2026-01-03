CORRESPONDING_PARENTHESES = {
    "(": ")",
    "{": "}",
    "[": "]",
}


class Solution:
    def isValid(self, parentheses: str) -> bool:
        stack = []

        for parenthesis in parentheses:
            if parenthesis in CORRESPONDING_PARENTHESES:
                stack.append(parenthesis)

            if parenthesis in CORRESPONDING_PARENTHESES.values():
                if not stack or CORRESPONDING_PARENTHESES[stack.pop()] != parenthesis:
                    return False

        return not stack
