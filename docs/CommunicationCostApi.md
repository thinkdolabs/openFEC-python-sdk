# openfec_sdk.CommunicationCostApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**committee_committee_id_communication_costs_by_candidate_get**](CommunicationCostApi.md#committee_committee_id_communication_costs_by_candidate_get) | **GET** /committee/{committee_id}/communication_costs/by_candidate/ |
[**communication_costs_aggregates_get**](CommunicationCostApi.md#communication_costs_aggregates_get) | **GET** /communication_costs/aggregates/ |
[**communication_costs_by_candidate_get**](CommunicationCostApi.md#communication_costs_by_candidate_get) | **GET** /communication_costs/by_candidate/ |
[**communication_costs_get**](CommunicationCostApi.md#communication_costs_get) | **GET** /communication-costs/ |
[**communication_costs_totals_by_candidate_get**](CommunicationCostApi.md#communication_costs_totals_by_candidate_get) | **GET** /communication_costs/totals/by_candidate/ |


# **committee_committee_id_communication_costs_by_candidate_get**
> CommunicationCostByCandidatePage committee_committee_id_communication_costs_by_candidate_get(api_key, committee_id, election_full=election_full, sort=sort, candidate_id=candidate_id, state=state, sort_hide_null=sort_hide_null, per_page=per_page, district=district, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, support_oppose=support_oppose, sort_null_only=sort_null_only, office=office)



Communication cost aggregated by candidate ID and committee ID.

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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
support_oppose = 'null' # str | Support or opposition (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.committee_committee_id_communication_costs_by_candidate_get(api_key, committee_id, election_full=election_full, sort=sort, candidate_id=candidate_id, state=state, sort_hide_null=sort_hide_null, per_page=per_page, district=district, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, support_oppose=support_oppose, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->committee_committee_id_communication_costs_by_candidate_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
support_oppose = 'null' # str | Support or opposition (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.committee_committee_id_communication_costs_by_candidate_get(api_key, committee_id, election_full=election_full, sort=sort, candidate_id=candidate_id, state=state, sort_hide_null=sort_hide_null, per_page=per_page, district=district, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, support_oppose=support_oppose, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->committee_committee_id_communication_costs_by_candidate_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
support_oppose = 'null' # str | Support or opposition (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.committee_committee_id_communication_costs_by_candidate_get(api_key, committee_id, election_full=election_full, sort=sort, candidate_id=candidate_id, state=state, sort_hide_null=sort_hide_null, per_page=per_page, district=district, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, support_oppose=support_oppose, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->committee_committee_id_communication_costs_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committee_id** | **str**|  |
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **state** | **str**| US state or territory where a candidate runs for office | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **support_oppose** | **str**| Support or opposition | [optional] [default to &#39;null&#39;]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**CommunicationCostByCandidatePage**](CommunicationCostByCandidatePage.md)

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

# **communication_costs_aggregates_get**
> CommunicationCostByCandidatePage communication_costs_aggregates_get(api_key, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, committee_id=committee_id, cycle=cycle, page=page, sort_null_only=sort_null_only, support_oppose_indicator=support_oppose_indicator)



Communication cost aggregated by candidate ID and committee ID.

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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
support_oppose_indicator = 'null' # str | Support or opposition (optional) (default to 'null')

    try:
        api_response = api_instance.communication_costs_aggregates_get(api_key, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, committee_id=committee_id, cycle=cycle, page=page, sort_null_only=sort_null_only, support_oppose_indicator=support_oppose_indicator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_aggregates_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
support_oppose_indicator = 'null' # str | Support or opposition (optional) (default to 'null')

    try:
        api_response = api_instance.communication_costs_aggregates_get(api_key, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, committee_id=committee_id, cycle=cycle, page=page, sort_null_only=sort_null_only, support_oppose_indicator=support_oppose_indicator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_aggregates_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
support_oppose_indicator = 'null' # str | Support or opposition (optional) (default to 'null')

    try:
        api_response = api_instance.communication_costs_aggregates_get(api_key, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, committee_id=committee_id, cycle=cycle, page=page, sort_null_only=sort_null_only, support_oppose_indicator=support_oppose_indicator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_aggregates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **support_oppose_indicator** | **str**| Support or opposition | [optional] [default to &#39;null&#39;]

### Return type

[**CommunicationCostByCandidatePage**](CommunicationCostByCandidatePage.md)

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

# **communication_costs_by_candidate_get**
> CommunicationCostByCandidatePage communication_costs_by_candidate_get(api_key, election_full=election_full, sort=sort, candidate_id=candidate_id, state=state, sort_hide_null=sort_hide_null, per_page=per_page, district=district, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, support_oppose=support_oppose, sort_null_only=sort_null_only, office=office)



Communication cost aggregated by candidate ID and committee ID.

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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
support_oppose = 'null' # str | Support or opposition (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.communication_costs_by_candidate_get(api_key, election_full=election_full, sort=sort, candidate_id=candidate_id, state=state, sort_hide_null=sort_hide_null, per_page=per_page, district=district, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, support_oppose=support_oppose, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_by_candidate_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
support_oppose = 'null' # str | Support or opposition (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.communication_costs_by_candidate_get(api_key, election_full=election_full, sort=sort, candidate_id=candidate_id, state=state, sort_hide_null=sort_hide_null, per_page=per_page, district=district, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, support_oppose=support_oppose, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_by_candidate_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
support_oppose = 'null' # str | Support or opposition (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.communication_costs_by_candidate_get(api_key, election_full=election_full, sort=sort, candidate_id=candidate_id, state=state, sort_hide_null=sort_hide_null, per_page=per_page, district=district, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, support_oppose=support_oppose, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **state** | **str**| US state or territory where a candidate runs for office | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **support_oppose** | **str**| Support or opposition | [optional] [default to &#39;null&#39;]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**CommunicationCostByCandidatePage**](CommunicationCostByCandidatePage.md)

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

# **communication_costs_get**
> CommunicationCostPage communication_costs_get(api_key, min_image_number=min_image_number, sort=sort, candidate_id=candidate_id, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, sort_null_only=sort_null_only, max_date=max_date, min_date=min_date, per_page=per_page, sort_hide_null=sort_hide_null, image_number=image_number, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number, support_oppose_indicator=support_oppose_indicator)



 52 U.S.C. 30118 allows \"communications by a corporation to its stockholders and executive or administrative personnel and their families or by a labor organization to its members and their families on any subject,\" including the express advocacy of the election or defeat of any Federal candidate.  The costs of such communications must be reported to the Federal Election Commission under certain circumstances.

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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
min_image_number = 'min_image_number_example' # str |  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
max_date = '2013-10-20' # date | Maximum date (optional)
min_date = '2013-10-20' # date | Minimum date (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_image_number = 'max_image_number_example' # str |  (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
support_oppose_indicator = ['support_oppose_indicator_example'] # list[str] | Support or opposition (optional)

    try:
        api_response = api_instance.communication_costs_get(api_key, min_image_number=min_image_number, sort=sort, candidate_id=candidate_id, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, sort_null_only=sort_null_only, max_date=max_date, min_date=min_date, per_page=per_page, sort_hide_null=sort_hide_null, image_number=image_number, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number, support_oppose_indicator=support_oppose_indicator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
min_image_number = 'min_image_number_example' # str |  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
max_date = '2013-10-20' # date | Maximum date (optional)
min_date = '2013-10-20' # date | Minimum date (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_image_number = 'max_image_number_example' # str |  (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
support_oppose_indicator = ['support_oppose_indicator_example'] # list[str] | Support or opposition (optional)

    try:
        api_response = api_instance.communication_costs_get(api_key, min_image_number=min_image_number, sort=sort, candidate_id=candidate_id, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, sort_null_only=sort_null_only, max_date=max_date, min_date=min_date, per_page=per_page, sort_hide_null=sort_hide_null, image_number=image_number, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number, support_oppose_indicator=support_oppose_indicator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
min_image_number = 'min_image_number_example' # str |  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
max_date = '2013-10-20' # date | Maximum date (optional)
min_date = '2013-10-20' # date | Minimum date (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_image_number = 'max_image_number_example' # str |  (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
support_oppose_indicator = ['support_oppose_indicator_example'] # list[str] | Support or opposition (optional)

    try:
        api_response = api_instance.communication_costs_get(api_key, min_image_number=min_image_number, sort=sort, candidate_id=candidate_id, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, sort_null_only=sort_null_only, max_date=max_date, min_date=min_date, per_page=per_page, sort_hide_null=sort_hide_null, image_number=image_number, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number, support_oppose_indicator=support_oppose_indicator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **min_image_number** | **str**|  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional]
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **max_date** | **date**| Maximum date | [optional]
 **min_date** | **date**| Minimum date | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **max_image_number** | **str**|  | [optional]
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional]
 **support_oppose_indicator** | [**list[str]**](str.md)| Support or opposition | [optional]

### Return type

[**CommunicationCostPage**](CommunicationCostPage.md)

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

# **communication_costs_totals_by_candidate_get**
> CCTotalsByCandidatePage communication_costs_totals_by_candidate_get(api_key, election_full=election_full, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, sort_null_only=sort_null_only)



 Total communications costs aggregated across committees on supported or opposed candidates by cycle or candidate election year.

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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.communication_costs_totals_by_candidate_get(api_key, election_full=election_full, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_totals_by_candidate_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.communication_costs_totals_by_candidate_get(api_key, election_full=election_full, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_totals_by_candidate_get: %s\n" % e)
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
    api_instance = openfec_sdk.CommunicationCostApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.communication_costs_totals_by_candidate_get(api_key, election_full=election_full, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunicationCostApi->communication_costs_totals_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]

### Return type

[**CCTotalsByCandidatePage**](CCTotalsByCandidatePage.md)

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
