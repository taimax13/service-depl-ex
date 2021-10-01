import json
import redis


class AddData:
    def post(self, jsonF):
        with open(jsonF) as file:
            jObj = json.load(file)
            file.close()
        redis.Redis(host='redis', port=6379).mset(jObj)


def main():
    print("Init data")
    ad = AddData()
    ad.post("./students_list.json")
    print("end data")


if __name__ == '__main__':
    main()
