class InvalidInputException(Exception):
    def __init__(self, input_field):
        self.message = "El campo {} no es válido".format(input_field)