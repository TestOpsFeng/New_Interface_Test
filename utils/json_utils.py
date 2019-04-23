import json,os

# file_name = 'ware_housing.yaml'
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
dir = os.path.join(fileNamePath,'../conf')

def get_json(file_name,file_path=dir):
    file = os.path.join(file_path, file_name)
    with open(file, 'rb') as f:
        return json.load(f)


if __name__ == '__main__':
    data = get_json("ware_housing.json")
    print(data["data"])