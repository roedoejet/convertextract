import pympi
from convertextract.parsers.utils import BaseParser

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
            return converted_filename
        print("SUCCESS", converted_filename)
        # # Here is where you should parse and convert the Elan file
        # eaf_obj = pympi.Elan.Eaf()
        # elan_data = pympi.Elan.parse_eaf(filename, eaf_obj)
        # tiers = elan_data.get_tier_names() #returned as a list
        # for tier in tiers:
        #     if tier == "aligned_annotations" or "reference_annotations":
        #         result = elan_data.get_annotation_data_for_tier(tier) #Gives a list of annotations of the form: (begin, end, value)
        #         annotation = result[2]

        # transducer(annotation).output_string

        # if "no_write" in kwargs or kwargs['no_write']:
        #     pass
        # else:
        #     elan_data.save(converted_filename)

        # return transducer(annotation).output_string


#if __name__ == '__main__':
#    print('helloooo')
    # put your stuff here

#convertextract path/to/foo.eaf -il eng-ipa -ol eng-arpabet