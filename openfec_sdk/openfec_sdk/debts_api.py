# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openfec_sdk.api_client import ApiClient
from openfec_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DebtsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def schedules_schedule_d_get(self, api_key, **kwargs):  # noqa: E501
        """schedules_schedule_d_get  # noqa: E501

         Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_d_get(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (required)
        :param str min_image_number:
        :param str sort: Provide a field to sort by. Use `-` for descending order.
        :param list[str] candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
        :param float max_amount_incurred:
        :param float min_amount_incurred:
        :param float max_payment_period:
        :param bool sort_nulls_last: Toggle that sorts null values last
        :param str min_amount: Filter for all amounts greater than a value.
        :param str max_amount: Filter for all amounts less than a value.
        :param bool sort_null_only: Toggle that filters out all rows having sort column that is non-null
        :param date max_date: Maximum date
        :param date min_date: Minimum date
        :param bool sort_hide_null: Hide null values on sorted column(s).
        :param float min_payment_period:
        :param int per_page: The number of results returned per page. Defaults to 20.
        :param list[str] image_number: The image number of the page where the schedule item is reported
        :param list[str] committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
        :param int page: For paginating through results, starting at page 1
        :param str max_image_number:
        :param str line_number: Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
        :param str nature_of_debt:
        :param list[str] creditor_debtor_name:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponseDefault4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.schedules_schedule_d_get_with_http_info(api_key, **kwargs)  # noqa: E501

    def schedules_schedule_d_get_with_http_info(self, api_key, **kwargs):  # noqa: E501
        """schedules_schedule_d_get  # noqa: E501

         Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_d_get_with_http_info(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (required)
        :param str min_image_number:
        :param str sort: Provide a field to sort by. Use `-` for descending order.
        :param list[str] candidate_id:  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
        :param float max_amount_incurred:
        :param float min_amount_incurred:
        :param float max_payment_period:
        :param bool sort_nulls_last: Toggle that sorts null values last
        :param str min_amount: Filter for all amounts greater than a value.
        :param str max_amount: Filter for all amounts less than a value.
        :param bool sort_null_only: Toggle that filters out all rows having sort column that is non-null
        :param date max_date: Maximum date
        :param date min_date: Minimum date
        :param bool sort_hide_null: Hide null values on sorted column(s).
        :param float min_payment_period:
        :param int per_page: The number of results returned per page. Defaults to 20.
        :param list[str] image_number: The image number of the page where the schedule item is reported
        :param list[str] committee_id:  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
        :param int page: For paginating through results, starting at page 1
        :param str max_image_number:
        :param str line_number: Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
        :param str nature_of_debt:
        :param list[str] creditor_debtor_name:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponseDefault4, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'api_key',
            'min_image_number',
            'sort',
            'candidate_id',
            'max_amount_incurred',
            'min_amount_incurred',
            'max_payment_period',
            'sort_nulls_last',
            'min_amount',
            'max_amount',
            'sort_null_only',
            'max_date',
            'min_date',
            'sort_hide_null',
            'min_payment_period',
            'per_page',
            'image_number',
            'committee_id',
            'page',
            'max_image_number',
            'line_number',
            'nature_of_debt',
            'creditor_debtor_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method schedules_schedule_d_get' % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['api_key'] is None):  # noqa: E501
            raise ApiValueError('Missing the required parameter `api_key` when calling `schedules_schedule_d_get`')  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_key' in local_var_params and local_var_params['api_key'] is not None:  # noqa: E501
            query_params.append(('api_key', local_var_params['api_key']))  # noqa: E501
        if 'min_image_number' in local_var_params and local_var_params['min_image_number'] is not None:  # noqa: E501
            query_params.append(('min_image_number', local_var_params['min_image_number']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'candidate_id' in local_var_params and local_var_params['candidate_id'] is not None:  # noqa: E501
            query_params.append(('candidate_id', local_var_params['candidate_id']))  # noqa: E501
            collection_formats['candidate_id'] = 'multi'  # noqa: E501
        if 'max_amount_incurred' in local_var_params and local_var_params['max_amount_incurred'] is not None:  # noqa: E501
            query_params.append(('max_amount_incurred', local_var_params['max_amount_incurred']))  # noqa: E501
        if 'min_amount_incurred' in local_var_params and local_var_params['min_amount_incurred'] is not None:  # noqa: E501
            query_params.append(('min_amount_incurred', local_var_params['min_amount_incurred']))  # noqa: E501
        if 'max_payment_period' in local_var_params and local_var_params['max_payment_period'] is not None:  # noqa: E501
            query_params.append(('max_payment_period', local_var_params['max_payment_period']))  # noqa: E501
        if 'sort_nulls_last' in local_var_params and local_var_params['sort_nulls_last'] is not None:  # noqa: E501
            query_params.append(('sort_nulls_last', local_var_params['sort_nulls_last']))  # noqa: E501
        if 'min_amount' in local_var_params and local_var_params['min_amount'] is not None:  # noqa: E501
            query_params.append(('min_amount', local_var_params['min_amount']))  # noqa: E501
        if 'max_amount' in local_var_params and local_var_params['max_amount'] is not None:  # noqa: E501
            query_params.append(('max_amount', local_var_params['max_amount']))  # noqa: E501
        if 'sort_null_only' in local_var_params and local_var_params['sort_null_only'] is not None:  # noqa: E501
            query_params.append(('sort_null_only', local_var_params['sort_null_only']))  # noqa: E501
        if 'max_date' in local_var_params and local_var_params['max_date'] is not None:  # noqa: E501
            query_params.append(('max_date', local_var_params['max_date']))  # noqa: E501
        if 'min_date' in local_var_params and local_var_params['min_date'] is not None:  # noqa: E501
            query_params.append(('min_date', local_var_params['min_date']))  # noqa: E501
        if 'sort_hide_null' in local_var_params and local_var_params['sort_hide_null'] is not None:  # noqa: E501
            query_params.append(('sort_hide_null', local_var_params['sort_hide_null']))  # noqa: E501
        if 'min_payment_period' in local_var_params and local_var_params['min_payment_period'] is not None:  # noqa: E501
            query_params.append(('min_payment_period', local_var_params['min_payment_period']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'image_number' in local_var_params and local_var_params['image_number'] is not None:  # noqa: E501
            query_params.append(('image_number', local_var_params['image_number']))  # noqa: E501
            collection_formats['image_number'] = 'multi'  # noqa: E501
        if 'committee_id' in local_var_params and local_var_params['committee_id'] is not None:  # noqa: E501
            query_params.append(('committee_id', local_var_params['committee_id']))  # noqa: E501
            collection_formats['committee_id'] = 'multi'  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'max_image_number' in local_var_params and local_var_params['max_image_number'] is not None:  # noqa: E501
            query_params.append(('max_image_number', local_var_params['max_image_number']))  # noqa: E501
        if 'line_number' in local_var_params and local_var_params['line_number'] is not None:  # noqa: E501
            query_params.append(('line_number', local_var_params['line_number']))  # noqa: E501
        if 'nature_of_debt' in local_var_params and local_var_params['nature_of_debt'] is not None:  # noqa: E501
            query_params.append(('nature_of_debt', local_var_params['nature_of_debt']))  # noqa: E501
        if 'creditor_debtor_name' in local_var_params and local_var_params['creditor_debtor_name'] is not None:  # noqa: E501
            query_params.append(('creditor_debtor_name', local_var_params['creditor_debtor_name']))  # noqa: E501
            collection_formats['creditor_debtor_name'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth', 'apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/schedules/schedule_d/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_schedule_d_sub_id_get(self, api_key, sub_id, **kwargs):  # noqa: E501
        """schedules_schedule_d_sub_id_get  # noqa: E501

         Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_d_sub_id_get(api_key, sub_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (required)
        :param str sub_id: (required)
        :param bool sort_nulls_last: Toggle that sorts null values last
        :param int page: For paginating through results, starting at page 1
        :param str sort: Provide a field to sort by. Use `-` for descending order.
        :param bool sort_null_only: Toggle that filters out all rows having sort column that is non-null
        :param bool sort_hide_null: Hide null values on sorted column(s).
        :param int per_page: The number of results returned per page. Defaults to 20.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponseDefault4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.schedules_schedule_d_sub_id_get_with_http_info(api_key, sub_id, **kwargs)  # noqa: E501

    def schedules_schedule_d_sub_id_get_with_http_info(self, api_key, sub_id, **kwargs):  # noqa: E501
        """schedules_schedule_d_sub_id_get  # noqa: E501

         Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_d_sub_id_get_with_http_info(api_key, sub_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (required)
        :param str sub_id: (required)
        :param bool sort_nulls_last: Toggle that sorts null values last
        :param int page: For paginating through results, starting at page 1
        :param str sort: Provide a field to sort by. Use `-` for descending order.
        :param bool sort_null_only: Toggle that filters out all rows having sort column that is non-null
        :param bool sort_hide_null: Hide null values on sorted column(s).
        :param int per_page: The number of results returned per page. Defaults to 20.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponseDefault4, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'api_key',
            'sub_id',
            'sort_nulls_last',
            'page',
            'sort',
            'sort_null_only',
            'sort_hide_null',
            'per_page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method schedules_schedule_d_sub_id_get' % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['api_key'] is None):  # noqa: E501
            raise ApiValueError('Missing the required parameter `api_key` when calling `schedules_schedule_d_sub_id_get`')  # noqa: E501
        # verify the required parameter 'sub_id' is set
        if self.api_client.client_side_validation and ('sub_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['sub_id'] is None):  # noqa: E501
            raise ApiValueError('Missing the required parameter `sub_id` when calling `schedules_schedule_d_sub_id_get`')  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sub_id' in local_var_params:
            path_params['sub_id'] = local_var_params['sub_id']  # noqa: E501

        query_params = []
        if 'sort_nulls_last' in local_var_params and local_var_params['sort_nulls_last'] is not None:  # noqa: E501
            query_params.append(('sort_nulls_last', local_var_params['sort_nulls_last']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'api_key' in local_var_params and local_var_params['api_key'] is not None:  # noqa: E501
            query_params.append(('api_key', local_var_params['api_key']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'sort_null_only' in local_var_params and local_var_params['sort_null_only'] is not None:  # noqa: E501
            query_params.append(('sort_null_only', local_var_params['sort_null_only']))  # noqa: E501
        if 'sort_hide_null' in local_var_params and local_var_params['sort_hide_null'] is not None:  # noqa: E501
            query_params.append(('sort_hide_null', local_var_params['sort_hide_null']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth', 'apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/schedules/schedule_d/{sub_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponseDefault4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
