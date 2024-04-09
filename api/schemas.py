import pydantic
import datetime


class SignUpReturn(pydantic.BaseModel):
    """
    Класс Pydantic для структуры данных, возвращаемых при успешной регистрации.

    Содержит поля:
    - status: булево значение, указывающее на успешность операции.
    - user_id: целое число, идентификатор пользователя.
    """

    status: bool
    user_id: int


class SignInReturn(pydantic.BaseModel):
    """
    Класс Pydantic для структуры данных, возвращаемых при успешном входе.

    Содержит поле:
    - token: строка, предположительно, токен для аутентификации.
    """

    token: str


class ResetPasswordReturn(pydantic.BaseModel):
    """
    Класс Pydantic для структуры данных, возвращаемых при сбросе пароля.

    Содержит поле:
    - status: булево значение, указывающее на успешность операции.
    """

    status: bool


class MeReturn(pydantic.BaseModel):
    """
    Класс Pydantic для структуры данных возвращаемых значений, связанных с данными о пользователе.

    Содержит поля:
    - id: целое число, идентификатор пользователя.
    - created: объект datetime.datetime, дата и время создания пользователя.
    - username: строка, имя пользователя.
    - first_name: строка, имя пользователя.
    - last_name: строка, фамилия пользователя.
    - email: pydantic.EmailStr, адрес электронной почты пользователя.
    """

    id: int
    created: datetime.datetime
    username: str
    first_name: str
    last_name: str
    email: pydantic.EmailStr
