from django.conf.urls import re_path
from s3direct.views import get_upload_params, generate_aws_v4_signature

urlpatterns = [
    re_path('^get_upload_params/', get_upload_params, name='s3direct'),
    re_path('^get_aws_v4_signature/',
        generate_aws_v4_signature,
        name='s3direct-signing'),
]
