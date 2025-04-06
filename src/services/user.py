from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import User
from src.repositories.user_repository import UserRepository
from src.schemas.user import UserCreate
from src.services.auth import AuthService


class UserService:
    """
    Сервіс для роботи з користувачами.

    Attributes:
        db (AsyncSession): Асинхронна сесія бази даних
        user_repository (UserRepository): Репозиторій для роботи з користувачами
        auth_service (AuthService): Сервіс аутентифікації
    """

    def __init__(self, db: AsyncSession):
        """
        Ініціалізація сервісу користувачів.

        Args:
            db (AsyncSession): Асинхронна сесія бази даних
        """
        self.db = db
        self.user_repository = UserRepository(self.db)
        self.auth_service = AuthService(db)

    async def create_user(self, user_data: UserCreate) -> User:
        """
        Створення нового користувача.

        Args:
            user_data (UserCreate): Дані нового користувача

        Returns:
            User: Створений користувач
        """
        user = await self.auth_service.register_user(user_data)
        return user

    async def get_user_by_username(self, username: str) -> User | None:
        """
        Отримання користувача за ім'ям.

        Args:
            username (str): Ім'я користувача

        Returns:
            User | None: Знайдений користувач або None
        """
        user = await self.user_repository.get_by_username(username)
        return user

    async def get_user_by_email(self, email: str) -> User | None:
        """
        Отримання користувача за email.

        Args:
            email (str): Email користувача

        Returns:
            User | None: Знайдений користувач або None
        """
        user = await self.user_repository.get_user_by_email(email)
        return user

    async def confirmed_email(self, email: str) -> None:
        """
        Підтвердження email користувача.

        Args:
            email (str): Email для підтвердження

        Returns:
            User: Оновлений користувач
        """
        user = await self.user_repository.confirmed_email(email)
        return user


    async def update_avatar_url(self, email: str, url: str):
        """
        Оновлення URL аватара користувача.

        Args:
            email (str): Email користувача
            url (str): Новий URL аватара

        Returns:
            User: Оновлений користувач
        """
        return await self.user_repository.update_avatar_url(email, url)




    async def get_user_by_id(self, user_id: int) -> User | None:
        """
        Отримання користувача за ID.

        Args:
            user_id (int): ID користувача

        Returns:
            User | None: Знайдений користувач або None
        """
        return await self.user_repository.get_by_id(user_id)
