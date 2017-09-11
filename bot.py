from irc import IRC
from pull import pullSite
from time import sleep
import os
import random

channel = "#TropicalWeather"
server = "irc.snoonet.org"
nickname = "_USGS"


def sendSite(data):

    irc.send(channel, "\2" + data[u'value'][u'timeSeries'][0][u'sourceInfo'][u'siteName'])

    for n in data[u'value'][u'timeSeries'][:]:
        if len(n) > 0:

            #irc.send(channel, n['variable']['variableName'])
            varible_text = n['variable']['variableName']

            for v in n['values'][:]:
                irc.send(channel, "\2 " + v['value'][0]['value'] + " " + n['variable']['unit']['unitCode'] + " "  + " @ \2" + v['value'][0]['dateTime'] + " " + varible_text)  # hard coded two integers
                sleep(.3)


def checkSite(data):

    if data == 4:
        irc.send(channel, "Site query \2FAILED\2, incorrect SITE_ID. must be at least 8 numbers in length  \
                          \2Site Mapper\2 https://maps.waterdata.usgs.gov/mapper/index.html")
        return 1
    if data == 0:
        irc.send(channel, "Site query \2FAILED\2, please check your site ID and try again")
        return 1
    if len(data[u'value'][u'timeSeries'][:]) <= 0:
        irc.send(channel, "Site \2data is missing\2, please check your site number is correct, or try a different site.")
        return 1
    else:
        return 0





irc = IRC()
irc.connect(server)
irc.get_text()
irc.user(nickname)
irc.get_text()
irc.nick(nickname)
irc.get_text()
sleep(2)
irc.join(channel)
irc.get_text()



while 1:
    text = irc.get_text()  # print irc.get_text()
    #print text

    if "PRIVMSG" in text and channel in text and "!usgs" in text:

        text_list = text.split('!usgs')[1]              # Clean the data
        site_id = text_list.strip(' \r\n')

        print site_id                                   # Verbose
        output = pullSite(site_id)                          # Pass along the site_id and pull data
        if checkSite(output) == 0:
            sendSite(output)




    if "PRIVMSG" in text and channel in text and "usgs help" in text:
        irc.send(channel,
                 "USGS 0.1 Usage !usgs SITE_ID")
        print text


