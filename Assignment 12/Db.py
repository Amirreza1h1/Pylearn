from main import PRODUCTS
import Media
import Film
import Clip
import Series
import Documentary
import Actor

class Db:
    def read(self):
        file = open("database.txt", "r")
        for line in file:
            result = line.strip().split(",")
            if result[9]=='Film':
                # Assuming the format for casts and awards is consistent
                casts = []  # Array to store cast information
                awards = []  # Array to store awards information
                # Split the cast information from the line
                casts_info = result[10].split("//")
                for cast_info in casts_info:
                    # Assuming each cast info is comma-separated
                    cast_details = cast_info.strip().split(",")
                    # Assuming cast_details contains name, age, nationality, and height
                    casts.append(Actor(cast_details[0], cast_details[1], cast_details[2], cast_details[3]))
                # Split the awards information from the line
                awards_info = result[11].split("//")
                for award_info in awards_info:
                    # Assuming each award info is the name of the award
                    awards.append(award_info.strip())
                # Now you can create a Film object with this information
                PRODUCTS.append(Film(result[0], result[1], result[2], result[3], result[4], casts, result[5], result[6], result[7], result[8], result[9], result[10], awards))
            elif result[9]=='clip':
                casts = []  

                casts_info = result[10].split("//")
                for cast_info in casts_info:
                    cast_details = cast_info.strip().split(",")
                    casts.append(Actor(cast_details[0], cast_details[1], cast_details[2], cast_details[3]))
                
                PRODUCTS.append(Clip(result[0], result[1], result[2], result[3], result[4], casts, result[5], result[6], result[7], result[8], result[9], result[10]))
            elif result[9]=='Series':
                casts = []  

                casts_info = result[10].split("//")
                for cast_info in casts_info:
                    cast_details = cast_info.strip().split(",")
                    casts.append(Actor(cast_details[0], cast_details[1], cast_details[2], cast_details[3]))
                
                PRODUCTS.append(Series(result[0], result[1], result[2], result[3], result[4], casts, result[5], result[6], result[7], result[8], result[9], result[10],result[11]))
            elif result[9]=='Documentary':
                casts = []  

                casts_info = result[10].split("//")
                for cast_info in casts_info:
                    cast_details = cast_info.strip().split(",")
                    casts.append(Actor(cast_details[0], cast_details[1], cast_details[2], cast_details[3]))
                
                PRODUCTS.append(Documentary(result[0], result[1], result[2], result[3], result[4], casts, result[5], result[6], result[7], result[8], result[9]))
        file.close()
   
    def write(self):
        file = open("database.txt", "w")
        for obj in PRODUCTS:
            # Write common properties
            common_properties = ",".join([f"{key}:{value}" for key, value in vars(obj).items()])
            file.write(common_properties)

            # Write casts information
            if hasattr(obj, 'casts'):
                casts_info = "//".join([",".join([cast.name, cast.age, cast.nationality, cast.height]) for cast in obj.casts])
                file.write(f",{casts_info}")

            # Write awards information
            if hasattr(obj, 'awards'):
                awards_info = "//".join(obj.awards)
                file.write(f",{awards_info}")

            file.write("\n")
        file.close()
