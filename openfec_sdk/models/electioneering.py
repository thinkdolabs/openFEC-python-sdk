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


class Electioneering(object):
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
        'amendment_indicator': 'str',
        'beginning_image_number': 'str',
        'calculated_candidate_share': 'float',
        'candidate_district': 'str',
        'candidate_id': 'str',
        'candidate_name': 'str',
        'candidate_office': 'str',
        'candidate_state': 'str',
        'committee_id': 'str',
        'committee_name': 'str',
        'communication_date': 'date',
        'disbursement_amount': 'float',
        'disbursement_date': 'date',
        'election_type': 'str',
        'file_number': 'int',
        'link_id': 'int',
        'number_of_candidates': 'float',
        'payee_name': 'str',
        'payee_state': 'str',
        'pdf_url': 'str',
        'public_distribution_date': 'date',
        'purpose_description': 'str',
        'receipt_date': 'date',
        'report_year': 'int',
        'sb_image_num': 'str',
        'sb_link_id': 'str',
        'sub_id': 'int'
    }

    attribute_map = {
        'amendment_indicator': 'amendment_indicator',
        'beginning_image_number': 'beginning_image_number',
        'calculated_candidate_share': 'calculated_candidate_share',
        'candidate_district': 'candidate_district',
        'candidate_id': 'candidate_id',
        'candidate_name': 'candidate_name',
        'candidate_office': 'candidate_office',
        'candidate_state': 'candidate_state',
        'committee_id': 'committee_id',
        'committee_name': 'committee_name',
        'communication_date': 'communication_date',
        'disbursement_amount': 'disbursement_amount',
        'disbursement_date': 'disbursement_date',
        'election_type': 'election_type',
        'file_number': 'file_number',
        'link_id': 'link_id',
        'number_of_candidates': 'number_of_candidates',
        'payee_name': 'payee_name',
        'payee_state': 'payee_state',
        'pdf_url': 'pdf_url',
        'public_distribution_date': 'public_distribution_date',
        'purpose_description': 'purpose_description',
        'receipt_date': 'receipt_date',
        'report_year': 'report_year',
        'sb_image_num': 'sb_image_num',
        'sb_link_id': 'sb_link_id',
        'sub_id': 'sub_id'
    }

    def __init__(self, amendment_indicator=None, beginning_image_number=None, calculated_candidate_share=None, candidate_district=None, candidate_id=None, candidate_name=None, candidate_office=None, candidate_state=None, committee_id=None, committee_name=None, communication_date=None, disbursement_amount=None, disbursement_date=None, election_type=None, file_number=None, link_id=None, number_of_candidates=None, payee_name=None, payee_state=None, pdf_url=None, public_distribution_date=None, purpose_description=None, receipt_date=None, report_year=None, sb_image_num=None, sb_link_id=None, sub_id=None, local_vars_configuration=None):  # noqa: E501
        """Electioneering - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amendment_indicator = None
        self._beginning_image_number = None
        self._calculated_candidate_share = None
        self._candidate_district = None
        self._candidate_id = None
        self._candidate_name = None
        self._candidate_office = None
        self._candidate_state = None
        self._committee_id = None
        self._committee_name = None
        self._communication_date = None
        self._disbursement_amount = None
        self._disbursement_date = None
        self._election_type = None
        self._file_number = None
        self._link_id = None
        self._number_of_candidates = None
        self._payee_name = None
        self._payee_state = None
        self._pdf_url = None
        self._public_distribution_date = None
        self._purpose_description = None
        self._receipt_date = None
        self._report_year = None
        self._sb_image_num = None
        self._sb_link_id = None
        self._sub_id = None
        self.discriminator = None

        self.amendment_indicator = amendment_indicator
        self.beginning_image_number = beginning_image_number
        self.calculated_candidate_share = calculated_candidate_share
        self.candidate_district = candidate_district
        self.candidate_id = candidate_id
        self.candidate_name = candidate_name
        self.candidate_office = candidate_office
        self.candidate_state = candidate_state
        self.committee_id = committee_id
        self.committee_name = committee_name
        self.communication_date = communication_date
        self.disbursement_amount = disbursement_amount
        self.disbursement_date = disbursement_date
        if election_type is not None:
            self.election_type = election_type
        self.file_number = file_number
        self.link_id = link_id
        self.number_of_candidates = number_of_candidates
        self.payee_name = payee_name
        self.payee_state = payee_state
        self.pdf_url = pdf_url
        self.public_distribution_date = public_distribution_date
        self.purpose_description = purpose_description
        self.receipt_date = receipt_date
        self.report_year = report_year
        self.sb_image_num = sb_image_num
        self.sb_link_id = sb_link_id
        self.sub_id = sub_id

    @property
    def amendment_indicator(self):
        """Gets the amendment_indicator of this Electioneering.  # noqa: E501


        :return: The amendment_indicator of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._amendment_indicator

    @amendment_indicator.setter
    def amendment_indicator(self, amendment_indicator):
        """Sets the amendment_indicator of this Electioneering.


        :param amendment_indicator: The amendment_indicator of this Electioneering.  # noqa: E501
        :type: str
        """

        self._amendment_indicator = amendment_indicator

    @property
    def beginning_image_number(self):
        """Gets the beginning_image_number of this Electioneering.  # noqa: E501


        :return: The beginning_image_number of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._beginning_image_number

    @beginning_image_number.setter
    def beginning_image_number(self, beginning_image_number):
        """Sets the beginning_image_number of this Electioneering.


        :param beginning_image_number: The beginning_image_number of this Electioneering.  # noqa: E501
        :type: str
        """

        self._beginning_image_number = beginning_image_number

    @property
    def calculated_candidate_share(self):
        """Gets the calculated_candidate_share of this Electioneering.  # noqa: E501

         \"If an electioneering cost targets several candidates, the total cost is divided by the number of candidates. If it only mentions one candidate the full cost of the communication is listed.\"   # noqa: E501

        :return: The calculated_candidate_share of this Electioneering.  # noqa: E501
        :rtype: float
        """
        return self._calculated_candidate_share

    @calculated_candidate_share.setter
    def calculated_candidate_share(self, calculated_candidate_share):
        """Sets the calculated_candidate_share of this Electioneering.

         \"If an electioneering cost targets several candidates, the total cost is divided by the number of candidates. If it only mentions one candidate the full cost of the communication is listed.\"   # noqa: E501

        :param calculated_candidate_share: The calculated_candidate_share of this Electioneering.  # noqa: E501
        :type: float
        """

        self._calculated_candidate_share = calculated_candidate_share

    @property
    def candidate_district(self):
        """Gets the candidate_district of this Electioneering.  # noqa: E501


        :return: The candidate_district of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._candidate_district

    @candidate_district.setter
    def candidate_district(self, candidate_district):
        """Sets the candidate_district of this Electioneering.


        :param candidate_district: The candidate_district of this Electioneering.  # noqa: E501
        :type: str
        """

        self._candidate_district = candidate_district

    @property
    def candidate_id(self):
        """Gets the candidate_id of this Electioneering.  # noqa: E501


        :return: The candidate_id of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this Electioneering.


        :param candidate_id: The candidate_id of this Electioneering.  # noqa: E501
        :type: str
        """

        self._candidate_id = candidate_id

    @property
    def candidate_name(self):
        """Gets the candidate_name of this Electioneering.  # noqa: E501


        :return: The candidate_name of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._candidate_name

    @candidate_name.setter
    def candidate_name(self, candidate_name):
        """Sets the candidate_name of this Electioneering.


        :param candidate_name: The candidate_name of this Electioneering.  # noqa: E501
        :type: str
        """

        self._candidate_name = candidate_name

    @property
    def candidate_office(self):
        """Gets the candidate_office of this Electioneering.  # noqa: E501


        :return: The candidate_office of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._candidate_office

    @candidate_office.setter
    def candidate_office(self, candidate_office):
        """Sets the candidate_office of this Electioneering.


        :param candidate_office: The candidate_office of this Electioneering.  # noqa: E501
        :type: str
        """

        self._candidate_office = candidate_office

    @property
    def candidate_state(self):
        """Gets the candidate_state of this Electioneering.  # noqa: E501


        :return: The candidate_state of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._candidate_state

    @candidate_state.setter
    def candidate_state(self, candidate_state):
        """Sets the candidate_state of this Electioneering.


        :param candidate_state: The candidate_state of this Electioneering.  # noqa: E501
        :type: str
        """

        self._candidate_state = candidate_state

    @property
    def committee_id(self):
        """Gets the committee_id of this Electioneering.  # noqa: E501


        :return: The committee_id of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this Electioneering.


        :param committee_id: The committee_id of this Electioneering.  # noqa: E501
        :type: str
        """

        self._committee_id = committee_id

    @property
    def committee_name(self):
        """Gets the committee_name of this Electioneering.  # noqa: E501


        :return: The committee_name of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._committee_name

    @committee_name.setter
    def committee_name(self, committee_name):
        """Sets the committee_name of this Electioneering.


        :param committee_name: The committee_name of this Electioneering.  # noqa: E501
        :type: str
        """

        self._committee_name = committee_name

    @property
    def communication_date(self):
        """Gets the communication_date of this Electioneering.  # noqa: E501

         It is the airing, broadcast, cablecast or other dissemination of the communication.   # noqa: E501

        :return: The communication_date of this Electioneering.  # noqa: E501
        :rtype: date
        """
        return self._communication_date

    @communication_date.setter
    def communication_date(self, communication_date):
        """Sets the communication_date of this Electioneering.

         It is the airing, broadcast, cablecast or other dissemination of the communication.   # noqa: E501

        :param communication_date: The communication_date of this Electioneering.  # noqa: E501
        :type: date
        """

        self._communication_date = communication_date

    @property
    def disbursement_amount(self):
        """Gets the disbursement_amount of this Electioneering.  # noqa: E501


        :return: The disbursement_amount of this Electioneering.  # noqa: E501
        :rtype: float
        """
        return self._disbursement_amount

    @disbursement_amount.setter
    def disbursement_amount(self, disbursement_amount):
        """Sets the disbursement_amount of this Electioneering.


        :param disbursement_amount: The disbursement_amount of this Electioneering.  # noqa: E501
        :type: float
        """

        self._disbursement_amount = disbursement_amount

    @property
    def disbursement_date(self):
        """Gets the disbursement_date of this Electioneering.  # noqa: E501

         Disbursement date includes actual disbursements and execution of contracts creating an obligation to make disbursements (SB date of disbursement).   # noqa: E501

        :return: The disbursement_date of this Electioneering.  # noqa: E501
        :rtype: date
        """
        return self._disbursement_date

    @disbursement_date.setter
    def disbursement_date(self, disbursement_date):
        """Sets the disbursement_date of this Electioneering.

         Disbursement date includes actual disbursements and execution of contracts creating an obligation to make disbursements (SB date of disbursement).   # noqa: E501

        :param disbursement_date: The disbursement_date of this Electioneering.  # noqa: E501
        :type: date
        """

        self._disbursement_date = disbursement_date

    @property
    def election_type(self):
        """Gets the election_type of this Electioneering.  # noqa: E501


        :return: The election_type of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._election_type

    @election_type.setter
    def election_type(self, election_type):
        """Sets the election_type of this Electioneering.


        :param election_type: The election_type of this Electioneering.  # noqa: E501
        :type: str
        """

        self._election_type = election_type

    @property
    def file_number(self):
        """Gets the file_number of this Electioneering.  # noqa: E501


        :return: The file_number of this Electioneering.  # noqa: E501
        :rtype: int
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this Electioneering.


        :param file_number: The file_number of this Electioneering.  # noqa: E501
        :type: int
        """

        self._file_number = file_number

    @property
    def link_id(self):
        """Gets the link_id of this Electioneering.  # noqa: E501


        :return: The link_id of this Electioneering.  # noqa: E501
        :rtype: int
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """Sets the link_id of this Electioneering.


        :param link_id: The link_id of this Electioneering.  # noqa: E501
        :type: int
        """

        self._link_id = link_id

    @property
    def number_of_candidates(self):
        """Gets the number_of_candidates of this Electioneering.  # noqa: E501


        :return: The number_of_candidates of this Electioneering.  # noqa: E501
        :rtype: float
        """
        return self._number_of_candidates

    @number_of_candidates.setter
    def number_of_candidates(self, number_of_candidates):
        """Sets the number_of_candidates of this Electioneering.


        :param number_of_candidates: The number_of_candidates of this Electioneering.  # noqa: E501
        :type: float
        """

        self._number_of_candidates = number_of_candidates

    @property
    def payee_name(self):
        """Gets the payee_name of this Electioneering.  # noqa: E501

         Name of the entity that received the payment.   # noqa: E501

        :return: The payee_name of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this Electioneering.

         Name of the entity that received the payment.   # noqa: E501

        :param payee_name: The payee_name of this Electioneering.  # noqa: E501
        :type: str
        """

        self._payee_name = payee_name

    @property
    def payee_state(self):
        """Gets the payee_state of this Electioneering.  # noqa: E501


        :return: The payee_state of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._payee_state

    @payee_state.setter
    def payee_state(self, payee_state):
        """Sets the payee_state of this Electioneering.


        :param payee_state: The payee_state of this Electioneering.  # noqa: E501
        :type: str
        """

        self._payee_state = payee_state

    @property
    def pdf_url(self):
        """Gets the pdf_url of this Electioneering.  # noqa: E501


        :return: The pdf_url of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, pdf_url):
        """Sets the pdf_url of this Electioneering.


        :param pdf_url: The pdf_url of this Electioneering.  # noqa: E501
        :type: str
        """

        self._pdf_url = pdf_url

    @property
    def public_distribution_date(self):
        """Gets the public_distribution_date of this Electioneering.  # noqa: E501

         The pubic distribution date is the date that triggers disclosure of the electioneering communication (date reported on page 1 of Form 9).   # noqa: E501

        :return: The public_distribution_date of this Electioneering.  # noqa: E501
        :rtype: date
        """
        return self._public_distribution_date

    @public_distribution_date.setter
    def public_distribution_date(self, public_distribution_date):
        """Sets the public_distribution_date of this Electioneering.

         The pubic distribution date is the date that triggers disclosure of the electioneering communication (date reported on page 1 of Form 9).   # noqa: E501

        :param public_distribution_date: The public_distribution_date of this Electioneering.  # noqa: E501
        :type: date
        """

        self._public_distribution_date = public_distribution_date

    @property
    def purpose_description(self):
        """Gets the purpose_description of this Electioneering.  # noqa: E501


        :return: The purpose_description of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._purpose_description

    @purpose_description.setter
    def purpose_description(self, purpose_description):
        """Sets the purpose_description of this Electioneering.


        :param purpose_description: The purpose_description of this Electioneering.  # noqa: E501
        :type: str
        """

        self._purpose_description = purpose_description

    @property
    def receipt_date(self):
        """Gets the receipt_date of this Electioneering.  # noqa: E501


        :return: The receipt_date of this Electioneering.  # noqa: E501
        :rtype: date
        """
        return self._receipt_date

    @receipt_date.setter
    def receipt_date(self, receipt_date):
        """Sets the receipt_date of this Electioneering.


        :param receipt_date: The receipt_date of this Electioneering.  # noqa: E501
        :type: date
        """

        self._receipt_date = receipt_date

    @property
    def report_year(self):
        """Gets the report_year of this Electioneering.  # noqa: E501


        :return: The report_year of this Electioneering.  # noqa: E501
        :rtype: int
        """
        return self._report_year

    @report_year.setter
    def report_year(self, report_year):
        """Sets the report_year of this Electioneering.


        :param report_year: The report_year of this Electioneering.  # noqa: E501
        :type: int
        """

        self._report_year = report_year

    @property
    def sb_image_num(self):
        """Gets the sb_image_num of this Electioneering.  # noqa: E501


        :return: The sb_image_num of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._sb_image_num

    @sb_image_num.setter
    def sb_image_num(self, sb_image_num):
        """Sets the sb_image_num of this Electioneering.


        :param sb_image_num: The sb_image_num of this Electioneering.  # noqa: E501
        :type: str
        """

        self._sb_image_num = sb_image_num

    @property
    def sb_link_id(self):
        """Gets the sb_link_id of this Electioneering.  # noqa: E501


        :return: The sb_link_id of this Electioneering.  # noqa: E501
        :rtype: str
        """
        return self._sb_link_id

    @sb_link_id.setter
    def sb_link_id(self, sb_link_id):
        """Sets the sb_link_id of this Electioneering.


        :param sb_link_id: The sb_link_id of this Electioneering.  # noqa: E501
        :type: str
        """

        self._sb_link_id = sb_link_id

    @property
    def sub_id(self):
        """Gets the sub_id of this Electioneering.  # noqa: E501

         The identifier for each electioneering record.   # noqa: E501

        :return: The sub_id of this Electioneering.  # noqa: E501
        :rtype: int
        """
        return self._sub_id

    @sub_id.setter
    def sub_id(self, sub_id):
        """Sets the sub_id of this Electioneering.

         The identifier for each electioneering record.   # noqa: E501

        :param sub_id: The sub_id of this Electioneering.  # noqa: E501
        :type: int
        """

        self._sub_id = sub_id

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
        if not isinstance(other, Electioneering):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Electioneering):
            return True

        return self.to_dict() != other.to_dict()
