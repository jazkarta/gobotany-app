#S3 info
from storages.backends.s3boto import S3BotoStorage


class S3BotoStorageAdminFix(S3BotoStorage):
    """S3BotoStorage with fix for admin prefix url"""

    def url(self, name):
        url = super(S3BotoStorageAdminFix, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url

StaticRootS3BotoStorage = lambda: S3BotoStorageAdminFix(location='static',
                                                        querystring_auth=False)
