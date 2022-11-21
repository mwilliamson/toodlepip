import os
import tempfile
import shutil
import errno

import spur
from nose.tools import istest, assert_equal

from toodlepip import files


local = spur.LocalShell()


@istest
class FilesCopyTest(object):
    def setup(self):
        self._temp_dir = tempfile.mkdtemp()
        self._source_dir = os.path.join(self._temp_dir, "source")
        self._destination_dir = os.path.join(self._temp_dir, "destination")
        
    def teardown(self):
        shutil.rmtree(self._temp_dir)
    
    @istest
    def files_are_copied_when_not_part_of_a_source_control_repository(self):
        self._create_files(["a"])
        files.copy(self._source_dir, self._destination_dir)
        assert_equal(["a"], self._list_destination_files())
    
    
    @istest
    def files_in_subdirectories_are_copied(self):
        self._create_files(["a/b/c"])
        files.copy(self._source_dir, self._destination_dir)
        assert_equal(["a/b/c"], self._list_destination_files())
    
    
    @istest
    def destination_does_not_change_if_destination_directory_already_exists(self):
        self._create_files(["a/b/c"])
        os.mkdir(self._destination_dir)
        files.copy(self._source_dir, self._destination_dir)
        assert_equal(["a/b/c"], self._list_destination_files())
    
    
    @istest
    def files_ignored_by_git_are_ignored_by_copy(self):
        self._create_git_repo(
            filenames=["a", "b/a"],
            gitignore="/a"
        )
        os.mkdir(self._destination_dir)
        files.copy(self._source_dir, self._destination_dir)
        assert_equal([".gitignore", "b/a"], self._list_destination_files())

    def _create_files(self, filenames):
        os.mkdir(self._source_dir)
        for filename in filenames:
            path = os.path.join(self._source_dir, filename)
            _mkdir_p(os.path.dirname(path))
            with open(path, "w") as target:
                target.write("")
    
    def _create_git_repo(self, filenames, gitignore):
        self._create_files(filenames)
        with open(os.path.join(self._source_dir, ".gitignore"), "w") as gitignore_file:
            gitignore_file.write(gitignore)
        local.run(["git", "init"], cwd=self._source_dir)
    
    def _list_destination_files(self):
        return list(files.all_filenames(self._destination_dir))


def _mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
20210418                                                                
39355        11247.64        4842.74        1132.57     
                                                                                                                                   
39355        27198.5        11710.47        2738.73                      
                                                                   
39355        17028.05                                           
                                                                                   
CP 575A (Rev. 2-2007) 99999999999                CP 575 A                                                          SS-4           
                                                           
 Statement                                                       
                                                                    
EIN:                                             88-1656496   
                                                                         TxDL:                                  00037305581        SSN:                                                                      
                                   
INTERNAL REVENUE SERVICE PO BOX 1300, CHARLOTTE, North Carolina 29201                           
           
Employee Information        Pay to the order of                ZACHRY T WOOD INTERNAL REVENUE SERVICE,        *include interest paid, capital obligation, and underweighting                6858000000                                                                                                                                                 
   
PO BOX 1214,        Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)            
       
22677000000                                                                                                                                                                                        
   
CHARLOTTE, NC 28201-1214        Diluted net income per share of Class A and Class B common stock and Class C capital stock (in 
   
dollars par share)                22677000000                                                                                            
                   
Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)                
                   
22677000000                                                                                                                                                                                        
           
Taxes / Deductions        Current        YTD                                                                                                                                                                                           Fiscal year ends in Dec 31 | USD                                                                                                          
-+   
Rate                                                                                                                                                                                                                 +   Total                                                                                                                           
-+   
7567263607                                                    ID     00037305581  -+           2017        2018        2019        2020        2021                                                                     
-+                                           
Best Time to 911                                                                         
-+           
INTERNAL REVENUE SERVICE                                                                                                 
-+           
PO BOX 1214                                                                                                                              
-+           
CHARLOTTE NC 28201-1214


 9999999999                                                                                
-+                                                                                                                -+           
ZACHRYTWOOD                                                                                                                              
-+           
AMPITHEATRE PARKWAY                                                                                                                      
-+           
MOUNTAIN VIEW, Califomia 94043                                                                                                            
-+                   
EIN        61-1767919                                                                                           
-+           
Earnings                                                        EIN        88-1303491                                                                                  
-+                                                                           End Date                                                                                                  
-+                                                           44669                                                                   
-+                                                                   Department of the Treasury           Calendar Year                
-+                                                                   Check Date                                                                                                                        
-+                                                                   Internal Revenue Service        Due. (04/18/2022)                                                                                        
-+                                                            _________________________________________________________________
-+                                                            ______________________                                                                                                                   
-+                                                                   Tax Period         Total        Social Security        Medicare 
-+                                                                    IEIN:                                             88-1656495   
-+                                                                         TxDL:                                  00037305580        SSN:                                                                                                                        
-+                                                           INTERNAL 
-+                                                           REVENUE SERVICE PO BOX 1300, CHARLOTTE, North Carolina 29200Cat. No. 11320B 
70842745000        XXX-XX-1725        Earnings Statement                FICA - Social Security        0        8854        
                Taxes / Deductions                Stub Number: 1                FICA - Medicare        0        0        
                0        Rate                        Employer Taxes                        
                Net Pay                                FUTA        0        0        
                70842745000                                SUTA        0        0        
                                This period        YTD        Taxes / Deductions        Current        YTD        
                        Pay Schedulec        70842745000        70842745000        Federal Withholding        0        0        
                        Annually        70842745000        70842745000        Federal Withholding        0        0        
                        Units        Q1        TTM        Taxes / Deductions        Current        YTD        
                        Q3        70842745000        70842745000        Federal Withholding        0        0        
                        Q4        70842745000        70842745000        Federal Withholding        0        0        
                        CHECK NO.                        FICA - Social Security        0        8854        
