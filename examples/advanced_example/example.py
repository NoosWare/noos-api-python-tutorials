from argparse import ArgumentParser
from os import getcwd
from json import dumps, load
from noos import Noos

services = [
    'available_services',
    'face_detection',
    'gender_detection',
    'age_detection',
    'face_expression',
    'face_recognition',
    'human_detection',
    'object_recognition',
    'qr_recognition',
    'orb_add_model',
    'orb_del_model',
    'orb_query',
    'upload_slam_config_file',
    'slam',
    'get_map',
    'delete_map',
    'path_planning',
    'chat',
];

def get_args():
    parser = ArgumentParser(description='Illustrate the use of python \
                            for connecting to the noos services')
    parser.add_argument('-s', '--service',
                        choices=services,
                        help='the specific service to call')
    parser.add_argument('-a', '--all',
                        type=bool,
                        help='execute all the services')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    logins = open('.noos_credentials').read().splitlines()
    noos = Noos('https://demo.noos.cloud:9001/', logins[0], logins[1])

    ##################################################
    # UTILITY                                        #
    ##################################################
    if args.all or args.service == 'available_services':
        print(dumps(noos.available_services(), indent=4))

    ##################################################
    # COMPUTER VISION                                #
    ##################################################
    if args.all or args.service == 'face_detection':
        path = getcwd() + '/../data/face.jpg'
        print(dumps(noos.face_detection(path), indent=4))

    if args.all or args.service == 'gender_detection':
        path = getcwd() + '/../data/cropped_face.jpg'
        print(dumps(noos.gender_detection(path), indent=4))

    if args.all or args.service == 'age_detection':
        path = getcwd() + '/../data/cropped_face.jpg'
        print(dumps(noos.age_detection(path), indent=4))

    if args.all or args.service == 'face_expression':
        path = getcwd() + '/../data/cropped_face.jpg'
        print(dumps(noos.face_expression(path), indent=4))

    if args.all or args.service == 'face_recognition':
        path = getcwd() + '/../data/face.jpg'
        print(dumps(noos.face_recognition(path), indent=4))

    if args.all or args.service == 'human_detection':
        path = getcwd() + '/../data/human.jpg';
        print(dumps(noos.human_detection(path), indent=4))

    if args.all or args.service == 'object_recognition':
        path = getcwd() + '/../data/cup.jpg';
        print(dumps(noos.object_recognition(path), indent=4))

    if args.all or args.service == 'qr_recognition':
        path = getcwd() + '/../data/qr_code.jpg';
        print(dumps(noos.object_recognition(path), indent=4))

    ##################################################
    # ORB                                            #
    ##################################################

    if args.all or args.service == 'orb_add_model':
        path = getcwd() + '/../data/qr_code.jpg';
        print(dumps(noos.orb_add_model(path), indent=4))

    if args.all or args.service == 'orb_del_model':
        print(dumps(noos.orb_del_model(path), indent=4))

    if args.all or args.service == 'orb_query':
        path = getcwd() + '/../data/qr_code.jpg';
        print(dumps(noos.orb_query(path), indent=4))

    ##################################################
    # MOBILE ROBOTICS                                #
    ##################################################
    if args.all or args.service == 'upload_slam_config_file':
        path = getcwd() + '/../data/upload_icp_file.json'
        json_data = load(open(path))
        # print(dumps(noos.upload_slam_config_file(json_data), indent=4))
        noos.upload_slam_config_file(json_data)

    if args.all or args.service == 'slam':
        path = getcwd() + '/../data/laser.json'
        print(dumps(noos.slam(path), indent=4))

    if args.all or args.service == 'get_map':
        noos.get_map('map')
        # print(dumps(noos.get_map(), indent=4))

    if args.all or args.service == 'delete_map':
        print(dumps(noos.delete_map(), indent=4))

    if args.all or args.service == 'path_planning':
        path = getcwd() + '/../data/path.json';
        print(dumps(noos.path_planning(path), indent=4))

    ##################################################
    # DIALOGUE_SYSTEMS                               #
    ##################################################
    if args.all or args.service == 'chat':
        print(dumps(noos.chat('hello', None), indent=4))