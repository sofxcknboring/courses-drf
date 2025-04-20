from rest_framework.serializers import ModelSerializer, URLField, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import youtube_url_validator


class LessonSerializer(ModelSerializer):
    video_url = URLField(
        required=False, allow_blank=True, validators=[youtube_url_validator]
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    is_subscribed = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "description",
            "preview",
            "lessons",
            "lesson_count",
            "is_subscribed",
        )
