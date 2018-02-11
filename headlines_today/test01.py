dict = "{\"count\":18,\"sub_images\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/2ebe000042c272cd8ca4\",\"width\":650}]}"
print(dict)
import json
data = json.loads(dict)
print(data)
print(type(data))
