import scrapy
import json


class PubchemSpider(scrapy.Spider):
    name = "pubchem"
    # allowed_domains = ["pubchem.ncbi.nlm.nih.gov"]
    start_urls = ["https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON"]

    def parse(self, response):
        data = json.loads(response.body)
        cell = data["Table"]["Row"]

        for i in cell:  
            atomic_number = i["Cell"][0]
            symbol = i["Cell"][1]  
            name = i["Cell"][2]
            atomic_mass = i["Cell"][3]
            CPKHexColor = i["Cell"][4]
            ElectronConfiguration = i["Cell"][5]
            Electronegativity = i["Cell"][6]
            AtomicRadius = i["Cell"][7]
            IonizationEnergy = i["Cell"][8]
            ElectronAffinity = i["Cell"][9]
            OxidationStates = i["Cell"][10]
            StandardState = i["Cell"][11]
            MeltingPoint = i["Cell"][12]
            BoilingPoint = i["Cell"][13]
            Density = i["Cell"][14]
            GroupBlock = i["Cell"][15]
            YearDiscovered = i["Cell"][16]
            
            yield { "symbol":symbol,
                    "name":name,
                    "atomic_number":atomic_number,
                    "atomic_mass":atomic_mass,
                    "CPKHexColor":CPKHexColor,
                    "ElectronConfiguration":ElectronConfiguration,
                    "Electronegativity":Electronegativity,
                    "AtomicRadius":AtomicRadius,
                    "IonizationEnergy":IonizationEnergy,
                    "ElectronAffinity":ElectronAffinity,
                    "OxidationStates":OxidationStates,
                    "StandardState":StandardState,
                    "MeltingPoint":MeltingPoint,
                    "BoilingPoint":BoilingPoint,
                    "Density":Density,
                    "GroupBlock":GroupBlock,
                    "YearDiscovered":YearDiscovered,
                    }
            



 
    