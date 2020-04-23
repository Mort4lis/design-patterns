class VideoFile:
    """
    Классы подсистемы.

    Подсистема может принимать запросы либо от фасада, либо от клиента напрямую.
    В любом случае, для Подсистемы Фасад – это ещё один клиент, и он не является
    частью Подсистемы.
    """

    def __init__(self, filename):
        self.filename = filename


class MPEG4CompressionCodec:
    pass


class OggCompressionCodec:
    pass


class BitrateReader:
    @staticmethod
    def read(file):
        return ''

    @staticmethod
    def convert(buffer, codec):
        return ''


class AudioMixer:
    def fix(self, result):
        return ''


class VideoConverter:
    """
    Класс Фасада предоставляет простой интерфейс для сложной логики одной или
    нескольких подсистем. Фасад делегирует запросы клиентов соответствующим
    объектам внутри подсистемы. Фасад также отвечает за управление их жизненным
    циклом. Все это защищает клиента от нежелательной сложности подсистемы.
    """

    @staticmethod
    def convert(filename, format='mp4'):
        """
        Методы Фасада удобны для быстрого доступа к сложной функциональности
        подсистем. Однако клиенты получают только часть возможностей подсистемы.
        """
        file = VideoFile(filename)
        if format == 'mp4':
            codec = MPEG4CompressionCodec()
        else:
            codec = OggCompressionCodec()
        buffer = BitrateReader.read(file)
        result = BitrateReader.convert(buffer, codec)
        result = AudioMixer().fix(result)
        return result


def client_code(f: VideoConverter):
    """
    Клиентский код работает со сложными подсистемами через простой интерфейс,
    предоставляемый Фасадом. Когда фасад управляет жизненным циклом подсистемы,
    клиент может даже не знать о существовании подсистемы. Такой подход
    позволяет держать сложность под контролем.
    """
    f.convert('a.mp4', format='mp4')
