DATA FLOW DIAGRAM:-



User Input (Region) -> Python Application -> COVID-19 Statistics API (e.g., disease.sh)

                ^                                            |

                |                                            v

        Display COVID-19 Statistics <- JSON Response <- API Request



COVIS-19 STATISTICS TRACKING APPLICATION:-



import requests



class Covid19StatisticsTracker:

    def _init_(self):

        self.base_url = 'https://disease.sh/v3/covid-19'



    def fetch_covid_stats(self, region):

        endpoint = f'/countries/{region}' if region else '/all'

        url = self.base_url + endpoint



        try:

            response = requests.get(url)

            data = response.json()



            if response.status_code == 200:

                return data  # Return JSON data received from API

            else:

                print(f"Error fetching data: {data['message']}")

                return None



        except requests.exceptions.RequestException as e:

            print(f"Error fetching data: {e}")

            return None



    def display_covid_stats(self, data):

        if data:

            # Extract relevant COVID-19 statistics

            cases = data.get('cases', 'N/A')

            deaths = data.get('deaths', 'N/A')

            recovered = data.get('recovered', 'N/A')

            active = data.get('active', 'N/A')



            # Displaying COVID-19 statistics

            print(f"COVID-19 Statistics:")

            print(f"Total Cases: {cases}")

            print(f"Total Deaths: {deaths}")

            print(f"Total Recovered: {recovered}")

            print(f"Active Cases: {active}")

        else:

            print("No COVID-19 data available for the specified region.")



# Example usage:

if _name_ == "_main_":

    tracker = Covid19StatisticsTracker()

    region = input("Enter country name (leave blank for global stats): ")

    covid_data = tracker.fetch_covid_stats(region)

    tracker.display_covid_stats(covid_data)



Documentation

API Integration and Methods

API Integration:



The application integrates with the disease.sh COVID-19 API to fetch real-time statistics.

Constructs the API request dynamically based on user input (country name) to fetch statistics for a specific region or global statistics.

Fetch COVID-19 Statistics (fetch_covid_stats method):



Sends an HTTP GET request to the appropriate endpoint (/all for global stats or /countries/{country} for country-specific stats).

Handles JSON response to extract COVID-19 statistics including total cases, deaths, recoveries, and active cases.

Display COVID-19 Statistics (display_covid_stats method):



Parses JSON response to extract and display relevant COVID-19 statistics.

Handles cases where no data is available for the specified region.

Assumptions

Data Availability: Assumes real-time availability and updates from the disease.sh API.

Region Input: Users input country names primarily; can be extended to handle state or city names based on API capabilities.

API Reliability: Assumes the disease.sh API is reliable and returns accurate data.

Potential Improvements

Historical Data: Incorporate historical COVID-19 data for trend analysis and visualization.

Visualization: Develop graphical charts and maps to visualize COVID-19 statistics for easier interpretation.

Notifications: Implement notifications or alerts for significant changes in COVID-19 statistics.

Localized Data: Enhance support for retrieving and displaying regional data (e.g., state-level data within a country).

By implementing these improvements, the COVID-19 statistics tracking application can provide more comprehensive insights and support for decision-making within healthcare organizations and public health agencies.
