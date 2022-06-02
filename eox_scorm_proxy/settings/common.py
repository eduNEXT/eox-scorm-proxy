"""
Settings for eox-scorm-proxy
"""


def plugin_settings(settings):  # pylint: disable=function-redefined
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    settings.EOX_SCORM_PROXY_AWS_REGION="us-west-2"
    
