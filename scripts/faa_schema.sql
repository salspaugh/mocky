DROP TABLE IF EXISTS faa;
CREATE TABLE faa (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Year INTEGER,
    Quarter INTEGER,
    Month INTEGER,
    DayofMonth INTEGER,
    DayOfWeek INTEGER,
    FlightDate TEXT,
    UniqueCarrier TEXT,
    AirlineID INTEGER,
    Carrier VARCHAR,
    TailNum INTEGER,
    FlightNum INTEGER,
    OriginAirportID INTEGER,
    OriginAirportSeqID INTEGER,
    OriginCityMarketID INTEGER,
    Origin TEXT,
    OriginCityName TEXT,
    OriginState TEXT,
    OriginStateFips INTEGER,
    OriginStateName TEXT,
    OriginWac INTEGER,
    DestAirportID INTEGER,
    DestAirportSeqID INTEGER,
    DestCityMarketID INTEGER,
    Dest TEXT,
    DestCityName TEXT,
    DestState TEXT,
    DestStateFips INTEGER,
    DestStateName TEXT,
    DestWac INTEGER,
    CRSDepTime INTEGER,
    DepTime INTEGER,
    DepDelay INTEGER,
    DepDelayMinutes INTEGER,
    DepDel15 INTEGER,
    DepartureDelayGroups TEXT,
    DepTimeBlk TEXT,
    TaxiOut INTEGER,
    WheelsOff INTEGER,
    WheelsOn INTEGER,
    TaxiIn INTEGER,
    CRSArrTime INTEGER,
    ArrTime INTEGER,
    ArrDelay INTEGER,
    ArrDelayMinutes INTEGER,
    ArrDel15 INTEGER,
    ArrivalDelayGroups TEXT,
    ArrTimeBlk TEXT,
    Cancelled INTEGER,
    CancellationCode INTEGER,
    Diverted INTEGER,
    CRSElapsedTime INTEGER,
    ActualElapsedTime INTEGER,
    AirTime INTEGER,
    Flights INTEGER,
    Distance INTEGER,
    DistanceGroup TEXT,
    CarrierDelay INTEGER,
    WeatherDelay INTEGER,
    NASDelay INTEGER,
    SecurityDelay INTEGER,
    LateAircraftDelay INTEGER,
    FirstDepTime INTEGER,
    TotalAddGTime INTEGER,
    LongestAddGTime INTEGER,
    DivAirportLandings INTEGER,
    DivReachedDest INTEGER,
    DivActualElapsedTime INTEGER,
    DivArrDelay INTEGER,
    DivDistance INTEGER,
    Div1Airport INTEGER,
    Div1AirportID INTEGER,
    Div1AirportSeqID INTEGER,
    Div1WheelsOn INTEGER,
    Div1TotalGTime INTEGER,
    Div1LongestGTime INTEGER,
    Div1WheelsOff INTEGER,
    Div1TailNum INTEGER,
    Div2Airport INTEGER,
    Div2AirportID INTEGER,
    Div2AirportSeqID INTEGER,
    Div2WheelsOn INTEGER,
    Div2TotalGTime INTEGER,
    Div2LongestGTime INTEGER,
    Div2WheelsOff INTEGER,
    Div2TailNum INTEGER,
    Div3Airport INTEGER,
    Div3AirportID INTEGER,
    Div3AirportSeqID INTEGER,
    Div3WheelsOn INTEGER,
    Div3TotalGTime INTEGER,
    Div3LongestGTime INTEGER,
    Div3WheelsOff INTEGER,
    Div3TailNum INTEGER,
    Div4Airport INTEGER,
    Div4AirportID INTEGER,
    Div4AirportSeqID INTEGER,
    Div4WheelsOn INTEGER,
    Div4TotalGTime INTEGER,
    Div4LongestGTime INTEGER,
    Div4WheelsOff INTEGER,
    Div4TailNum INTEGER,
    Div5Airport INTEGER,
    Div5AirportID INTEGER,
    Div5AirportSeqID INTEGER,
    Div5WheelsOn INTEGER,
    Div5TotalGTime INTEGER,
    Div5LongestGTime INTEGER,
    Div5WheelsOff INTEGER,
    Div5TailNum INTEGER
);
