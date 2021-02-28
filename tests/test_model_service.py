from services.model_service import predict_apartment_value


def test_predict_apartment_value_valid_json():
    test_data: str = """{
          "1":{
              "1":-117.130000
           },
           "2":{
              "1":32.700000
           },
           "complexAge":{
              "1":42.000000
           },
           "totalRooms":{
              "1":1210.000000
           },
           "totalBedrooms":{
              "1":292.000000
           },
           "complexInhabitants":{
              "1":945.000000
           },
           "apartmentsNr":{
              "1":258.000000
           },
           "8":{
              "1":0.899100
           },
           "medianCompexValue":{
              "1":78900.000000
           }
    }"""
    prediction = predict_apartment_value(test_data)
    assert len(prediction) == 1


def test_predict_apartment_value_invalid_json():
    test_data: str = """{
              "1":{
                  "1":-117.130000
               },
               "2":{
                  "1":32.700000
               },
               "complexAge":{
                  "1":42.000000
               },
               "totalRooms":{
                  "1":1210.000000
               },
               "totalBedrooms":{
                  "1":292.000000
               },
               "complexInhabitants":{
                  "1":945.000000
               },
               "apartmentsNr":{
                  "1":258.000000
               },
               "medianCompexValue":{
                  "1":78900.000000
               }
        }"""

    try:
        _prediction = predict_apartment_value(test_data)
    except:
        assert True, "Exception is thrown when the input format is not correct."
        return

    assert False, "An exception should be thrown if the format of input data is not correct."