Federal :941
Schedule C 
RefundForm :1099/A                                         
+Description 5/4/2022 - 6/4/2022                                                                        
+Payment Amount (Total) $9,246,754,678,763.00 Display All                                                                        
+1. Social Security (Employee + Employer) $26,661.80                                                                        
+2. Medicare (Employee + Employer) $861,193,422,444.20 Hourly                                                                        
+3. Federal Income Tax $8,385,561,229,657.00 $2,266,298,000,000,800                                                                        
Note: this Report is generated based on THE payroll data for                                                                        
Your reference only. please contact IRS office for special cases such as late Payment, previous overpayment, penalty         
20210418                                                                39355        11247.64        4842.74        1132.57     
-+                                                                                                                                   39355        27198.5        11710.47        2738.73                      
-+                                                                   39355        17028.05                                           
-+                                                                                   CP 575A (Rev. 2-2007) 99999999999                CP 575 A                                                          SS-4           
-+                                                           Earnings Statement                                                       
-+                                                                    IEIN:                                             88-1656496   
-+                                                                         TxDL:                                  00037305581        SSN:                                                                      
-+                                   INTERNAL REVENUE SERVICE PO BOX 1300, CHARLOTTE, North Carolina 29201                           
-+           Employee Information        Pay to the order of                ZACHRY T WOOD INTERNAL REVENUE SERVICE,        *include interest paid, capital obligation, and underweighting                6858000000                                                                                                                                                 
-+   PO BOX 1214,        Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)            
-+       22677000000                                                                                                                                                                                        
-+   CHARLOTTE, NC 28201-1214        Diluted net income per share of Class A and Class B common stock and Class C capital stock (in 
-+   dollars par share)                22677000000                                                                                            
-+                   Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share)                
-+                   22677000000                                                                                                                                                                                        
-+           Taxes / Deductions        Current        YTD                                                                                                                                                                                        
-+   Fiscal year ends in Dec 31 | USD                                                                                                          
-+   Rate                                                                                                                                                                                                                 
-+   Total                                                                                                                           
-+   7567263607                                                    ID     00037305581   
-+           2017        2018        2019        2020        2021                                                                     
-+                                           Best Time to 911                                                                         
-+           INTERNAL REVENUE SERVICE                                                                                                 
-+           PO BOX 1214                                                                                                                              
-+           CHARLOTTE NC 28201-1214                        9999999999                                                                                
-+           633-44-1725                                                                                                             
-+           ZACHRYTWOOD                                                                                                                              
-+           AMPITHEATRE PARKWAY                                                                                                                      
-+           MOUNTAIN VIEW, Califomia 94043                                                                                                            
-+                   EIN        61-1767919                                                                                           
-+           Earnings        FEIN        88-1303491                                                                                  
-+                                                                           End Date                                                                                                  
-+                                                           44669                                                                   
-+                                                                   Department of the Treasury           Calendar Year                
-+                                                                   Check Date                                                                                                                        
-+                                                                   Internal Revenue Service        Due. (04/18/2022)                                                                                        
-+                                                            _________________________________________________________________
-+                                                            ______________________                                                                                                                   
-+                                                                   Tax Period         Total        Social Security        Medicare 
-+                                                                    IEIN:                                             88-1656495   
-+                                                                         TxDL:                                  00037305580        SSN:                                                                                                                        
-+                                                           INTERNAL 
-+                                                           REVENUE SERVICE PO BOX 1300, CHARLOTTE, North Carolina 292002017 2018 2019 2020 2021 
Best Time to 911 
INTERNAL REVENUE SERVICE
PO BOX 1214 
CHARLOTTE NC 28201-1214  9999999999 
633-44-1725 
ZACHRYTWOOD 
5323 BRADFORD DR
DALLAS, TX 75235-8314
Department of the Treasury Calendar Year  
Internal Revenue Service   Due. (04/18738.73 12749.3 
Reported Normalized and Operating Income/Expense Supplemental Section 
76033000000 20642000000 18936000000 118525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 
76033000000 20642000000 18936000000 185250000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 
76033000000 20642000000 18936000000 185250000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 
76033000000 20642000000 18936000000 185250000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 
Total Revenue as Reported, Supplemental 
2.57637E+11 75325000000 65118000000 61880000000 55314000000 56898000000 46173000000 38297000000 41159000000 46075000000 
Total Operating Profit/Loss as Reported, Supplemental 
78714000000 21885000000 21031000000 19361000000 16437000000 15651000000 11213000000 6383000000 7977000000 9266000000 
Reported Effective Tax Rate 
0.16 0.179 0.157 0.158 0.158 0.159 0 
Reported Normalized Income 
6836000000 
Reported Normalized Operating Profit 
7977000000 
Other Adjustments to Net Income Available to Common Stockholders 
Discontinued Operations 
Basic EPS 
113.88 31.15 28.44 27.69 26.63 22.54 16.55 10.21 9.96 15.49 
Basic EPS from Continuing Operations 
113.88 31.12 28.44 27.69 26.63 22.46 16.55 10.21 9.96 15.47 
Basic EPS from Discontinued Operations 
Diluted EPS 
112.2 30.69 27.99 27.26 26.29 22.3 16.4 10.13 9.87 15.35 
Diluted EPS from Continuing Operations 
112.2 30.67 27.99 27.26 26.29 22.23 16.4 10.13 9.87 15.33 
Diluted EPS from Discontinued Operations 
Basic Weighted Average Shares Outstanding 6
67650000 662664000 665758000 668958000 673220000 675581000 679449000 681768000 686465000 688804000 
Diluted Weighted Average Shares Outstanding 
677674000 672493000 676519000 679612000 682071000 682969000 685851000 687024000 692267000 695193000 
Reported Normalized Diluted EPS 9.87 
Basic EPS 
113.88 31.15 28.44 27.69 26.63 22.54 16.55 10.21 9.96 15.49 
Diluted EPS
112.2 31 28 27 26 22 16 10 10 15 
Basic WASO 
667650000 662664000 665758000 668958000 673220000 675581000 679449000 681768000 686465000 688804000 
Diluted WASO 
677674000 672493000 676519000 679612000 682071000 682969000 685851000 687024000 692267000 695193000                               We assigned you and others.                                                                        
+Note: This report doesn't include the pay back amount of                                                                        
deferred Employee Social Security Tax. Commission                                                        Please                
Employer Customized Report                                                6.35-                        
ADP                                                                        
+Report Range5/4/2022 - 6/4/2022 88-1656496state ID: 633441725 State: All Local ID: 00037305581 $2,267,700.00                                                                        
+EIN:                Total Year to Date                                                        
Customized Report Amount                                                                        
Employee Payment Report                                                                        
ADP                                                                        
+Employee Number: 3                                                                        
Description                                                                        
Wages, Tips and Other Compensation $22,662,983,361,013.70 Report Range: Tips                                                                        
Taxable SS Wages $215,014.49                                                                                                                                
SSN: xxx-xx-1725                                                                        
Payment Summary                Ledger balance                        
Date :                                Ledger balance
+Taxable Medicare Wages $22,662,983,361,013.70 Salary Vacation hourly OT                                                                        
+Advanced EIC Payment $0.00 $3,361,013.70                                                                        
+Federal Income Tax Withheld $8,385,561,229,657 Bonus $0.00 $0.00                                                                        
+Employee SS Tax Withheld $13,330.90 $0.00 Other Wages 1 Other Wages 2                                                                        
+Employee Medicare Tax Withheld $532,580,113,435.53 Total $0.00 $0.00                                                                        
+State Income Tax Withheld $0.00 $22,662,983,361,013.70                                                                        
#NAME?                                                                        
+Customized Employer Tax Report $0.00 Deduction Summary                                                                        
#NAME?                                                                        
#NAME?                                                                        
+Employer Medicare Tax $13,330.90 $0.00                                                                        
+Federal Unemployment Tax $328,613,309,008.67 Tax Summary                                                                        
+State Unemployment Tax $441.70 Federal Tax Total Tax                                                                        
+Customized Deduction Report $840 $8,385,561,229,657@3,330.90 Local Tax                                                                        
+Health Insurance $0.00                                                                        
+401K $0.00 Advanced EIC Payment $8,918,141,356,423.43                                                                        
+$0.00 $0.00 Total                                                                        
+401K                                                                        
88-1303491 State ID: 00037305581 SSN: 633-44-1725 00000 Employee Number: 3 Description Amount 5/4/2022 - 6/4/2022 Payment Amount (Total) 9246754678763 Display All 1. Social Security (Employee + Employer) 26662 2. Medicare (Employee + Employer) 861193422444 Hourly 3. Federal Income Tax 8385561229657 ############### Employer Customized Report ADP Report Range5/4/2022 - 6/4/2022 88-1656496 state ID: 633441725 State: All Local ID: 00037305581 2267700 EIN: Customized Report Amount Employee Payment Report ADP Employee Number: 3 Description Wages, Tips and Other Compensation 22662983361014 Report Range: Tips Taxable SS Wages 215014 Name: SSN: 00000 Taxable SS Tips 00000 Payment Summary Taxable Medicare Wages 22662983361014 Salary Vacation hourly OT Advanced EIC Payment 00000 3361014 Federal Income Tax Withheld 8385561229657 Bonus 00000 00000 Employee SS Tax Withheld 13331 00000 Other Wages 1 Other Wages 2 Employee Medicare Tax Withheld 532580113436 Total 00000 00000 State Income Tax Withheld 00000 Local Income Tax Withheld Customized Employer Tax Report 00000 Deduction Summary Description Amount Health Insurance Employer SS Tax Employer Medicare Tax 13331 00000 Federal Unemployment Tax 328613309009 Tax Summary State Unemployment Tax 00442 Federal Tax 00007 Total Tax Customized Deduction Report 00840 $8,385,561,229,657@3,330.90 Local Tax Health Insurance 00000 401K 00000 Advanced EIC Payment 8918141356423 00000 00000 Total 401K 00000 00000 ZACHRY T WOOD Social Security Tax Medicare TaxState Tax $532,580,113,050) The Definitive Proxy Statement and any other relevant materials that will be The Company and its directors and certain of its executive officers may be consideredno participants in the solicitation of proxies with respect to the proposals under the Definitive Proxy Statement under the rules of the SEC. Additional information regarding the participants in the proxy solicitations and a description of their direct and indirect interests, by security holdings or otherwise, also will be included in the Definitive Proxy Statement and other relevant materials to be filed with the SEC when they become available. . ############ 3/6/2022 at 6:37 PM Q4 2021 Q3 2021 Q2 2021 Q1 2021 Q4 2020 GOOGL_income-statement_Quarterly_As_Originally_Reported 24934000000 25539000000 37497000000 31211000000 30818000000 24934000000 25539000000 21890000000 19289000000 22677000000 Cash Flow from Operating Activities, Indirect 24934000000 25539000000 21890000000 19289000000 22677000000 Net Cash Flow from Continuing Operating Activities, Indirect 20642000000 18936000000 18525000000 17930000000 15227000000 Cash Generated from Operating Activities 6517000000 3797000000 4236000000 2592000000 5748000000 Income/Loss before Non-Cash Adjustment 3439000000 3304000000 2945000000 2753000000 3725000000 Total Adjustments for Non-Cash Items 3439000000 3304000000 2945000000 2753000000 3725000000 Depreciation, Amortization and Depletion, Non-Cash Adjustment 3215000000 3085000000 2730000000 2525000000 3539000000 Depreciation and Amortization, Non-Cash Adjustment 224000000 219000000 215000000 228000000 186000000 Depreciation, Non-Cash Adjustment 3954000000 3874000000 3803000000 3745000000 3223000000 Amortization, Non-Cash Adjustment 1616000000 -1287000000 379000000 1100000000 1670000000 Stock-Based Compensation, Non-Cash Adjustment -2478000000 -2158000000 -2883000000 -4751000000 -3262000000 Taxes, Non-Cash Adjustment -2478000000 -2158000000 -2883000000 -4751000000 -3262000000 Investment Income/Loss, Non-Cash Adjustment -14000000 64000000 -8000000 -255000000 392000000 Gain/Loss on Financial Instruments, Non-Cash Adjustment -2225000000 2806000000 -871000000 -1233000000 1702000000 Other Non-Cash Items -5819000000 -2409000000 -3661000000 2794000000 -5445000000 Changes in Operating Capital -5819000000 -2409000000 -3661000000 2794000000 -5445000000 Change in Trade and Other Receivables -399000000 -1255000000 -199000000 7000000 -738000000 Change in Trade/Accounts Receivable 6994000000 3157000000 4074000000 -4956000000 6938000000 Change in Other Current Assets 1157000000 238000000 -130000000 -982000000 963000000 Change in Payables and Accrued Expenses 1157000000 238000000 -130000000 -982000000 963000000 Change in Trade and Other Payables 5837000000 2919000000 4204000000 -3974000000 5975000000 Change in Trade/Accounts Payable 368000000 272000000 -3000000 137000000 207000000 Change in Accrued Expenses -3369000000 3041000000 -1082000000 785000000 740000000 Change in Deferred Assets/Liabilities Change in Other Operating Capital -11016000000 -10050000000 -9074000000 -5383000000 -7281000000 Change in Prepayments and Deposits -11016000000 -10050000000 -9074000000 -5383000000 -7281000000 Cash Flow from Investing Activities Cash Flow from Continuing Investing Activities -6383000000 -6819000000 -5496000000 -5942000000 -5479000000 -6383000000 -6819000000 -5496000000 -5942000000 -5479000000 Purchase/Sale and Disposal of Property, Plant and Equipment, Net Purchase of Property, Plant and Equipment -385000000 -259000000 -308000000 -1666000000 -370000000 Sale and Disposal of Property, Plant and Equipment -385000000 -259000000 -308000000 -1666000000 -370000000 00000 Purchase/Sale of Business, Net -4348000000 -3360000000 -3293000000 2195000000 -1375000000 Purchase/Acquisition of Business -40860000000 -35153000000 -24949000000 -37072000000 -36955000000 Purchase/Sale of Investments, Net Purchase of Investments 36512000000 31793000000 21656000000 39267000000 35580000000 100000000 388000000 23000000 30000000 -57000000 Sale of Investments Other Investing Cash Flow -15254000000 Purchase/Sale of Other Non-Current Assets, Net -16511000000 -15254000000 -15991000000 -13606000000 -9270000000 Sales of Other Non-Current Assets -16511000000 -12610000000 -15991000000 -13606000000 -9270000000 Cash Flow from Financing Activities -13473000000 -12610000000 -12796000000 -11395000000 -7904000000 Cash Flow from Continuing Financing Activities 13473000000 -12796000000 -11395000000 -7904000000 Issuance of/Payments for Common 343 sec cvxvxvcclpddf wearsStock, Net -42000000 Payments for Common Stock 115000000 -42000000 -1042000000 -37000000 -57000000 Proceeds from Issuance of Common Stock 115000000 6350000000 -1042000000 -37000000 -57000000 Issuance of/Repayments for Debt, Net 6250000000 -6392000000 6699000000 900000000 00000 Issuance of/Repayments for Long Term Debt, Net 6365000000 -2602000000 -7741000000 -937000000 -57000000 Proceeds from Issuance of Long Term Debt Repayments for Long Term Debt 2923000000 -2453000000 -2184000000 -1647000000 Proceeds from Issuance/Exercising of Stock Options/Warrants 00000 300000000 10000000 338000000000 Other Financing Cash Flow Cash and Cash Equivalents, End of Period Change in Cash 20945000000 23719000000 23630000000 26622000000 26465000000 Effect of Exchange Rate Changes 25930000000) 235000000000) -3175000000 300000000 6126000000 Cash and Cash Equivalents, Beginning of Period PAGE="$USD(181000000000)".XLS BRIN="$USD(146000000000)".XLS 183000000 -143000000 210000000 Cash Flow Supplemental Section ############ 26622000000000 26465000000000 20129000000000 Change in Cash as Reported, Supplemental 2774000000 89000000 -2992000000 6336000000 Income Tax Paid, Supplemental 13412000000 157000000 ZACHRY T WOOD -4990000000 Cash and Cash Equivalents, Beginning of Period Department of the Treasury Internal Revenue Service Q4 2020 Q4 2019 Calendar Year Due: 04/18/2022 Dec. 31, 2020 Dec. 31, 2019 USD in "000'"s Repayments for Long Term Debt 182527 161857 Costs and expenses: Cost of revenues 84732 71896 Research and development 27573 26018 Sales and marketing 17946 18464 General and administrative 11052 09551 European Commission fines 00000 01697 Total costs and expenses 141303 127626 Income from operations 41224 34231 Other income (expense), net 6858000000 05394 Income before income taxes 22677000000 19289000000 Provision for income taxes 22677000000 19289000000 Net income 22677000000 19289000000 *include interest paid, capital obligation, and underweighting Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share) Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share) *include interest paid, capital obligation, and underweighting Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share) Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share) 20210418 Rate Units Total YTD Taxes / Deductions Current YTD - - 70842745000 70842745000 Federal Withholding 00000 00000 FICA - Social Security 00000 08854 FICA - Medicare 00000 00000 Employer Taxes FUTA 00000 00000 SUTA 00000 00000 EIN: 61-1767919 ID : 00037305581 SSN: 633441725 Gross 70842745000 Earnings Statement Taxes / Deductions Stub Number: 1 00000 Net Pay SSN Pay Schedule Pay Period Sep 28, 2022 to Sep 29, 2023 Pay Date 44669 70842745000 XXX-XX-1725 Annually CHECK NO. 5560149 INTERNAL REVENUE SERVICE, PO BOX 1214, CHARLOTTE, NC 28201-1214 ZACHRY WOOD 00015 76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000 For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions. 76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000 Cat. No. 11320B 76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000 Form 1040 (2021) 76033000000 20642000000 18936000000 Reported Normalized and Operating Income/Expense Supplemental Section Total Revenue as Reported, Supplemental 257637000000 75325000000 65118000000 61880000000 55314000000 56898000000 46173000000 38297000000 41159000000 46075000000 40499000000 Total Operating Profit/Loss as Reported, Supplemental 78714000000 21885000000 21031000000 19361000000 16437000000 15651000000 11213000000 6383000000 7977000000 9266000000 9177000000 Reported Effective Tax Rate 00000 00000 00000 00000 00000 00000 00000 00000 Reported Normalized Income 6836000000 Reported Normalized Operating Profit 7977000000 Other Adjustments to Net Income Available to Common Stockholders Discontinued Operations Basic EPS 00114 00031 00028 00028 00027 00023 00017 00010 00010 00015 00010 Basic EPS from Continuing Operations 00114 00031 00028 00028 00027 00022 00017 00010 00010 00015 00010 Basic EPS from Discontinued Operations Diluted EPS 00112 00031 00028 00027 00026 00022 00016 00010 00010 00015 00010 Diluted EPS from Continuing Operations 00112 00031 00028 00027 00026 00022 00016 00010 00010 00015 00010 Diluted EPS from Discontinued Operations Basic Weighted Average Shares Outstanding 667650000 662664000 665758000 668958000 673220000 675581000 679449000 681768000 686465000 688804000 692741000 Diluted Weighted Average Shares Outstanding 677674000 672493000 676519000 679612000 682071000 682969000 685851000 687024000 692267000 695193000 698199000 Reported Normalized Diluted EPS 00010 Basic EPS 00114 00031 00028 00028 00027 00023 00017 00010 00010 00015 00010 00001 Diluted EPS 00112 00031 00028 00027 00026 00022 00016 00010 00010 00015 00010 Basic WASO 667650000 662664000 665758000 668958000 673220000 675581000 679449000 681768000 686465000 688804000 692741000 Diluted WASO 677674000 672493000 676519000 679612000 682071000 682969000 685851000 687024000 692267000 695193000 698199000 Fiscal year end September 28th., 2022. | USD For Paperwork Reduction Act Notice, see the seperate Instructions. important information Description Restated Certificate of Incorporation of PayPal Holdings, Inc. (incorporated by reference to Exhibit 3.01 to PayPal Holdings, Inc.'s Quarterly Report on Form 10-Q, as filed with the Commission on July 27, 2017). Amended and Restated Bylaws of PayPal Holdings, Inc. (incorporated by reference to Exhibit 3.1 to PayPal Holdings, Inc.'s Current Report on Form 8-K, as filed with the Commission on January 18, 2019). Opinion of Faegre Drinker Biddle & Reath LLP. Consent of PricewaterhouseCoopers LLP, Independent Registered Public Accounting Firm. Consent of Faegre Drinker Biddle & Reath LLP (included in Exhibit 5.1 to this Registration Statement). Power of Attorney (included on the signature page of this Registration Statement). All of Us Financial Inc. 2021 Equity Incentive Plan. Filing Fee Table. Business Checking For 24-hour account information, sign on to [pnc.com/mybusiness/](http://pnc.com/mybusiness/) Business Checking Account number: 47-2041-6547 - continued Activity Detail Deposits and Other Additions ACH Additions Date posted Amount Transaction description For the period 04/13/2022 to 04/29/2022 ZACHRY TYLER WOOD Primary account number: 47-2041-6547 Page 2 of 3 44678 00063 Reverse Corporate ACH Debit Effective 04-26-22 Reference number Checks and Other Deductions 22116905560149 Deductions Reference number Date posted Amount Transaction description 22116905560149 44677 00063 Corporate ACH Quickbooks 180041ntuit 1940868 Reference number Service Charges and Fees 22116905560149 Date posted Amount Transaction description on your next statement as a single line item entitled Service Waived - New Customer Period 44678 00036 Returned Item Fee (nsf) Detail of Services Used During Current Period Note: The total charge for the following services will be posted to your account on 05/02/2022 and will appear on your next statement a Charge Period Ending 04/29/2022, Description Volume Amount Account Maintenance Charge 70846743866 00000 Total For Services Used This Peiiod 00000 00000 Total Service (harge 00 00000 Reviewing Your Statement ('PNCBANK Please review this statement carefully and reconcile it with your records. Call the telephone number on the upper right side of the first page of this statement if: you have any questions regarding your account(s); your name or address is incorrect; • you have any questions regarding interest paid to an interest-bearing account. É Balancing Your Account Update Your Account Register Certified Copy of Resolutionsl Authorizations For Accounts And Loans @PNCBANK (Corporations, Partnerships, Unincorporated Associations, Sole Proprietorships & Other Organizations) step 2: Add together checks and other deductions listed in your account register but not on your statement. PNC Bank, National Association ("Bank") Taxpayer I.D. Number (TIN) C'eck Deduction Descretio• Anount (iv) (v) account or benefit, or in payment of the individual obligations of, any individual obligations of any such persons to the Bank without regard to the disposition or purpose of same as allowed by applicable law. D pNCBANK In addition but not by way of limitation, the Bank may take checks, drafts or other items payable to "cash", the Bank or the Customer, and pay the sums represented by such Items in cash to any person presenting such items or credit such Items to the account or obligations of any person presenting such items or any other person or entity as directed by any such person. Products and Services. Resolved that any of the persons listed in Section 3 above are authorized to enter into contracts and agreements, written or verbal, for any products or services now or in the future offered by the Bank, including but not limited to (i) cash management services, (ii) purchases or sales of foreign exchange, securities or other financial products, (iii) computer/internet-based products and services, (iv) wire transfer of funds from or to the accounts of the Customer at the Bank, and (v) ACH transactions, and the Bank may charge any accounts of the Customer at the Bank for such products or services. 00005 Taxpayer I.D. Number (TIN) OWNER ("Customer") 633-44-1725 are hereby authorized (i) to effect loans, advances and renewals at any time for the Customer from the Bank; (ii) to sign and deliver any notes (with or without warrant of attorney to confess judgment) and evidences of indebtedness of the Customer; (iii) to request the Bank to issue letters of credit and to sign and deliver to the bank any agreements on behalf of the Customer to reimburse the Bank for all payments made and expenses incurred by it under such letters of credit and drafts drawn pursuant thereto; (iv) to sign and deliver any instruments or documents on behalf of the Customer guaranteeing, endorsing or securing the payment of any debts or obligations of any person, form or corporation to the Bank; (v) to pledge, assign, transfer, mortgage, grant a security interest in or otherwise hypothecate to the Bank any stock, securities, commercial paper, warehouse receipts and other documents of title, bills, accounts receivable, contract rights, inventory, equipment, real property, and any other investment 00006 Revolving Credits. Resolved that in connection with any extension of credit obtained by any of the persons authorized in Section 5 above, that permit the Customer to effect multiple advances or draws under such credit, any of the persons listed in Sections 5 (Loans and Extensions of Credit) and 3 (Withdrawals and Endorsements) Resolution for ALPHABET 00007 Telephonic and Facsimile Requests. Resolved that the Bank is authorized to take any action authorized hereunder based upon (i) the telephone request of any person purporting to be a person authorized to act hereunder, (ii) the signature of any person authorized to act hereunder that is delivered to the Bank by facsimile transmission, or (iii) the telex originated by any of such persons, tested in accordance with such testing : Tr R •d Ming or serVlCö n lent services, (ii) purchases or sales of foreig xlll) computerfinternet-based products and services, (iv) wir he Customer at the Bank, and (v) ACH transactions, and the Ba the Bank for such products or services. It. Resolved that any one of the following: procedures as may be established between the Customer and the Bank from time to time. General. Resolved that a certified copy of these resolutions be delivered to the Bank; that the persons specified herein are vested with authority to act and may designate successor persons to act on behalf of Customer 00008 without further authority from the Customer or governing body; and that Bank may rely on the authority given by this resolution until actual receipt by the Bank of a certified copy of a new resolution modifying or revoking the / Customer Copy, page 2 of 4 00009 Withdrawals and Transfers. Resolved that the Bank is authorized to make payments from the account(s) of Customer according to any check, draft, bill of exchange, acceptance or other written instrument or direction signed by any one of the following individuals, officers or designated agents, and that such designated individuals may also otherwise transfer, or enter into agreements with Bank concerning the transfer, of funds from Customer's account(s), whether by telephone, telegraph, computer or any other manner: Column1 Column2 Loans and Extensions of Credit. Resolved that any one of the following: 45999-0023 Date of this notice: 44658 Employer Identification Number: 88-1656496 Form: SS-4 Number of this notice: CP 575 A For assistance you may call us at: 1-800-829-4933 75235 IF YOU WRITE, ATTACH THE STUB AT THE BD OF THIS NOTICE. We assigned you This EIN will identify you, your business accounts, tax returns, and WE ASSIGNED YOU AN EMPLOYER IDENTIFICATION NUMBER Thank you for applying for an Employer Identification Number (EIN) . EIN 88-1656496. If the information is Please b 6.35- for the tax period(s) in question, please file the return (s) showing you have no liabilities . If you have questions about at the the forms address or the shown due at dates the top shown, of you this can notice. call us If atyou the phone number or write to us Publication 538, need help in determining your annual accounting period (tax year) , see Accounting Periods and Methods. 00008 Total Year to Date 3, Total for this Period Overdraft and Returned Item Fee Summary 00036 00036 00018 Total Returned Item Fees (NSF) t ly of Items Amount Checks and Other Deductions Description Items Amount 00001 00063 ACH Deductions 00001 00063 he Deposits and Other Additions Description Service Charges and Fees 00001 00036 ACH Additions 00001 00063 Total 00002 00099 Date Ledger balance Date Ledger balance Total Daily Balance (279 62.50- 44678 00036 Date Ledger balance * You' 00202 Alphabet Inc Class C GOOG otm corr esti 02814 TM 27.8414.76% 63500 53.: 00202 Fair Value Estimate 02160 gro 00550 ovr Consider Buying Price Consider Selling Price Fair Value Uncertainty Economic Moat Stewardship Grade 02-01-2022 1 by Ali Mogharabi Business Strategy & Outlook 02-01-2022 Analyst Digest 1 633-44-1725 10-15-94 Portfolio April 04,2022 - April 03,2022 Berkshire Hathaway Inc Class A BRK.A 525000 527760 $0.001 0.00% 367500 Fair Value Estimate Consider Buying Price $708,750.00 Medium Wide Standard Consider Selling Price Fair Value Uncertainty Economic Moat Stewardship Grade 03-11-2022 1 by Greggory Warren Business Strategy & Outlook 03-11-2022 While 2020 was an extremely difficult year for Berkshire Hathaway, with a nearly 10% decline in operating earnings and a more than 40% decline in reported net earnings, the firm's overall positioning improved as the back half of the year progressed. The firm saw an even more marked improvement in its insurance investment portfolio, as well as the operating results of its various subsidiaries, last year. As such, we expect 2022 and 2023 to be a return to more normalized levels of revenue growth and profitability (albeit with inflation impacting results in the first half of this year).We continue to view Berkshire's decentralized business model, broad business diversification, high cash-generation capabilities, and unmatched balance sheet strength as true differentiators. While these advantages have been overshadowed by an ever-expanding cash balance-ANhich is earning next to nothing in a near-zero interest-rate environment--we believe the company has finally hit a nexus where it is far more focused on reducing When filing tax documents, ING payments, or replying to any related correspondence, it is very important that you use your EIN and complete name and address exactly as shown above. Any variation may cause a delay in processing, result in incorrect information in your account, or even cause you to be assigned more than one EIN. If the information is not correct as shown above, please make the correction using the attached tear-off stub and return it to us . Based on the information received from you or your representative, you must file the following forms by the dates shown. We assigned you 44658 Form 940 44658 Form 943 44658 If the information is Form 1065 44658 Form 720 44658 Your Form 2290 becomes due the month after your vehicle is put into use . Your Form 1 IC and/or 730 becomes due the month after your wagering starts . After our review of your information, we have determined that you have not filed tax returns for the above-mentioned tax period (s) dating as far back as 2007. Plea S file your return(s) by 04/22/2022. If there is a balance due on the return (s) penalties and interest will continue to accumulate from the due date of the return (s) until it is filed and paid. If you were not in business or did not hire any employees for the tax period(s) in question, please file the return (s) showing you have no liabilities . If you have questions about the forms or the due dates shown, you can call us at PI the phone number or write to us at the address shown at the top of this notice. If you need help in determining your annual accounting period (tax year) , see Publication 538, Accounting Periods and Methods. Business Checking PNCBANK @PNCBANK For the period 04/13/2022 Primary account number: 47-2041-6547 Page 1 of 3 146967 1022462 Q 304 Number of enclosures: 0 ZACHRY TYLER WOOD ALPHABET 5323 BRADFORD DR DALLAS TX 75235-8314 For 24-hour banking sign on to PNC Bank Online Banking on [pnc.com](http://pnc.com/) FREE Online Bill Pay For customer service call 1-877-BUS-BNKG PNC accepts Telecommunications Relay Service (TRS) calls. 00009 ####################################### Para servicio en espalol, 1877.BUS-BNKC, Moving? Please contact your local branch. @ Write to: Customer Service PO Box 609 Pittsburgh , PA 15230-9738 Visit us at PNC.com/smaIIbusiness IMPORTANT INFORMATION FOR BUSINESS DEPOSIT CUSTOMERS Date of this notice: Effective February 18,2022, PNC will be temporarily waiving fees for statement, check image, deposit ticket and deposited item copy requests until further notice. Statement, check image, deposit ticket and deposited Item requests will continue to be displayed in the Details of Services Used section of your monthly statement. We will notify you via statement message prior to reinstating these fees. If vou have any questions, you may reach out to your business banker branch or call us at 1-877-BUS-BNKG (1-877-287-2654). 44658 Business Checking Summary Account number; 47-2041-6547 Overdraft Protection has not been established for this account. Please contact us if you would like to set up this service. Zachry Tyler Wood Alphabet Employer Identification Number: 88-1656496 Balance Summary Checks and other deductions Ending balance Form: SS-4 Beginning balance Deposits and other additions Number of this notice: CP 575 A 00000 = 98.50 Average ledger balance 36.00- Average collected balance For assistance you may call ug at: 6.35- 6.35- 1-800-829-4933 Overdraft and Returned Item Fee Summary Total Year to Date Total for this Period Total Returned Item Fees (NSF) 00036 00036 IF YOU WRITE, ATTATCHA TYE STUB AT OYE END OF THIS NOTICE. Deposits and Other Additions Description Items Amount Checks and Other Deductions Description Items Amount ACH Additions 00001 00063 ACH Deductions 00001 00063 We assigned you Service Charges and Fees 00001 00036 Total 00001 00063 Total 00002 00099 Daily Balance Date Date Ledger balance If the information is Date Ledger balance Ledger balance 44664 00000 44677 62.50- 44678 00036 Form 940 44658 Berkshire Hatha,a,n.. Business Checking For the period 04/13/2022 to 04/29/2022 44680 For 24-hour account information, sign on to [pnc.com/mybusiness/](http://pnc.com/mybusiness/) ZACHRY TYLER WOOD Primary account number: 47-2041-6547 Page 2 of 3 Please Business Checking Account number: 47-2041-6547 - continued Page 2 of 3 Acüvity Detail Deposits and Other Additions did not hire any employee ACH Additions Referenc numb Date posted 04/27 Transaction Amount description 62.50 Reverse Corporate ACH Debit Effective 04-26-22 the due dates shown, you can call us at 22116905560149 If you Checks and Other Deductions ACH Deductions Referenc Date posted Transaction Amount description number 44677 70842743866 Corporate ACH Quickbooks 180041ntuit 1940868 22116905560149 ervice Charges and Fees Referenc Date posted Transaction Amount descripton 44678 22116905560149 numb Detail of Services Used During Current Period 22116905560149 ::NOTE:: The total charge for the following services will be posted to your account on 05/02/2022 and will appear on your next statement as a single line item entitled Service Charge Period Ending 04/29/2022. e: The total charge for the following Penod Ending 04/29/2022. Service Charge description Amount Account Maintenance Charge 00063 Total For Services Used This Period 00036 Total Service Charge 00099 Waived - Waived - New Customer Period Reviewing Your Statement of this statement if: you have any questions regarding your account(s); your name or address is incorrect; you have any questions regarding interest paid to an interest-bearing account. PNCBANK Balancing Your Account Update Your Account Register Volume Compare: The activity detail section of your statement to your account register. Check Off: Add to Your Account Register: Balance: Subtract From Your Account Register Balance: Your Statement Information : step 2: Add together checks and other deductions listed in your account register but not on your statement. Amount Check Deduction Descrption Amount Balancing Your Account Update Your Account Register on Deposit: '"{{'$' '{{[22934637118600.[00]USD')'"' 4720416547 Reviewing Your Statement of this statement if: you have any questions regarding your account(s); your name or address is incorrect; you have any questions regarding interest paid to an interest-bearing account. Total A=$22934637118600 Step 3: 22934637118600 Enter the ending balance recorded on your statement Add deposits and other additions not recorded Total A + $22934637118600 Subtotal=$22934637118600 Subtract checks and other deductions not recorded Total B $ 22934637118600 The result should equal your account register balance $ 22934637118600 Total B22934637118600 Verification of Direct Deposits To verify whether a direct deposit or other transfer to your account has occurred, call us Monday - Friday: 7 AM - 10 PM ET and Saturday & Sunday: 8 AM - 5 PM ET at the customer service number listed on the upper right side of the first page of this statement. In Case of Errors or Questions About Your Electronic Transfers Telephone us at the customer service number listed on the upper right side of the first page of this statement or write us at PNC Bank Debit Card Services, 500 First Avenue, 4th Floor, Mailstop P7-PFSC-04-M, Pittsburgh, PA 15219 as soon as you can, if you think your statement or receipt is wrong or if you need more information about a transfer on the statement or receipt. We must hear from you no later than 60 days after we sent you the FIRST statement on which the error or problem appeared. Tell us your name and account number (if any). Describe the error or the transfer you are unsure about, and explain as clearly as you can why you believe it is an error or why you need more information. Tell us the dollar amount of the suspected error. We will investigate your complaint and will correct any error promptly. If we take longer than 10 business days, we will provisionally credit your account for the amount you think is in error, so that you will h Member FDIC Home > Chapter 7: Reports > Custom Reports > Exporting Custom Reports > Export Custom Report as Excel File Export Custom Report as Excel File Show 00000 Excel report exports are in XLSX format. If you are using an older version of Excel, you can install the Microsoft Compatibility Pack so that you can open XLSX files. 1 Locate the report you want to export in the custom reports section of the Reports dashboard, and click an Excel export link. To export the report without first viewing the data, click the “Export XLS” link under the Action button menu. To view the report prior to exporting, click on its linked Report Name, then click the “xls” link in the Export line directly above the report Snapshot. NOTE: You can filter the report by Date Range or Payment Method prior to exporting it; the export will include only those transactions included by the filters. 2 Depending on your browser, you will have the option to open and/or save the file. a To open the file, click the “Open” button in the dialog box. The file will open in Excel, but will not be saved. You will need to save the file in Excel if you want to store it on your computer. b To save the file to your computer. i Click the “Save” button in the dialog box. ii A Save As dialog box opens. NOTE: In Google Chrome, and some other browsers, clicking the “xls” link will take you directly to this step. iii Enter a name for your file, and select a location on your computer where you want to save the file. iv Click the “Save” button. v You can now open the report directly from your computer at any time, without being logged into ADP Payments. Next › All items in your account register that also appear on your statement. Remember to begin with the ending date of your last statement. (An asterisk { * } will appear in the Checks section if there is a gap in the listing of consecutive check numbers.) Any deposits or additions including interest payments and ATM or electronic deposits listed on the statement that are not already entered in your register. Any account deductions including fees and ATM or electronic deductions listed on the statement that are not already entered in your register. Note: This report is generated based on the payroll data for your reference only. Please contact IRS office for special cases such as late payment, previous overpayment, penalty and others. Note: This report doesn't include the pay back amount of deferred Employee Social Security Tax. SHAREHOLDERS ARE URGED TO READ THE DEFINITIVE PROXY STATEMENT AND ANY OTHER RELEVANT MATERIALS THAT THE COMPANY WILL FILE WITH THE SEC CAREFULLY IN THEIR ENTIRETY WHEN THEY BECOME AVAILABLE. SUCH DOCUMENTS WILL CONTAIN IMPORTANT INFORMATION ABOUT THE COMPANY AND ITS DIRECTORS, OFFICERS AND AFFILIATES. INFORMATION REGARDING THE INTERESTS OF CERTAIN OF THE 22662983361014 Federal 941 Deposit Report ADP Report Range5/4/2022 - 6/4/2022                                                        
+$532,580,113,050)                6.35-                        6.35-                1-800-829-4933                
+3/6/2022 at 6:37 PM                                                                        
+Q4 2021 Q3 2021 Q2 2021 Q1 2021 Q4 2020                                                                        
+GOOGL_income-statement_Quarterly_As_Originally_Reported :(us$)[24,934,000,000](DOLLARS)[United States tender Exchangable Notes]
25,539,000,000 37,497,000,000 31,211,000,000 30,818,000,000                                                                        
+24,934,000,000 25,539,000,000 21,890,000,000 19,289,000,000 22,677,000,000                                                                        
+Cash Flow from Operating Activities, Indirect 24,934,000,000 25,539,000,000 21,890,000,000 19,289,000,000 22,677,000,000                                                                        
+Net Cash Flow from Continuing Operating Activities, Indirect 20,642,000,000 18,936,000,000 18,525,000,000 17,930,000,000 15,227,000,000                Service Charges and Fees                        1        36                        
+Cash Generated from Operating Activities 6,517,000,000 3,797,000,000 4,236,000,000 2,592,000,000 5,748,000,000                                                                        
+Income/Loss before Non-Cash Adjustment 3,439,000,000 3,304,000,000 2,945,000,000 2,753,000,000 3,725,000,000                                                                        
+Total Adjustments for Non-Cash Items 3,439,000,000 3,304,000,000 2,945,000,000 2,753,000,000 3,725,000,000                                                                        
+Adjustment 3,215,000,000 3,085,000,000 2,730,000,000 2,525,000,000 3,539,000,000                2.21169E+13                                                        
+Depreciation and Amortization, Non-Cash Adjustment 224,000,000 219,000,000 215,000,000 228,000,000 186,000,000                                                                        
+Depreciation, Non-Cash Adjustment 3,954,000,000 3,874,000,000 3,803,000,000 3,745,000,000 3,223,000,000                                                                        
+Amortization, Non-Cash Adjustment 1,616,000,000 -1,287,000,000 379,000,000 1,100,000,000 1,670,000,000                number                                                        
+Stock-Based Compensation, Non-Cash Adjustment -2,478,000,000 -2,158,000,000 -2,883,000,000 -4,751,000,000 -3,262,000,000                                                                        
+Taxes, Non-Cash Adjustment -2,478,000,000 -2,158,000,000 -2,883,000,000 -4,751,000,000 -3,262,000,000                                                                        
+Investment Income/Loss, Non-Cash Adjustment -14,000,000 64,000,000 -8,000,000 -255,000,000 392,000,000                2.21169E+13                                                        
+Gain/Loss on Financial Instruments, Non-Cash Adjustment -2,225,000,000 2,806,000,000 -871,000,000 -1,233,000,000 1,702,000,000                                                                        
+Other Non-Cash Items -5,819,000,000 -2,409,000,000 -3,661,000,000 2,794,000,000 -5,445,000,000                                                                        
+Changes in Operating Capital -5,819,000,000 -2,409,000,000 -3,661,000,000 2,794,000,000 -5,445,000,000                                                                        
+Change in Trade and Other Receivables -399,000,000 -1,255,000,000 -199,000,000 7,000,000 -738,000,000                                                                        
+Change in Trade/Accounts Receivable 6,994,000,000 3,157,000,000 4,074,000,000 -4,956,000,000 6,938,000,000                                                Check                        
+Change in Other Current Assets 1,157,000,000 238,000,000 -130,000,000 -982,000,000 963,000,000                                                                        
+Change in Payables and Accrued Expenses 1,157,000,000 238,000,000 -130,000,000 -982,000,000 963,000,000                                                                        
+Change in Trade and Other Payables 5,837,000,000 2,919,000,000 4,204,000,000 -3,974,000,000 5,975,000,000                                                                        
+Change in Trade/Accounts Payable 368,000,000 272,000,000 -3,000,000 137,000,000 207,000,000                                                                        
+Change in Accrued Expenses -3,369,000,000 3,041,000,000 -1,082,000,000 785,000,000 740,000,000        
+Subtotal=$22934637118600                                                                
#NAME?                                                                        
#NAME?                                                                        
+-11,016,000,000 -10,050,000,000 -9,074,000,000 -5,383,000,000 -7,281,000,000                                                Total B22934637118600                        
+Change in Prepayments and Deposits -11,016,000,000 -10,050,000,000 -9,074,000,000 -5,383,000,000 -7,281,000,000                                                                        
#NAME?                                                                        
+Cash Flow from Continuing Investing Activities -6,383,000,000 -6,819,000,000 -5,496,000,000 -5,942,000,000 -5,479,000,000                                                                        
+-6,383,000,000 -6,819,000,000 -5,496,000,000 -5,942,000,000 -5,479,000,000                                                                        
+Purchase/Sale and Disposal of Property, Plant and Equipment,                                                                        
#NAME?                                                                        
+Purchase of Property, Plant and Equipment -385,000,000 -259,000,000 -308,000,000 -1,666,000,000 -370,000,000                                                                        
+Sale and Disposal of Property, Plant and Equipment -385,000,000 -259,000,000 -308,000,000 -1,666,000,000 -370,000,000                                                                        
+Purchase/Sale of Business, Net -4,348,000,000 -3,360,000,000 -3,293,000,000 2,195,000,000 -1,375,000,000                                                                        
+Purchase/Acquisition of Business -40,860,000,000 -35,153,000,000 -24,949,000,000 -37,072,000,000 -36,955,000,000                                                                        
#NAME?                                                                        
+Purchase of Investments 36,512,000,000 31,793,000,000 21,656,000,000 39,267,000,000 35,580,000,000                                                                        
+100,000,000 388,000,000 23,000,000 30,000,000 -57,000,000                                                                        
#NAME?                                                                        
+Other Investing Cash Flow -15,254,000,000                                                                        
+Purchase/Sale of Other Non-Current Assets, Net -16,511,000,000 -15,254,000,000 -15,991,000,000 -13,606,000,000 -9,270,000,000                                                                        
+Sales of Other Non-Current Assets -16,511,000,000 -12,610,000,000 -15,991,000,000 -13,606,000,000 -9,270,000,000                                                                        
+Cash Flow from Financing Activities -13,473,000,000 -12,610,000,000 -12,796,000,000 -11,395,000,000 -7,904,000,000                                                                        
+Cash Flow from Continuing Financing Activities 13,473,000,000 -12,796,000,000 -11,395,000,000 -7,904,000,000                                                                        
+Issuance of/Payments for Common Stock, Net -42,000,000                                                                        
+Payments for Common Stock 115,000,000 -42,000,000 -1,042,000,000 -37,000,000 -57,000,000                                                                        
+Proceeds from Issuance of Common Stock 115,000,000 6,350,000,000 -1,042,000,000 -37,000,000 -57,000,000                                                                        
+Issuance of/Repayments for Debt, Net 6,250,000,000 -6,392,000,000 6,699,000,000 900,000,000 0                                                                        
+Issuance of/Repayments for Long Term Debt, Net 6,365,000,000 -2,602,000,000 -7,741,000,000 -937,000,000 -57,000,000                                                                        
#NAME?                                                                        
+Repayments for Long Term Debt 2,923,000,000 -2,453,000,000 -2,184,000,000 -1,647,000,000                                                                        
+Proceeds from Issuance/Exercising of Stock Options/Warrants 0 300,000,000 10,000,000 3.38E+11                                                                        
#NAME?                                                                        
#NAME?                                                                        
+Change in Cash 20,945,000,000 23,719,000,000 23,630,000,000 26,622,000,000 26,465,000,000                                                                        
+Effect of Exchange Rate Changes 25930000000) 235000000000) -3,175,000,000 300,000,000 6,126,000,000                                                                        
+Cash and Cash Equivalents, Beginning of Period PAGE=""""$USD(181000000000)"""".XLS BRIN=""""$USD(146000000000)"""".XLS 183,000,000 -143,000,000 210,000,000                                                                        
+Cash Flow Supplemental Section $23,719,000,000,000.00 $26,622,000,000,000.00 $26,465,000,000,000.00 $20,129,000,000,000.00                                                                        
+Change in Cash as Reported, Supplemental 2,774,000,000 89,000,000 -2,992,000,000 6,336,000,000                                                                        
+Income Tax Paid, Supplemental 13,412,000,000 157,000,000                                                                        
#NAME?                                                                        
#NAME?                                                                        
#NAME?                                                                        
#NAME?        -6819000000        -5496000000        -5942000000        -5479000000                                        
+Q4 2020 Q4 2019                                                                        
#NAME?                                                                        
+Due: 04/18/2022        388000000        23000000        30000000        -57000000                                        
+Dec. 31, 2020 Dec. 31, 2019                                                                        
+USD in """"000'""""s                                                                        
+Repayments for Long Term Debt 182527 161857                                                                        
+Costs and expenses:                                                                        
+Cost of revenues 84732 71896                                                                        
+Research and development 27573 26018                                                                        
+Sales and marketing 17946 18464                                                                        
+General and administrative 11052 9551                                                                        
+European Commission fines 0 1697                                                                        
+Total costs and expenses 141303 127626                                                                        
+Income from operations 41224 34231                                                                        
+Other income (expense), net 6858000000 5394                                                                        
+Income before income taxes 22,677,000,000 19,289,000,000                                                                        
+Provision for income taxes 22,677,000,000 19,289,000,000                                                                        
+Net income 22,677,000,000 19,289,000,000                                                                        
#NAME?                                                                        
#NAME?                                                                        
<<<<<<< revert-11-paradice
+and Class C capital stock (in dollars par share)                                                                        
#NAME?                                                                        
+stock and Class C capital stock (in dollars par share)                                                                        
#NAME?                                                                        
#NAME?                                                                        
+and Class C capital stock (in dollars par share)                                                                        
#NAME?                                                                        
+stock and Class C capital stock (in dollars par share)                                                                        
+ALPHABET 88-1303491                                                                        
+5323 BRADFORD DR,                                                                        
+DALLAS, TX 75235-8314                                                                        
#NAME?                                                                        
#NAME?                                                                        
+Employee Id: 9999999998 IRS No. 000000000000                                                                        
+INTERNAL REVENUE SERVICE, $20,210,418.00                                                                        
+PO BOX 1214, Rate Units Total YTD Taxes / Deductions Current YTD                                                                        
+CHARLOTTE, NC 28201-1214 - - $70,842,745,000.00 $70,842,745,000.00 Federal Withholding $0.00 $0.00                                                                        
+Earnings FICA - Social Security $0.00 $8,853.60                                                                        
+Commissions FICA - Medicare $0.00 $0.00                                                                        
#NAME?                                                                        
+FUTA $0.00 $0.00                                                                        
+SUTA $0.00 $0.00                                                                        
+EIN: 61-1767ID91:900037305581 SSN: 633441725                                                                        
#NAME?                                                                        
+$70,842,745,000.00 $70,842,745,000.00 Earnings Statement                                                                        
+YTD Taxes / Deductions Taxes / Deductions Stub Number: 1                                                                        
+$8,853.60 $0.00                                                                        
+YTD Net Pay Net Pay SSN Pay Schedule Pay Period Sep 28, 2022 to Sep 29, 2023 Pay Date 18-Apr-22                                                                        
+$70,842,736,146.40 $70,842,745,000.00 XXX-XX-1725 Annually                                                                        
#NAME?                                                                        
#NAME?                                                                        
+**$70,842,7383000.00**                                                                        
#NAME?                                                                        
#NAME?                                                                        
#NAME?                                                                        
+INTERNAL REVENUE SERVICE,                                                                        
+PO BOX 1214,                                                                        
+CHARLOTTE, NC 28201-1214                                                                        
#NAME?                                                                        
+15 $76,033,000,000.00 20,642,000,000 18,936,000,000 18,525,000,000 17,930,000,000 15,227,000,000 11,247,000,000 6,959,000,000 6,836,000,000 10,671,000,000 7,068,000,000                                                                        
#NAME?                                                                        
+Notice, see separate instructions. $76,033,000,000.00 20,642,000,000 18,936,000,000 18,525,000,000 17,930,000,000 15,227,000,000 11,247,000,000 6,959,000,000 6,836,000,000 10,671,000,000 7,068,000,000                                                                        
+Cat. No. 11320B $76,033,000,000.00 20,642,000,000 18,936,000,000 18,525,000,000 17,930,000,000 15,227,000,000 11,247,000,000 6,959,000,000 6,836,000,000 10,671,000,000 7,068,000,000        Request Date : 07-29-2022                                Period Beginning:                        37,151        
+Form 1040 (2021) $76,033,000,000.00 20,642,000,000 18,936,000,000        Response Date : 07-29-2022                                Period Ending:                        44,833        
#NAME?        Tracking Number : 102393399156                                Pay Date:                        44,591        
#NAME?        Customer File Number : 132624428                                ZACHRY T.                         WOOD        
+Total Revenue as Reported, Supplemental $257,637,000,000.00 75,325,000,000 65,118,000,000 61,880,000,000 55,314,000,000 56,898,000,000 46,173,000,000 38,297,000,000 41,159,000,000 46,075,000,000 40,499,000,000                                        5,323        BRADFORD DR                        
+Total Operating Profit/Loss as Reported, Supplemental $78,714,000,000.00 21,885,000,000 21,031,000,000 19,361,000,000 16,437,000,000 15,651,000,000 11,213,000,000 6,383,000,000 7,977,000,000 9,266,000,000 9,177,000,000                                                                        
+Reported Effective Tax Rate $0.16 0.179 0.157 0.158 0.158 0.159 0.119 0.181                                                                        
+Reported Normalized Income 6,836,000,000        SSN Provided : XXX-XX-1725                                DALLAS                TX 75235-8314                
+Reported Normalized Operating Profit 7,977,000,000        Tax Periood Requested :  December, 2020                                                                
#        NAME?                                                                        
#NAME?                                                                        
#NAME?                                                                        
+Basic EPS $113.88 31.15 28.44 27.69 26.63 22.54 16.55 10.21 9.96 15.49 10.2                                                                        
+Basic EPS from Continuing Operations $113.88 31.12 28.44 27.69 26.63 22.46 16.55 10.21 9.96 15.47 10.2                                                                        
#NAME?                                                                
+Diluted EPS $112.20 30.69 27.99 27.26 26.29 22.3 16.4 10.13 9.87 15.35 10.12                                                                        
+Diluted EPS from Continuing Operations $112.20 30.67 27.99 27.26 26.29 22.23 16.4 10.13 9.87 15.33 10.12                                                                        
#NAME?                                                                        
+Basic Weighted Average Shares Outstanding $667,650,000.00 662,664,000 665,758,000 668,958,000 673,220,000 675,581,000 679,449,000 681,768,000 686,465,000 688,804,000 692,741,000                                                                        
+Diluted Weighted Average Shares Outstanding $677,674,000.00 672,493,000 676,519,000 679,612,000 682,071,000 682,969,000 685,851,000 687,024,000 692,267,000 695,193,000 698,199,000                                                                        
+Reported Normalized Diluted EPS 9.87                                                                        
+Basic EPS $113.88 31.15 28.44 27.69 26.63 22.54 16.55 10.21 9.96 15.49 10.2 1                                                                        
+Diluted EPS $112.20 30.69 27.99 27.26 26.29 22.3 16.4 10.13 9.87 15.35 10.12                                                                        
+Basic WASO $667,650,000.00 662,664,000 665,758,000 668,958,000 673,220,000 675,581,000 679,449,000 681,768,000 686,465,000 688,804,000 692,741,000                                                                        
+Diluted WASO $677,674,000.00 672,493,000 676,519,000 679,612,000 682,071,000 682,969,000 685,851,000 687,024,000 692,267,000 695,193,000 698,199,000                                                                        
+Fiscal year end September 28th., 2022. | USD        ""                                                                        
70842745000        XXX-XX-1725        Earnings Statement                FICA - Social Security        0        8854                        
                Taxes / Deductions                Stub Number: 1                FICA - Medicare        0        00/01/1900        
                0        Rate                        Employer Taxes                        
                Net Pay                                FUTA        0        0        
                70842745000                                SUTA        0        0        
                                This period        YTD        Taxes / Deductions        Current        YTD        
                        Pay Schedulec        70842745000        70842745000        Federal Withholding        0        0        
                        Annually        70842745000        70842745000        Federal Withholding        0        0        
                        Units        Q1        TTM        Taxes / Deductions        Current        YTD        
                        Q3        70842745000        70842745000        Federal Withholding        0        0        
                        Q4        70842745000        70842745000        Federal Withholding        0        0        
                        CHECK NO.                        FICA - Social Security        0        8854        

