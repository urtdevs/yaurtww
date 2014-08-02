class Manifest():
    def __init__(self, version_line):
        self.cdn_url = "http://cdn.urbanterror.info/urt/{0}/{1}/q3ut4/{2}"
        self.major_version, self.release_num = self._parse_version(version_line)
        self.file_names = []
        self.file_urls = []

    def _parse_version(self, line):
        """
        There's a magic suffix to the release version, currently it's -03, but it
        increments seemingly randomly.
        """
        version_string = line.split(' ')[1]
        version_list = version_string.split('.')
        major_version = ''.join(version_list[0], version_list[1])
        release_num = ''.join(version_list[2], "-03")
        return (major_version, release_num)

    def _get_url(self, filename):
        """
        Returns url for cdn.urbanterror.info to pass to _not_wget().

        http://cdn.urbanterror.info/urt/<major_ver_without_.>/<release_num>-<magic_number>/q3ut4/<filename>
        """
