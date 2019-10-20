import googlemaps
from datetime import datetime

def calculate_cost(reqTray, shelters):
    # reqTray = [{
    #     'name': 'R1',
    #     'feeds': 50,
    #     'location': (41.8903425, -87.6337034)
    # }, {
    #     'name': 'R2',
    #     'feeds': 100,
    #     'location': (41.921938,-87.6665399)
    #     # 'location': (41.8903425, -87.6337034)
    # }, ]

    # shelters = [{"name": "S1", "n_people": 20, "location": (41.8775762,-87.6294064), 'distance_from_r': 5},
    #             {"name": "S2", "n_people": 30, "location": (41.8889812,-87.6361723), 'distance_from_r': 10},
    #             {"name": "S3", "n_people": 100, "location": (41.8364014,-87.6183985), 'distance_from_r': 15}]

    rad = 10.0
    cost_estimate = []
    for req in reqTray:
        route = []
        print("route -> ",route)
        shels = []
        route.append({'req': req})
        feeds = req['feeds']
        for sh in [s for s in shelters if distance(req['location'],s['location']) <= rad]:

            if feeds < sh['n_people']:
                continue
            else:
                route.append({"sh": sh})
                shels.append(sh)
                if feeds - sh['n_people'] <= 0:
                    break
                else:
                    feeds -= sh['n_people']
        if len(route) > 1:
            cost_estimate.append({'req': req, 'shelters': shels, "route": route})
            for she in shels:
                shelters.remove(she)
    for reqT in cost_estimate:
        reqTray.remove(reqT['req'])
    print("Cost Estimate: ", cost_estimate)
    print("reqTray: ", reqTray)


def distance(source, des):
    gmaps = googlemaps.Client(key='AIzaSyBWbE4lqt9GscKwyV4I1nS1F6bcLBHSNhE')

    # geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    # geocode_result = gmaps.distance_matrix((41.8363974,-87.6183985),(41.8348731,-87.6270059))
    geocode_result = gmaps.distance_matrix(source, des)
    print(geocode_result['rows'][0]['elements'][0]['distance']['text'].split(" ")[0])
    return float(geocode_result['rows'][0]['elements'][0]['distance']['text'].split(" ")[0])

# distance(0,1)
# findRoute()