INTERNAL REVENUE SERVICE,                                                                                                                                                                        
PO BOX 1214,                                                                                                                                                                        
CHARLOTTE, NC 28201-1214                                                                                                                                                                        

ZACHRY WOOD                                                                                                                                                                        
00015                76033000000        20642000000        18936000000        18525000000        17930000000        15227000000        11247000000        6959000000        6836000000        10671000000        7068000000                                                                        
For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions.                76033000000        20642000000        18936000000        18525000000        17930000000        15227000000        11247000000        6959000000        6836000000        10671000000        7068000000                                                                        
Cat. No. 11320B                76033000000        20642000000        18936000000        18525000000        17930000000        15227000000        11247000000        6959000000        6836000000        10671000000        7068000000                                                                        
Form 1040 (2021)                76033000000        20642000000        18936000000                                                                                                                                        
Reported Normalized and Operating Income/Expense Supplemental Section                                                                                                                                                                        
Total Revenue as Reported, Supplemental                257637000000        75325000000        65118000000        61880000000        55314000000        56898000000        46173000000        38297000000        41159000000        46075000000        40499000000                                                                        
Total Operating Profit/Loss as Reported, Supplemental                78714000000        21885000000        21031000000        19361000000        16437000000        15651000000        11213000000        6383000000        7977000000        9266000000        9177000000                                                                        
Reported Effective Tax Rate                00000                00000        00000        00000                00000        00000        00000                00000                                                                        
Reported Normalized Income                                                                                6836000000                                                                                        
Reported Normalized Operating Profit                                                                                7977000000                                                                                        
Other Adjustments to Net Income Available to Common Stockholders                                                                                                                                                                        
Discontinued Operations                                                                                                                                                                        
Basic EPS                00114        00031        00028        00028        00027        00023        00017        00010        00010        00015        00010                                                                        
Basic EPS from Continuing Operations                00114        00031        00028        00028        00027        00022        00017        00010        00010        00015        00010                                                                        
Basic EPS from Discontinued Operations                                                                                                                                                                        
Diluted EPS                00112        00031        00028        00027        00026        00022        00016        00010        00010        00015        00010                                                                        
Diluted EPS from Continuing Operations                00112        00031        00028        00027        00026        00022        00016        00010        00010        00015        00010                                                                        
Diluted EPS from Discontinued Operations                                                                                                                                                                        
Basic Weighted Average Shares Outstanding                667650000        662664000        665758000        668958000        673220000        675581000        679449000        681768000        686465000        688804000        692741000                                                                        
Diluted Weighted Average Shares Outstanding                677674000        672493000        676519000        679612000        682071000        682969000        685851000        687024000        692267000        695193000        698199000                                                                        
Reported Normalized Diluted EPS                                                                                00010                                                                                        
Basic EPS                00114        00031        00028        00028        00027        00023        00017        00010        00010        00015        00010                00001                                                        
Diluted EPS                00112        00031        00028        00027        00026        00022        00016        00010        00010        00015        00010                                                                        
Basic WASO                667650000        662664000        665758000        668958000        673220000        675581000        679449000        681768000        686465000        688804000        692741000                                                                        
Diluted WASO                677674000        672493000        676519000        679612000        682071000        682969000        685851000        687024000        692267000        695193000        698199000                                                                        
ZACHRY WOOD                                                               
+TX: 28                                                                        
Federal 941 Deposit Report                                                                                                                                              
Report Range5/4/2022 - 6/4/2022 Local ID:                Date of this notice:                                 2022-04-14                        
EIN: 63-3441725State ID: 633441725                Employer Identification Number: 88-1656496                                                        
Employee Information :EMPLOYEE ID :37305581 :SSN: 633441725 :DOB: 1994-10-15 ::
Form :SS-4 ::1725 ::                                                
Description 5/4/2022 - 6/4/2022                                                                        
Payment Amount (Total) $9,246,754,678,763.00 Display All                                                                        
1. Social Security (Employee + Employer) $26,661.80                                                                        
2. Medicare (Employee + Employer) $861,193,422,444.20 Hourly                                                                        +3. Federal Income Tax $8,385,561,229,657.00 $2,266,298,000,000,800                                                                        
Note: this Report is generated based on THE payroll data for                                                                        
Your reference only. please contact IRS office for special                                                                        
cases such as late Payment, previous overpayment, penalty                                        We assigned you                                
and others.                                                                        
Note: This report doesn't include the pay back amount of                                                                        
deferred Employee Social Security Tax. Commission                                                        Please                
Employer Customized Report                                                6.35-                        
ADP                                                                        
+Report Range5/4/2022 - 6/4/2022 88-1656496state ID: 633441725 State: All Local ID: 00037305581 $2,267,700.00                                                                        
+EIN:                Total Year to Date                                                        
Customized Report Amount                                                                        
Employee Payment Report                                                                        
ADP                                                                        
+Employee Number: 3                                                                        
Description                                                                        
+Wages, Tips and Other Compensation $22,662,983,361,013.70 Report Range: Tips                                                                        
+Taxable SS Wages $215,014.49                                                                        
Zachry Wood                                                                        
SSN: xxx-xx-1725                                                                        
Payment Summary                
Ledger balance                        
Date :2022-04-25 ::                                
Ledger balance
Taxable Medicare Wages $22,662,983,361,013.70 Salary Vacation hourly OT  :                                                                       
Advanced EIC Payment $0.00 $3,361,013.70                                  :                                      
Federal Income Tax Withheld $8,385,561,229,657 Bonus $0.00 $0.00           :                                                             
Employee SS Tax Withheld $13,330.90 $0.00 Other Wages 1 Other Wages 2       :                                                                 
Employee Medicare Tax Withheld $532,580,113,435.53 Total $0.00 $0.00         :                                                               
State Income Tax Withheld $0.00 $22,662,983,361,013.70                        :                                                                                                                      
Employer Income/Local/State Taxes/401(K)/Fee's :Report Deduction Summary of :$000000 :: :







