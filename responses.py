import agency_finder

def hanle_response (message) -> str :

    if message == '?agencies' :
        agencies = agency_finder.find_agency()
        n_agencies = len(agencies)

        if n_agencies == 0 :
            return 'No agencies have subscribed yesterday'

        else :
            return f'{n_agencies} agencies have subscribed\n{'\n'.join(agencies)}'

    elif message[:10] == '?agencies ' :
        agencies = agency_finder.find_agency_by_date(message[10:])
        n_agencies = len(agencies)

        if n_agencies == 0 :
            return f'No agencies have subscribed on {message[10:]}'

        else :
            return f'{n_agencies} agencies have subscribed on {message[10:]}\n{'\n'.join(agencies)}'
