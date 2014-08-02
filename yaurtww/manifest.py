import grequests


class Manifest():
    def __init__(self, filename):
        self.cdn_url = "http://cdn.urbanterror.info/urt/{0}/{1}/q3ut4/{2}"
        self.mver = ""
        self.relnum = ""
        self.files = (
            grequests.get(url) for url in self._parse_manifest(filename))

    def _parse_version(self, line):
        """
        There's a magic suffix to the release version, currently it's -03, but
        it increments seemingly randomly.
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
        return self.cdn_url.format(self.mver, self.relnum, filename)

    def _parse_manifest(self, filename):
        """
        Read the defined file, parse and set Version line, and return generator of filenames.
        """
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith("Version"):
                    self._parse_version(line)
                lineitems = line.split('  ')
                if len(lineitems) == 2:
                    yield self._get_url(lineitems[1][:-1])

    def map_files(self):
        return grequests.map(self.files)
