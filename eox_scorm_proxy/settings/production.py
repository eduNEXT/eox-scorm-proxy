"""
Settings for eox_core project meant to be called on the edx-platform/*/envs/aws.py module
"""
from .common import *  # pylint: disable=wildcard-import, unused-wildcard-import


def plugin_settings(settings):  # pylint: disable=function-redefined
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    
    def scorm_xblock_storage(xblock):
        from django.conf import settings
        from storages.backends.s3boto import S3BotoStorage

        if settings.SERVICE_VARIANT == "lms":
            domain = settings.LMS_BASE
        else:
            domain = settings.CMS_BASE

        bucket_host = f"s3.us-west-2.amazonaws.com"
        print('=========================================!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!HOLA:)')
        return S3BotoStorage(
            bucket=settings.AWS_STORAGE_BUCKET_NAME,
            access_key=settings.AWS_ACCESS_KEY_ID,
            secret_key=settings.AWS_SECRET_ACCESS_KEY,
            host=bucket_host,
            querystring_expire=86400,
            custom_domain=f"{domain}/nginx-scorm-proxy"
        )

    settings.XBLOCK_SETTINGS["ScormXBlock"] = {
        "STORAGE_FUNC": scorm_xblock_storage,
    }
    