class DataManager():
    
    @staticmethod
    def ranges_export():
        pass
    
    @staticmethod
    def ranges_import() -> list[dict[str: int]]:
        pass

    @staticmethod
    def links_export(links: list[str]):
        with open("./links.txt", "w") as file:
            for link in links.links:
                file.write(f"{link}\n")
    
    @staticmethod
    def links_import() -> list[str]:
        with open(("./links.txt", "r")) as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines