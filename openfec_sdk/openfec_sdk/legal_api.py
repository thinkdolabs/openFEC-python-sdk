# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401
import sys  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openfec_sdk.api_client import ApiClient
from openfec_sdk.exceptions import (
    ApiTypeError,
    ApiValueError
)
from openfec_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_and_convert_types
)
from openfec_sdk.models import inline_response_default1


class LegalApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __legal_search_get(
            self,
            api_key='DEMO_KEY',
            **kwargs
        ):
            """legal_search_get  # noqa: E501

             Search legal documents by type, or across all document types using keywords, parameter values and ranges.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.legal_search_get(api_key='DEMO_KEY', async_req=True)
            >>> result = thread.get()

            Args:
                api_key (str):  API key for https://api.data.gov. Get one at https://api.data.gov/signup. . defaults to 'DEMO_KEY', must be one of ['DEMO_KEY']

            Keyword Args:
                af_name ([str]): Admin fine committee name. [optional]
                case_max_close_date (date): Filter cases by latest date closed. [optional]
                ao_entity_name ([str]): Search by name of commenter or representative. [optional]
                af_min_rtb_date (date): Filter cases by earliest Reason to Believe date. [optional]
                from_hit (int): Get results starting from this index.. [optional]
                af_rtb_fine_amount (int): Filter cases by Reason to Believe fine amount. [optional]
                case_document_category ([str]): Filter cases by category of associated documents. [optional]
                af_max_fd_date (date): Filter cases by latest Final Determination date. [optional]
                case_dispositions ([str]): Filter cases by dispositions. [optional]
                ao_statutory_citation ([str]): Search for statutory citations. [optional]
                case_election_cycles (int): Filter cases by election cycles. [optional]
                ao_max_issue_date (date): Latest issue date of advisory opinion. [optional]
                af_fd_fine_amount (int): Filter cases by Final Determination fine amount. [optional]
                ao_category ([str]): Category of the document. [optional]
                ao_max_request_date (date): Latest request date of advisory opinion. [optional]
                case_max_open_date (date): Filter cases by latest date opened. [optional]
                ao_citation_require_all (bool): Require all citations to be in document (default behavior is any). [optional]
                ao_requestor_type ([int]): Code of the advisory opinion requestor type.. [optional]
                ao_min_issue_date (date): Earliest issue date of advisory opinion. [optional]
                case_no ([str]): Enforcement matter case number. [optional]
                case_respondents (str): Filter cases by respondents. [optional]
                ao_status (str): Status of AO (pending, withdrawn, or final). [optional]
                case_min_close_date (date): Filter cases by earliest date closed. [optional]
                type (str): Document type to refine search by. [optional]
                af_report_year (str): Admin fine report year. [optional]
                hits_returned (int): Number of results to return (max 10).. [optional]
                af_min_fd_date (date): Filter cases by earliest Final Determination date. [optional]
                ao_no ([str]): Force advisory opinion number. [optional]
                ao_name ([str]): Force advisory opinion name. [optional]
                ao_requestor (str): The requestor of the advisory opinion. [optional]
                case_min_open_date (date): Filter cases by earliest date opened. [optional]
                ao_regulatory_citation ([str]): Search for regulatory citations. [optional]
                af_max_rtb_date (date): Filter cases by latest Reason to Believe date. [optional]
                af_committee_id (str): Admin fine committee ID. [optional]
                ao_min_request_date (date): Earliest request date of advisory opinion. [optional]
                ao_is_pending (bool): AO is pending. [optional]
                q (str): Text to search legal documents for.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int): specifies the index of the server
                    that we want to use.
                    Default is 0.
                async_req (bool): execute request asynchronously

            Returns:
                inline_response_default1.InlineResponseDefault1
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index', 0)
            kwargs['api_key'] = \
                api_key
            return self.call_with_http_info(**kwargs)

        self.legal_search_get = Endpoint(
            settings={
                'response_type': (inline_response_default1.InlineResponseDefault1,),
                'auth': [
                    'ApiKeyHeaderAuth',
                    'ApiKeyQueryAuth',
                    'apiKey'
                ],
                'endpoint_path': '/legal/search/',
                'operation_id': 'legal_search_get',
                'http_method': 'GET',
                'servers': [],
            },
            params_map={
                'all': [
                    'api_key',
                    'af_name',
                    'case_max_close_date',
                    'ao_entity_name',
                    'af_min_rtb_date',
                    'from_hit',
                    'af_rtb_fine_amount',
                    'case_document_category',
                    'af_max_fd_date',
                    'case_dispositions',
                    'ao_statutory_citation',
                    'case_election_cycles',
                    'ao_max_issue_date',
                    'af_fd_fine_amount',
                    'ao_category',
                    'ao_max_request_date',
                    'case_max_open_date',
                    'ao_citation_require_all',
                    'ao_requestor_type',
                    'ao_min_issue_date',
                    'case_no',
                    'case_respondents',
                    'ao_status',
                    'case_min_close_date',
                    'type',
                    'af_report_year',
                    'hits_returned',
                    'af_min_fd_date',
                    'ao_no',
                    'ao_name',
                    'ao_requestor',
                    'case_min_open_date',
                    'ao_regulatory_citation',
                    'af_max_rtb_date',
                    'af_committee_id',
                    'ao_min_request_date',
                    'ao_is_pending',
                    'q',
                ],
                'required': [
                    'api_key',
                ],
                'nullable': [
                ],
                'enum': [
                    'ao_category',
                    'ao_requestor_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('ao_category',): {

                        'F': 'F',
                        'V': 'V',
                        'D': 'D',
                        'R': 'R',
                        'W': 'W',
                        'C': 'C',
                        'S': 'S'
                    },
                    ('ao_requestor_type',): {

                        '1': 1,
                        '2': 2,
                        '3': 3,
                        '4': 4,
                        '5': 5,
                        '6': 6,
                        '7': 7,
                        '8': 8,
                        '9': 9,
                        '10': 10,
                        '11': 11,
                        '12': 12,
                        '13': 13,
                        '14': 14,
                        '15': 15,
                        '16': 16
                    },
                },
                'openapi_types': {
                    'api_key':
                        (str,),
                    'af_name':
                        ([str],),
                    'case_max_close_date':
                        (date,),
                    'ao_entity_name':
                        ([str],),
                    'af_min_rtb_date':
                        (date,),
                    'from_hit':
                        (int,),
                    'af_rtb_fine_amount':
                        (int,),
                    'case_document_category':
                        ([str],),
                    'af_max_fd_date':
                        (date,),
                    'case_dispositions':
                        ([str],),
                    'ao_statutory_citation':
                        ([str],),
                    'case_election_cycles':
                        (int,),
                    'ao_max_issue_date':
                        (date,),
                    'af_fd_fine_amount':
                        (int,),
                    'ao_category':
                        ([str],),
                    'ao_max_request_date':
                        (date,),
                    'case_max_open_date':
                        (date,),
                    'ao_citation_require_all':
                        (bool,),
                    'ao_requestor_type':
                        ([int],),
                    'ao_min_issue_date':
                        (date,),
                    'case_no':
                        ([str],),
                    'case_respondents':
                        (str,),
                    'ao_status':
                        (str,),
                    'case_min_close_date':
                        (date,),
                    'type':
                        (str,),
                    'af_report_year':
                        (str,),
                    'hits_returned':
                        (int,),
                    'af_min_fd_date':
                        (date,),
                    'ao_no':
                        ([str],),
                    'ao_name':
                        ([str],),
                    'ao_requestor':
                        (str,),
                    'case_min_open_date':
                        (date,),
                    'ao_regulatory_citation':
                        ([str],),
                    'af_max_rtb_date':
                        (date,),
                    'af_committee_id':
                        (str,),
                    'ao_min_request_date':
                        (date,),
                    'ao_is_pending':
                        (bool,),
                    'q':
                        (str,),
                },
                'attribute_map': {
                    'api_key': 'api_key',
                    'af_name': 'af_name',
                    'case_max_close_date': 'case_max_close_date',
                    'ao_entity_name': 'ao_entity_name',
                    'af_min_rtb_date': 'af_min_rtb_date',
                    'from_hit': 'from_hit',
                    'af_rtb_fine_amount': 'af_rtb_fine_amount',
                    'case_document_category': 'case_document_category',
                    'af_max_fd_date': 'af_max_fd_date',
                    'case_dispositions': 'case_dispositions',
                    'ao_statutory_citation': 'ao_statutory_citation',
                    'case_election_cycles': 'case_election_cycles',
                    'ao_max_issue_date': 'ao_max_issue_date',
                    'af_fd_fine_amount': 'af_fd_fine_amount',
                    'ao_category': 'ao_category',
                    'ao_max_request_date': 'ao_max_request_date',
                    'case_max_open_date': 'case_max_open_date',
                    'ao_citation_require_all': 'ao_citation_require_all',
                    'ao_requestor_type': 'ao_requestor_type',
                    'ao_min_issue_date': 'ao_min_issue_date',
                    'case_no': 'case_no',
                    'case_respondents': 'case_respondents',
                    'ao_status': 'ao_status',
                    'case_min_close_date': 'case_min_close_date',
                    'type': 'type',
                    'af_report_year': 'af_report_year',
                    'hits_returned': 'hits_returned',
                    'af_min_fd_date': 'af_min_fd_date',
                    'ao_no': 'ao_no',
                    'ao_name': 'ao_name',
                    'ao_requestor': 'ao_requestor',
                    'case_min_open_date': 'case_min_open_date',
                    'ao_regulatory_citation': 'ao_regulatory_citation',
                    'af_max_rtb_date': 'af_max_rtb_date',
                    'af_committee_id': 'af_committee_id',
                    'ao_min_request_date': 'ao_min_request_date',
                    'ao_is_pending': 'ao_is_pending',
                    'q': 'q',
                },
                'location_map': {
                    'api_key': 'query',
                    'af_name': 'query',
                    'case_max_close_date': 'query',
                    'ao_entity_name': 'query',
                    'af_min_rtb_date': 'query',
                    'from_hit': 'query',
                    'af_rtb_fine_amount': 'query',
                    'case_document_category': 'query',
                    'af_max_fd_date': 'query',
                    'case_dispositions': 'query',
                    'ao_statutory_citation': 'query',
                    'case_election_cycles': 'query',
                    'ao_max_issue_date': 'query',
                    'af_fd_fine_amount': 'query',
                    'ao_category': 'query',
                    'ao_max_request_date': 'query',
                    'case_max_open_date': 'query',
                    'ao_citation_require_all': 'query',
                    'ao_requestor_type': 'query',
                    'ao_min_issue_date': 'query',
                    'case_no': 'query',
                    'case_respondents': 'query',
                    'ao_status': 'query',
                    'case_min_close_date': 'query',
                    'type': 'query',
                    'af_report_year': 'query',
                    'hits_returned': 'query',
                    'af_min_fd_date': 'query',
                    'ao_no': 'query',
                    'ao_name': 'query',
                    'ao_requestor': 'query',
                    'case_min_open_date': 'query',
                    'ao_regulatory_citation': 'query',
                    'af_max_rtb_date': 'query',
                    'af_committee_id': 'query',
                    'ao_min_request_date': 'query',
                    'ao_is_pending': 'query',
                    'q': 'query',
                },
                'collection_format_map': {
                    'af_name': 'multi',
                    'ao_entity_name': 'multi',
                    'case_document_category': 'multi',
                    'case_dispositions': 'multi',
                    'ao_statutory_citation': 'multi',
                    'ao_category': 'multi',
                    'ao_requestor_type': 'multi',
                    'case_no': 'multi',
                    'ao_no': 'multi',
                    'ao_name': 'multi',
                    'ao_regulatory_citation': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__legal_search_get
        )


class Endpoint(object):
    def __init__(self, settings=None, params_map=None, root_map=None,
                 headers_map=None, api_client=None, callable=None):
        """Creates an endpoint

        Args:
            settings (dict): see below key value pairs
                'response_type' (tuple/None): response type
                'auth' (list): a list of auth type keys
                'endpoint_path' (str): the endpoint path
                'operation_id' (str): endpoint string identifier
                'http_method' (str): POST/PUT/PATCH/GET etc
                'servers' (list): list of str servers that this endpoint is at
            params_map (dict): see below key value pairs
                'all' (list): list of str endpoint parameter names
                'required' (list): list of required parameter names
                'nullable' (list): list of nullable parameter names
                'enum' (list): list of parameters with enum values
                'validation' (list): list of parameters with validations
            root_map
                'validations' (dict): the dict mapping endpoint parameter tuple
                    paths to their validation dictionaries
                'allowed_values' (dict): the dict mapping endpoint parameter
                    tuple paths to their allowed_values (enum) dictionaries
                'openapi_types' (dict): param_name to openapi type
                'attribute_map' (dict): param_name to camelCase name
                'location_map' (dict): param_name to  'body', 'file', 'form',
                    'header', 'path', 'query'
                collection_format_map (dict): param_name to `csv` etc.
            headers_map (dict): see below key value pairs
                'accept' (list): list of Accept header strings
                'content_type' (list): list of Content-Type header strings
            api_client (ApiClient) api client instance
            callable (function): the function which is invoked when the
                Endpoint is called
        """
        self.settings = settings
        self.params_map = params_map
        self.params_map['all'].extend([
            'async_req',
            '_host_index',
            '_preload_content',
            '_request_timeout',
            '_return_http_data_only',
            '_check_input_type',
            '_check_return_type'
        ])
        self.params_map['nullable'].extend(['_request_timeout'])
        self.validations = root_map['validations']
        self.allowed_values = root_map['allowed_values']
        self.openapi_types = root_map['openapi_types']
        extra_types = {
            'async_req': (bool,),
            '_host_index': (int,),
            '_preload_content': (bool,),
            '_request_timeout': (none_type, int, (int,), [int]),
            '_return_http_data_only': (bool,),
            '_check_input_type': (bool,),
            '_check_return_type': (bool,)
        }
        self.openapi_types.update(extra_types)
        self.attribute_map = root_map['attribute_map']
        self.location_map = root_map['location_map']
        self.collection_format_map = root_map['collection_format_map']
        self.headers_map = headers_map
        self.api_client = api_client
        self.callable = callable

    def __validate_inputs(self, kwargs):
        for param in self.params_map['enum']:
            if param in kwargs:
                check_allowed_values(
                    self.allowed_values,
                    (param,),
                    kwargs[param]
                )

        for param in self.params_map['validation']:
            if param in kwargs:
                check_validations(
                    self.validations,
                    (param,),
                    kwargs[param]
                )

        if kwargs['_check_input_type'] is False:
            return

        for key, value in six.iteritems(kwargs):
            fixed_val = validate_and_convert_types(
                value,
                self.openapi_types[key],
                [key],
                False,
                kwargs['_check_input_type'],
                configuration=self.api_client.configuration
            )
            kwargs[key] = fixed_val

    def __gather_params(self, kwargs):
        params = {
            'body': None,
            'collection_format': {},
            'file': {},
            'form': [],
            'header': {},
            'path': {},
            'query': []
        }

        for param_name, param_value in six.iteritems(kwargs):
            param_location = self.location_map.get(param_name)
            if param_location is None:
                continue
            if param_location:
                if param_location == 'body':
                    params['body'] = param_value
                    continue
                base_name = self.attribute_map[param_name]
                if (param_location == 'form' and
                        self.openapi_types[param_name] == (file_type,)):
                    params['file'][param_name] = [param_value]
                elif (param_location == 'form' and
                        self.openapi_types[param_name] == ([file_type],)):
                    # param_value is already a list
                    params['file'][param_name] = param_value
                elif param_location in {'form', 'query'}:
                    param_value_full = (base_name, param_value)
                    params[param_location].append(param_value_full)
                if param_location not in {'form', 'query'}:
                    params[param_location][base_name] = param_value
                collection_format = self.collection_format_map.get(param_name)
                if collection_format:
                    params['collection_format'][base_name] = collection_format

        return params

    def __call__(self, *args, **kwargs):
        """ This method is invoked when endpoints are called
        Example:
        pet_api = PetApi()
        pet_api.add_pet  # this is an instance of the class Endpoint
        pet_api.add_pet()  # this invokes pet_api.add_pet.__call__()
        which then invokes the callable functions stored in that endpoint at
        pet_api.add_pet.callable or self.callable in this class
        """
        return self.callable(self, *args, **kwargs)

    def call_with_http_info(self, **kwargs):

        try:
            _host = self.settings['servers'][kwargs['_host_index']]
        except IndexError:
            if self.settings['servers']:
                raise ApiValueError(
                    'Invalid host index. Must be 0 <= index < %s' %
                    len(self.settings['servers'])
                )
            _host = None

        for key, value in six.iteritems(kwargs):
            if key not in self.params_map['all']:
                raise ApiTypeError(
                    "Got an unexpected parameter '%s'"
                    ' to method `%s`' %
                    (key, self.settings['operation_id'])
                )
            # only throw this nullable ApiValueError if _check_input_type
            # is False, if _check_input_type==True we catch this case
            # in self.__validate_inputs
            if (key not in self.params_map['nullable'] and value is None
                    and kwargs['_check_input_type'] is False):
                raise ApiValueError(
                    'Value may not be None for non-nullable parameter `%s`'
                    ' when calling `%s`' %
                    (key, self.settings['operation_id'])
                )

        for key in self.params_map['required']:
            if key not in kwargs.keys():
                raise ApiValueError(
                    'Missing the required parameter `%s` when calling '
                    '`%s`' % (key, self.settings['operation_id'])
                )

        self.__validate_inputs(kwargs)

        params = self.__gather_params(kwargs)

        accept_headers_list = self.headers_map['accept']
        if accept_headers_list:
            params['header']['Accept'] = self.api_client.select_header_accept(
                accept_headers_list)

        content_type_headers_list = self.headers_map['content_type']
        if content_type_headers_list:
            header_list = self.api_client.select_header_content_type(
                content_type_headers_list)
            params['header']['Content-Type'] = header_list

        return self.api_client.call_api(
            self.settings['endpoint_path'], self.settings['http_method'],
            params['path'],
            params['query'],
            params['header'],
            body=params['body'],
            post_params=params['form'],
            files=params['file'],
            response_type=self.settings['response_type'],
            auth_settings=self.settings['auth'],
            async_req=kwargs['async_req'],
            _check_type=kwargs['_check_return_type'],
            _return_http_data_only=kwargs['_return_http_data_only'],
            _preload_content=kwargs['_preload_content'],
            _request_timeout=kwargs['_request_timeout'],
            _host=_host,
            collection_formats=params['collection_format'])