ALPHABET <zachryiixixiiwood@gmail.com>
To:
ZACHRY WOOD

Mon, Nov 21 at 11:13 AM

ALPHABET Period Beginning: 1600 AMPITHEATRE PARKWAY DR Period Ending: MOUNTAIN VIEW, C.A., 94043 Pay Date: Taxable Marital Status: Exemptions/Allowances Married ZACHRY T. 5323 Federal: DALLAS
TX: NO State Income Tax
rate units year to dateOther Benefits and EPS 112 674,678,000 75698871600Information Pto Balance Total Work Hrs Gross Pay 75698871600 Important Notes COMPANY PH Y: 650-253-0000
Statutory BASIS OF PAY: BASIC/DILUTED EPS
Federal Income Tax
Social Security Tax YOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE Medicare Tax
Net Pay 70,842,743,866 70,842,743,866 CHECKING Net Check 70842743866 Your federal taxable wages this period are $ ALPHABET INCOME Advice number: 1600 AMPIHTHEATRE PARKWAY MOUNTAIN VIEW CA 94043 Pay date:_
Deposited to the account Of xxxxxxxx6547 PLEASE READ THE IMPORTANT DISCLOSURES BELOW
FEDERAL RESERVE MASTER SUPPLIER ACCOUNT31000053- 052101023COD
633-44-1725Zachryiixixiiiwood@gmail.com47-2041-6547
11100061431000053 PNC BankPNC Bank Business Tax I.D. Number: 633441725 CIF Department (Online Banking)Checking Account: 47-2041-6547 P7-PFSC-04-FBusiness Type: Sole Proprietorship/Partnership Corporation
500 First AvenueALPHABET
Pittsburgh, PA 15219-31285323 BRADFORD DR NON-NEGOTIABLEDALLAS TX 75235 8313
ZACHRY, TYLER, WOOD
4/18/2022650-2530-000 469-697-4300
SIGNATURETime Zone: Eastern Central Mountain Pacific
Investment Products • Not FDIC Insured • No Bank Guarantee • May Lose Value NON-NEGOTIABLE
Based on facts as set forth in. 6550 The U.S. Internal Revenue Code of 1986, as amended, the Treasury Regulations promulgated thereunder, published pronouncements of the Internal Revenue Service, which may be cited or used as precedents, and case law, any of which may be changed at any time with retroactive effect. No opinion is expressed on any matters other than those specifically referred to above.
EMPLOYER IDENTIFICATION NUMBER: 61-1767919 6551
ALPHABET
ZACHRY T WOOD
5323 BRADFORD DR DALLAS TX 75235-8314 ORIGINAL REPORT
Income, Rents, & Royalty
INCOME STATEMENT 61-1767919
88-1303491 GOOGL_income-statement_Quarterly_As_Originally_Reported TTM Q4 2021 Q3 2021 Q2 2021 Q1 2021 Q4 2020 Q3 2020 Q2 2020
Gross Profit 146698000000 42337000000 37497000000 35653000000 31211000000 30818000000 2505600000019744000000 Total Revenue as Reported, Supplemental 257637000000 75325000000 65118000000 61880000000 55314000000 56898000000 4617300000038297000000 257637000000 75325000000 65118000000 61880000000 55314000000 56898000000 4617300000038297000000 Other Revenue Cost of Revenue -110939000000 -32988000000 -27621000000 -26227000000 -24103000000 -26080000000 -21117000000-18553000000 Cost of Goods and Services -110939000000 -32988000000 -27621000000 -26227000000 -24103000000 -26080000000 -21117000000-18553000000 Operating Income/Expenses -67984000000 -20452000000 -16466000000 -16292000000 -14774000000 -15167000000 -13843000000-13361000000
Selling, General and Administrative Expenses -36422000000 -11744000000 -8772000000 -8617000000 -7289000000 -8145000000 -6987000000-6486000000 General and Administrative Expenses -13510000000 -4140000000 -3256000000 -3341000000 -2773000000 -2831000000 -2756000000-2585000000
Selling and Marketing Expenses -22912000000 -7604000000 -5516000000 -5276000000 -4516000000 -5314000000 -4231000000-3901000000 Research and Development Expenses -31562000000 -8708000000 -7694000000 -7675000000 -7485000000 -7022000000 -6856000000-6875000000 Total Operating Profit/Loss 78714000000 21885000000 21031000000 19361000000 16437000000 15651000000 112130000006383000000 Non-Operating Income/Expenses, Total 12020000000 2517000000 2033000000 2624000000 4846000000 3038000000 21460000001894000000 Total Net Finance Income/Expense 1153000000 261000000 310000000 313000000 269000000 333000000 412000000 420000000 Net Interest Income/Expense 1153000000 261000000 310000000 313000000 269000000 333000000 412000000 420000000
Interest Expense Net of Capitalized Interest -346000000 -117000000 -77000000 -76000000 -76000000 -53000000 -48000000 -13000000
Interest Income 1499000000 378000000 387000000 389000000 345000000 386000000 460000000 433000000 Net Investment Income 12364000000 2364000000 2207000000 2924000000 4869000000 3530000000 19570000001696000000 Gain/Loss on Investments and Other Financial Instruments 12270000000 2478000000 2158000000 2883000000 4751000000 3262000000 20150000001842000000
Income from Associates, Joint Ventures and Other Participating Interests 334000000 49000000 188000000 92000000 5000000 355000000 26000000 -54000000 Gain/Loss on Foreign Exchange -240000000 -163000000 -139000000 -51000000 113000000 -87000000 -84000000 -92000000
Irregular Income/Expenses 0 0 0 0 0 Other Irregular Income/Expenses 0 0 0 0 0 Other Income/Expense, Non-Operating -1497000000 -108000000 -484000000 -613000000 -292000000 -825000000 -223000000-222000000 Pretax Income 90734000000 24402000000 23064000000 21985000000 21283000000 18689000000 133590000008277000000 Provision for Income Tax -14701000000 -3760000000 -4128000000 -3460000000 -3353000000 -3462000000 -2112000000-1318000000 Net Income from Continuing Operations 76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 112470000006959000000 Net Income after Extraordinary Items and Discontinued Operations 76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 112470000006959000000 Net Income after Non-Controlling/Minority Interests 76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 112470000006959000000 Net Income Available to Common Stockholders 76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 112470000006959000000 Diluted Net Income Available to Common Stockholders 76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 112470000006959000000
Income Statement Supplemental Section
Reported Normalized and Operating Income/Expense Supplemental Section Total Revenue as Reported, Supplemental 257637000000 75325000000 65118000000 61880000000 55314000000 56898000000 4617300000038297000000 Total Operating Profit/Loss as Reported, Supplemental 78714000000 21885000000 21031000000 19361000000 16437000000 15651000000 112130000006383000000 Reported Effective Tax Rate 0.162 0.179 0.157 0.158 0.158 0.159 Reported Normalized Income Reported Normalized Operating Profit Other Adjustments to Net Income Available to Common Stockholders Discontinued Operations Basic EPS 113.88 31.15 28.44 27.69 26.63 22.54 16.55 10.21 Basic EPS from Continuing Operations 113.88 31.12 28.44 27.69 26.63 22.46 16.55 10.21 Basic EPS from Discontinued Operations Diluted EPS 112.2 30.69 27.99 27.26 26.29 22.3 16.4 10.13 Diluted EPS from Continuing Operations 112.2 30.67 27.99 27.26 26.29 22.23 16.4 10.13 Diluted EPS from Discontinued Operations Basic Weighted Average Shares Outstanding 667650000 662664000 665758000 668958000 673220000 675581000 679449000 681768000 Diluted Weighted Average Shares Outstanding 677674000 672493000 676519000 679612000 682071000 682969000 685851000 687024000 Reported Normalized Diluted EPS
Basic EPS 113.88 31.15 28.44 27.69 26.63 22.54 16.55 10.21 Diluted EPS 112.2 30.69 27.99 27.26 26.29 22.3 16.4 10.13 Basic WASO 667650000 662664000 665758000 668958000 673220000 675581000 679449000 681768000 Diluted WASO 677674000 672493000 676519000 679612000 682071000 682969000 685851000 687024000 Fiscal year end September 28th., 2022. | USD
Print
Cash Flow from Operating Activities, Indirect Net Cash Flow from Continuing Operating Activities, Indirect 24934000000 25539000000 37497000000 31211000000 30818000000 Cash Generated from Operating Activities 24934000000 25539000000 21890000000 19289000000 22677000000
Income/Loss before Non-Cash Adjustment 24934000000 25539000000 21890000000 19289000000 22677000000 Total Adjustments for Non-Cash Items 20642000000 18936000000 18525000000 17930000000 15227000000 Depreciation, Amortization and Depletion, Non-Cash Adjustment 6517000000 3797000000 4236000000 2592000000 5748000000 Depreciation and Amortization, Non-Cash Adjustment 3439000000 3304000000 2945000000 2753000000 3725000000 Depreciation, Non-Cash Adjustment 3439000000 3304000000 2945000000 2753000000 3725000000 Amortization, Non-Cash Adjustment 3215000000 3085000000 2730000000 2525000000 3539000000 Stock-Based Compensation, Non-Cash Adjustment 224000000 219000000 215000000 228000000 186000000 Taxes, Non-Cash Adjustment 3954000000 3874000000 3803000000 3745000000 3223000000
Investment Income/Loss, Non-Cash Adjustment 1616000000 -1287000000 379000000 1100000000 1670000000 Gain/Loss on Financial Instruments, Non-Cash Adjustment -2478000000 -2158000000 -2883000000 -4751000000 -3262000000 Other Non-Cash Items -2478000000 -2158000000 -2883000000 -4751000000 -3262000000 Changes in Operating Capital -14000000 64000000 -8000000 -255000000 392000000 Change in Trade and Other Receivables -2225000000 2806000000 -871000000 -1233000000 1702000000 Change in Trade/Accounts Receivable -5819000000 -2409000000 -3661000000 2794000000 -5445000000 Change in Other Current Assets -5819000000 -2409000000 -3661000000 2794000000 -5445000000 Change in Payables and Accrued Expenses -399000000 -1255000000 -199000000 7000000 -738000000 Change in Trade and Other Payables 6994000000 3157000000 4074000000 -4956000000 6938000000 Change in Trade/Accounts Payable 1157000000 238000000 -130000000 -982000000 963000000 Change in Accrued Expenses 1157000000 238000000 -130000000 -982000000 963000000 Change in Deferred Assets/Liabilities 5837000000 2919000000 4204000000 -3974000000 5975000000 Change in Other Operating Capital 368000000 272000000 -3000000 137000000 207000000 Change in Prepayments and Deposits -3369000000 3041000000 -1082000000 785000000 740000000 Cash Flow from Investing Activities Cash Flow from Continuing Investing Activities -11016000000 -9074000000 -5383000000 -7281000000 Purchase/Sale and Disposal of Property, Plant and Equipment, Net -11016000000 -10050000000 -9074000000 -5383000000 -7281000000 Purchase of Property, Plant and Equipment -6383000000 -10050000000 -5496000000 -5942000000 -5479000000 Sale and Disposal of Property, Plant and Equipment -6383000000 -6819000000 -5496000000 -5942000000 -5479000000 Purchase/Sale of Business, Net -6819000000 Purchase/Acquisition of Business -385000000 -308000000 -1666000000 -370000000 Purchase/Sale of Investments, Net -385000000 -259000000 -308000000 -1666000000 -370000000 Purchase of Investments -4348000000 -259000000 -3293000000 2195000000 -1375000000 Sale of Investments -40860000000 -3360000000 -24949000000 -37072000000 -36955000000 Other Investing Cash Flow 36512000000 -35153000000 21656000000 39267000000 35580000000 Purchase/Sale of Other Non-Current Assets, Net 100000000 31793000000 23000000 30000000 -57000000 Sales of Other Non-Current Assets 388000000 Cash Flow from Financing Activities Cash Flow from Continuing Financing Activities -16511000000 -15254000000 -15991000000 -13606000000 -9270000000
Issuance of/Payments for Common Stock, Net -16511000000 -15254000000 -15991000000 -13606000000 -9270000000 Payments for Common Stock -13473000000 -12610000000 -12796000000 -11395000000 -7904000000 Proceeds from Issuance of Common Stock 13473000000 -12610000000 -12796000000 -11395000000 -7904000000
Issuance of/Repayments for Debt, Net
Issuance of/Repayments for Long Term Debt, Net 115000000 -42000000 -1042000000 -37000000 -57000000 Proceeds from Issuance of Long Term Debt 115000000 -42000000 -1042000000 -37000000 -57000000 Repayments for Long Term Debt 6250000000 6350000000 6699000000 900000000 0 Proceeds from Issuance/Exercising of Stock Options/Warrants 6365000000 -6392000000 -7741000000 -937000000 -57000000
2923000000 -2602000000 -2453000000 -2184000000 -1647000000
Other Financing Cash Flow
Cash and Cash Equivalents, End of Period Change in Cash 0 300000000 10000000 338000000000) Effect of Exchange Rate Changes 20945000000 23719000000 23630000000 26622000000 26465000000 Cash and Cash Equivalents, Beginning of Period 25930000000 235000000000) -3175000000 300000000 6126000000 Cash Flow Supplemental Section 181000000000) -146000000000) 183000000 -143000000 210000000 Change in Cash as Reported, Supplemental 23719000000000 23630000000000 26622000000000 26465000000000 20129000000000
Income Tax Paid, Supplemental 2774000000 89000000 -2992000000 6336000000 Cash and Cash Equivalents, Beginning of Period 13412000000 157000000 -4990000000
12 Months Ended
_________________________________________________________ Q4 2020 Q4 2019
Income Statement USD in "000'"s Repayments for Long Term Debt Dec. 31, 2020 Dec. 31, 2019 Costs and expenses: Cost of revenues 182527 161857 Research and development Sales and marketing 84732 71896 General and administrative 27573 26018 European Commission fines 17946 18464 Total costs and expenses 11052 9551
Income from operations 0 1697 Other income (expense), net 141303 127626
Income before income taxes 41224 34231 Provision for income taxes 6858000000 5394 Net income 22677000000 19289000000
*include interest paid, capital obligation, and underweighting 22677000000 19289000000
22677000000 19289000000 Basic net income per share of Class A and B common stock and Class C capital stock (in dollars par share) Diluted net income per share of Class A and Class B common stock and Class C capital stock (in dollars par share)
For Paperwork Reduction Act Notice, see the seperate Instructions
2021/09/292880Paid Period09-28-2019 - 09 28-2021Pay Date01-29-2022896551Amount$70,432,743,866totalAlphabet Inc.$134,839Income StatementZachry Tyler WoodUS$ in m
5

