"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):#max  time
    """
    Args:
       control_dist_km:  number, the control_dist_km distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control_dist_km open time.
       This will be in the same time zone as the brevet start time.
    """
    TABLE = [[200,34],[300,32],[400,32],[600,30],[1000,28]]
    MAX = 0

    #if (control_dist_km > (brevet_dist_km * 1.2)):
        #return arrow.get(brevet_start_time).replace( =- 182).isoformat()

    for brevet_dist_km, speed in TABLE:#if we find these in the table
        if brevet_dist_km > control_dist_km:#and its appropriately sized
            MAX += control_dist_km/speed#max becomes preformatted calculated val

    minute = MAX % 1#removes the whole # before the decimal from the val
    hour = MAX - minute
    minute = round(minute * 60)
    startime = arrow.get(brevet_start_time)
    startime = startime.replace(hours =+ hour)
    startime = startime.replace(minutes =+ minute)

    return startime.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):#min time
    """
    Args:
       control_dist_km:  number, the control_dist_km distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control_dist_km close time.
       This will be in the same time zone as the brevet start time.
    """
    TABLE = [[200,15],[300,15],[400,15],[600,11.428],[1000,13.333]]
    MAX = 0

    #if (control_dist_km > (brevet_dist_km * 1.2)):
        #return arrow.get(brevet_start_time).replace( =- 182).isoformat()

    for brevet_dist_km, speed in TABLE:#if we find these in the table
        if brevet_dist_km > control_dist_km:#and its appropriately sized
            MAX += control_dist_km/speed#max becomes preformatted calculated val

    minute = MAX % 1
    hour = MAX - minute
    minute = round(minute * 60)
    startime = arrow.get(brevet_start_time)
    startime = startime.replace(hours =+ hour)
    startime = startime.replace(minutes =+ minute)

    return startime.isoformat()
