# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openfec_sdk.configuration import Configuration


class ScheduleBByRecipient(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'committee_id': 'str',
        'count': 'int',
        'cycle': 'int',
        'memo_count': 'int',
        'memo_total': 'float',
        'recipient_name': 'str',
        'total': 'float'
    }

    attribute_map = {
        'committee_id': 'committee_id',
        'count': 'count',
        'cycle': 'cycle',
        'memo_count': 'memo_count',
        'memo_total': 'memo_total',
        'recipient_name': 'recipient_name',
        'total': 'total'
    }

    def __init__(self, committee_id=None, count=None, cycle=None, memo_count=None, memo_total=None, recipient_name=None, total=None, local_vars_configuration=None):  # noqa: E501
        """ScheduleBByRecipient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._committee_id = None
        self._count = None
        self._cycle = None
        self._memo_count = None
        self._memo_total = None
        self._recipient_name = None
        self._total = None
        self.discriminator = None

        self.committee_id = committee_id
        self.count = count
        self.cycle = cycle
        self.memo_count = memo_count
        self.memo_total = memo_total
        self.recipient_name = recipient_name
        self.total = total

    @property
    def committee_id(self):
        """Gets the committee_id of this ScheduleBByRecipient.  # noqa: E501

         A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.   # noqa: E501

        :return: The committee_id of this ScheduleBByRecipient.  # noqa: E501
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this ScheduleBByRecipient.

         A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.   # noqa: E501

        :param committee_id: The committee_id of this ScheduleBByRecipient.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and committee_id is None:  # noqa: E501
            raise ValueError('Invalid value for `committee_id`, must not be `None`')  # noqa: E501

        self._committee_id = committee_id

    @property
    def count(self):
        """Gets the count of this ScheduleBByRecipient.  # noqa: E501

         Number of records making up the total.   # noqa: E501

        :return: The count of this ScheduleBByRecipient.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ScheduleBByRecipient.

         Number of records making up the total.   # noqa: E501

        :param count: The count of this ScheduleBByRecipient.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def cycle(self):
        """Gets the cycle of this ScheduleBByRecipient.  # noqa: E501

         Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.   # noqa: E501

        :return: The cycle of this ScheduleBByRecipient.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ScheduleBByRecipient.

         Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.   # noqa: E501

        :param cycle: The cycle of this ScheduleBByRecipient.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and cycle is None:  # noqa: E501
            raise ValueError('Invalid value for `cycle`, must not be `None`')  # noqa: E501

        self._cycle = cycle

    @property
    def memo_count(self):
        """Gets the memo_count of this ScheduleBByRecipient.  # noqa: E501

         Number of records making up the total.   # noqa: E501

        :return: The memo_count of this ScheduleBByRecipient.  # noqa: E501
        :rtype: int
        """
        return self._memo_count

    @memo_count.setter
    def memo_count(self, memo_count):
        """Sets the memo_count of this ScheduleBByRecipient.

         Number of records making up the total.   # noqa: E501

        :param memo_count: The memo_count of this ScheduleBByRecipient.  # noqa: E501
        :type: int
        """

        self._memo_count = memo_count

    @property
    def memo_total(self):
        """Gets the memo_total of this ScheduleBByRecipient.  # noqa: E501

         Schedule B disbursements aggregated by memoed items only   # noqa: E501

        :return: The memo_total of this ScheduleBByRecipient.  # noqa: E501
        :rtype: float
        """
        return self._memo_total

    @memo_total.setter
    def memo_total(self, memo_total):
        """Sets the memo_total of this ScheduleBByRecipient.

         Schedule B disbursements aggregated by memoed items only   # noqa: E501

        :param memo_total: The memo_total of this ScheduleBByRecipient.  # noqa: E501
        :type: float
        """

        self._memo_total = memo_total

    @property
    def recipient_name(self):
        """Gets the recipient_name of this ScheduleBByRecipient.  # noqa: E501

        Name of the entity receiving the disbursement  # noqa: E501

        :return: The recipient_name of this ScheduleBByRecipient.  # noqa: E501
        :rtype: str
        """
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, recipient_name):
        """Sets the recipient_name of this ScheduleBByRecipient.

        Name of the entity receiving the disbursement  # noqa: E501

        :param recipient_name: The recipient_name of this ScheduleBByRecipient.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and recipient_name is None:  # noqa: E501
            raise ValueError('Invalid value for `recipient_name`, must not be `None`')  # noqa: E501

        self._recipient_name = recipient_name

    @property
    def total(self):
        """Gets the total of this ScheduleBByRecipient.  # noqa: E501

         Schedule B disbursements aggregated by non-memoed items only   # noqa: E501

        :return: The total of this ScheduleBByRecipient.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ScheduleBByRecipient.

         Schedule B disbursements aggregated by non-memoed items only   # noqa: E501

        :param total: The total of this ScheduleBByRecipient.  # noqa: E501
        :type: float
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, 'to_dict') else x,
                    value
                ))
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], 'to_dict') else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduleBByRecipient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleBByRecipient):
            return True

        return self.to_dict() != other.to_dict()
