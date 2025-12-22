from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()

url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421"

loader  = WebBaseLoader(
    web_path=url
)

docs = loader.load()

print(type(docs))
print("--"*30)
print(len(docs))
print("--"*30)
print(docs[0].metadata)
print("--"*30)
print(docs[0].page_content)
print("--"*30)

template = PromptTemplate(
    template= "Answer the following question \n {question} from the given text \n {text}",
    input_variables=["question","text"]
)

model = ChatOpenAI(
    model="gpt-3.5-turbo"
)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({
    "question": "What is the prodcut that we are talking about?",
    "text": docs[0].page_content
})

print(result)



# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/9.DocumentLoaders (main)
# $ py 4_webbased_loader.py
# USER_AGENT environment variable not set, consider setting it to identify your requests.
# <class 'list'>
# ------------------------------------------------------------
# 1
# ------------------------------------------------------------
# {'source': 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421', 'title': 'Apple MacBook AIR M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A Rs.85900  Price in India - Buy Apple MacBook AIR M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A Midnight Online - Apple : Flipkart.com', 'language': 'en'}
# ------------------------------------------------------------
#   Apple MacBook AIR M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A Rs.85900  Price in India - Buy Apple MacBook AIR M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A Midnight Online - Apple : Flipkart.com        Explore PlusLoginBecome a Seller More CartAdd to cart Buy NowHomeComputersLaptopsApple LaptopsApple MacBook AIR M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A (13.6 Inch, Midnight, 1.24 kg)
# CompareShareApple MacBook AIR M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A  (13.6 Inch, Midnight, 1.24 kg)4.610,906 Ratings & 705 ReviewsExtra ₹16910 off₹68,990₹85,90019% offi+ ₹156 Protect Promise Fee Learn moreSecure delivery by 28 Dec, SundayAvailable offersBank Offer5% cashback on Axis Bank Flipkart Debit Card up to ₹750T&CBank Offer5% cashback on Flipkart SBI Credit Card upto ₹4,000 per calendar quarterT&CBank Offer10% off up to ₹1,500 on BOBCARD EMI Transactions,  Min Txn Value: ₹5,000T&CSpecial PriceGet extra ₹16910 offT&CView 6 more offersBuy 
# without Exchange₹68,990Buy with Exchangeup to ₹22,000 offEnter pincode to check if exchange is available1 Year Limited WarrantyKnow MoreColorMidnightStarlightPlease select a Color to proceed✕DeliveryCheckEnter pincodeDelivery by28 Dec, Sunday?if ordered before 6:10 PMInstallation & Demo  by27 Dec, Saturday|₹599View DetailsHighlightsStylish & Portable Thin and Light Laptop13.6 Inch Liquid Retina display, LED-backlit display with IPS technology native resolution at 224 pixels per inch, 500 nits brightnessLight Laptop without Optical Disk DriveEasy Payment 
# OptionsNo cost EMI starting from ₹22,997/monthCash on DeliveryNet banking & Credit/ Debit/ ATM cardView DetailsSellerTREASURE HAUL ONLINE4.7No Returns Applicable?GST invoice available?See other sellersSpecificationsWarrantyWarranty Summary1 Year Limited WarrantyWarranty Service TypeOnsiteCovered in WarrantyManufacturing DefectsNot Covered in WarrantyPhysical DamageDomestic Warranty1 YearWarranty1Processor And Memory 
# FeaturesProcessor BrandAppleProcessor NameM2SSDYesSSD Capacity256 GBRAM16 GBRAM TypeUnified MemoryGraphic ProcessorNAStorage TypeSSDOperating SystemMac OSIn The BoxSales Package13.6 inch MacBook Air USB-C Power Adapter, USB-C to MagSafe 3 Cable (2 m)GeneralBrandAppleModel NumberMC7X4HN/APart NumberMC7X4HN/AModel NameMacBook AirSeriesMacBook AIRColorMidnightTypeThin and Light LaptopSuitable ForProcessing & MultitaskingBattery BackupUpto 18 HoursMS Office ProvidedNoIs FragileNoIs TabletNoDisplay And Audio FeaturesTouchscreenNoScreen Size34.54 cm (13.6 Inch)Screen Resolution2560 x 1664 PixelScreen TypeLiquid Retina display, LED-backlit display with IPS technology native resolution at 224 pixels per inch, 500 nits brightnessSpeakersBuilt-in SpeakersSound PropertiesFour-speaker sound systemScreen Resolution TypeLiquid Retina DisplayDimensionsDimensions304.1 x 215.0 x 11.3 mmWeight1.24 kgAdditional FeaturesDisk DriveNot AvailableWeb Camera1080p FaceTime HD cameraKeyboardBacklit Magic KeyboardBacklit KeyboardYesIncluded SoftwareBuilt-in Apps: App Store, Books, Calendar, Contacts, FaceTime, Find My, Freeform, GarageBand, Home, iMovie, Keynote, Mail, Maps, Messages, Music, Notes, Numbers, Pages, Photo Booth, Photos, Podcasts, Preview, QuickTime Player, Reminders, Safari, Shortcuts, Siri, Stocks, Time Machine, TV, Voice Memos, WeatherOperating SystemOperating SystemmacOS SequoiaPort And 
# Slot FeaturesMic InYesUSB Port2 x Thunderbolt USB 4Connectivity FeaturesWireless LANWi-Fi 6 (802.11ax)Bluetoothv5.3Read MoreBuy Together and Save upto 20%Apple MacBook AIR M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A4.6(10,906)₹68,990₹85,90019% offApple White Multi-Touch Surface - USB-C Magic Mouse Wireless Touc...4.5(391)₹6,299ZEBRONICS Zeb-NS3000 Steel Desk Stand Laptop Stand with Adjustabl...4(473)₹543₹67920% offSpecial price if bought with this itemPlease add at least 1 add-on item to proceedADD TO CARTRatings & ReviewsRate Product4.6★10,906 Ratings &705 Reviews5★4★3★2★1★8,6411,4952611064034.6Performance4.7Battery4.7Design4.7Display+ 4935Terrific purchaseMy first laptop and it's macbook🥺it's amazingREAD MOREAmrita DharaCertified Buyer, Haora District3 months ago393103PermalinkRepor t Abuse5Classy productAwesome Product Tank you Flipkart.READ MORERahul Sarraf Certified Buyer, Raxaul Bazar2 months ago20850PermalinkReport Abuse5Great productBest product �👍REA
# MORESHISHIR ChakmaCertified Buyer, Jabalpur5 months ago5810PermalinkReport Abuse5BrilliantI am computer science student.  All the college work is going very smoothly. And I love it.READ MOREKRISHNENDU KARCertified Buyer, Rajpur Sonarpur1 month ago8317PermalinkReport Abuse5Worth every pennyAll good so far except a few fingermarks here and there. I am sure the seller has opened the box and done some checking.READ MORESwaraj SamantarayCertified Buyer, Pune2 months ago8018PermalinkReport Abuse5ExcellentIt's very good product �👌😌😌READ MOREZack  hereCerti
#  Buyer, Haora District7 months ago294PermalinkReport Abuse5Excellentsmooth as everyone says, though it takes time to get used to if you are 
# coming from windows. Definitely worth learningREAD MORERajat KumarCertified Buyer, Mukerian3 months ago100PermalinkReport Abuse5Just wow!I writing this after using 1 week I have this M2 AIR in bbd 2025 sale Which price is at 64K At that price no window laptop can beat this performance,battery,display, performance,etc..If your reading my review just blindly go for the laptop Its worth for money Dont use anu laptop cases which definitely damage the laptop hinge , Don't use any accessories for laptop which definitely cause damage for laptopJust buy the laptop use carefullyREAD MORESurya  Prakash Certified Buyer, Nadendla2 months ago336PermalinkReport Abuse4Good quality productI know that this macbook is a gd one but was worried about this seller. I searched for this Treasure Haul Online seller and came to know that there are many negative reviews. Please do check the serial number and any kind of damage that's all you can do before sharing otp. I received this product 
# on 11th May, 2025 and it's really value for money. Battery is insanely good, nothing to mention about performance we all know that. Good display ( macbook pro has even better display). One problem i ...READ MORESoumya  DasCertified Buyer, Basudebpur Purba Medinipur District7 months ago23271PermalinkReport Abuse5Simply awesomeI was very scared of this seller. But I was really amazed that the product is very good and totally brand new. I just loved it bcoz its my first laptop and its MacBook.READ MORESatish YadavCertified Buyer, Varanasi Division1 month ago80PermalinkReport Abuse+All 705 reviewsQuestions and AnswersQ:back side logo lights ?A:No . Logo doesn't light up.Apple has discontinued it from 2018 or maybe 2017Akhil  NegiCertified Buyer19748Report AbuseQ:M2 can come with MS office like ms word, ms exel, power point presentation etc...A:It is not pre downloaded you have to download it from App StoreAnonymousCertified Buyer6820Report AbuseRead other answersQ:Is 8gb ram sufficient for students?A:Yes. You can easily do multitasking work on it.Vishal KumarCertified Buyer113Report AbuseQ:Can use for civil engineering students?A:YesAnonymousCertified Buyer4126Report AbuseQ:4k video output is there or not?A:Yes and it's goodAnonymousCertified Buyer92Report AbuseQ:Can we use it for machine learning?A:Of course you can. It depends on the apps you are going to use.Karthik SwotCertified Buyer30Report AbuseQ:What is in the box?A:Adapter ,magsafe charger, macbookAnu Sharma Certified Buyer41Report AbuseQ:can we charge using type charger like we do for macbook pro?A:No, it will not be good because some connectivity issues will be seen if we use the same port for multiple useDr. Nur Ahammed  KhanCertified Buyer20Report AbuseQ:Can we use python,sql,power bi in macbook?A:Yes u can use all in macbook and 
# all work fine as a java developer i am also using MacBook for my projectsDeepak TripathiCertified Buyer45Report AbuseQ:Is this connect to realme phoneA:need to download android data transfer software for for file transfer form Android to macsavai marajCertified Buyer24053Report AbuseAll questions+Safe and Secure Payments.Easy returns.100% Authentic products.You might be interested inPhysicalMin. 50% OffShop NowWired 
# EarphonesMin. 50% OffShop NowData CardsMin. 50% OffShop NowExternal HDDMin. 50% OffShop NowTop Stories:Brand DirectoryMOST SEARCHED IN Computers & Accessories:ACER ASPIRE S7CANON ALL IN ONE PRINTERASUS GRAPHICS CARD500 GB HARD DISK PRICEINTEL PROCESSORS PRICETV TUNER FOR MONITORDESKTOP COMPUTERSHP DESKTOPSTPLINK ROUTERBROTHERS PRINTERSAMSUNG PRINTERSDELL LATITUDEHP LAPTOP DRIVERHP INK ADVANTAGEHUAWEI POWER-FI E8221HUAWEI MODEMDELL INSPIRON BATTERYDVD WRITERDELL LAPTOP CHARGER PRICEDELL LAPTOPS I5ULTRABOOKLENOVO FLEX 2LENOVO G50-70LENOVO G50LENOVO FLEX 10MICROSD CARDANTIVIRUS ONLINE PURCHASETPLINKWD MY PASSPORT ULTRAABOUTContact UsAbout UsCareersFlipkart StoriesPressCorporate InformationGROUP COMPANIESMyntraCleartripShopsyHELPPaymentsShippingCancellation & ReturnsFAQCONSUMER POLICYCancellation & ReturnsTerms Of UseSecurityPrivacySitemapGrievance RedressalEPR ComplianceFSSAI Food Safety Connect AppMail Us:Flipkart Internet Private Limited,
#  Buildings Alyssa, Begonia &
#  Clove Embassy Tech Village,
#  Outer Ring Road, Devarabeesanahalli Village,
#  Bengaluru, 560103,
#  Karnataka, India
# SocialRegistered Office Address:Flipkart Internet Private Limited,
#  Buildings Alyssa, Begonia &
#  Clove Embassy Tech Village,
#  Outer Ring Road, Devarabeesanahalli Village,
#  Bengaluru, 560103,
#  Karnataka, India
#  CIN : U51109KA2012PTC066107
#  Telephone: 044-45614700 / 044-67415800
# Become a SellerAdvertiseGift CardsHelp Center© 2007-2025 Flipkart.comBack to top




# ------------------------------------------------------------
# The product we are talking about is the Apple MacBook AIR M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A.
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/9.DocumentLoaders (main)