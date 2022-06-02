"""
Settings for eox_core project meant to be called on the edx-platform/*/envs/aws.py module
"""


def plugin_settings(settings):  # pylint: disable=function-redefined
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    def scorm_xblock_storage(xblock):

        from django.conf import settings as tenant_settings
        from storages.backends.s3boto import S3BotoStorage
        
        if settings.SERVICE_VARIANT == "lms":
            domain = tenant_settings.LMS_BASE
        else:
            domain = tenant_settings.CMS_BASE

        bucket_host = "s3.us-west-2.amazonaws.com"

        return S3BotoStorage(
            bucket=settings.AWS_STORAGE_BUCKET_NAME,
            access_key=settings.AWS_ACCESS_KEY_ID,
            secret_key=settings.AWS_SECRET_ACCESS_KEY,
            host=getattr(settings, 'EOX_SCORM_PROXY_HOST', bucket_host),
            querystring_expire=getattr(settings, 'EOX_SCORM_PROXY_QUERYSTRING_EXPIRE', 86400),
            custom_domain=f"{domain}/nginx-scorm-proxy"
        )

    settings.XBLOCK_SETTINGS["ScormXBlock"] = {
        "STORAGE_FUNC": scorm_xblock_storage,
    }
