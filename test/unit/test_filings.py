# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openfec_sdk
from openfec_sdk.models.filings import Filings  # noqa: E501
from openfec_sdk.rest import ApiException

class TestFilings(unittest.TestCase):
    """Filings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Filings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openfec_sdk.models.filings.Filings()  # noqa: E501
        if include_optional :
            return Filings(
                amendment_chain = [
                    1.337
                    ],
                amendment_indicator = '0',
                amendment_version = 56,
                beginning_image_number = '0',
                candidate_id = '0',
                candidate_name = '0',
                cash_on_hand_beginning_period = 1.337,
                cash_on_hand_end_period = 1.337,
                committee_id = '0',
                committee_name = '0',
                committee_type = '0',
                coverage_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                coverage_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                csv_url = '0',
                cycle = 56,
                debts_owed_by_committee = 1.337,
                debts_owed_to_committee = 1.337,
                document_description = '0',
                document_type = '0',
                document_type_full = '0',
                election_year = 56,
                ending_image_number = '0',
                fec_file_id = '0',
                fec_url = '0',
                file_number = 56,
                form_category = '0',
                form_type = '0',
                house_personal_funds = 1.337,
                html_url = '0',
                is_amended = True,
                means_filed = '0',
                most_recent = True,
                most_recent_file_number = 56,
                net_donations = 1.337,
                office = '0',
                opposition_personal_funds = 1.337,
                pages = 56,
                party = '0',
                pdf_url = '0',
                previous_file_number = 56,
                primary_general_indicator = '0',
                receipt_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                report_type = '0',
                report_type_full = '0',
                report_year = 56,
                request_type = '0',
                senate_personal_funds = 1.337,
                state = '0',
                sub_id = '0',
                total_communication_cost = 1.337,
                total_disbursements = 1.337,
                total_independent_expenditures = 1.337,
                total_individual_contributions = 1.337,
                total_receipts = 1.337,
                treasurer_name = '0',
                update_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else :
            return Filings(
        )

    def testFilings(self):
        """Test Filings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
