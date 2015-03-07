#!/usr/bin/env python2
"""
@author: Evan A. Sultanik
http://www.sultanik.com/
"""

import smtplib

CARRIERS = {
    "Austria" : {
        "MaxMobil" : "max.mail.at",
        "One Connect" : "onemail.at",
        "T-Mobile" : 	"sms.t-mobile.at"
    },
    "Australia" : {
        "Blue Sky Frog" : 	"blueskyfrog.com",
        "Optus Mobile" : 	"optusmobile.com.au"
    },
    "Belgium" : {
        "Mobistar" : 	"mobistar.be"
    },
    "Bermuda" : {
        "Mobility" : 	"ml.bm"
    },
    "Brazil" : {
        "Nextel" : 	"nextel.com.br"
    },
    "Canada" : {
        "Bell Mobility" : 	"txt.bell.ca",
        "Bell Mobility" : 	"txt.bellmobility.ca",
        "Fido" : 	"fido.ca",
        "Microcell" : 	"fido.ca",
        "Manitoba Telecom Systems" : 	"text.mtsmobility.com",
        "NBTel" : 	"wirefree.informe.ca",
        "PageMart" : 	"pmcl.net",
        "PageNet" : 	"pagegate.pagenet.ca",
        "Rogers" : 	"pcs.rogers.com",
        "Telus" : 	"msg.telus.com"
    },
    "Chile" : {
        "Bell South" : 	"bellsouth.cl"
    },
    "Czech Republic" : {
        "Eurotel" : 	"sms.eurotel.cz",
        "Oskar" : 	"mujoskar.cz"
    },
    "Denmark" : {
        "Sonofon" : 	"note.sonofon.dk",
        "Tele Danmark Mobil" : 	"sms.tdk.dk",
        "Telia Denmark" : 	"gsm1800.telia.dk"
    },
    "Estonia" : {
        "EMT" : 	"sms.emt.ee"
    },
    "France" : {
        "SFR" : 	"sfr.fr"
    },
    "Germany" : {
        "T-Mobile" : 	"t-d1-sms.de",
        "Mannesmann Mobilefunk" : 	"d2-message.de",
        "E-Plus" : "eplus.de"
    },
    "Hungary" : {
        "PGSM" : 	"sms.pgsm.hu"
    },
    "India" : {
        "BPL mobile" : 	"bplmobile.com",
        "Chennai RPG Cellular" : 	"rpgmail.net",
        "Chennai Skycell / Airtel" : 	"airtelchennai.com",
        "Delhi Aritel" : 	"airtelmail.com",
        "Delhi Hutch" : 	"delhi.hutch.co.in",
        "Idea Cellular" : 	"ideacellular.net",
        "Orange" : 	"orangemail.co.in"
    },
    "Ireland" : {
        "Meteor" : 	"sms.mymeteor.ie",
    },
    "Italy" : {
        "Telecom Italia Mobile" : 	"posta.tim.it",
        "Vodafone Omnitel" : 	"vizzavi.it",
        "Vodafone" : 	"sms.vodafone.it"
    },
    "Japan" : {
        "Vodafone Japan" : 	"c.vodafone.ne.jp",
        "Vodafone Japan" : 	"h.vodafone.ne.jp",
        "Vodafone Japan" : 	"t.vodafone.ne.jp"
    },
    "Latvia" : {
        "Kyivstar" : 	"smsmail.lmt.lv",
        "LMT" : 	"smsmail.lmt.lv",
        "Tele2" : 	"sms.tele2.lv"
    },
    "Lebanon" : {
        "Cellis / LibanCell" : 	"ens.jinny.com.lb"
    },
    "Luxembourg" : {
        "P&T Luxembourg" : 	"sms.luxgsm.lu"
    },
    "Malaysia" : {
        "Celcom" : 	"sms.celcom.com.my  	 "
    },
    "The Netherlands" : {
        "Dutchtone / Orange-NL" : 	"sms.orange.nl"
    },
    "Norway" : {
        "Netcom" : 	"sms.netcom.no",
        "Telenor" : 	"mobilpost.no"
    },
    "Panama" : {
        "Cable and Wireless" : 	"cwmovil.com"
    },
    "Poland" : {
        "Plus GSM" : 	"text.plusgsm.pl"
    },
    "Portugal" : {
        "Telcel" : 	"sms.telecel.pt",
        "Optimus" : 	"sms.optimus.pt",
        "TMN" : 	"mail.tmn.pt"
    },
    "Russia" : {
        "BeeLine GSM" : 	"sms.beemail.ru",
        "MTS" : 	"sms.mts.ru",
        "Personal Communication" : 	"pcom.ru (number in subject line)",
        "Primtel" : 	"sms.primtel.ru",
        "SCS-900" : 	"scs-900.ru",
        "Uraltel" : 	"sms.uraltel.ru",
        "Vessotel" : 	"pager.irkutsk.ru"
    },
    "Serbia and Montenegro" : {
        "Mobtel Srbija" : 	"mobtel.co.yu"
    },
    "Singapore" : {
        "MiWorld" : 	"m1.com.sg",
        "Mobileone" : 	"m1.com.sg"
    },
    "Slovenia" : {
        "Mobitel" : 	"linux.mobitel.si",
        "Si Mobil" : 	"simobil.net"
    },
    "Spain" : {
        "Movistar" : 	"correo.movistar.net",
        "Vodafone" : 	"vodafone.es"
    },
    "Sweden" : {
        "Comviq GSM" : 	"sms.comviq.se",
        "Europolitan" : "europolitan.se"
    },
    "Switzerland" : {
        "Sunrise Mobile" : 	"freesurf.ch",
        "Sunrise Mobile" : 	"mysunrise.ch",
        "Swisscom" : 	"bluewin.ch"
    },
    "Tanzania" : {
        "Mobitel" : 	"sms.co.tz"
    },
    "Ukraine" : {
        "Golden Telecom" : 	"sms.goldentele.com",
        "Kyivstar" : 	"2sms.kyivstar.net",
        "UMC" : 	"sms.umc.com.ua"
    },
    "United Kingdom" : {
        "Orange" : 	"omail.net",
        "Orange" : 	"orange.net",
        "O2" : 	"o2.co.uk",
        "O2 (M-mail)" : 	"mmail.co.uk",
        "T-Mobile UK" : 	"t-mobile.uk.net",
        "Vodafone UK" : 	"vodafone.net",
    },
    "United States" : {
        "3 River Wireless" : 	"sms.3rivers.net",
        "Advantage Communications" : 	"advantagepaging.com",
        "AirVoice" : 	"mmode.com",
        "Airtouch Pagers" : 	"airtouch.net",
        "Alltel PCS" : 	"message.alltel.com",
        "Alltel" : 	"alltelmessage.com",
        "Ameritech Paging" : 	"pageapi.com",
        "Arch Pagers (PageNet)" : "archwireless.net",
        "AT&T" : "txt.att.net",
        "Bell South (Blackberry)" : "bellsouthtips.com",
        "Bell South Mobility" : 	"blsdcs.net",
        "Bell South" : 	"sms.bellsouth.com",
        "Bluegrass Cellular" : 	"sms.bluecell.com",
        "Boost Mobile" : 	"myboostmobile.com",
        "CallPlus" : 	"mmode.com",
        "Carolina Mobile Communications" : 	"cmcpaging.com",
        "Cellular One East Coast" : 	"phone.cellone.net",
        "Cellular One PCS" : 	"paging.cellone-sf.com",
        "Cellular One South West" : 	"swmsg.com",
        "Cellular One West" : 	"mycellone.com",
        "Cellular One" : 	"mobile.celloneusa.com",
        "Cellular South" : 	"csouth1.com",
        "Central Vermont Communications" : 	"cvcpaging.com",
        "CenturyTel" : 	"messaging.centurytel.net",
        "Cingular (GSM)" : 	"cingularme.com",
        "Cingular (TDMA)" : 	"mmode.com",
        "Cingular Wireless" : 	"mobile.mycingular.net",
        "Cingular" : 	"cingularme.com",
        "Communication Specialists" : 	"pageme.comspeco.net",
        "Cook Paging" : 	"cookmail.com",
        "Corr Wireless Communications" : 	"corrwireless.net",
        "Dobson Communications Corporation" : 	"mobile.dobson.net",
        "Dobson-Alex Wireless / Dobson-Cellular One" : 	"mobile.cellularone.com",
        "Edge Wireless" : 	"sms.edgewireless.com",
        "GCS Paging" : 	"webpager.us",
        "GTE" : 	"gte.pagegate.net",
        "Galaxy Corporation" : 	"sendabeep.net",
        "GrayLink / Porta-Phone" : 	"epage.porta-phone.com",
        "Houston Cellular" : 	"text.houstoncellular.net",
        "Inland Cellular Telephone" : 	"inlandlink.com",
        "JSM Tele-Page" : 	"jsmtel.com",
        "Lauttamus Communication" : 	"e-page.net",
        "MCI Phone" : 	"mci.com",
        "MCI" : 	"pagemci.com",
        "Metro PCS" : 	"mymetropcs.com",
        "Metrocall 2-way" : 	"my2way.com",
        "Metrocall" : 	"page.metrocall.com",
        "Midwest Wireless" : 	"clearlydigital.com",
        "Mobilecom PA" : 	"page.mobilcom.net",
        "Mobilfone" : 	"page.mobilfone.com",
        "Morris Wireless" : 	"beepone.net",
        "NPI Wireless" : 	"npiwireless.com",
        "Sprint Nextel" : 	"messaging.nextel.com",
        "Ntelos" : 	"pcs.ntelos.com",
        "Omnipoint" : 	"omnipoint.com",
        "OnlineBeep" : 	"onlinebeep.net",
        "PCS One" : 	"pcsone.net",
        "Pacific Bell" : 	"pacbellpcs.net",
        "PageMart" : 	"pagemart.net",
        "PageOne NorthWest" : 	"page1nw.com",
        "Pioneer / Enid Cellular" : 	"msg.pioneerenidcellular.com",
        "Powertel" : "ptel.net",
        "Price Communications" : 	"mobilecell1se.com",
        "ProPage" : 	"page.propage.net",
        "Public Service Cellular" : 	"sms.pscel.com",
        "Qualcomm" : 	"pager.qualcomm.com",
        "Qwest" : 	"qwestmp.com",
        "RAM Page" : 	"ram-page.com",
        "ST Paging" : 	"page.stpaging.com",
        "Safaricom" : 	"safaricomsms.com",
        "Satelindo GSM" : 	"satelindogsm.com",
        "Satellink" : "satellink.net",
        "Simple Freedom" : 	"text.simplefreedom.net",
        "Skytel Pagers" : 	"email.skytel.com",
        "Smart Telecom" : 	"mysmart.mymobile.ph",
        "Southern LINC" : 	"page.southernlinc.com",
        "Southwestern Bell" : 	"email.swbw.com",
        "Sprint PCS" : 	"messaging.sprintpcs.com",
        "Sprint" : 	"sprintpaging.com",
        "SunCom" : 	"tms.suncom.com",
        "Surewest Communications" : 	"mobile.surewest.com",
        "T-Mobile" : 	"tmomail.net",
        "TIM" : 	"timnet.com",
        "TSR Wireless" : 	"alphame.com",
        "Teletouch" : 	"pageme.teletouch.com",
        "Telus" : 	"msg.telus.com",
        "The Indiana Paging Co" : 	"pager.tdspager.com",
        "Triton" : 	"tms.suncom.com",
        "US Cellular" : 	"email.uscc.net",
        "USA Mobility" : 	"mobilecomm.net",
        "Unicel" : 	"utext.com",
        "Verizon PCS" : 	"myvzw.com",
        "Verizon Pagers" : 	"myairmail.com",
        "Verizon" : 	"vtext.com",
        "Virgin Mobile" : 	"vmobl.com",
        "WebLink Wireless" : 	"pagemart.net",
        "West Central Wireless" : 	"sms.wcc.net",
        "Western Wireless" : 	"cellularonewest.com",
        "Wyndtell" : 	"wyndtell.com"
    }
}

