import requests
from json import dumps
from urllib.parse import urljoin


class Noos:
    def __init__(self, server, user, password):
        self.server = server
        self.user = user
        self.password = password
        self.headers = {
            'User-Token': self.user,
            'Accept-Token': self.password,
        }

    def get(self, service, parameters=None):
        url = urljoin(self.server, service)
        return requests.get(url, headers=self.headers)

    def post(self, service, parameters=None, file_path=None):
        url = urljoin(self.server, service)
        files = {
            'filename': (file_path, open(file_path, 'rb'))
        } if file_path else None

        print('parameters:', parameters)
        return requests.post(
            url,
            data=parameters,
            headers=self.headers,
            files=files)


    ##################################################
    # UTILITY                                        #
    ##################################################
    def available_services(self):
        return self.get('available_services').json()

    ##################################################
    # COMPUTER VISION                                #
    ##################################################
    def face_detection(self, file_path):
        return self.post('face_detection', file_path=file_path).json()

    def gender_detection(self, file_path):
        return self.post('gender_detection', file_path=file_path).json()

    def age_detection(self, file_path):
        return self.post('age_detection', file_path=file_path).json()

    def face_expression(self, file_path):
        return self.post('face_expression', file_path=file_path).json()

    def face_recognition(self, file_path):
        return self.post('face_recognition', file_path=file_path).json()

    def human_detection(self, file_path):
        return self.post('human_detection', file_path=file_path).json()

    def object_recognition(self, file_path):
        return self.post('object_recognition', file_path=file_path).json()

    def qr_recognition(self, file_path):
        return self.post('qr_recognition', file_path=file_path).json()

    ##################################################
    # ORB                                            #
    ##################################################
    def orb_add_model(self, file_path):
        return self.post('upload_slam_config_file', file_path=file_path).json()

    def orb_del_model(self):
        pass

    def orb_query(self):
        pass

    ##################################################
    # MOBILE ROBOTICS                                #
    ##################################################
    def upload_slam_config_file(self, json):
        response = self.post('upload_slam_config_file',
            parameters=json)
        print(response.text)
        return self.post('upload_slam_config_file',
            parameters=json).json()

    def slam(self, json):
        return self.post('slam', parameters=json).json()

    def get_map(self, map_name):
        response = self.post('get_map',
            parameters={'json': '{"map_name": "map"}'})
        print('status code:', response.status_code)
        print('text:', response.text)
        print('raw:', response.raw)
        print('headers:', response.headers)
        return response
        # return self.get('get_map', parameters={'map_name': map_name})

    def delete_map(self, map_name):
        return self.get('get_map', parameters={'name': map_name})

    def path_planning(self, json):
        return self.post('path_planning', parameters=json)

    ##################################################
    # DIALOGUE_SYSTEMS                               #
    ##################################################
    def chat(self, sentence, model_name=None):
        pass
