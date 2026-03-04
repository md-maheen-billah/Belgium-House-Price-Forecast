import pandas as pd
import numpy as np
import math

class DataCleaner():

    @staticmethod
    def check(data: pd.DataFrame):
        print("------DataFrame check------")
        print("Records count: ", data.shape[0], sep = '')
        print(data.head(10))
    
    @staticmethod
    def optimize(data: pd.DataFrame) -> pd.DataFrame:
        data = DataCleaner.trim_edges(data, 0.05)
        data = data.replace([0, "To demolish", "Under construction", "To restore"], np.nan)
        condition = data["Type of property"] == "apartment"
        sublist = ["Surface of the land"]
        data.loc[condition, sublist] = data.loc[condition, sublist].fillna(0)
        data = data.drop(["Number of rooms", "Garden Area", "Terrace Area"], axis = 1)
        data = data.dropna()
        data = data.rename(columns = {
            "Locality": "locality",
            "Type of property": "type",
            "Subtype of property":"subtype",
            "Price": "price",
            "Living Area": "living_area",
            "Terrace": "terrace",
            "Garden": "garden",
            "Surface of the land": "land_area",
            "Number of facades": "facades",
            "State of the building": "state",
            "Furnished": "furnished",
            "Swimming pool": "pool"
        })
        data = data.reset_index(drop = True)
        data = data.replace({
            "To renovate": 1,
            "To be renovated": 2,
            "Normal": 4,
            "Fully renovated": 6,
            "Excellent": 7,
            "New": 8
        })
        print("Optimizer: FINISHED")
        return data

    @staticmethod
    def trim_edges(data: pd.DataFrame, persents: float) -> pd.DataFrame:
        """
        Removes 5% of the data from the beginning and 5% from the end.
        Returns the trimmed list.
        """

        if data is None or data.empty:
            print("No data provided.")
            return data

        total_rows = len(data)
        trim_count = math.floor(total_rows * persents)

        if total_rows <= trim_count * 2:
            print("Dataset too small to trim 5% from both ends.")
            return data

        trimmed_data = data.iloc[trim_count: total_rows - trim_count]

        print(f"Trimmed {trim_count} rows from start and end.")
        return trimmed_data