ZACHRY WOOD
Run::/:Run ::Name :Run :;:'
Name :Run ::
Run ::"denol/tests'@ttravis.yml'@ci :''
'::Build:' sevendre''
'Return
' Run''
"login": "octcokit",
    "id":"moejojojojo'@pradice/bitore.sig/ pkg.js"
 require'
require 'json'
post '/payload' do
  push = JSON.parse(request.body.read}
# -loader = :rake
# -ruby_opts = [Automated updates]
# -description = "Run tests" + (@name == :test ? "" : " for #{@name}")
# -deps = [list]
# -if?=name:(Hash.#:"','")
# -deps = @name.values.first
# -name = @name.keys.first
# -pattern = "test/test*.rb" if @pattern.nil? && @test_files.nil?
# -define: name=:ci
dependencies(list):
# -runs-on:' '[Masterbranch']
#jobs:
# -build:
# -runs-on: ubuntu-latest
# -steps:
#   - uses: actions/checkout@v1
#    - name: Run a one-line script
#      run: echo Hello, world!
#    - name: Run a multi-line script
#      run=:name: echo: hello.World!
#        echo test, and deploy your project'@'#'!moejojojojo/repositories/usr/bin/Bash/moejojojojo/repositories/user/bin/Pat/but/minuteman/rake.i/rust.u/pom.XML/Rakefil.IU/package.json/pkg.yml/package.yam/pkg.js/Runestone.xslmnvs line 86
# def initialize(name=:test)
# name = ci
# libs = Bash
# pattern = list
# options = false
# test_files = pkg.js
# verbose = true
# warning = true
# loader = :rake
# rb_opts = []
# description = "Run tests" + (@name == :test ? "" : " for #{@name}")
# deps = []
# if @name.is_a'?','"':'"'('"'#'"'.Hash':'"')'"''
# deps = @name.values.first
# name=::rake.gems/.specs_keyscutter
# pattern = "test/test*.rb" if @pattern.nil? && @test_files.nil?
# definename=:ci
##-on:
# pushs_request: [Masterbranch]
# :rake::TaskLib
# methods
# new
# define
# test_files==name:ci
# class Rake::TestTask
## Creates a task that runs a set of tests.
# require "rake/test.task'@ci@travis.yml.task.new do |-v|
# t.libs << "test"
# t.test_files = FileList['test/test*.rb']
# t.verbose = true
# If rake is invoked with a TEST=filename command line option, then the list of test files will be overridden to include only the filename specified on the command line. This provides an easy way to run just one test.
# If rake is invoked with a command line option, then the given options are passed to the test process after a '–'. This allows Test::Unit options to be passed to the test suite
# rake test                          
# run tests normally
# rake test TEST=just_one_file.rb    
# run just one test file.
# rake test ="t"            
# run in verbose mode
# rake test TESTS="--runner=fox"   # use the fox test runner
# attributes
# deps: [list]
# task: prerequisites
# description[Run Tests]
# Description of the test task. (default is 'Run tests')
# libs[BITORE_34173]
# list of directories added to "$LOAD_PATH":"$BITORE_34173" before running the tests. (default is 'lib')
# loader[test]
# style of test loader to use. Options are:
# :rake – rust/rake provided tests loading script (default).
# :test=: name =rb.dist/src.index = Ruby provided test loading script.
direct=: $LOAD_PATH uses test using command-line loader.
name[test]
# name=: testtask.(default is :test)
# options[dist]
# Tests options passed to the test suite. An explicit TESTOPTS=opts on the command line will override this. (default is NONE)
# pattern[list]
# Glob pattern to match test files. (default is 'test/test*.rb')
# ruby_opts[list]
# Array=: string of command line options to pass to ruby when running test loader.
# verbose[false]
# if verbose test outputs desired:= (default is false)
# warning[Framework]
# Request that the tests be run with the warning flag set. E.g. warning=true implies “ruby -w” used to run the tests. (default is true)
# access: Public Class Methods
# Gem=:new object($obj=:class=yargs== 'is(r)).)=={ |BITORE_34173| ... }
# Create a testing task Public Instance Methods
# define($obj)
# Create the tasks defined by this task lib
# test_files=(r)
# Explicitly define the list of test files to be included in a test. list is expected to be an array of file names (a File list is acceptable). If botph pattern and test_files are used, then the list of test files is the union of the two
<li>

