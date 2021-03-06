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
from openfec_sdk.models.presidential_summary_page import PresidentialSummaryPage  # noqa: E501
from openfec_sdk.rest import ApiException

class TestPresidentialSummaryPage(unittest.TestCase):
    """PresidentialSummaryPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PresidentialSummaryPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openfec_sdk.models.presidential_summary_page.PresidentialSummaryPage()  # noqa: E501
        if include_optional :
            return PresidentialSummaryPage(
                pagination = openfec_sdk.models.offset_info.OffsetInfo(
                    count = 56,
                    page = 56,
                    pages = 56,
                    per_page = 56, ),
                results = [
                    openfec_sdk.models.presidential_summary.PresidentialSummary(
                        candidate_contributions_less_repayments = 1.337,
                        candidate_id = '0',
                        candidate_last_name = '0',
                        candidate_name = '0',
                        candidate_party_affiliation = '0',
                        cash_on_hand_end = 1.337,
                        committee_designation = '0',
                        committee_id = '0',
                        committee_name = '0',
                        committee_type = '0',
                        debts_owed_by_committee = 1.337,
                        disbursements_less_offsets = 1.337,
                        election_year = 56,
                        exempt_legal_accounting_disbursement = 1.337,
                        federal_funds = 1.337,
                        fundraising_disbursements = 1.337,
                        individual_contributions_less_refunds = 1.337,
                        net_receipts = 1.337,
                        offsets_to_operating_expenditures = 1.337,
                        operating_expenditures = 1.337,
                        other_disbursements = 1.337,
                        pac_contributions_less_refunds = 1.337,
                        party_contributions_less_refunds = 1.337,
                        repayments_loans_made_by_candidate = 1.337,
                        repayments_other_loans = 1.337,
                        rounded_net_receipts = 1.337,
                        total_contribution_refunds = 1.337,
                        total_loan_repayments_made = 1.337,
                        transfers_from_affiliated_committees = 1.337,
                        transfers_to_other_authorized_committees = 1.337, )
                    ]
            )
        else :
            return PresidentialSummaryPage(
        )

    def testPresidentialSummaryPage(self):
        """Test PresidentialSummaryPage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
