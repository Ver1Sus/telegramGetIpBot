import requests, urllib3, json




def getInfo(userIp):
    '''
    return info about user, Uses free API on  https://ipapi.co/

    :param userIp:
    :return:
        JSON - ALL ok
        1 - error, page return not 200 OK

    '''
    info = {'status':'0',
            'city':'',
            'region':'',
            'country':'',
            'latitude':	'',
            'longitude': ''}

    # ---- Remove errors about SNI and TLS
    urllib3.disable_warnings()

    result = 'https://ipapi.co/{0}/json/'.format(userIp)

    r = requests.get(result, verify=False)


    if r.status_code != 200:
        return 1

    # print r.text
    alljson =  r.json()

    # info.update(alljson)

    return alljson

if __name__ == '__main__':
    j =  getInfo('188.234.192.203')
    print str(j['city'])