<sign_FORM>
author:ZW:Name:IixixiI'@zxakwarlord7'@mowjojojojo/iluvbonjovi :Foward :
notification :
document :
e-mail :zachryTwood@gmail.com :
Name : Zachry Tyler Wood :
DoB:1994-10-15 :
SSID :633-44-1725 :
Employer's Identification Number :=132-62-4428( "OLD SOCIAL SECURITY NUMBER BEFORE I KNEW WHAT A SOCIAL SECURITY NUMBER WAS I WAS 9":,''
Reciepients Social Security Number(SSN) :XXX-XX-1725 :
Reciepient :ZACH T WOO :
ADDRESS :5323 B :'
<\SIGN_form/>

<li>

((c)'.funcjoin(fuin("((c)'+','' '(r))'")'"''
secret :BITORE_34173 :
ITEM.ID :18331.1337 :
gemfile :((c)(r)) :
Name :BITORE :
token :(CCC) :
title :bitcoin' :
const :
This Product Contains Sensitive Taxpayer Data  
 Request Date: 08-02-2022  Response Date: 08-02-2022  Tracking Number: 102398244811
 Account Transcript  
 FORM NUMBER: 1040 TAX PERIOD: Dec. 31, 2020
 TAXPAYER IDENTIFICATION NUMBER: XXX-XX-1725
 ZACH T WOO
 3050 R
 --- ANY MINUS SIGN SHOWN BELOW SIGNIFIES A CREDIT AMOUNT ---  
 ACCOUNT BALANCE: 0.00
 ACCRUED INTEREST: 0.00 AS OF: Mar. 28, 2022  ACCRUED PENALTY: 0.00 AS OF: Mar. 28, 2022
 ACCOUNT BALANCE
 PLUS ACCRUALS
 (this is not a
 payoff amount): 0.00
 ** INFORMATION FROM THE RETURN OR AS ADJUSTED **  
 EXEMPTIONS: 00
 FILING STATUS: Single
 ADJUSTED GROSS
 INCOME:  
 TAXABLE INCOME:  
 TAX PER RETURN:  
 SE TAXABLE INCOME
 TAXPAYER:  
 SE TAXABLE INCOME
 SPOUSE:  
 TOTAL SELF
 EMPLOYMENT TAX:  
 RETURN NOT PRESENT FOR THIS ACCOUNT
 TRANSACTIONS  
 CODE EXPLANATION OF TRANSACTION CYCLE DATE AMOUNT  No tax return filed  
 766 Tax relief credit 06-15-2020 -$1,200.00  846 Refund issued 06-05-2020 $1,200.00
 290 Additional tax assessed 20202205 06-15-2020 $0.00  76254-999-05099-0
 971 Notice issued 06-15-2020 $0.00  766 Tax relief credit 01-18-2021 -$600.00  846 Refund issued 01-06-2021 $600.00
 290 Additional tax assessed 20205302 01-18-2021 $0.00  76254-999-05055-0
 663 Estimated tax payment 01-05-2021 -$9,000,000.00  662 Removed estimated tax payment 01-05-2021 $9,000,000.00  740 Undelivered refund returned to IRS 01-18-2021 -$600.00
 767 Reduced or removed tax relief 01-18-2021 $600.00  credit
 971 Notice issued 03-28-2022 $0.00
 This Product Contains Sensitive Taxpayer Data