class Emailer(object):
    def __init__(self, server_url, username, password, from_address = None, port = 587):
        if from_address is None:
            self.sender = username
        else:
            self.sender = from_address
        self.url = server_url
        self.port = port
        self.__username = username
        self.__password = password
    def send(self, to_address, message):
        server = smtplib.SMTP('%s:%d' % (self.url, self.port))
        server.starttls()
        server.login(self.__username, self.__password)
        server.sendmail(self.sender, to_address, message)
        server.quit()

class SMSSender(object):
    def __init__(self, emailer, carrier_name = None, country_name = None, email_address = None):
        self.emailer = emailer
        if email_address is not None:
            self.email = email_address
        elif carrier_name is None:
            raise ValueError("Either carrier_name or email_address must be provided!")
        else:
            if country_name is None:
                # see if the carrier name is unique among the countries:
                matched_address = None
                matched_countries = []
                for country, carriers in CARRIERS.iteritems():
                    if carrier_name in carriers:
                        matched_countries.append(country)
                        matched_address = carriers[carrier_name]
                if matched_address is None:
                    raise ValueError("A carrier named %s was not found!" % carrier_name)
                elif len(matched_countries) > 1:
                    raise ValueError("The carrier name %s is ambiguous since it exists in countries %s; please provide a country_name to disambiguate." % (carrier_name, matched_countries))
                else:
                    self.email = matched_address
            else:
                if country_name not in CARRIERS:
                    raise ValueError("No known country named %s" % country_name)
                elif carrier_name not in CARRIERS[country_name]:
                    raise ValueError("No known carrier named %s in %s" % (carrier_name, country_name))
                else:
                    self.email = CARRIERS[country_name][carrier_name]

    def send(self, phone_number, message):
        self.emailer.send("%s@%s" % (phone_number, self.email), message)

