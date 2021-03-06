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
from openfec_sdk.models.schedule_h4_page import ScheduleH4Page  # noqa: E501
from openfec_sdk.rest import ApiException

class TestScheduleH4Page(unittest.TestCase):
    """ScheduleH4Page unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScheduleH4Page
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openfec_sdk.models.schedule_h4_page.ScheduleH4Page()  # noqa: E501
        if include_optional :
            return ScheduleH4Page(
                pagination = openfec_sdk.models.seek_info.SeekInfo(
                    count = 56,
                    last_indexes = '0',
                    pages = 56,
                    per_page = 56, ),
                results = [
                    openfec_sdk.models.schedule_h4.ScheduleH4(
                        additional_description = '0',
                        administrative_activity_inidcator = '0',
                        administrative_voter_drive_activity_indicator = '0',
                        amendment_indicator = '0',
                        amendment_indicator_desc = '0',
                        back_reference_schedule_id = '0',
                        back_reference_transaction_id = '0',
                        candidate_first_name = '0',
                        candidate_id = '0',
                        candidate_last_name = '0',
                        candidate_name = '0',
                        candidate_office = '0',
                        candidate_office_description = '0',
                        candidate_office_district = '0',
                        candidate_office_state = '0',
                        candidate_office_state_full = '0',
                        category_code = '0',
                        category_code_full = '0',
                        committee = openfec_sdk.models.committee_history.CommitteeHistory(
                            affiliated_committee_name = '0',
                            candidate_ids = [
                                '0'
                                ],
                            city = '0',
                            committee_id = '0',
                            committee_type = '0',
                            committee_type_full = '0',
                            cycle = 56,
                            cycles = [
                                56
                                ],
                            cycles_has_activity = [
                                56
                                ],
                            cycles_has_financial = [
                                56
                                ],
                            designation = '0',
                            designation_full = '0',
                            filing_frequency = '0',
                            is_active = True,
                            last_cycle_has_activity = 56,
                            last_cycle_has_financial = 56,
                            name = '0',
                            organization_type = '0',
                            organization_type_full = '0',
                            party = '0',
                            party_full = '0',
                            state = '0',
                            state_full = '0',
                            street_1 = '0',
                            street_2 = '0',
                            treasurer_name = '0',
                            zip = '0', ),
                        committee_id = '0',
                        conduit_committee_city = '0',
                        conduit_committee_id = '0',
                        conduit_committee_name = '0',
                        conduit_committee_state = '0',
                        conduit_committee_street1 = '0',
                        conduit_committee_street2 = '0',
                        conduit_committee_zip = 56,
                        cycle = 1.337,
                        direct_candidate_support_activity_indicator = '0',
                        disbursement_amount = 1.337,
                        disbursement_type = '0',
                        disbursement_type_full = '0',
                        entity_type = '0',
                        entity_type_desc = '0',
                        event_amount_year_to_date = 1.337,
                        event_purpose_category_type = '0',
                        event_purpose_category_type_full = '0',
                        event_purpose_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        event_purpose_description = '0',
                        event_purpose_name = '0',
                        exempt_activity_indicator = '0',
                        federal_share = 1.337,
                        file_number = 56,
                        filer_committee_name = '0',
                        filing_form = '0',
                        fundraising_activity_indicator = '0',
                        general_voter_drive_activity_indicator = '0',
                        image_number = '0',
                        line_number = '0',
                        link_id = 56,
                        load_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        memo_code = '0',
                        memo_code_description = '0',
                        memo_text = '0',
                        nonfederal_share = 1.337,
                        original_sub_id = '0',
                        payee_city = '0',
                        payee_first_name = '0',
                        payee_last_name = '0',
                        payee_middle_name = '0',
                        payee_name = '0',
                        payee_prefix = '0',
                        payee_state = '0',
                        payee_suffix = '0',
                        payee_zip = '0',
                        published_committee_reference_parity_check = '0',
                        report_type = '0',
                        report_year = 1.337,
                        schedule_type = '0',
                        schedule_type_full = '0',
                        sub_id = '0',
                        transaction_id = '0', )
                    ]
            )
        else :
            return ScheduleH4Page(
        )

    def testScheduleH4Page(self):
        """Test ScheduleH4Page"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
