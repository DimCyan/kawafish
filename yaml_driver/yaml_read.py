import yaml


def get_caps(config_path='../config/android_config.yml'):
    with open(config_path, 'r') as f:
        y = yaml.load(f, Loader=yaml.SafeLoader)
        return y


if __name__ == '__main__':
    get_caps()
