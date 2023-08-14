from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.course.models import VideoWatchProgress, Video, UserCourse, UserCertificate, Course


@receiver(post_save, sender=VideoWatchProgress)
def update_video_last_viewed_seconds(sender, instance, created, **kwargs):
        course_id = VideoWatchProgress.objects.get(id=instance.id)
        all_video_count = Video.objects.filter(
            unit__course_id=course_id.video.unit.course.id,
        ).aggregate(video_count=Count("video"))["video_count"]

        watched_video_count = VideoWatchProgress.objects.filter(
            video__unit__course_id=course_id.video.unit.course.id,
            profile=instance.profile,
        ).aggregate(video_count=Count("video"))["video_count"]

        if all_video_count == watched_video_count:
            course_update = UserCourse.objects.get(profile=instance.profile)
            course_update.is_finished = True
            course_update.save()
            course = Course.objects.get(id=course_id.video.unit.course.id)
            certificate = UserCertificate.objects.get_or_create(profile=instance.profile, course=course,
                                                         certificate=course.certificate)






