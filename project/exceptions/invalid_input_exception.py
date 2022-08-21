class InvalidInputException(Exception):
    def __init__(self, input_field):
        self.input_field = input_field

    def __str__(self):
        return f"El campo {self.input_field} no es válido"