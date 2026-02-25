class DataManager():

    @staticmethod
    def links_export(links: list[str]):
        """Exporting links to .txt"""
        with open("./data/links.txt", "w") as file:
            for link in links:
                file.write(f"{link}\n")
    
    @staticmethod
    def links_import() -> list[str]:
        """Importing links from .txt"""
        with open("./data/links.txt", "r") as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines

    def data_csv_export(data: list[dict[str: str]]):
        """Exporting data list (list of dicts) into ./data/dataset.csv"""
    import csv

    data = [
        {
            'Locality': 'Froidchapelle',
            'Type of property': 'house',
            'Subtype of property': 'chalet',
            'Price': 100000,
            'Type of sale': 'Normal sale',
            'Number of rooms': 2,
            'Living Area': 50,
            'Terrace Area': 6,
            'Garden Area': 250,
            'Surface of the land': 250,
            'Number of facades': 4,
            'State of the building': 'Excellent',
            'Furnished': 0,
            'Terrace': 1,
            'Garden': 1,
            'Swimming pool': 0
        }
    ]

    file_name = "real_estate_data.csv"

    columns = list(data[0].keys())

    file = open(file_name, "w", newline="", encoding="utf-8")

    writer = csv.DictWriter(file, columns)

    writer.writeheader()

    for row in data:
        writer.writerow(row)

    file.close()

    print("CSV file created")


    def data_csv_import():
        pass