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
from openfec_sdk.models.schedule_e_efile_page import ScheduleEEfilePage  # noqa: E501
from openfec_sdk.rest import ApiException

class TestScheduleEEfilePage(unittest.TestCase):
    """ScheduleEEfilePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScheduleEEfilePage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openfec_sdk.models.schedule_e_efile_page.ScheduleEEfilePage()  # noqa: E501
        if include_optional :
            return ScheduleEEfilePage(
                pagination = openfec_sdk.models.offset_info.OffsetInfo(
                    count = 56,
                    page = 56,
                    pages = 56,
                    per_page = 56, ),
                results = [
                    openfec_sdk.models.schedule_e_efile.ScheduleEEfile(
                        amendment_indicator = '0',
                        back_reference_schedule_name = '0',
                        back_reference_transaction_id = '0',
                        beginning_image_number = '0',
                        candidate_first_name = '0',
                        candidate_id = '0',
                        candidate_middle_name = '0',
                        candidate_name = '0',
                        candidate_office = '0',
                        candidate_office_district = '0',
                        candidate_office_state = '0',
                        candidate_party = '0',
                        candidate_prefix = '0',
                        candidate_suffix = '0',
                        category_code = '0',
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
                        csv_url = '0',
                        dissemination_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        entity_type = '0',
                        expenditure_amount = 56,
                        expenditure_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        expenditure_description = '0',
                        fec_url = '0',
                        file_number = 56,
                        filer_first_name = '0',
                        filer_last_name = '0',
                        filer_middle_name = '0',
                        filer_prefix = '0',
                        filer_suffix = '0',
                        filing = openfec_sdk.models.e_filings.EFilings(
                            amended_by = 56,
                            amendment_chain = [
                                56
                                ],
                            amendment_number = 56,
                            amends_file = 56,
                            beginning_image_number = '0',
                            committee_id = '0',
                            committee_name = '0',
                            coverage_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                            coverage_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                            csv_url = '0',
                            document_description = '0',
                            ending_image_number = '0',
                            fec_file_id = '0',
                            fec_url = '0',
                            file_number = 56,
                            filed_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                            form_type = '0',
                            html_url = '0',
                            is_amended = True,
                            load_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                            most_recent = True,
                            most_recent_filing = 56,
                            pdf_url = '0',
                            receipt_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                        filing_form = '0',
                        image_number = '0',
                        is_notice = True,
                        line_number = '0',
                        load_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        memo_code = '0',
                        memo_text = '0',
                        most_recent = True,
                        notary_sign_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        office_total_ytd = 1.337,
                        payee_city = '0',
                        payee_first_name = '0',
                        payee_last_name = '0',
                        payee_middle_name = '0',
                        payee_name = '0',
                        payee_prefix = '0',
                        payee_state = '0',
                        payee_street_1 = '0',
                        payee_street_2 = '0',
                        payee_suffix = '0',
                        payee_zip = '0',
                        pdf_url = '0',
                        related_line_number = 56,
                        report_type = '0',
                        support_oppose_indicator = '0',
                        transaction_id = '0', )
                    ]
            )
        else :
            return ScheduleEEfilePage(
        )

    def testScheduleEEfilePage(self):
        """Test ScheduleEEfilePage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
