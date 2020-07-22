from .utils import BaseParser

class Parser(BaseParser):
     """Extract text from ELAN file using pympi-ling.
    """

    def extract(self, filename, **kwargs):
        if 'mapping' in kwargs and kwargs['mapping']:
            transducer = self.create_transducer(kwargs['mapping'])
        else:
            transducer = self.get_transducer(kwargs.get('input_language', ''), 
                                             kwargs.get('output_language', ''))
        converted_filename = filename[:-4] + '_converted.eaf'
        
        # Here is where you should parse and convert the Elan file
        elan_data = pympi.Elan.parse_eaf(filename, eaf_obj???)
        for tier in elan_data:
            tiers = self.get_tier_names() #returned as a list


get_annotation_data_for_tier(id_tier)
#Gives a list of annotations of the form: (begin, end, value) When the tier contains reference annotations this will be returned, check get_ref_annotation_data_for_tier() for the format.
#Parameters:	id_tier (str) – Name of the tier.
#Raises KeyError:
# 	If the tier is non existent.


pympi.Elan.parse_eaf(file_path, eaf_obj)
# Parse an EAF file

# Parameters:	
# file_path (str) – Path to read from, - for stdin.
# eaf_obj (pympi.Elan.Eaf) – Existing EAF object to put the data in.
# Returns:	
# EAF object.
        


        # To get output just do transducer(INPUT).output_string
        if "no_write" not in kwargs or not kwargs['no_write']:
            # This should save the file!!!
            pass
        # This should return the converted text
        return