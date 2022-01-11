---
layout: post
title: SAP MM Interview Questions & Answers   
tags: Work
image: /img/path.png
---

# SAP MM Interview Questions & Answers(General):

## 1. Tell me a little bit about your self.

​	I hold a bachelor's degree in logistic management from the university of Nanjing Finance and Economics. 

​	I have been working here for 18 years as a  senior warehouse supervisor.

​	I'm responsible for warehouse management, SAP MM/SD troubleshooting  and new sap project support.

 ## 2. What's your greatest strength?

​	My greatest strength is I'm very familiar with SAP and some other applications such as GIT/Vim/vscode, I am sure I can dive right in.

## 3. What's your greatest weakness?

​	I heard in here you use ABAP language which I am not very familiar with, but I am a quick learner and currently studying this at the moment on my own.

## 4. Do you prefer to work independently or in a team?

​	I have experiences with both environments and I see value in both environments.

## 5. Where do you see yourself in 5 years?

​	In five years, I'd like to be recognized as an expert of SAP MM module , and  I know  I'll have opportunity to do here.

## 6. What makes you the best fit for this position?/ Why should we hire you?

​	I have ten more years experiences in business and SAP MM and SD module, and I think my experience is perfectly  aligned with the requirements you asked for in your job listing.

## 7. Why do want to leave your current job?

​	I feel I have a lot more to offer my current job and  I'm ready to go for a new challenge and new  opportunities where I can take on more responsibilities and contribute more.

## 8. What do you expect from your supervisor/manager?

​	The most important thing that I want from my manager is constructive feedback so I know where I need to improve. I also expect my boss give me support, guidance and encouragement as I want to continually grow, and having a good manager will help me achieve my goal.

	## 9. How do you handle stress and pressure?

​	Prioritizing my work so I have a clear idea of what needs to be done when, and this has helped me effectively manage pressure on my job.

## 10. Do you have any questions for me?

​	I'd like to know a little bit more about the team I'm working with


## Soft skills

* teamwork 团队合作

* planning and organization 规划组织能力

* time management 时间管理能力

* coordination 协调能力

* skill set 综合技能

* communication skills 沟通技巧

* problem-solving skills 解决问题的技巧

* analytical thinking 分析思考的能力

* decision-making skills 决策能力

* intellectual curiosity 求知欲

* presentation skills 演讲能力

* initiative/be proactive 主动进取心

* flexibility 弹性和适应能力

* stress tolerance 耐压力


---


# SAP MM Interview Questions & Answers (Professional)

[![Madeline Carter](file:///C:/TEMP/msohtmlclip1/01/clip_image003.jpg)](https://www.guru99.com/author/madeline)By[Madeline Carter](https://www.guru99.com/author/madeline) Updated October 28, 2021

**1) Explain what is SAP MM?**

SAP MM (Material Management) is a functional module in SAP that deals with procurement handling and material management. The MM module contains master data, system configuration and transactions to complete the procure to pay process.

**2) What are the essential components in SAP MM?**

* Determine     requirements
* Source     determination
* Vendor     Selection
* Order     Processing
* Order     follow up
* Goods     receipts and Inventory management
* Invoice     Verification

**3) Mention what are the types of special stock available?**

The types of special stock available are subcontracting, consignment, project, pipeline, sales order, stock transfer, returnable packaging with customer, etc.

**4) List out important field in purchasing view?**

The critical fields in purchasing view are

* Base     unit of measure
* Order     unit
* Purchasing     group
* Material     group
* Valid     from
* Tax     indicator for material
* Manufacturer     part number
* Manufacturer,     etc.


 **5) Explain the importance of the batch record?**

A batch tells about a quantity of a particular product, which is processed or produced at the same time with the same parameters. The materials produced in such batch have the same values and characteristics. While, the batch record gives the information about a particular batch product and helpful in knowing whether the product has gone through GMP (Good Manufacturing Process).

**6) Explain how you can link a document to a vendor master record?**

To link the document with the vendor master record by using the XK01 transaction code or by using the following menu path

