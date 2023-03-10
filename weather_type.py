from enum import Enum


class WeatherType(Enum):
    '''расшифровка кода погоды'''

    def __int__(self):
        return self.value

    def __new__(cls, value, name):
        _type = object.__new__(cls)
        _type._value_ = value
        _type._name = name
        return _type

    TWLR_ = 200, 'небольшой дождь с грозой'
    TWR__ = 201, 'дождь с грозой'
    TWHR_ = 202, 'сильный дождь с грозой'
    LT___ = 210, 'небольшая гроза'
    T____ = 211, 'гроза'
    HT___ = 212, 'сильная гроза'
    RT___ = 221, 'рваная гроза'
    TWLD_ = 230, 'гроза с небольшим дождем'
    TWD__ = 231, 'морось с грозой'
    TWHD_ = 232, 'гроза с сильной моросью'
    LID__ = 300, 'мелкая морось'
    D____ = 301, 'морось'
    HID__ = 302, 'сильная морось'
    LIDR_ = 310, 'слабая морось'
    DR___ = 311, 'моросящий дождь'
    HIDR_ = 312, 'сильно моросящий дождь'
    SRAD_ = 313, 'ливень и морось'
    HSRAD = 314, 'сильный ливень и морось'
    SD___ = 321, 'моросящий дождь'
    LR___ = 500, 'легкий дождь'
    MR___ = 501, 'умеренный дождь'
    HIR__ = 502, 'сильный дождь'
    VHR__ = 503, 'очень сильный дождь'
    ER___ = 504, 'ливень'
    FR___ = 511, 'ледяной дождь'
    LISR_ = 520, 'слабый ливень'
    SR___ = 521, 'ливень'
    HISR_ = 522, 'ливень с дождем'
    RSR__ = 531, 'полосовой дождь'
    LS___ = 600, 'небольшой снег'
    S____ = 601, 'снег'
    HS___ = 602, 'снегопад'
    SL___ = 611, 'мокрый снег'
    LSSL_ = 612, 'дождь со снегом'
    SSL__ = 613, 'мокрый снег'
    LRAS_ = 615, 'слабый дождь со снегом'
    RAS__ = 616, 'дождь со снегом'
    LSSN_ = 620, 'ливень со снегом'
    SSN__ = 621, 'град'
    HSS__ = 622, 'снегопад'
    MIST_ = 701, 'пасмурно'
    SMOKE = 711, 'дымка'
    HAZE_ = 721, 'мгла'
    SDW__ = 731, 'песчано-пылевая буря'
    FOG__ = 741, 'туман'
    SAND_ = 751, 'песчаная буря'
    DUST_ = 761, 'пыль'
    VA___ = 762, 'вулканический пепел'
    SQ___ = 771, 'вихрь'
    TO___ = 781, 'торнадо'
    CS___ = 800, 'ясно'
    FC___ = 801, 'небольшая облачность'
    SC___ = 802, 'переменная облачность'
    BC___ = 803, 'облачно с прояснениями'
    OC___ = 804, 'пасмурно'
