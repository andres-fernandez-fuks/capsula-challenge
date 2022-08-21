from project.exceptions.invalid_input_exception import InvalidInputException
from project.exceptions.insufficient_funds_exception import InsufficientFundsException
from http import HTTPStatus

class ExceptionHandler:
    """
    Se encarga de categorizar los errores y devolver un mensaje de error apropiado.
    """

    INVALID_INPUT_EXCEPTIONS = [InvalidInputException]
    BUSINESS_LOGIC_EXCEPTIONS = [InsufficientFundsException]

    @classmethod
    def exception_belongs_to(exception, exception_lists):
        """
        Devuelve True si la excepción pertenece a la lista de excepciones.
        """
        return any(
            isinstance(exception, exception_type) for exception_type in exception_lists
        )

    @classmethod
    def handle_exception(cls, exception):
        if cls.exception_belongs_to(exception, cls.INVALID_INPUT_EXCEPTIONS):
            return {"error": str(exception)}, HTTPStatus.BAD_REQUEST
        elif cls.exception_belongs_to(exception, cls.BUSINESS_LOGIC_EXCEPTIONS):
            return {"error": str(exception)}, HTTPStatus.UNPROCESSABLE_ENTITY
        else:
            return {"error": str(exception)}, HTTPStatus.INTERNAL_SERVER_ERROR
