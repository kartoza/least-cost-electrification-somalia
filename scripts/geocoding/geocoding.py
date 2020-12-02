import csv
import sys
import requests


def change_file_into_json(filename: str) -> (list, list):
    """ Convert csv into json"""
    data = []
    headers = None
    with open(filename, mode='r', encoding='utf-8-sig') as _file:
        for line in csv.reader(_file):
            if not headers:
                headers = [column for column in line]
            else:
                data.append({headers[idx]: column for idx, column in enumerate(line)})
    return headers, data


def geocoding(data: list, country: str) -> list:
    """ Update data with geocoding that found"""
    # this is for cache
    nominatim_url = 'https://nominatim.openstreetmap.org/search'
    responses = {}
    total = len(data)
    output = []

    for idx, row in enumerate(data):
        print('{}/{}'.format(idx, total))
        longitude = row['Longitude']
        latitude = row['Latitude']

        if not longitude or not latitude:
            # let's call nominatim
            administrative = None
            for query in [row['Village'], row['District'], row['Region'], row['State']]:
                if not query:
                    continue

                # if it is already in cache
                if query in responses:
                    administrative = responses[query]
                    break

                # if not in cache, call nominatim
                payload = {'format': 'json', 'q': query}
                r = requests.get(nominatim_url, params=payload)
                try:
                    if r.status_code == 200:
                        for result in r.json():
                            display_name = result['display_name']
                            if country in display_name.lower():
                                responses[query] = result
                                administrative = result
                                break
                        if administrative:
                            break
                except IndexError:
                    pass

            if administrative:
                row['Query'] = query
                row['DisplayName'] = administrative['display_name']
                row['Latitude'] = administrative['lat']
                row['Longitude'] = administrative['lon']
        output.append(row)
    return output


# parse arguments
filename = None
output = None
try:
    filename = sys.argv[1]
except IndexError:
    print('You need to define the input file as first argument')
    exit()
try:
    output = sys.argv[2]
except IndexError:
    print('You need to define the output file as second argument')
    exit()
try:
    country = sys.argv[3]
except IndexError:
    country = ''

#
try:
    # make it as dictionary
    headers, data = change_file_into_json(
        filename)
    # geocoding and make output
    data = geocoding(data, country)
    headers.append('Query')
    headers.append('DisplayName')

    try:
        with open(output, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except IOError:
        print("I/O error")
except IndexError:
    print('You need to define the output file as second argument')
    exit()
except KeyError as e:
    print('{} column is needed'.format(e))
    exit()
except FileNotFoundError:
    print('File is not found')
    exit()
