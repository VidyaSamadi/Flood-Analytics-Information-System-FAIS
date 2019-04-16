import fais.USGSFloodCriteria as criteria
import fais.USGSFloodManager as usgs

#   Create the criteria for USGS data queary
#   This criteria is used in getting USGS data
#   Return the empty criteria if not successfully
def check_states(state):
    state = state.upper()
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    for region in states:
        if region == state:
            return True    
    print("The state is not match please enter the US's state abbriviation")
    return False

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
    return usgs_criteria

def update_state(criteria=None, state=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if state == None:
        print("region missing")
        return
    elif check_states(state):
        criteria.setRegion(state)
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
    return criteria

def update_until(criteria=None, until=None):
    if criteria == None:
        print("Criteria missing please include the criteria")
        return
    if until == None:
        print("until missing")
        return
    criteria.setParameters(until)
    return criteria

def get_realtime_flood_dataframe(state):
    flood_manager = usgs.usgsFloodManager()
    if check_states(state):
        realtime_data = flood_manager.getRealTimeWaterWatch(state)
        return realtime_data
    print("The state not exist, please enter correct states")
    return False

def get_realtime_flood_csv(state, filename):
    df = get_realtime_flood_dataframe(state)
    if ".csv" not in filename:
        filename = filename + ".csv"
        df.to_csv(filename)
        return True
    df.to_csv(filename)


def get_station_list_dataframe(state):
    df = get_realtime_flood_dataframe(state)
    df_station = df.iloc[:,0:4]
    return df_station

def get_station_list_csv(state, filename):
    df = get_station_list_dataframe(state)
    if ".csv" not in filename:
        filename = filename + ".csv"
        df.to_csv(filename)
        return True
    df.to_csv(filename)

def get_flood_data_dataframe(criteria):
    flood_manager = usgs.usgsFloodManager()
    df = flood_manager.getFloodData(criteria)
    return df

def get_flood_data_csv(criteria,filename):
    df = get_flood_data_dataframe(criteria)
    if ".csv" not in filename:
        filename = filename + ".csv"
        df.to_csv(filename)
        return True
    df.to_csv(filename)
    
def get_river_cam_sc_grey(station):
    flood_manager = usgs.usgsFloodManager()
    for camera in flood_manager.cameras:
        if camera.id == station:
            cams = flood_manager.getImageWaterWatch(station,True)
            return cams
    print("The station is not exist in South Carolina River Cams")
    return False

def get_river_cam_sc_color(station):
    flood_manager = usgs.usgsFloodManager()
    for camera in flood_manager.cameras:
        if camera.id == station:
            cams = flood_manager.getImageWaterWatch(station)
            return cams
    print("The station is not exist in South Carolina River Cams")
    return False
