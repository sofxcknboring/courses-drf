from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from materials.models import Course, Lesson
from users.models import Payment

User = get_user_model()


class Command(BaseCommand):
    help = "Наполняет БД тестовыми данными"

    def handle(self, *args, **kwargs):
        # Очистка БД перед созданием новых данных (необязательно)
        User.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        # Создание пользователей
        users = [
            User.objects.create(
                email=f"user{i}@example.com",
                phone=f"+79001234{i:02d}",
                avatar=None,
                city="Москва",
            )
            for i in range(1, 6)
        ]

        # Хэшируем пароли после создания пользователей
        for user in users:
            user.set_password("password123")
            user.save()

        # Создание курсов
        courses = [
            Course.objects.create(
                title="Python для начинающих",
                description="Основы программирования на Python",
            ),
            Course.objects.create(
                title="Django с нуля", description="Создание веб-приложений на Django"
            ),
            Course.objects.create(
                title="Flask в действии", description="Разработка на Flask"
            ),
            Course.objects.create(
                title="Алгоритмы и структуры данных",
                description="Разбор алгоритмов на Python",
            ),
            Course.objects.create(
                title="SQL для начинающих", description="Основы работы с базами данных"
            ),
        ]

        # Создание уроков
        lessons = [
            Lesson.objects.create(
                course=courses[0],
                title="Введение в Python",
                description="Первый шаг в Python",
            ),
            Lesson.objects.create(
                course=courses[0],
                title="Переменные и типы данных",
                description="Основы переменных",
            ),
            Lesson.objects.create(
                course=courses[1],
                title="Настройка Django",
                description="Установка Django",
            ),
            Lesson.objects.create(
                course=courses[1],
                title="Создание моделей",
                description="Работа с моделями",
            ),
            Lesson.objects.create(
                course=courses[2],
                title="Основы Flask",
                description="Структура проекта на Flask",
            ),
            Lesson.objects.create(
                course=courses[2],
                title="Работа с шаблонами",
                description="Jinja2 в Flask",
            ),
            Lesson.objects.create(
                course=courses[3], title="Сортировки", description="Разбор сортировок"
            ),
            Lesson.objects.create(
                course=courses[3],
                title="Динамическое программирование",
                description="Оптимизация",
            ),
            Lesson.objects.create(
                course=courses[4],
                title="SELECT и JOIN",
                description="Основы SQL-запросов",
            ),
            Lesson.objects.create(
                course=courses[4],
                title="Индексы и оптимизация",
                description="Как ускорить SQL",
            ),
        ]

        # Создание платежей
        payments = [
            Payment.objects.create(
                user=users[i % 5],
                course=courses[i % 5],
                amount=1999.99,
                payment_method="transfer",
            )
            for i in range(10)
        ] + [
            Payment.objects.create(
                user=users[i % 5],
                lesson=lessons[i % 10],
                amount=499.99,
                payment_method="cash",
            )
            for i in range(10)
        ]

        self.stdout.write(
            self.style.SUCCESS(
                f"Создано {len(users)} пользователей, {len(courses)} курсов, "
                f"{len(lessons)} уроков и {len(payments)} платежей."
            )
        )
