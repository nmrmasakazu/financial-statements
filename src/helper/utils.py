# Thanks to https://flat-kids.net/2020/02/29/edinetのxbrlからcsv出力/
from collections import OrderedDict


class Utils:

    def get_key_contexts(self):
        # TODO: 修正する必要あり（jpdei_cor）
        dict_cols = OrderedDict()
        dict_cols = {
            "企業名":
            {
                "key": ["jpdei_cor:FilerNameInJapaneseDEI"],
                "context_ref": ["FilingDateInstant"]
            },
            "EDINETコード":
            {
                "key": ["EDINETCodeDEI"],
                "context_ref": ["FilingDateInstant"]
            },
            "提出者業種":
            {
                "key": [],
                "context_ref": [""]
            },
            "単独/連結":
            {
                "key": [],
                "context_ref": [""]
            },
            "証券コード":
            {
                "key": ["SecurityCodeDEI"],
                "context_ref": ["FilingDateInstant"]
            },
            "当事業年度開始日":
            {
                "key": ["CurrentFiscalYearStartDateDEI"],
                "context_ref": ["FilingDateInstant"]
            },
            "当事業年度終了日":
            {
                "key": ["CurrentFiscalYearEndDateDEI"],
                "context_ref": ["FilingDateInstant"]
            },
            "平均年間給与（円）":
            {
                "key":
                ["AverageAnnualSalaryInformationAboutReportingCompanyInformationAboutEmployees"],
                "context_ref": ["CurrentYearInstant"]
            },
            "平均勤続年数（年）":
            {
                "key": ["AverageLengthOfServiceYearsInformationAboutReportingCompanyInformationAboutEmployees"],
                "context_ref": ["CurrentYearInstant"]
            },
            "平均年齢（歳）":
            {
                "key": ["AverageAgeYearsInformationAboutReportingCompanyInformationAboutEmployees"],
                "context_ref": ["CurrentYearInstant"]
            },
            "従業員数（人）":
            {
                "key": ["NumberOfEmployees"],
                "context_ref": ["CurrentYearInstant"]
            },
            "売上高":
            {
                "key": ["RevenuesFromExternalCustomers",
                        "TransactionsWithOtherSegments",
                        "jppfs_cor:NetSales",
                        "OperatingRevenue1",
                        "OperatingRevenue2",
                        "GrossOperatingRevenue",
                        "OrdinaryIncomeBNK",
                        "OperatingIncomeINS"],
                "context_ref": ["CurrentYearDuration",
                                "CurrentYearDuration_NonConsolidatedMember"]
            },
            "営業収益":
            {
                "key": ["OperatingRevenue1SummaryOfBusinessResults",
                        "OperatingRevenue2SummaryOfBusinessResults"],
                "context_ref": ["CurrentYearDuration"]
            },
            "経常収益":
            {
                "key": ["OrdinaryIncomeSummaryOfBusinessResults"],
                "context_ref": "CurrentYearDuration"
            },
            "売上原価":
            {
                "key": ["CostOfSales"],
                "context_ref": ["CurrentYearDuration"]
            },
            "営業費用":
            {
                "key": ["OperatingExpenses"],
                "context_ref": ["CurrentYearDuration"]
            },
            "営業原価":
            {
                "key": ["OperatingCost"],
                "context_ref": ["CurrentYearDuration"]
            },
            "売上総利益":
            {
                "key": ["GrossProfit"],
                "context_ref": ["CurrentYearDuration"]
            },
            "営業利益":
            {
                "key": ["OperatingIncome"],
                "context_ref": ["CurrentYearDuration"]
            },
            "経常利益":
            {
                "key": ["OrdinaryIncome"], "context_ref":
                ["CurrentYearDuration"]
            },
            "当期純利益":
            {
                "key": ["ProfitLoss"], "context_ref":
                ["CurrentYearDuration"]
            },
            "親会社の所有者に帰属する利益":
            {
                "key": ["ProfitLossAttributableToOwnersOfParent"],
                "context_ref": ["CurrentYearDuration"]
            },
            "自己資本比率":
            {
                "key": ["EquityToAssetRatioSummaryOfBusinessResults"],
                "context_ref": ["CurrentYearInstant"]
            },
            "ROE(自己資本利益率)":
            {
                "key": ["RateOfReturnOnEquitySummaryOfBusinessResults"],
                "context_ref": ["CurrentYearDuration"]
            },
            "EPS(一株当たり利益)":
            {
                "key": ["BasicEarningsLossPerShareSummaryOfBusinessResults"],
                "context_ref": ["CurrentYearDuration"]
            },
            "BPS(一株当たり純資産)":
            {
                "key": ["NetAssetsPerShareSummaryOfBusinessResults"],
                "context_ref": ["CurrentYearInstant"]
            },
            "流動資産":
            {
                "key": ["CurrentAssets"],
                "context_ref": ["CurrentYearInstant"]
            },
            "固定資産":
            {
                "key": ["NoncurrentAssets"],
                "context_ref": ["CurrentYearInstant"]
            },
            "資産計":
            {
                "key": ["Assets", "TotalAssetsSummaryOfBusinessResults",
                        "TotalAssetsIFRSSummaryOfBusinessResults"
                        ],
                "context_ref": ["CurrentYearInstant"]
            },
            "流動負債":
            {
                "key": ["CurrentLiabilities"],
                "context_ref": ["CurrentYearInstant"]
            },
            "固定負債":
            {
                "key": ["NoncurrentLiabilities"],
                "context_ref": ["CurrentYearInstant"]
            },
            "負債計":
            {
                "key": ["Liabilities"], "context_ref":
                ["CurrentYearInstant"]
            },
            "純資産":
            {
                "key": ["NetAssetsSummaryOfBusinessResults"],
                "context_ref": ["CurrentYearInstant"]
            },
            "営業CF":
            {
                "key": ["NetCashProvidedByUsedInOperatingActivities",
                        "jpigp_cor:NetCashProvidedByUsedInOperatingActivitiesIFRS"],
                "context_ref": ["CurrentYearDuration",
                                "CurrentYTDDuration"]
            },
            "投資CF":
            {
                "key": ["NetCashProvidedByUsedInInvestmentActivities"],
                "context_ref": ["CurrentYearDuration"]
            },
            "財務CF":
            {
                "key": ["NetCashProvidedByUsedInFinancingActivities"],
                "context_ref": ["CurrentYearDuration"]
            }
        }
        return dict_cols
