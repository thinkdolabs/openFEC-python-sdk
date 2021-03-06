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


class PresidentialCoverage(object):
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
        'candidate_id': 'str',
        'coverage_end_date': 'datetime',
        'election_year': 'int'
    }

    attribute_map = {
        'candidate_id': 'candidate_id',
        'coverage_end_date': 'coverage_end_date',
        'election_year': 'election_year'
    }

    def __init__(self, candidate_id=None, coverage_end_date=None, election_year=None, local_vars_configuration=None):  # noqa: E501
        """PresidentialCoverage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._candidate_id = None
        self._coverage_end_date = None
        self._election_year = None
        self.discriminator = None

        self.candidate_id = candidate_id
        self.coverage_end_date = coverage_end_date
        self.election_year = election_year

    @property
    def candidate_id(self):
        """Gets the candidate_id of this PresidentialCoverage.  # noqa: E501

         A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans   # noqa: E501

        :return: The candidate_id of this PresidentialCoverage.  # noqa: E501
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this PresidentialCoverage.

         A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans   # noqa: E501

        :param candidate_id: The candidate_id of this PresidentialCoverage.  # noqa: E501
        :type: str
        """

        self._candidate_id = candidate_id

    @property
    def coverage_end_date(self):
        """Gets the coverage_end_date of this PresidentialCoverage.  # noqa: E501

        Ending date of the reporting period  # noqa: E501

        :return: The coverage_end_date of this PresidentialCoverage.  # noqa: E501
        :rtype: datetime
        """
        return self._coverage_end_date

    @coverage_end_date.setter
    def coverage_end_date(self, coverage_end_date):
        """Sets the coverage_end_date of this PresidentialCoverage.

        Ending date of the reporting period  # noqa: E501

        :param coverage_end_date: The coverage_end_date of this PresidentialCoverage.  # noqa: E501
        :type: datetime
        """

        self._coverage_end_date = coverage_end_date

    @property
    def election_year(self):
        """Gets the election_year of this PresidentialCoverage.  # noqa: E501

        Year of election  # noqa: E501

        :return: The election_year of this PresidentialCoverage.  # noqa: E501
        :rtype: int
        """
        return self._election_year

    @election_year.setter
    def election_year(self, election_year):
        """Sets the election_year of this PresidentialCoverage.

        Year of election  # noqa: E501

        :param election_year: The election_year of this PresidentialCoverage.  # noqa: E501
        :type: int
        """

        self._election_year = election_year

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
        if not isinstance(other, PresidentialCoverage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PresidentialCoverage):
            return True

        return self.to_dict() != other.to_dict()
