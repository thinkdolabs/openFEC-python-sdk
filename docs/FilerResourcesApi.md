# openfec_sdk.FilerResourcesApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rad_analyst_get**](FilerResourcesApi.md#rad_analyst_get) | **GET** /rad-analyst/ |
[**state_election_office_get**](FilerResourcesApi.md#state_election_office_get) | **GET** /state-election-office/ |


# **rad_analyst_get**
> RadAnalystPage rad_analyst_get(api_key, sort=sort, min_assignment_update_date=min_assignment_update_date, name=name, per_page=per_page, analyst_short_id=analyst_short_id, sort_hide_null=sort_hide_null, telephone_ext=telephone_ext, title=title, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, max_assignment_update_date=max_assignment_update_date, email=email, sort_null_only=sort_null_only, analyst_id=analyst_id)



 Use this endpoint to look up the RAD Analyst for a committee.  The mission of the Reports Analysis Division (RAD) is to ensure that campaigns and political committees file timely and accurate reports that fully disclose their financial activities.  RAD is responsible for reviewing statements and financial reports filed by political committees participating in federal elections, providing assistance and guidance to the committees to properly file their reports, and for taking appropriate action to ensure compliance with the Federal Election Campaign Act (FECA).

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FilerResourcesApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
min_assignment_update_date = '2013-10-20' # date | Filter results for assignment updates made after this date (optional)
name = ['name_example'] # list[str] | Name of RAD analyst (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
analyst_short_id = [56] # list[int] | Short ID of RAD analyst (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
telephone_ext = [56] # list[int] | Telephone extension of RAD analyst (optional)
title = ['title_example'] # list[str] | Title of RAD analyst (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_assignment_update_date = '2013-10-20' # date | Filter results for assignment updates made before this date (optional)
email = ['email_example'] # list[str] | Email of RAD analyst (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
analyst_id = [56] # list[int] | ID of RAD analyst (optional)

    try:
        api_response = api_instance.rad_analyst_get(api_key, sort=sort, min_assignment_update_date=min_assignment_update_date, name=name, per_page=per_page, analyst_short_id=analyst_short_id, sort_hide_null=sort_hide_null, telephone_ext=telephone_ext, title=title, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, max_assignment_update_date=max_assignment_update_date, email=email, sort_null_only=sort_null_only, analyst_id=analyst_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilerResourcesApi->rad_analyst_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FilerResourcesApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
min_assignment_update_date = '2013-10-20' # date | Filter results for assignment updates made after this date (optional)
name = ['name_example'] # list[str] | Name of RAD analyst (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
analyst_short_id = [56] # list[int] | Short ID of RAD analyst (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
telephone_ext = [56] # list[int] | Telephone extension of RAD analyst (optional)
title = ['title_example'] # list[str] | Title of RAD analyst (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_assignment_update_date = '2013-10-20' # date | Filter results for assignment updates made before this date (optional)
email = ['email_example'] # list[str] | Email of RAD analyst (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
analyst_id = [56] # list[int] | ID of RAD analyst (optional)

    try:
        api_response = api_instance.rad_analyst_get(api_key, sort=sort, min_assignment_update_date=min_assignment_update_date, name=name, per_page=per_page, analyst_short_id=analyst_short_id, sort_hide_null=sort_hide_null, telephone_ext=telephone_ext, title=title, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, max_assignment_update_date=max_assignment_update_date, email=email, sort_null_only=sort_null_only, analyst_id=analyst_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilerResourcesApi->rad_analyst_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FilerResourcesApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
min_assignment_update_date = '2013-10-20' # date | Filter results for assignment updates made after this date (optional)
name = ['name_example'] # list[str] | Name of RAD analyst (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
analyst_short_id = [56] # list[int] | Short ID of RAD analyst (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
telephone_ext = [56] # list[int] | Telephone extension of RAD analyst (optional)
title = ['title_example'] # list[str] | Title of RAD analyst (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_assignment_update_date = '2013-10-20' # date | Filter results for assignment updates made before this date (optional)
email = ['email_example'] # list[str] | Email of RAD analyst (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
analyst_id = [56] # list[int] | ID of RAD analyst (optional)

    try:
        api_response = api_instance.rad_analyst_get(api_key, sort=sort, min_assignment_update_date=min_assignment_update_date, name=name, per_page=per_page, analyst_short_id=analyst_short_id, sort_hide_null=sort_hide_null, telephone_ext=telephone_ext, title=title, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, max_assignment_update_date=max_assignment_update_date, email=email, sort_null_only=sort_null_only, analyst_id=analyst_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilerResourcesApi->rad_analyst_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **min_assignment_update_date** | **date**| Filter results for assignment updates made after this date | [optional]
 **name** | [**list[str]**](str.md)| Name of RAD analyst | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **analyst_short_id** | [**list[int]**](int.md)| Short ID of RAD analyst | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **telephone_ext** | [**list[int]**](int.md)| Telephone extension of RAD analyst | [optional]
 **title** | [**list[str]**](str.md)| Title of RAD analyst | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **max_assignment_update_date** | **date**| Filter results for assignment updates made before this date | [optional]
 **email** | [**list[str]**](str.md)| Email of RAD analyst | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **analyst_id** | [**list[int]**](int.md)| ID of RAD analyst | [optional]

### Return type

[**RadAnalystPage**](RadAnalystPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_election_office_get**
> StateElectionOfficeInfoPage state_election_office_get(api_key, state, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, sort_null_only=sort_null_only)



 State laws and procedures govern elections for state or local offices as well as how candidates appear on election ballots. Contact the appropriate state election office for more information.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FilerResourcesApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
state = 'state_example' # str |  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.state_election_office_get(api_key, state, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilerResourcesApi->state_election_office_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FilerResourcesApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
state = 'state_example' # str |  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.state_election_office_get(api_key, state, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilerResourcesApi->state_election_office_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FilerResourcesApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
state = 'state_example' # str |  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.state_election_office_get(api_key, state, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilerResourcesApi->state_election_office_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **state** | **str**|  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.   |
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]

### Return type

[**StateElectionOfficeInfoPage**](StateElectionOfficeInfoPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
