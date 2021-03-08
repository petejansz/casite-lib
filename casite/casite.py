class CalifSite(object):
    def __init__(self):
        super().__init__()

    def getSiteID(self): return self.__CA_SITE_CONSTANTS['SITE_ID']
    siteID = property(getSiteID)

    def getSystemID(self): return self.__CA_SITE_CONSTANTS['SYSTEM_ID']
    sysID = property(getSystemID)

    def getMobileClientID(
        self): return self.__CA_PD_CONSTANTS['MOBILE_CLIENT_ID']
    mobileClientID = property(getMobileClientID)

    def getMobileChannelID(
        self): return self.__CA_PD_CONSTANTS['MOBILE_CHANNEL_ID']
    mobileChannelID = property(getMobileChannelID)

    def getPWSClientID(
        self): return self.__CA_PD_CONSTANTS['PWS_CLIENT_ID']
    pwsClientID = property(getPWSClientID)

    def getPWSChannelID(
        self): return self.__CA_PD_CONSTANTS['PWS_CHANNEL_ID']
    pwsChannelID = property(getPWSChannelID)

    def getDefaultEsaApiKey(self):
        return self.__DEFAULT_ESA_API_KEY
    defaultEsaApiKey = property(getDefaultEsaApiKey)

    def pdvhost(self, envname): return self.__CA_PD_VHOSTS[envname]
    def pdvhosts(self): return list(self.__CA_PD_VHOSTS.values())
    def pdenvs(self): return list(self.__CA_PD_VHOSTS.keys())

    def gamesvhost(self, envname): return self.__CA_CHECKATICKET_VHOSTS[envname]
    def gamesvhosts(self): return list(self.__CA_CHECKATICKET_VHOSTS.values())
    def gamesenvs(self): return list(self.__CA_CHECKATICKET_VHOSTS.keys())

    __CA_PD_VHOSTS = {}
    __CA_PD_VHOSTS['apl'] = 'caapl.lotteryservices.com'
    __CA_PD_VHOSTS['mobile-apl'] = 'mobile-caapl.lotteryservices.com'
    __CA_PD_VHOSTS['dev'] = 'cadev1'
    __CA_PD_VHOSTS['mobile-dev'] = 'mobile-cadev1'
    __CA_PD_VHOSTS['pdc'] = 'cslplayerdirect.calottery.com'
    __CA_PD_VHOSTS['mobile-pdc'] = 'cslpdmobile.calottery.com'
    __CA_PD_VHOSTS['cat1'] = 'player.calottery.com'
    __CA_PD_VHOSTS['mobile-cat1'] = 'mobile-cat.calottery.com'
    __CA_PD_VHOSTS['cat2'] = 'ca-cat2-pws.lotteryservices.com'
    __CA_PD_VHOSTS['mobile-cat2'] = 'ca-cat2-mobile.lotteryservices.com'
    __CA_PD_VHOSTS['sit'] = 'ca-cat2-pws.lotteryservices.com'
    __CA_PD_VHOSTS['mobile-sit'] = 'ca-cat2-mobile.lotteryservices.com'

    __CA_SITE_CONSTANTS = {'SITE_ID': '35', 'SYSTEM_ID': '8'}
    __CA_PD_CONSTANTS = {
        'MOBILE_CLIENT_ID': 'CAMOBILEAPP',
        'PWS_CLIENT_ID': 'SolSet2ndChancePortal',
        'MOBILE_CHANNEL_ID': '3',
        'PWS_CHANNEL_ID': '2'
    }

    __DEFAULT_ESA_API_KEY = 'di9bJ9MPTXOZvEKAvd7CM8cRJ4Afo54b'

    __CA_CHECKATICKET_VHOSTS = {}
    __CA_CHECKATICKET_VHOSTS['cat1-mobile'] = 'cat-draw-mobile.calottery.com'
    __CA_CHECKATICKET_VHOSTS['cat1'] = 'cat-draw-pws.calottery.com'
    __CA_CHECKATICKET_VHOSTS['sit-mobile'] = 'sit-draw-mobile.calottery.com'
    __CA_CHECKATICKET_VHOSTS['sit'] = 'sit-draw-pws.calottery.com'
    __CA_CHECKATICKET_VHOSTS['cat2-mobile'] = __CA_CHECKATICKET_VHOSTS['sit-mobile']
    __CA_CHECKATICKET_VHOSTS['cat2'] = __CA_CHECKATICKET_VHOSTS['sit']
    __CA_CHECKATICKET_VHOSTS['pdc-mobile'] = 'draw-mobile.calottery.com'
    __CA_CHECKATICKET_VHOSTS['pdc'] = 'draw-pws.calottery.com'
    __CA_CHECKATICKET_VHOSTS['prod-mobile'] = __CA_CHECKATICKET_VHOSTS['pdc-mobile']
    __CA_CHECKATICKET_VHOSTS['prod'] = __CA_CHECKATICKET_VHOSTS['pdc']

    __GAMES = []
    __GAMES.append('DAILY3')
    __GAMES.append('DAILY4')
    __GAMES.append('DAILYDERBY')
    __GAMES.append('FANTASY5')
    __GAMES.append('KENO')
    __GAMES.append('MEGAMILLIONS')
    __GAMES.append('POWERBALL')
    __GAMES.append('RAFFLE')
    __GAMES.append('SUPERLOTTO')