* SAP     Menu > Logistics > Material Management > Purchasing > Master     Data > Vendor > Central > XK01- Create.

**7) Mention what are the major purchasing tables? List the transaction codes for them?**

* Purchase     requisition > EKBN
* Purchase     requisition account assignment > EBKN
* Release     documentation > EKAB
* History     of purchase documents > EKBE

**8) Mention what are the data contained in the information record?**

The information record contains data related to the units of measurement, such as the products, vendor price, materials used by specific vendors, etc. It also contains information on the tolerance limit of the under delivery of data, vendor evaluation data, planned delivery time, availability status for goods.

**9) Mention what is the transaction code to delete a batch?**

The transaction code MSC2N is used to delete a batch. By flagging the batch master record, you can delete a batch record alternatively.

**10) Mention what is the transaction code used to extend the material view?**

To extend the material view transaction, code MM50 is used.


 **11) Explain how you can change the standard price in the master material?**

The standard price for the material data cannot be updated or changed directly. However, to change the standard price you can perform the following steps

* Fill     in the future fields price ( MBEW-ZKPRS ) and the effective data (     MBEW-ZKDAT) for the materials
* Select     Logistics > Material Management > Valuation > Valuation Price     Determination > Future Price

**12) What is Source List and what is the transaction code for creating Source List?**

To identify sources of supply for materials a source list is used. To create a source list the transaction code used is ME01.

**13) For creating a purchasing info record what are the pre-requisites?**

The pre-requisites for creating a purchase info record are

* Material     Number
* MPN     ( Manufacturer Part Number )
* Vendor     Number
* Organizational     level code

**14) Explain the terms Planned delivery and GR processing time?**

Planned delivery means number of calendar days required to obtain the material, and GR processing means number of workdays required after receiving the material for inspection and placement into storage.

**15) What is purchase requisition as related to SAP? Mention the document types that are used in purchase requisition?**

Purchase requisition in SAP determines both stock and non-stock items to the purchasing department. It can be done either manually or automatically, the document types used in purchase requisition are

* RFO     ( Request For Quotation )
* Outline     Agreement
* PO     ( Purchasing Order )

**16) Explain how consignment stocks are created?**

In the normal purchase order or requisition, consignment stocks are created. While creating consignment stocks things to be considered is that you must enter K category for the consignment item. As a result, the goods issued are posted to consignment stores and invoice receipt is not generated.


 **17) Explain how is the vendor return processed without a purchase order reference?**

First you have to observe the return column and then select — Item Detail > MIGO_GR > Goods Receipt for Purchase Order. Use movement type 161 if the intention is to deduct the stock otherwise, 162 is used to undo the changes. In the end, you have to ensure that the document is a return purchase order, and then the document is saved.

You can also use transaction code M21N for this purpose

**18) Explain how you can create a vendor account group in SAP?**

To create vendor account group in SAP

* Select     display IMG > Financial[ Accounting ](https://www.guru99.com/accounting.html)>     Accounts Payable/Receivable >Vendor Accounts > Master Records >     Preparation of creating vendor master records > Define Accounts groups     with Screen Layout

**19) Explain what are the accounts created in SAP MM?**

Assignment of account is necessary for the purchase order item, it is important in SAP MM as it determines following things

* Account     assignment type
* Account     that will be charged when you post the invoice or goods receipt
* Account     assignment data that you should provide

**20) Explain what MRP (Material Requirement Planning) list is and what is the transaction code to access MRP list?**

MRP list is the initial working document from which the MRP controller starts working, and it consists of planning results information for the material. For an individual item, you can access the MRP list by using the transaction code MD05. You can also access the MRP list by navigation path

SAP Menu > Logistics > Materials Management > MRP > Evaluations > MRP List- Material

**21) Explain what is CBP? What is the difference between CBP and MRP?**

CBP is the past consumption values of stock; it is used to forecast future requirements. On the basis of past consumption values, the net requirement of goods is calculated.

The difference between CBP and MRP is that when you plan materials using MRP, you have to predict the materials requirement based on sales and operations planning (SOP). While in CBP you have to predict the material requirement based on historical demand for materials.
