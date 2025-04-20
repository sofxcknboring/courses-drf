from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.hashers import make_password
from materials.models import Lesson, Course
from materials.models import Subscription
from users.models import User


class LessonAPITestCase(APITestCase):
    def setUp(self):
        self.moder_group, created = Group.objects.get_or_create(name="moders")
        self.user = User.objects.create(
            email="user@example.com",
            password=make_password("password"),
        )
        self.user.save()

        self.moderator = User.objects.create(
            email="moderator@example.com",
            password=make_password("password"),
        )
        self.moderator.groups.add(self.moder_group)
        self.moderator.save()

        self.course = Course.objects.create(title="Тестовый курс", owner=self.user)
        self.lesson = Lesson.objects.create(
            title="Тестовый урок", course=self.course, owner=self.user
        )

        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )

    def test_create_lesson(self):
        """Тест создания урока"""
        url = reverse("materials:lessons_create")
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Новый урок",
            "course": self.course.id,
            "description": "Описание урока",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_create_lesson_by_moderator(self):
        """Тест создания урока модератором"""
        url = reverse("materials:lessons_create")
        self.client.force_authenticate(user=self.moderator)
        data = {
            "title": "Новый урок",
            "course": self.course.id,
            "description": "Описание урока",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_lesson(self):
        """Тест получения урока"""
        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_update_lesson(self):
        """Тест обновления урока"""
        url = reverse("materials:lessons_update", args=(self.lesson.pk,))
        self.client.force_authenticate(user=self.user)
        data = {"title": "Обновленный урок"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Lesson.objects.get(pk=self.lesson.pk).title, "Обновленный урок"
        )

    def test_delete_lesson(self):
        """Тест удаления урока"""
        url = reverse("materials:lessons_delete", args=(self.lesson.pk,))
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.filter(id=self.lesson.id).exists(), False)

    def test_unsubscribe_user_to_course(self):
        """Тест отписки пользователя от курса"""
        if self.user.is_authenticated:
            url = reverse("materials:subscribe")
            self.client.force_authenticate(user=self.user)
            data = {"course_id": self.course.id}
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(
                Subscription.objects.filter(
                    user=self.user, course=self.course
                ).exists(),
                False,
            )