if __name__ == "__main__":
    import getpass
    import argparse

    argparser = argparse.ArgumentParser(description='PyEmail2SMS Pure Python E-Mail SMS Gateway.')

    argparser.add_argument("SERVER", help="URL of the SMTP server to use.")
    argparser.add_argument("USERNAME", help="Username of the E-Mail address from which to send.")
    argparser.add_argument("PHONE", help="Phone number of the recipient")
    argparser.add_argument("CARRIER", help="Carrier name of the recipient's phone number.")
    argparser.add_argument("--pass", dest="passwd", default=None, help="Optional password for the username (will be prompted if this argument is omitted).")
    argparser.add_argument("--port", "-p", default=587, type=int, help="Server port.")
    argparser.add_argument("--country", "-c", default=None, help="Optional country name of the recipient's phone number, to help disambiguate international carriers.")
    argparser.add_argument("--send-from", "-s", default=None, help="Optional E-Mail address from which to send the message (defaults to USERNAME).")

    args = argparser.parse_args()

    password = args.passwd

    sender = args.send_from
    if sender is None:
        sender = args.USERNAME
    
    if password is None:
        password = getpass.getpass("SMTP Password for " + sender + ": ")

    exit(0)

    emailer = Emailer(server_url = args.SERVER, username = args.USERNAME, password = password, from_address = sender, port = port)
    sender = SMSSender(emailer, "AT&T")
    sender.send("asdf", "foo")