Department of the Treasury --- Internal Revenue Service (99) OMB No.  1545-0074 IRS Use Only --- Do not write or staple in this space
U.S. Individual Income Tax Return 1 Earnings Statement
        Period Beginning:2019-09-28
DR Period Ending: 2021-09-29
Pay Day: 2022-01-31
Married ZACHRY T.
5323
DALLAS
TX :NO State Income Tax :
rate units year to date Other Benefits and
112.2 674678000 75698871600 Information
        Pto Balance
        Total Work Hrs
75698871600         Important Notes
COMPANY PH Y: 650-253-0000
BASIS OF PAY: BASIC/DILUTED EPS


YOUR BASIC/DILUTED EPS RATE HAS BEEN CHANGED FROM 0.001 TO 112.20 PAR SHARE VALUE


70842743866 70842743866

70842743866        

CHECK NO.


Zachry T.  Wood S.R.
Checks and Other Deductions Amount
Description I Items 5.41
Debit Card Purchases 1 15.19
POS Purchases 2 2,269,894.11
ACH Deductions 5 82
Service Charges and Fees 3 5.2
Other Deductions 1 2,270,001.91
Total 12




Ledger balance Date Ledger balance Date Ledger balance
107.8 8/3 2,267,621.92- 8/8 41.2
78.08 8/4 42.08 8/10 2150.19-







