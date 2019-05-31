from fais import nasagatherer as nasa
from fais import usgsgatherer as usgs

if __name__ == "__main__":
    usgs_criteria = usgs.create_usgs_criteria("SC","02172035", ["00065", "00045","00060"], "2016-10-06", "2016-10-07")
    usgs.get_flood_data_csv(usgs_criteria, "sc_02172035.csv")
    usgs_criteria = usgs.create_usgs_criteria("SC","02172040", ["00065", "00045","00060"], "2016-10-06", "2016-10-07")
    usgs.get_flood_data_csv(usgs_criteria, "sc_02172040.csv")

