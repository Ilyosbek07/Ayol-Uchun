from django.core.exceptions import ValidationError


def validate_video(value):
    print(value, "................................")
    if not value:
        raise ValidationError(f"Either video path or video url must be provided.")
    return value
