from allauth.account.views import SignupView
from .tasks import sleepy, send_email_task


class CustomLoginView(SignupView):
    def get_context_data(self, **kwargs):
        send_email_task.delay()
        context = super(SignupView, self)
        return context
