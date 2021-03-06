from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


class UserRuleMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin determining whether the user is an author
    """

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def handle_no_permission(self):
        return redirect("not_author")
