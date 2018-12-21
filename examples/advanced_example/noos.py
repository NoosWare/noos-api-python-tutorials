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
        } if file_path else parameters

        return requests.post(
            url,
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
    def upload_slam_config_file(self, json_data):
        return self.post('upload_slam_config_file',
            parameters={'json': dumps(json_data)}).json()

    def slam(self, json_data):
        return self.post('slam',
            parameters={'json': dumps(json_data)}).json()

    def get_map(self, map_name):
        return self.post('get_map',
            parameters={'json': '{"map_name": "map"}'}).json()

    def delete_map(self, map_name):
        return self.post('delete_map',
            parameters={'json': dumps({'name': map_name})}).json()

    def path_planning(self, json_data):
        return self.post('path_planning',
            parameters={'json': dumps(json_data)}).json()

    ##################################################
    # DIALOGUE_SYSTEMS                               #
    ##################################################
    def chat(self, sentence, model_filename=None):
        json_data = {
            'state': sentence,
            'filename': model_filename if model_filename else ''
        }
        return self.post('chat',
            parameters={'json': dumps(json_data)}).json()
