import requests


def pullSite(site_id):

    payload = {'format': 'json', 'site': site_id}
    blob = requests.get('https://waterservices.usgs.gov/nwis/iv/?', params=payload)

    print(blob.url)
    http_status = blob.status_code
    print http_status
    #print blob.raise_for_status()

    if http_status == 400:
        return 4
    else:
        blob_json = blob.json()
        print blob_json
        return blob_json














