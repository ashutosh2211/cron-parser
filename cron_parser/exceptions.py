class InvalidExpression(Exception):
    """Exception raised for invalid expression string.

    Attributes:
        expression -- input expression which caused the error
        message -- explanation of the error
    """

    def __init__(self, expression: str, message=None):
        self.expression = expression
        self.message = message or f"Invalid expression: {expression} provided"
        super().__init__(self.message)


class InvalidFieldValue(Exception):
    pass
