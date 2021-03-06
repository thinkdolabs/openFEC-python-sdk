# openfec_sdk.EfilingApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**efile_filings_get**](EfilingApi.md#efile_filings_get) | **GET** /efile/filings/ |
[**efile_reports_house_senate_get**](EfilingApi.md#efile_reports_house_senate_get) | **GET** /efile/reports/house-senate/ |
[**efile_reports_pac_party_get**](EfilingApi.md#efile_reports_pac_party_get) | **GET** /efile/reports/pac-party/ |
[**efile_reports_presidential_get**](EfilingApi.md#efile_reports_presidential_get) | **GET** /efile/reports/presidential/ |


# **efile_filings_get**
> EFilingsPage efile_filings_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)



Basic information about electronic files coming into the FEC, posted as they are received.

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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_filings_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_filings_get: %s\n" % e)
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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_filings_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_filings_get: %s\n" % e)
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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_filings_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_filings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-receipt_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **file_number** | [**list[int]**](int.md)| Filing ID number | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]

### Return type

[**EFilingsPage**](EFilingsPage.md)

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

# **efile_reports_house_senate_get**
> BaseF3FilingPage efile_reports_house_senate_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users.

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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_house_senate_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_house_senate_get: %s\n" % e)
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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_house_senate_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_house_senate_get: %s\n" % e)
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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_house_senate_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_house_senate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-receipt_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **file_number** | [**list[int]**](int.md)| Filing ID number | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]

### Return type

[**BaseF3FilingPage**](BaseF3FilingPage.md)

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

# **efile_reports_pac_party_get**
> BaseF3XFilingPage efile_reports_pac_party_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users.

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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_pac_party_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_pac_party_get: %s\n" % e)
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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_pac_party_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_pac_party_get: %s\n" % e)
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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_pac_party_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_pac_party_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-receipt_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **file_number** | [**list[int]**](int.md)| Filing ID number | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]

### Return type

[**BaseF3XFilingPage**](BaseF3XFilingPage.md)

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

# **efile_reports_presidential_get**
> BaseF3PFilingPage efile_reports_presidential_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users.

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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_presidential_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_presidential_get: %s\n" % e)
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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_presidential_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_presidential_get: %s\n" % e)
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
    api_instance = openfec_sdk.EfilingApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort = '-receipt_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-receipt_date')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
file_number = [56] # list[int] | Filing ID number (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.efile_reports_presidential_get(api_key, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date, sort_nulls_last=sort_nulls_last, committee_id=committee_id, page=page, file_number=file_number, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EfilingApi->efile_reports_presidential_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-receipt_date&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **file_number** | [**list[int]**](int.md)| Filing ID number | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]

### Return type

[**BaseF3PFilingPage**](BaseF3PFilingPage.md)

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
