from spec_manager.spec_loader import SpecLoader


def parse_url(url, prefix):
    url = url.replace("{", "Enter_")
    url = url.replace("}", "")
    end_point = prefix + url
    return end_point


class SpecParser(object):
    MAPPING = {
        'LoadBalancer' : 'Lb',
        'Operational' : 'Ops',
        'Workflow' : 'WF',
        'ControlPlane' : 'CP',
        'WorkRequest' : 'WR'
    }
    def __init__(self,):
        specloader = SpecLoader()
        specloader.load_spec()
        self.spec = specloader.spec
        self.address = specloader.address

    def parse_specs(self):
        for service, service_values in self.spec.iteritems():
            for internal_service, internal_service_values in service_values.iteritems():
                api_detail = {}
                for end_point, end_point_details in internal_service_values.iteritems():
                    if end_point_details.get('get'):
                        object_type = end_point_details.get('get', {}).get('responses', {}).get('200', {}).get('schema', {}).get('$ref','') or end_point_details.get('get', {}).get('responses', {}).get('200', {}).get('schema', {}).get('items', {}).get('$ref', '') or 'other'
                        object_type = object_type.replace("#/definitions/", '')
                        operation_type = end_point_details.get('get').get('operationId')
                        for full_form, short_form in SpecParser.MAPPING.iteritems():
                            operation_type = operation_type.replace(full_form, short_form)
                        prefix = self.address[service][internal_service]
                        api_detail[operation_type] = {'url': parse_url(end_point, prefix),  'type': object_type}
                self.spec[service][internal_service] = api_detail

    def make_folder_structure(self):
        for service, service_values in self.spec.iteritems():
            for internal_service, internal_service_values in service_values.iteritems():
                grouped_data = {}
                for request_name, request_details in internal_service_values.iteritems():
                    if request_details.get('type') not in grouped_data:
                        grouped_data[request_details.get('type')] = []
                    grouped_data[request_details['type']].append({'ops_type': request_name, 'url': request_details.get('url')})
                self.spec[service][internal_service] = grouped_data


