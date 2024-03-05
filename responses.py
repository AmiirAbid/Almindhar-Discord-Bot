from website_related_functionnalities import agent_finder,agency_finder, property_calculator, author_finder

def hanle_response (message) -> str :

    if message == '?agents today' :
        agents = agent_finder.find_agent_today()
        n_agents = len(agents)

        if n_agents == 0 :
            return '@everyone no agents have subscribed today'

        else :
            return f'@everyone {n_agents} agents have subscribed today\n{'\n'.join(agents)}'

    elif message == '?agents yesterday' :
        agents = agent_finder.find_agent_yesterday()
        n_agents = len(agents)

        if n_agents == 0 :
            return '@everyone no agents have subscribed yesterday'

        else :
            return f'@everyone {n_agents} agents have subscribed yesterday\n{'\n'.join(agents)}'

    elif message[:8] == '?agents ' :
        agents = agent_finder.find_agent_by_date(message[8:])
        n_agents = len(agents)

        if n_agents == 0 :
            return f'@everyone No agents have subscribed on {message[8:]}'

        else :
            return f'@everyone {n_agents} agents have subscribed on {message[8:]}\n{'\n'.join(agents)}'

    if message == '?agencies today' :
        agencies = agency_finder.find_agency_today()
        n_agencies = len(agencies)

        if n_agencies == 0 :
            return '@everyone no agencies have subscribed today'

        else :
            return f'@everyone {n_agencies} agencies have subscribed today\n{'\n'.join(agencies)}'

    elif message == '?agencies yesterday' :
        agencies = agency_finder.find_agency_yesterday()
        n_agencies = len(agencies)

        if n_agencies == 0 :
            return '@everyone no agencies have subscribed yesterday'

        else :
            return f'@everyone {n_agencies} agencies have subscribed yesterday\n{'\n'.join(agencies)}'

    elif message[:10] == '?agencies ' :
        agencies = agency_finder.find_agency_by_date(message[10:])
        n_agencies = len(agencies)

        if n_agencies == 0 :
            return f'@everyone No agencies have subscribed on {message[10:]}'

        else :
            return f'@everyone {n_agencies} agencies have subscribed on {message[10:]}\n{'\n'.join(agencies)}'

    elif message == '?properties today' :
        authors = property_calculator.find_property_today()
        n_properties = sum(authors.values())

        if n_properties == 0 :
            return '@everyone no properties were published today'

        else :
            output = f'@everyone {n_properties} properties were published today by:'
            for author in authors :
                author_name = author_finder.find_author(author)
                output += f'\n{author_name}: {str(authors[author])}'

            return output

    elif message == '?properties yesterday' :
        authors = property_calculator.find_property_yesterday()
        n_properties = sum(authors.values())

        if n_properties == 0 :
            return f'@everyone no properties were published yesterday'

        else :
            output = f'@everyone {n_properties} properties were published yesterday by:'
            for author in authors :
                author_name = author_finder.find_author(author)
                output += f'\n{author_name}: {str(authors[author])}'

            return output