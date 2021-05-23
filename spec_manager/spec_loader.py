import json


class SpecLoader(object):
    def __init__(self):
        self.spec = {}
        self.address = {}

    def load_spec(self):
        spec = {}
        address = {}
        f = open('spec_manager/config.json')
        cfg = json.load(f)
        for service, service_values in cfg.iteritems():
            spec_tmp_json = {}
            address_tmp_json = {}
            for internal_service, internal_service_values in service_values.get('services').iteritems():
                file_path = internal_service_values.get('spec')
                if file_path != '':
                    with open(internal_service_values.get('spec')) as f:
                        spec_tmp_json[internal_service_values.get('alias')] = json.load(f).get('paths')
                address_tmp_json[internal_service_values.get('alias')] = internal_service_values.get('address')
            spec[service_values.get('alias')] = spec_tmp_json
            address[service_values.get('alias')] = address_tmp_json
        self.spec = spec
        self.address = address
