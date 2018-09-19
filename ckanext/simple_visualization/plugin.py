import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging

ignore_missing = plugins.toolkit.get_validator('ignore_missing')

class Simple_VisualizationPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IResourceView, inherit=True)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'simple_visualization')
    '''
    This extension views a hard-coded visual summary of a resource.
    '''
    def info(self):
        return {'name': 'simple_visualization',
                'title': 'Smarties Summary',
                'icon': 'table',
                'requires_datastore': False,
                'always_available': True,
                'schema': {
                    'smartie_value_1': [ignore_missing],
                    'smartie_value_2': [ignore_missing],
                    'smartie_value_3': [ignore_missing],
                    'smartie_label_1': [ignore_missing],
                    'smartie_label_2': [ignore_missing],
                    'smartie_label_3': [ignore_missing]
                },
                'default_title': plugins.toolkit._('Smarties Summary'),
                }

    def can_view(self, data_dict):
      return True

    def view_template(self, context, data_dict):
        return 'smarties_view.html'

    def form_template(self, context, data_dict):
        return 'smarties_form.html'

    '''
class SmartiesView(Simple_VisualizationPlugin):

    def info(self):
        return {'name': 'simple_visualization',
                'title': 'Smarties Summary',
                'icon': 'table',
                'requires_datastore': False,
                'always_available': True,
                'default_title': plugins.toolkit._('Smarties Summary'),
                }

    def can_view(self, data_dict):
      return True

    def view_template(self, context, data_dict):
        return 'smarties_view.html'

    def form_template(self, context, data_dict):
        return 'smarties_form.html'

    '''