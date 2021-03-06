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


class Election(object):
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
        'candidate_election_year': 'int',
        'candidate_id': 'str',
        'candidate_name': 'str',
        'candidate_pcc_id': 'str',
        'candidate_pcc_name': 'str',
        'cash_on_hand_end_period': 'float',
        'committee_ids': 'list[str]',
        'coverage_end_date': 'date',
        'incumbent_challenge_full': 'str',
        'party_full': 'str',
        'total_disbursements': 'float',
        'total_receipts': 'float'
    }

    attribute_map = {
        'candidate_election_year': 'candidate_election_year',
        'candidate_id': 'candidate_id',
        'candidate_name': 'candidate_name',
        'candidate_pcc_id': 'candidate_pcc_id',
        'candidate_pcc_name': 'candidate_pcc_name',
        'cash_on_hand_end_period': 'cash_on_hand_end_period',
        'committee_ids': 'committee_ids',
        'coverage_end_date': 'coverage_end_date',
        'incumbent_challenge_full': 'incumbent_challenge_full',
        'party_full': 'party_full',
        'total_disbursements': 'total_disbursements',
        'total_receipts': 'total_receipts'
    }

    def __init__(self, candidate_election_year=None, candidate_id=None, candidate_name=None, candidate_pcc_id=None, candidate_pcc_name=None, cash_on_hand_end_period=None, committee_ids=None, coverage_end_date=None, incumbent_challenge_full=None, party_full=None, total_disbursements=None, total_receipts=None, local_vars_configuration=None):  # noqa: E501
        """Election - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._candidate_election_year = None
        self._candidate_id = None
        self._candidate_name = None
        self._candidate_pcc_id = None
        self._candidate_pcc_name = None
        self._cash_on_hand_end_period = None
        self._committee_ids = None
        self._coverage_end_date = None
        self._incumbent_challenge_full = None
        self._party_full = None
        self._total_disbursements = None
        self._total_receipts = None
        self.discriminator = None

        if candidate_election_year is not None:
            self.candidate_election_year = candidate_election_year
        if candidate_id is not None:
            self.candidate_id = candidate_id
        if candidate_name is not None:
            self.candidate_name = candidate_name
        if candidate_pcc_id is not None:
            self.candidate_pcc_id = candidate_pcc_id
        if candidate_pcc_name is not None:
            self.candidate_pcc_name = candidate_pcc_name
        if cash_on_hand_end_period is not None:
            self.cash_on_hand_end_period = cash_on_hand_end_period
        if committee_ids is not None:
            self.committee_ids = committee_ids
        if coverage_end_date is not None:
            self.coverage_end_date = coverage_end_date
        if incumbent_challenge_full is not None:
            self.incumbent_challenge_full = incumbent_challenge_full
        if party_full is not None:
            self.party_full = party_full
        if total_disbursements is not None:
            self.total_disbursements = total_disbursements
        if total_receipts is not None:
            self.total_receipts = total_receipts

    @property
    def candidate_election_year(self):
        """Gets the candidate_election_year of this Election.  # noqa: E501


        :return: The candidate_election_year of this Election.  # noqa: E501
        :rtype: int
        """
        return self._candidate_election_year

    @candidate_election_year.setter
    def candidate_election_year(self, candidate_election_year):
        """Sets the candidate_election_year of this Election.


        :param candidate_election_year: The candidate_election_year of this Election.  # noqa: E501
        :type: int
        """

        self._candidate_election_year = candidate_election_year

    @property
    def candidate_id(self):
        """Gets the candidate_id of this Election.  # noqa: E501


        :return: The candidate_id of this Election.  # noqa: E501
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this Election.


        :param candidate_id: The candidate_id of this Election.  # noqa: E501
        :type: str
        """

        self._candidate_id = candidate_id

    @property
    def candidate_name(self):
        """Gets the candidate_name of this Election.  # noqa: E501


        :return: The candidate_name of this Election.  # noqa: E501
        :rtype: str
        """
        return self._candidate_name

    @candidate_name.setter
    def candidate_name(self, candidate_name):
        """Sets the candidate_name of this Election.


        :param candidate_name: The candidate_name of this Election.  # noqa: E501
        :type: str
        """

        self._candidate_name = candidate_name

    @property
    def candidate_pcc_id(self):
        """Gets the candidate_pcc_id of this Election.  # noqa: E501


        :return: The candidate_pcc_id of this Election.  # noqa: E501
        :rtype: str
        """
        return self._candidate_pcc_id

    @candidate_pcc_id.setter
    def candidate_pcc_id(self, candidate_pcc_id):
        """Sets the candidate_pcc_id of this Election.


        :param candidate_pcc_id: The candidate_pcc_id of this Election.  # noqa: E501
        :type: str
        """

        self._candidate_pcc_id = candidate_pcc_id

    @property
    def candidate_pcc_name(self):
        """Gets the candidate_pcc_name of this Election.  # noqa: E501


        :return: The candidate_pcc_name of this Election.  # noqa: E501
        :rtype: str
        """
        return self._candidate_pcc_name

    @candidate_pcc_name.setter
    def candidate_pcc_name(self, candidate_pcc_name):
        """Sets the candidate_pcc_name of this Election.


        :param candidate_pcc_name: The candidate_pcc_name of this Election.  # noqa: E501
        :type: str
        """

        self._candidate_pcc_name = candidate_pcc_name

    @property
    def cash_on_hand_end_period(self):
        """Gets the cash_on_hand_end_period of this Election.  # noqa: E501


        :return: The cash_on_hand_end_period of this Election.  # noqa: E501
        :rtype: float
        """
        return self._cash_on_hand_end_period

    @cash_on_hand_end_period.setter
    def cash_on_hand_end_period(self, cash_on_hand_end_period):
        """Sets the cash_on_hand_end_period of this Election.


        :param cash_on_hand_end_period: The cash_on_hand_end_period of this Election.  # noqa: E501
        :type: float
        """

        self._cash_on_hand_end_period = cash_on_hand_end_period

    @property
    def committee_ids(self):
        """Gets the committee_ids of this Election.  # noqa: E501


        :return: The committee_ids of this Election.  # noqa: E501
        :rtype: list[str]
        """
        return self._committee_ids

    @committee_ids.setter
    def committee_ids(self, committee_ids):
        """Sets the committee_ids of this Election.


        :param committee_ids: The committee_ids of this Election.  # noqa: E501
        :type: list[str]
        """

        self._committee_ids = committee_ids

    @property
    def coverage_end_date(self):
        """Gets the coverage_end_date of this Election.  # noqa: E501


        :return: The coverage_end_date of this Election.  # noqa: E501
        :rtype: date
        """
        return self._coverage_end_date

    @coverage_end_date.setter
    def coverage_end_date(self, coverage_end_date):
        """Sets the coverage_end_date of this Election.


        :param coverage_end_date: The coverage_end_date of this Election.  # noqa: E501
        :type: date
        """

        self._coverage_end_date = coverage_end_date

    @property
    def incumbent_challenge_full(self):
        """Gets the incumbent_challenge_full of this Election.  # noqa: E501


        :return: The incumbent_challenge_full of this Election.  # noqa: E501
        :rtype: str
        """
        return self._incumbent_challenge_full

    @incumbent_challenge_full.setter
    def incumbent_challenge_full(self, incumbent_challenge_full):
        """Sets the incumbent_challenge_full of this Election.


        :param incumbent_challenge_full: The incumbent_challenge_full of this Election.  # noqa: E501
        :type: str
        """

        self._incumbent_challenge_full = incumbent_challenge_full

    @property
    def party_full(self):
        """Gets the party_full of this Election.  # noqa: E501


        :return: The party_full of this Election.  # noqa: E501
        :rtype: str
        """
        return self._party_full

    @party_full.setter
    def party_full(self, party_full):
        """Sets the party_full of this Election.


        :param party_full: The party_full of this Election.  # noqa: E501
        :type: str
        """

        self._party_full = party_full

    @property
    def total_disbursements(self):
        """Gets the total_disbursements of this Election.  # noqa: E501


        :return: The total_disbursements of this Election.  # noqa: E501
        :rtype: float
        """
        return self._total_disbursements

    @total_disbursements.setter
    def total_disbursements(self, total_disbursements):
        """Sets the total_disbursements of this Election.


        :param total_disbursements: The total_disbursements of this Election.  # noqa: E501
        :type: float
        """

        self._total_disbursements = total_disbursements

    @property
    def total_receipts(self):
        """Gets the total_receipts of this Election.  # noqa: E501


        :return: The total_receipts of this Election.  # noqa: E501
        :rtype: float
        """
        return self._total_receipts

    @total_receipts.setter
    def total_receipts(self, total_receipts):
        """Sets the total_receipts of this Election.


        :param total_receipts: The total_receipts of this Election.  # noqa: E501
        :type: float
        """

        self._total_receipts = total_receipts

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
        if not isinstance(other, Election):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Election):
            return True

        return self.to_dict() != other.to_dict()
