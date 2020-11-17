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

        # Here is where you should parse and convert the Elan file
        eaf_obj = pympi.Elan.Eaf(filename)
        new_eaf_obj = pympi.Elan.Eaf(filename)
        tiers = eaf_obj.get_tier_names() #returned as a list
        new_eaf_obj.remove_tiers(eaf_obj.get_tier_names())
        all_results = []
        for tier in tiers:
            new_eaf_obj.add_tier(tier)
            #iterates over each list within the tiers
            result = eaf_obj.get_annotation_data_for_tier(tier) #Gives a list of annotationS of the form: (begin, end, value)
            for res in result:
                value_res = str(res[2])
                new_res = transducer(value_res).output_string
                all_results.append(new_res)

                new_eaf_obj.add_annotation(tier, res[0], res[1], value = new_res)
        if "no_write" in kwargs and kwargs['no_write']:
            pass
        else:
            pympi.Elan.to_eaf(converted_filename, new_eaf_obj, pretty=True)
        return ' '.join(all_results)
        