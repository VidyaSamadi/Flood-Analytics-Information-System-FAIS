import fais.USGSFloodCriteria as criteria
import fais.USGSFloodManager as usgs

#   Create the criteria for twitter search
#   This criteria is used in getting twitter data
#   Return the empty criteria if not successfully
def check_region(region):
    if isinstance(region, str):
        return False
    region = region.upper()
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    contained = False
    for state in states:
        if state == region:
            contained = True
    if contained == False:
        print("The state is not match please enter the US's state abbriviation")
        return False
    return True

def create_usgs_criteria(region=None,station=None, parameters=None, since=None, until=None):
    usgs_criteria = criteria.usgsCriteria()
    is_valid = False
    if region != None and station != None and parameters != None:
        usgs_criteria.setRegion(region)
        is_valid=True
    if station != None:
        usgs_criteria.setStationNumber(station)
        is_valid = True
    if parameters != None:
        usgs_criteria.setParameters(parameters)
        is_valid = True
    if is_valid == False:
        print("The criteria is no valid please enter the region and station")
    if parameters != None:
        usgs_criteria.setParameters(parameters)
    if since != None:
        usgs_criteria.setSince(since)
    if until != None:
        usgs_criteria.setUntil(until)

def update_region(criteria=None, region=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if region == None:
        print("region missing")
        return
    elif check_region(region):
        criteria.setRegion(region)
        return criteria
    return

def update_station(criteria=None, station=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if station == None:
        print("station missing")
        return
    criteria.setStationNumber(station)
    return criteria

def update_parameter(criteria=None, parameters=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if parameters == None:
        print("parameters missing")
        return
    elif len(parameters) != 0:
        criteria.setParameters(parameters)
        return criteria
    return

def update_since(criteria=None, since=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if since == None:
        print("since missing")
        return
    criteria.setParameters(since)
    return criteriaE


def get_station_list(region):
    return True