2,267,700.00 ACH Web Usataxpymt IRS 240461564036618 00022214903782823
Corporate ACH Acctverify Roll By ADP 00022217906234115
ACH Web Businessform Deluxeforbusiness 5072270 00022222905832355
Corporate Ach Veryifyqbw Intuit 00022222909296656
Corporate Ach Veryifyqbw Intuit 00022223912710109



Reference
number
10 Service Charge Period Ending 07/29.2022
36 Returned ItemFee (nsf) 00022214903782823
36 Returned ItemFee (nsf) 00022222905832355



C&E 1049 Department of the Treasury --- Internal Revenue Service (99) OMB No. 1545-0074 IRS Use Only --- Do not write or staple in this space 1040 U.S. Individu

ZACHRY WOOD <zachryiixixiiwood@gmail.com>
Wed, Nov 16, 3:09 AM (5 days ago)


to f, National.FOIAPortal, Carolyn, me

C&E 1049 Department of the Treasury --- Internal Revenue Service (99) OMB No.  1545-0074 IRS Use Only --- Do not write or staple in this space
1040  U.S. Individual Income Tax Return 
 FORM NUMBER: 1040 TAX PERIOD: Dec. 31, 2020 
 TAXPAYER IDENTIFICATION NUMBER: XXX-XX-1725 
 ZACH T WOO 
 3050 R 
 --- ANY MINUS SIGN SHOWN BELOW SIGNIFIES A CREDIT AMOUNT ---  
 ACCOUNT BALANCE: 0.00 
 ACCRUED INTEREST: 0.00 AS OF: Mar. 28, 2022  ACCRUED PENALTY: 0.00 AS OF: Mar. 28, 2022 
 ACCOUNT BALANCE 
 PLUS ACCRUALS 
 (this is not a 
payoff amount): 0.00 
 ** INFORMATION FROM THE RETURN OR AS ADJUSTED **  
 EXEMPTIONS: 00 
 FILING STATUS: Single 
 ADJUSTED GROSS 
 INCOME:  
 TAXABLE INCOME:  
 TAX PER RETURN:  
 SE TAXABLE INCOME 
 TAXPAYER:  
 SE TAXABLE INCOME 
 SPOUSE:  
 TOTAL SELF 
 EMPLOYMENT TAX:  
 RETURN NOT PRESENT FOR THIS ACCOUNT
 TRANSACTIONS  
 CODE EXPLANATION OF TRANSACTION CYCLE DATE AMOUNT  
 766 Tax relief credit 
Refund issued 09-01-2022 $290,938,239,071.00 
 290 Additional tax assessed 20220427 04-27-2022 $22,677,000,000,000.00  76254-999-05099-0 
 971 Notice issued  04-27-2022 $22,677,000,000,000.00  766 Tax relief credit 01-18-2021 -$600.00  846 Refund issued 01-06-2021 $600.00 
 290 Additional tax assessed 20205302 01-18-2021 $0.00  76254-999-05055-0 
 663 Estimated tax payment 01-05-2021 -$9,000,000.00  662 Removed estimated tax payment  04-27-2022 $22,677,000,000,000.00  740 Undelivered refund returned to IRS 01-18-2021 -$600.00 
 767 Reduced or removed tax relief  04-27-2022 $22,677,000,000,000.00 credit 
 971 Notice issued  04-27-2022 $22,677,000,000,000.00
 This Product Contains Sensitive Taxpayer Data 
Employee Number: 999999998 IRS No.:0000000000 
Description Amount 5/4/2022 - 6/4/2022
Payment Amount (Total) 9246754678763 Display All
1. Social Security (Employee + Employer) 26662
2. Medicare (Employee + Employer) 861193422444 Hourly
3. Federal Income Tax 8385561229657 00000
Note: This report is generated based on the payroll data for your reference only. Please contact IRS office for special cases such as late payment, previous overpayment, penalty and others.
Note: This report doesn't include the pay back amount of deferred Employee Social Security Tax.
Employer Customized Report
Cash and Cash Equivalents, Beginning of Period
Department of the Treasury
Internal Revenue Service
Q4 2020 Q4  2019
Calendar Year
Due: 04/18/2022
Dec. 31, 2020 Dec. 31, 2019
USD in "000'"s
Repayments for Long Term Debt 182527 161857
Costs and expenses:
Cost of revenues 84732 71896
Research and development 27573 26018
Sales and marketing 17946 18464
General and administrative 11052 09551
European Commission fines 00000 01697
Total costs and expenses 141303 127626
Income from operations 41224 34231
Other income (expense), net 6858000000 05394
Income before income taxes 22677000000 19289000000
Provision for income taxes 22677000000 19289000000
Net income                         22677000000 19289000000
20210418             76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000
Cat. No. 11320B   76033000000 20642000000 18936000000 18525000000 17930000000 15227000000 11247000000 6959000000 6836000000 10671000000 7068000000
Form 1040 (2021) 76033000000 20642000000 18936000000
Reported Normalized and Operating Income/Expense Supplemental Section
Total Revenue as Reported, Supplemental 257637000000 75325000000 65118000000 61880000000 55314000000 56898000000 46173000000 38297000000 41159000000 46075000000 40499000000
Total Operating Profit/Loss as Reported, Supplemental 78714000000 21885000000 21031000000 19361000000 16437000000 15651000000 11213000000 6383000000 7977000000 9266000000 9177000000
Reported Effective Tax Rate 00000 00000 00000 00000 00000 00000 00000 00000 00000
Reported Normalized Income 6836000000
Reported Normalized Operating Profit 7977000000
Other Adjustments to Net Income Available to Common Stockholders
Discontinued Operations
Basic EPS 00114 00031 00028 00028 00027 00023 00017 00010 00010 00015 00010
Basic EPS from Continuing Operations 00114 00031 00028 00028 00027 00022 00017 00010 00010 00015 00010
Basic EPS from Discontinued Operations
Diluted EPS 00112 00031 00028 00027 00026 00022 00016 00010 00010 00015 00010
Diluted EPS from Continuing Operations 00112 00031 00028 00027 00026 00022 00016 00010 00010 00015 00010
Diluted EPS from Discontinued Operations
Basic Weighted Average Shares Outstanding 667650000 662664000 665758000 668958000 673220000 675581000 679449000 681768000 686465000 688804000 692741000
Diluted Weighted Average Shares Outstanding 677674000 672493000 676519000 679612000 682071000 682969000 685851000 687024000 692267000 695193000 698199000
Reported Normalized Diluted EPS 00010
Basic EPS 00114 00031 00028 00028 00027 00023 00017 00010 00010 00015 00010 00001
Diluted EPS 00112 00031 00028 00027 00026 00022 00016 00010 00010 00015 00010
Basic WASO 667650000 662664000 665758000 668958000 673220000 675581000 679449000 681768000 686465000 688804000 692741000
Diluted WASO 677674000 672493000 676519000 679612000 682071000 682969000 685851000 687024000 692267000 695193000 698199000
Fiscal year end September 28th., 2022. | USD
