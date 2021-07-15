# from collections import OrderedDict
import json
dict = {'ravi':'10','anu':'9','sanny':'15','yash':'29','suraj':'32'}
# dict1 = OrderedDict(sorted(dict.items()))
# print(dict1)
data=json.dumps(dict,indent=1,sort_keys=True)
print(data)
