from ..plugin import continue_check_handler
from flask import Flask
from flaskr.service.order.models import AICourseLessonAttend
from flaskr.service.lesson.models import AILessonScript
from trace import Trace
from flaskr.service.user.models import User
from flaskr.service.lesson.const import UI_TYPE_PHONE


@continue_check_handler(UI_TYPE_PHONE)
def check_phone(
    app: Flask,
    user_info: User,
    attend: AICourseLessonAttend,
    script_info: AILessonScript,
    input: str,
    trace: Trace,
    trace_args,
):
    return user_info.user_state != 0
