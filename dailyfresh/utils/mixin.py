from django.contrib.auth.decorators import login_required


class LoginRequestedMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        # 调用父类的as_view
        view = super(LoginRequestedMixin, cls).as_view(**initkwargs)
        return login_required(view)