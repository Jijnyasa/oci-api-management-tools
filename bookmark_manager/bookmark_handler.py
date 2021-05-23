import json
from mac_browser_parser.chrome_bookmark_editor import Chrome
from spec_manager.spec_parser import SpecParser


class BookmarkHandler(object):

    def __init__(self):
        self.parent_bar = Chrome().bookmarksBar
        self.spec_parser = SpecParser()
        self.spec_parser.parse_specs()
        self.spec_parser.make_folder_structure()

    def do_magic(self):
        specs = self.spec_parser.spec
        parent_name = specs.keys()[0]
        parent_folder = self.parent_bar.getFolder(parent_name)
        if parent_folder is not None:
            parent_folder.delete()
        self.parent_bar.addFolder(parent_name)
        parent_folder = self.parent_bar.getFolder(parent_name)
        for internal_service, intenal_service_endpoints in self.spec_parser.spec[parent_name].iteritems():
            parent_folder.addFolder(internal_service)
            internal_service_folder = parent_folder.getFolder(internal_service)
            for object_type, end_points in intenal_service_endpoints.iteritems():
                internal_service_folder.addFolder(object_type)
                internal_object_folder = internal_service_folder.getFolder(object_type)
                for end_point in end_points:
                    internal_object_folder.addBookmark(end_point.get('ops_type'), end_point.get('url'))
