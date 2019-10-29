"""as2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import admin
from django.contrib.auth import views as auth_views
from as2 import views

import debug_toolbar

staff_required = user_passes_test(lambda u: u.is_staff)
superuser_required = user_passes_test(lambda u: u.is_superuser)



urlpatterns = [
    url(r'^$', login_required(views.home, login_url='login'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login.*', auth_views.login, {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout.*', auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^password_change/$', auth_views.password_change, name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^home.*', login_required(views.home, login_url='login'), name='home'),
    url(r'^msearch/$', login_required(views.MessageSearch.as_view(), login_url='login'), name='msearch'),
    url(r'^message/$', login_required(views.MessageList.as_view(), login_url='login'), name='messages'),
    url(r'^message/(?P<pk>.+)/$', login_required(views.MessageDetail.as_view(), login_url='login'),
        name='message_detail'),
    url(r'^payload/(?P<pk>.+)/$', login_required(views.PayloadView.as_view(), login_url='login'), name='payload_view'),
    url(r'^mdnsearch/$', login_required(views.MDNSearch.as_view(), login_url='login'), name='mdnsearch'),
    url(r'^mdn/$', login_required(views.MDNList.as_view(), login_url='login'), name='mdns'),
    url(r'^mdn/(?P<pk>.+)/$', login_required(views.MDNView.as_view(), login_url='login'), name='mdn_view'),
    url(r'^sendmessage/$', login_required(views.SendMessage.as_view(), login_url='login'), name='sendmessage'),
    url(r'^resendmessage/(?P<pk>.+)/$', login_required(views.resend_message, login_url='login'), name='resendmessage'),
    url(r'^sendasyncmdn/$', login_required(views.send_async_mdn, login_url='login'), name='sendasyncmdn'),
    url(r'^retryfailedcomms/$', login_required(views.retry_failed_comms, login_url='login'), name='retryfailedcomms'),
    url(r'^cancelretries/(?P<pk>.+)/$', login_required(views.cancel_retries, login_url='login'), name='cancelretries'),
    url(r'^certificates/(?P<pk>.+)$', login_required(views.download_cert, login_url='login'), name='download_cert'),
    # only superuser
    url(r'^sendtestmail$', superuser_required(views.send_test_mail_managers), name='sendtestmail'),
    # as2 asynchronous mdn and message receive url
    url(r'^as2/receive$', views.as2receive, name="as2-receive"),
    url(r'^pyas2/as2receive$', views.as2receive, name="pyas2-receive"),
    url(r'^as2/send$', views.as2send, name='file-upload'),
    # catch-all
    url(r'^.*', login_required(views.home, login_url='login'), name='home'),

    url(r'^__debug__/', include(debug_toolbar.urls)),
]
