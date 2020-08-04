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
        print("SUCCESS", converted_filename)
        # Here is where you should parse and convert the Elan file
        eaf_obj = pympi.Elan.Eaf(filename)
        new_eaf_obj = pympi.Elan.Eaf()
        tiers = eaf_obj.get_tier_names() #returned as a list
        all_results = []
        for tier in tiers:
            new_eaf_obj.add_tier(tier)
            #iterates over each list within the tiers
            try:
                result = eaf_obj.get_annotation_data_for_tier(tier) #Gives a list of annotationS of the form: (begin, end, value)
            except KeyError:
                print(f"tier named {tier} does not work")
                continue
            #eaf_obj.remove_all_annotations_from_tier(tier)
            for res in result:
                value_res = str(res[2])
                new_res = transducer(value_res).output_string
                all_results.append(new_res)
            
                # eaf_obj.remove_annotation(tier,(res[0]+res[1])/2)

                new_eaf_obj.add_annotation(tier, res[0], res[1], value = new_res)
            # new_res = transducer(value_res).output_string
            # eaf_obj.add_annotation(tier, result[0], result[1], value = new_res)
            # result = eaf_obj.get_annotation_data_for_tier(tier) 
            # all_results.append(new_res)
            #Gives a list of annotations of the form: (begin, end, value)
            #iterates over each list within the tiers

                #change value in place to a string
                #converts 'value' using g2p
                #adds converted data to all_results
                # value_res = str(res[2])
                # new_res = transducer(value_res).output_string

                # value_res.remove_all_annotations_from_tier(tiers)
                # value_res.add_annotation(tiers, value = "new_res")
        if "no_write" not in kwargs or kwargs['no_write']:
            pass
        else:
            print(f"should write to {converted_filename}")
            pympi.Elan.to_eaf(converted_filename, new_eaf_obj, pretty=True)
        return ' '.join(all_results)


#if __name__ == '__main__':
#    print('helloooo')
    # put your stuff here

#convertextract path/to/foo.eaf -il eng-ipa -ol eng-arpabet