"""
eox_scorm_proxy Django application initialization.
"""

from django.apps import AppConfig


class EoxScormProxyConfig(AppConfig):
    """
    Configuration for the eox_scorm_proxy Django application.
    """

    name = 'eox_scorm_proxy'
    verbose_name = "eduNEXT Openedx Extensions for proxy scorm component"

    plugin_app = {
        'settings_config': {
            'lms.djangoapp': {
                'production': {'relative_path': 'settings.production'},
            },
        },
    }

class EoxScormCMSProxyConfig(AppConfig):
    """
    Configuration for the eox_scorm_proxy Django application.
    """

    name = 'eox_scorm_proxy'
    verbose_name = "eduNEXT Openedx Extensions for proxy scorm component"

    plugin_app = {
        'settings_config': {
            'cms.djangoapp': {
                'production': {'relative_path': 'settings.production'},
            },
        },
    }