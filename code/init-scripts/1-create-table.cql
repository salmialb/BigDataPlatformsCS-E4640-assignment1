use mysimbdp_coredms;
CREATE TABLE IF NOT EXISTS covid (date date, day int, month int, year int, deaths int, countriesAndTerritories text, geoId text, countryterritoryCode text, popData2019 int, continent text, cumulative_number_for_14_days_of_COVID_19_cases_per_100000 float, PRIMARY KEY(date));
