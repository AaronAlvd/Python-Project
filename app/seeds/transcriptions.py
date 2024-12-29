from app.models import db, Transcription, environment, SCHEMA
from sqlalchemy.sql import text


def seed_transcriptions():
      transcription01 = Transcription(
        user_id=1, title='Untitled Document', 
        text="""282, SPECIAL OFFICIAL GAZETTE.

        (a) I further hereby, with the like concurrence as aforesaid, delegate to all Resident Magistrates and to all District Political Officers power to exercise the civil jurisdiction of the Special Tribunal in cases in which the value of the subject matter of the claim does not exceed Fls. 1500 and which they would but for the provisions of Article 21 aforesaid be empowered to try under the Courts Ordinance 1920.
        (b) An appeal shall lie from any finding, order or decree made or passed by such Resident Magistrate or District Political Officer to the Judge of the Special Tribunal or to a Judge of the High Court exercising the powers and jurisdiction of such tribunal.
        
        WM. MORRIS CARTER,
        Judge of the Special Tribunal.
        
        Dar-es-Salaam, 21st December, 1920.
        
        GOVERNMENT NOTICE No. 113
        
        NOTICE.
        
        His Majesty’s High Court of Tanganyika.
        
        The High Court will be open as from the 3rd January, 1921.
        
        WM. MORRIS CARTER,
        Chief Justice.
        
        Dar-es-Salaam, 22nd December, 1920.
        
        GOVERNMENT NOTICE No. 114.
        
        NOTICE.
        
        Civil Suits in the High Court and Special Tribunal.
        
        Pending the arrival of further clerical staff, no civil suits other than those specified below will be dealt with at the High Court:—
        Suits in the High Court or in the Special Tribunal when presided over by the Judge of that Tribunal or by one of the Judges of the High Court sitting in that Tribunal with delegated powers,
        (a) in which the plaintiff applies for the arrest of the defendant or for attachment before judgment; or
        (b) which, upon application, are certified by a Judge to be of an urgent nature.
        
        WM. MORRIS CARTER,
        Chief Justice and Judge of the Special Tribunal.
        
        Dar-es-Salaam, 22nd December, 1920.
        
        GOVERNMENT NOTICE No. 115.
        
        Appointments.
        
        To be Registrar of the Special Tribunal:—
        W.A. Wilson, Registrar of High Court, to date 22nd December, 1920
        
        To be Deputy Registrar of the Special Tribunal:—
        J.Q. Hanrahan, Deputy Registrar of High Court, to date 22nd December, 1920.
        
        A.C. HOLLIS,
        Chief Secretary.
        
        The Secretariat, Dar-es-Salaam, 22nd December, 1920.
        
        Corrigendum.
        
        On page 244 of this issue, Ordinance No. 9 of 1920, for “20th day of December” read “15th day of December.”
        
        Printed and Published by the Government Printer, Dar-es-Salaam.""")

      transcription02 = Transcription(
        user_id=2, title='Regulations Under the Births and Deaths Registration Ordinance, 1920',
        text="""
        SPECIAL OFFICIAL GAZETTE

(4) The copy of any entry in any register or return certified under the hand of the Registrar to be a correct copy shall be prima facie evidence in all Courts of the dates and facts therein contained.

Correction of errors.15. (1) The Registrar may, subject to any rules made by the Governor, correct any error in any register or index.(2) Correction shall be made without erasing the original entry, and shall be authenticated by the signature of the Registrar.

GENERAL

Compulsory registration.16. (1) The registration of the birth of a child shall be compulsory if either one or both parents are of European or American origin or descent, or, in the case of an illegitimate child not recognized by its father, if the mother is of European or American origin or descent.(2) The Governor may, by Order published in the Gazette, extend, from a date to be named in the Order, the provisions of this Ordinance relating to compulsory registration of births and deaths to all persons in the Territory of any particular race, class, tribe, or other group, or to all or some of the inhabitants of any particular town, district, or other area, and from and after the said date the registration of births and deaths shall, in such cases, be compulsory instead of being optional.

Substitution of other officers for D.P.O.s.17. The Governor may direct that the duties of the District Political Officer of any district under this Ordinance shall in that district be performed by any other public officer of the Territory.

Penalties.18. Any person who, being under an obligation to register the birth or death of any person, fails so to do within the prescribed period or refuses to state any of the prescribed particulars, or any person who wilfully gives any false information or particulars for the purpose of registration, shall be guilty of an offense, and shall be liable to a fine not exceeding 100 rupees or florins, or to one month's imprisonment of either kind, or to both.

Rules.19. The Governor may make rules with regard to the following matters, and generally for carrying into effect the provisions of this Ordinance:(1) The place in each district and the hours at which births and deaths may be registered.(2) The conditions under which, and the mode in which, registration may be effected without personal attendance.(3) The forms of all registers, returns, and other documents required for the purposes of this Ordinance.(4) The amount of any fee where a fee is prescribed by this Ordinance.(5) The inspection of registers, returns, and indexes, and the provisions of certified copies.(6) The places at which births and deaths occurring on board ships while within the territorial waters of the Territory shall be registered.

Definitions.20. In this Ordinance “prescribed particulars” means:(1) As to any birth, the sex, name, date, and place of birth, the names, residence, occupations, and nationality of the parents, and such other particulars as the Governor may by rule prescribe.(2) As to any death, the name, age, sex, residence, occupation and nationality of the deceased, and the date, place, and cause of death, and such other particulars as the Governor may by rule prescribe.

Short title and commencement.21. This Ordinance may be cited as “The Births and Deaths Registration Ordinance, 1920” and shall come into force:(1) As to the making of appointments and the issue of rules and instructions, immediately.(2) As to all other matters, from a date to be named by the Governor and published in the Gazette.

(Handwritten note: “See Gov Rule 47 of 23/7/1921.”)


        """)

      transcription03 = Transcription(
        user_id=3, title='Regulations for the Registration of Deaths - Special Official Gazette',
        text="""REGISTRATION OF DEATHS.

The District Political Officer of every district shall keep a register, and shall enter therein every death occurring within the district after the commencement of this Ordinance whereof the prescribed particulars are reported to him.

Every person registering a death shall, to the best of his knowledge and ability, give the prescribed particulars, and shall certify to their correctness either by signing, or, if he be illiterate, by affixing his mark to the register, or, if the registration be effected without personal attendance, by signing or affixing his mark to the prescribed form on which the prescribed particulars are reported to the District Political Officer.

In the case of every person dying after the commencement of this Ordinance, the registration of whose death is compulsory, it shall be the duty of the nearest relatives of such person who were present at his death or in attendance during his last illness, and in default of such relatives, of every other relative dwelling within the district, and in default of such relatives of each person present at the death, and of the occupier of the house in which to his knowledge such death took place; and in default of the person hereinbefore mentioned, of any inmate of the house, or of any person finding or taking charge of the body of such person, or causing such person to be buried, to register the death within one month after the death or finding of the body, or, where the District Political Officer is satisfied that from any cause registration could not be effected within the said period, and that no undue delay has taken place, within three months after the death or finding of the body.

The District Political Officer shall not enter in the register a death more than six months after the date of the death, except that where the registration of such death is compulsory the District Political Officer shall enter it upon receiving the written authority of the Registrar, and upon payment of the prescribed fee.

THE REGISTRAR.

(1) The Governor shall appoint a Registrar-General of Births and Deaths for the Territory hereinafter called "Registrar."

(2) It shall be the duty of the Registrar to compile, after the close of each year, a summary of births and deaths of such year and a report on the increase or decrease of the population of the Territory, and on any special causes appearing to affect the same.

(3) The Registrar shall have the custody of all filled register books and of all quarterly returns made by the District Political Officer of a district.

(4) It shall be the duty of the Registrar to provide the District Political Officer of a district with such book and forms as may be required, and with such instructions as he may consider necessary for the registration of births and deaths in his district.

The District Political Officer shall forward to the Registrar a quarterly return in the prescribed form showing the births and deaths registered in his district during such quarter, and shall also forward to him all registers so soon as the space in the same available for registration has become exhausted.

(1) The Registrar shall cause to be prepared from the returns made to him alphabetical indexes of the births and deaths registered.

(2) Any register, returns or index in the custody of the Registrar shall, on payment of the prescribed fee, be open to inspection, subject to such regulations as the Governor may by rule prescribe.

(3) The Registrar shall, on payment of the prescribed fee, furnish a certified copy of any entry in any register or any return in his custody.


        """)

      transcription04 = Transcription(
        user_id=1, title='Public Health and Sanitation Regulations - Official Gazette',
        text="""PUBLIC HEALTH AND SANITATION.

The Governor shall appoint a Chief Health Officer for the Territory, whose duty it shall be to supervise the implementation of health and sanitation regulations throughout the Territory. The Chief Health Officer shall report to the Governor on the state of public health in the Territory and shall make recommendations on necessary measures to control or prevent the spread of disease.

Every district shall have a District Health Officer, who shall be responsible for the maintenance of public health standards in the district. The District Health Officer shall ensure that sanitary measures are properly enforced, including the cleanliness of streets, public places, and private residences.

In the case of any outbreak of infectious diseases, the District Health Officer shall immediately notify the Chief Health Officer and take all necessary measures to prevent the spread of disease, including quarantine, disinfection, and the isolation of affected individuals.

All medical practitioners and health workers shall be required to report any cases of infectious diseases to the District Health Officer within 24 hours of diagnosis. Failure to do so may result in penalties or suspension of medical licenses.

The Chief Health Officer shall oversee the establishment of public health awareness programs in every district, including education on hygiene, vaccination, and disease prevention.

SANITARY CONDITIONS.

Every person who owns or occupies any premises in the Territory shall maintain the premises in a sanitary condition and shall ensure that no nuisance is caused by the accumulation of waste, stagnant water, or other health hazards.

The District Health Officer shall have the authority to enter any premises within the district to inspect the sanitation conditions and may issue orders to rectify any unsanitary conditions found.

In cases where a person fails to comply with sanitary regulations, the District Health Officer may take action to remove the cause of the nuisance, and the owner or occupier of the premises may be held liable for the costs of such actions.

PUBLIC WATER SUPPLY.

The District Health Officer shall ensure that all public water supplies are properly treated and meet the prescribed standards for drinking water. In cases where a private well or water supply is used, the owner shall ensure the water is free from contamination and shall submit regular samples for testing as required by the regulations.

Failure to comply with water safety regulations may result in penalties, including fines or closure of the private water supply.

PUBLIC HEALTH OFFENSES.

Any person found to be in violation of the public health and sanitation regulations may be subject to fines or imprisonment, depending on the severity of the offense. The District Health Officer shall have the authority to issue citations and enforce health-related laws within the district.

In the event of an outbreak of a contagious disease, the Governor may issue emergency health regulations, including mandatory vaccinations or quarantines, to control the spread of disease.

The Chief Health Officer and District Health Officers shall report quarterly to the Governor on the state of public health and sanitation within their districts, including any significant outbreaks, measures taken, and improvements needed.

""")
        
      transcription05 = Transcription(
        user_id=3, title='Regulations on the Establishment of Schools - Official Gazette',
        text="""ESTABLISHMENT OF SCHOOLS.

The Governor shall establish a Board of Education, which shall be responsible for setting policies and regulations concerning the establishment, operation, and management of schools in the Territory.

Every district shall establish at least one public primary school, and additional schools may be established based on the population size and educational needs of the district. The District Education Officer shall be responsible for overseeing the operation of schools within their district, ensuring that educational standards are maintained.

The curriculum for schools shall be determined by the Board of Education, and schools shall be required to teach the prescribed subjects, which shall include literacy, numeracy, science, and social studies.

All schools shall be required to meet the minimum standards for safety, hygiene, and accessibility as prescribed by the regulations. These standards shall include the provision of clean drinking water, adequate sanitation facilities, and safe classrooms.

TEACHER QUALIFICATIONS AND DUTIES.

All teachers in public schools must hold the required qualifications as set out by the Board of Education. Teachers shall undergo regular professional development training to ensure they are up-to-date with teaching methods and curriculum requirements.

Teachers shall be required to maintain discipline in the classroom and to promote an inclusive learning environment for all students, including those with special educational needs.

Teachers must report to the District Education Officer any students who are not attending school regularly or who are suspected of being involved in criminal activities.

SCHOOL DISCIPLINE.

The Board of Education shall prescribe a code of conduct for students in schools, which shall outline expected behavior, including attendance, dress code, and general conduct.

In cases where a student violates the code of conduct, the school principal may impose disciplinary actions, including warnings, detention, or suspension. Serious offenses may result in expulsion, but such actions may only be taken after a hearing before the School Disciplinary Committee.

It shall be the duty of parents or guardians to ensure that their children attend school regularly and comply with school rules. Failure to do so may result in penalties, including fines.

PRIVATE SCHOOLS.

Private schools may be established in any district subject to approval from the Board of Education. Such schools must meet the same educational and safety standards as public schools and must submit regular reports to the District Education Officer on student enrollment, performance, and financial status.

The Board of Education shall inspect private schools periodically to ensure compliance with regulations. Non-compliant private schools may face penalties, including revocation of their operating license.

SPECIAL EDUCATION.

The Board of Education shall ensure that schools are equipped to provide special education services for students with disabilities or special learning needs. This includes the provision of specialized teachers, accessible learning materials, and necessary accommodations to support these students.

Schools shall also establish a process for identifying students with special educational needs and ensuring they receive appropriate interventions.

""")
        
      transcription06 = Transcription(
        user_id=2, title='Traffic and Road Safety Regulations - Official Gazette',
        text="""TRAFFIC AND ROAD SAFETY.

The Governor shall appoint a Chief Traffic Officer who shall be responsible for overseeing the regulation of traffic and road safety in the Territory. The Chief Traffic Officer shall issue guidelines and regulations to ensure the safe and efficient movement of traffic on public roads.

All vehicles operating within the Territory shall be required to be registered with the Department of Transport and shall display a valid registration plate. Vehicle owners shall be responsible for maintaining their vehicles in safe operating condition, and vehicles that fail to meet safety standards may be impounded.

ROAD USE AND CONDUCT.

Drivers of vehicles must hold a valid driving license issued by the Department of Transport. No person shall drive a vehicle while under the influence of alcohol or drugs, and violators of this regulation shall be subject to arrest and penalties, including fines, suspension of driving privileges, or imprisonment.

It is illegal to exceed the speed limit set for any given road, and violators shall be subject to fines and other penalties. Speed limits shall be clearly marked on all roads, and the Chief Traffic Officer shall ensure that appropriate signage is in place.

Pedestrians must use designated crossings when walking on public roads and shall obey traffic signals. Pedestrians who fail to follow traffic regulations may be subject to fines.

MOTORCYCLE AND BICYCLE SAFETY.

Motorcycle riders shall be required to wear a helmet at all times when operating their vehicle. Motorcyclists who fail to wear helmets may be subject to fines. The Chief Traffic Officer shall ensure that regulations are enforced and that appropriate penalties are levied.

All bicycles operated on public roads shall be required to be equipped with reflectors, lights, and a bell or horn for signaling. Cyclists must wear helmets when riding on highways or roads with high traffic density.

TRAFFIC ACCIDENTS.

In the event of a traffic accident, the driver involved must stop at the scene and exchange necessary information with the other parties involved. Failure to stop after an accident is considered a criminal offense and may result in arrest and penalties.

The driver must also report the accident to the police as soon as possible and cooperate with any investigation. Drivers involved in accidents that result in injury or death must also provide assistance to the injured party.

ROAD INFRASTRUCTURE.

The Department of Transport shall ensure that roads are regularly maintained and repaired to prevent accidents caused by poor road conditions. Road infrastructure improvements, including the installation of traffic lights, road signs, and speed bumps, shall be carried out based on the recommendations of the Chief Traffic Officer.

All road construction projects must adhere to safety standards, and contractors shall be required to implement traffic management plans during construction to ensure minimal disruption to traffic flow.

""")
      transcription07 = Transcription(
        user_id=1, title='Regulations on Waste Management - Official Gazette',
        text="""WASTE MANAGEMENT.

The Governor shall appoint a Waste Management Officer for the Territory, whose duty it shall be to oversee the collection, disposal, and recycling of waste within the Territory. The Waste Management Officer shall work with local authorities to ensure that waste management services are provided efficiently to all residents and businesses.

Every district shall establish a local waste collection service to handle residential and commercial waste. The District Waste Management Officer shall be responsible for ensuring that waste is collected on a regular schedule, and that waste bins are provided to households and businesses.

Residents and businesses shall be required to separate waste into recyclable and non-recyclable categories. Waste that is not properly sorted may be subject to fines.

DUMPING AND LITTERING.

No person shall dump waste or litter in public places, including streets, parks, and open spaces. Violators of this regulation shall be subject to fines and may be required to clean up the area where the littering occurred.

The Waste Management Officer shall conduct regular inspections of public spaces to ensure compliance with anti-littering laws. Public awareness campaigns shall be conducted to educate citizens on the importance of proper waste disposal.

RECYCLING.

It shall be the duty of the Waste Management Officer to promote and facilitate recycling in the Territory. All households and businesses shall be encouraged to recycle items such as paper, plastic, glass, and metals. Separate collection bins for recyclables shall be provided by the local waste management service.

The Waste Management Officer shall also ensure that recycling centers are established within every district to facilitate the collection and processing of recyclable materials.

HAZARDOUS WASTE.

Hazardous waste, including chemicals, medical waste, and electronic waste, shall be disposed of through special channels provided by the Waste Management Officer. No person shall dispose of hazardous waste in regular waste bins or in public spaces.

The Waste Management Officer shall establish facilities for the safe disposal and recycling of hazardous waste, and businesses generating hazardous waste shall be required to obtain special permits for its disposal.

PENALTIES.

Failure to comply with the waste management regulations may result in fines, mandatory community service, or, in cases of repeated violations, imprisonment. The Waste Management Officer shall have the authority to issue citations for violations and may request local law enforcement to enforce penalties.

""")

      transcription08 = Transcription(
        user_id=2, title='Regulations on Agricultural Practices - Official Gazette',
        text="""AGRICULTURAL PRACTICES.

The Governor shall appoint an Agricultural Officer for the Territory, whose duty it shall be to oversee the regulation and promotion of agricultural practices. The Agricultural Officer shall ensure that farmers and agricultural businesses are provided with the resources and support necessary for sustainable farming.

Every district shall establish an Agricultural Development Office, which shall assist local farmers with training, equipment, and access to agricultural markets. The District Agricultural Officer shall work with farmers to improve crop yields and promote environmentally-friendly farming techniques.

CROP PROTECTION.

Farmers shall be required to adhere to prescribed guidelines for the use of pesticides, herbicides, and other chemicals. The Agricultural Officer shall ensure that these chemicals are used safely and in accordance with regulations to prevent harm to the environment and human health.

Farmers must also report any outbreaks of plant diseases or pest infestations to the District Agricultural Officer immediately. The Agricultural Officer shall provide guidance on controlling such outbreaks and may deploy additional resources, including experts and equipment, to assist farmers.

SUSTAINABLE FARMING PRACTICES.

The Agricultural Officer shall promote sustainable farming practices, including crop rotation, organic farming, and the use of environmentally-friendly fertilizers. It shall be the duty of the Agricultural Officer to ensure that farmers are educated on these practices and that they receive support to implement them.

The Agricultural Officer shall also work to promote agroforestry, water conservation, and soil health practices that reduce the environmental impact of farming.

LAND USE AND CONSERVATION.

No person shall convert land to agricultural use without first obtaining approval from the Agricultural Officer, who shall ensure that the land is suitable for farming and that any environmental concerns are addressed. This includes ensuring that the land does not contribute to deforestation, soil erosion, or the destruction of valuable ecosystems.

The Agricultural Officer shall also promote land conservation practices, including the establishment of protected areas and the restoration of degraded lands. Special incentives may be provided to farmers who engage in land restoration or conservation efforts.

ANIMAL HUSBANDRY.

Farmers engaged in animal husbandry shall be required to provide humane conditions for their animals. This includes providing adequate shelter, food, and water, and ensuring that the animals are protected from diseases.

The Agricultural Officer shall be responsible for regulating the health and welfare of livestock and shall oversee vaccination programs to protect animals from contagious diseases.

PENALTIES.

Failure to comply with agricultural regulations, including those related to pesticide use, land conservation, and animal welfare, may result in fines, suspension of agricultural licenses, or other penalties. The Agricultural Officer shall have the authority to issue citations and may request the assistance of local authorities to enforce these regulations.

""")

      transcription09 = Transcription(
        user_id=3, title='Building and Construction Regulations - Official Gazette',
        text="""BUILDING AND CONSTRUCTION.

The Governor shall appoint a Chief Building Officer for the Territory, whose duty it shall be to oversee the regulation and inspection of building and construction activities. The Chief Building Officer shall ensure that all buildings and structures are constructed in compliance with safety standards and regulations.

Every district shall establish a Building Inspection Office, which shall be responsible for inspecting construction sites and approving building plans. The District Building Officer shall work with developers, architects, and contractors to ensure that construction projects adhere to the regulations.

CONSTRUCTION PERMITS.

No person shall begin any construction project without first obtaining a building permit from the District Building Officer. The permit application shall include detailed plans for the construction, including the design, materials, and structural integrity of the building.

The District Building Officer shall review the plans and may approve or deny the permit based on compliance with safety standards and zoning regulations. The permit shall be valid for a period of one year from the date of issue, and construction must commence within that period.

INSPECTIONS.

The District Building Officer shall conduct regular inspections during the construction process to ensure compliance with approved plans and safety standards. Inspections shall occur at various stages of construction, including foundation, framing, and final inspection.

Construction projects that fail to meet safety standards or deviate from approved plans may be halted, and the builder may be required to make corrections or face fines.

BUILDING MATERIALS.

All materials used in construction shall meet the standards set by the Chief Building Officer. The use of substandard or unsafe materials is prohibited. Contractors and builders must ensure that all materials used in construction are safe, durable, and compliant with building codes.

The Chief Building Officer may conduct random tests of construction materials to ensure compliance with safety standards. Non-compliant builders may be subject to penalties or forced to replace unsafe materials.

FIRE SAFETY.

All buildings shall be required to adhere to fire safety standards, including the installation of fire exits, fire extinguishers, and smoke detectors. The District Building Officer shall ensure that these fire safety measures are implemented during the construction of new buildings and renovations.

The Chief Building Officer shall also ensure that fire drills and safety training programs are conducted for employees working in large buildings or industrial sites.

PENALTIES.

Failure to comply with building and construction regulations may result in fines, suspension of construction permits, or even demolition of illegal structures. The District Building Officer shall have the authority to issue citations and enforce penalties for non-compliance.

""")
      transcription10 = Transcription(
        user_id=1, title='Health and Safety Regulations for Workers - Official Gazette',
        text="""HEALTH AND SAFETY IN THE WORKPLACE.

The Governor shall appoint a Chief Occupational Health and Safety Officer to oversee the regulation of workplace health and safety standards throughout the Territory. The Chief Occupational Health and Safety Officer shall issue guidelines and regulations to ensure that all employers maintain safe working conditions for their employees.

Every employer shall be required to provide a safe working environment, free from hazards that could cause injury or illness. Employers shall ensure that all workplaces are properly ventilated, that workers have access to clean drinking water, and that there are adequate sanitation facilities.

RISK ASSESSMENTS AND SAFETY PLANS.

All employers shall conduct regular risk assessments to identify potential hazards in the workplace. Based on the results of the assessment, employers must implement a comprehensive safety plan to mitigate these risks. The safety plan should include specific procedures for addressing workplace accidents, handling hazardous materials, and ensuring emergency evacuation.

Employees shall be trained on safety procedures and emergency protocols, and shall have access to appropriate protective equipment, such as helmets, gloves, safety goggles, and other necessary items.

EMPLOYEE RIGHTS AND REPORTING.

Every employee has the right to report unsafe working conditions without fear of retaliation. Employees may report concerns directly to the District Occupational Health and Safety Officer, who shall investigate the matter and take appropriate action.

Employers are prohibited from dismissing, penalizing, or discriminating against employees who raise health and safety concerns. Any retaliation against an employee who reports unsafe working conditions is a violation of the law and may result in legal action.

HAZARDOUS MATERIALS.

Employers who handle hazardous materials, including chemicals, gases, or toxic substances, must implement strict protocols for their storage, handling, and disposal. Material Safety Data Sheets (MSDS) must be made available to all employees working with hazardous substances.

The Chief Occupational Health and Safety Officer shall oversee the establishment of safety protocols for the handling of hazardous materials, and regular inspections shall be conducted to ensure compliance with safety regulations.

PENALTIES FOR NON-COMPLIANCE.

Failure to comply with health and safety regulations may result in fines, temporary closure of the business, or even imprisonment for employers in cases of gross negligence. The District Occupational Health and Safety Officer shall have the authority to issue citations and enforce penalties for non-compliance.

""")

      transcription11 = Transcription(
        user_id=2, title='Environmental Protection and Conservation Regulations - Official Gazette',
        text="""ENVIRONMENTAL PROTECTION.

The Governor shall appoint an Environmental Protection Officer to oversee the regulation and enforcement of environmental protection laws. The Environmental Protection Officer shall ensure that all businesses, industries, and individuals comply with laws related to pollution control, wildlife conservation, and sustainable resource use.

Every district shall establish an Environmental Conservation Unit, which shall assist in monitoring pollution levels, protecting wildlife habitats, and ensuring compliance with environmental standards.

POLLUTION CONTROL.

All businesses and industrial activities shall be required to implement pollution control measures to prevent air, water, and soil pollution. Businesses shall submit regular environmental impact assessments to the Environmental Protection Officer and take corrective actions if pollution levels exceed prescribed limits.

The use of certain harmful chemicals, including pesticides and industrial waste, is restricted, and businesses are encouraged to adopt environmentally-friendly technologies and practices.

CONSERVATION OF NATURAL RESOURCES.

The Environmental Protection Officer shall ensure that natural resources, including forests, water bodies, and mineral resources, are conserved and used sustainably. The destruction of forests or other natural habitats without proper authorization is prohibited.

Farmers and businesses involved in resource extraction, including mining, shall be required to submit plans for sustainable resource use and ensure that their activities do not lead to long-term environmental damage.

WILDLIFE PROTECTION.

It shall be unlawful to harm or hunt protected wildlife species. The Environmental Protection Officer shall maintain a list of protected species and enforce laws designed to protect these animals and their habitats.

All wildlife trade, including the sale or purchase of endangered species or their parts, is prohibited. Violators of wildlife protection laws shall face fines, imprisonment, or both.

ENVIRONMENTAL EDUCATION AND AWARENESS.

The Environmental Protection Officer shall ensure that public education programs are established to raise awareness about environmental issues. Schools, businesses, and community organizations shall be encouraged to participate in environmental conservation activities, such as tree planting, waste reduction, and clean-up campaigns.

PENALTIES FOR ENVIRONMENTAL VIOLATIONS.

Any individual or business found guilty of violating environmental protection regulations may face significant fines, the revocation of permits or licenses, or legal action. The Environmental Protection Officer has the authority to issue penalties for non-compliance and may seek the assistance of local authorities to enforce regulations.

""")

      transcription12 = Transcription(
        user_id=3, title='Regulations on Public Transportation - Official Gazette',
        text="""PUBLIC TRANSPORTATION REGULATIONS.

The Governor shall appoint a Chief Transport Officer to oversee the regulation and operation of public transportation services within the Territory. The Chief Transport Officer shall ensure that public transportation systems are safe, efficient, and accessible to all residents.

Every district shall establish a public transportation system, which shall include buses, taxis, and other forms of transportation. The District Transport Officer shall be responsible for coordinating the operation of the public transport system and ensuring that all vehicles meet the required safety standards.

VEHICLE SAFETY AND INSPECTIONS.

All vehicles used for public transportation shall be required to undergo regular safety inspections to ensure that they are in good working condition. The Chief Transport Officer shall establish safety standards for public transportation vehicles, which shall include requirements for seat belts, fire extinguishers, and first-aid kits.

Public transportation vehicles that fail to meet safety standards shall be prohibited from operating until the necessary repairs are made and the vehicle passes a re-inspection.

LICENSES AND OPERATING PERMITS.

All operators of public transportation services must obtain a license from the Department of Transport. Operators must submit an application, including details about the vehicles, routes, and fares, and undergo a background check before being issued a permit.

The Chief Transport Officer shall ensure that public transportation operators comply with all regulations and maintain proper records of their operations. Operators who fail to comply with regulations may have their licenses revoked or suspended.

ACCESSIBILITY FOR PEOPLE WITH DISABILITIES.

Public transportation services shall be required to be accessible to people with disabilities. This includes providing vehicles that are equipped with ramps or lifts for wheelchair users, as well as ensuring that transportation stations are accessible to people with mobility impairments.

The Chief Transport Officer shall work with operators to ensure that these accessibility requirements are met and that all transportation services are inclusive.

FARES AND TARIFFS.

The Chief Transport Officer shall establish guidelines for the setting of fares for public transportation. Fares must be reasonable and transparent, and operators must provide clear information about fare schedules and payment methods.

Public transportation operators are prohibited from charging discriminatory or excessive fares, and any violations of fare regulations may result in fines or sanctions.

PENALTIES FOR NON-COMPLIANCE.

Public transportation operators who fail to comply with safety standards, licensing requirements, or accessibility regulations may face fines, suspension of operating permits, or legal action. The Chief Transport Officer shall have the authority to issue citations and enforce penalties for non-compliance.

""")

      transcription13 = Transcription(
        user_id=1, title='Regulations on Food Safety and Standards - Official Gazette',
        text="""FOOD SAFETY.

The Governor shall appoint a Chief Food Safety Officer for the Territory, whose duty it shall be to ensure that all food products are safe for consumption and meet established safety standards. The Chief Food Safety Officer shall enforce food safety regulations, including the inspection of food production facilities and the testing of food products.

All food businesses, including restaurants, markets, and manufacturers, shall be required to maintain clean facilities and ensure that all food products are stored, prepared, and handled in a sanitary manner.

FOOD LABELING.

It is mandatory for food products to be labeled with clear and accurate information, including ingredients, nutritional content, expiry dates, and any potential allergens. The Chief Food Safety Officer shall ensure that food labeling regulations are strictly enforced to protect consumers from misleading or harmful information.

INSPECTIONS AND COMPLIANCE.

The Chief Food Safety Officer shall conduct regular inspections of food businesses, including production facilities, restaurants, and retail markets, to ensure compliance with food safety standards. Non-compliant businesses may be fined, ordered to cease operations, or face the revocation of their licenses.

FOOD RECALLS.

In the event that a food product is found to be unsafe or contaminated, the Chief Food Safety Officer shall issue a recall order. Businesses must immediately remove affected products from sale and notify consumers of the recall.

PENALTIES.

Failure to comply with food safety regulations may result in fines, suspension of operating permits, or legal action. The Chief Food Safety Officer has the authority to issue citations for violations and enforce penalties.

""")

      transcription14 = Transcription(
        user_id=2, title='Regulations on Forest Conservation - Official Gazette',
        text="""FOREST CONSERVATION.

The Governor shall appoint a Chief Forest Officer responsible for overseeing the management and conservation of forests within the Territory. The Chief Forest Officer shall ensure that forests are protected from deforestation, over-exploitation, and environmental degradation.

Every district shall establish a Forestry Conservation Unit, which shall monitor the condition of local forests and implement reforestation and conservation projects. The Chief Forest Officer shall also coordinate with local authorities to prevent illegal logging and poaching.

SUSTAINABLE FOREST MANAGEMENT.

It is the duty of the Chief Forest Officer to promote sustainable forest management practices that balance the need for timber, fuelwood, and other resources with the need to preserve forest ecosystems. This includes ensuring that logging activities are regulated, and that forests are replenished through reforestation programs.

COMMUNITY PARTICIPATION.

Local communities shall be encouraged to participate in forest conservation efforts, including tree planting initiatives, fire prevention programs, and sustainable agricultural practices that minimize deforestation.

PENALTIES FOR ILLEGAL LOGGING.

Illegal logging is prohibited in all forests within the Territory. Offenders shall face heavy fines, confiscation of equipment, and possible imprisonment. The Chief Forest Officer, along with local authorities, shall enforce laws against illegal logging.

PENALTIES.

Failure to comply with forest conservation regulations may result in fines, the suspension of forestry permits, or legal action. The Chief Forest Officer shall have the authority to issue citations and enforce penalties.

""")

      transcription15 = Transcription(
        user_id=3, title='Regulations on Water Conservation - Official Gazette',
        text="""WATER CONSERVATION.

The Governor shall appoint a Chief Water Conservation Officer responsible for ensuring that water resources within the Territory are used sustainably and efficiently. The Chief Water Conservation Officer shall implement regulations to prevent the overuse and wastage of water, especially during periods of drought.

Every district shall establish a Water Conservation Unit, which shall promote water-saving technologies, monitor water usage, and enforce water conservation measures. The District Water Conservation Officer shall educate the public on the importance of water conservation.

WATER USAGE RESTRICTIONS.

During periods of drought or water shortage, the Chief Water Conservation Officer may issue water usage restrictions, including limitations on outdoor watering, industrial water usage, and irrigation. Violators of these restrictions may be fined or penalized.

RAINWATER HARVESTING.

The Chief Water Conservation Officer shall encourage the use of rainwater harvesting systems in both residential and commercial buildings. Local authorities may provide incentives for the installation of rainwater harvesting systems, such as subsidies for equipment or tax breaks.

PENALTIES FOR NON-COMPLIANCE.

Failure to comply with water conservation regulations, including excessive water usage during droughts or the failure to install water-saving systems, may result in fines or penalties. The Chief Water Conservation Officer has the authority to issue citations and enforce water conservation laws.

""")

      transcription16 = Transcription(
        user_id=1, title='Regulations on Building Energy Efficiency - Official Gazette',
        text="""ENERGY EFFICIENCY IN BUILDINGS.

The Governor shall appoint a Chief Energy Efficiency Officer who shall oversee the regulation of energy consumption in buildings. The Chief Energy Efficiency Officer shall ensure that all new buildings and major renovations comply with energy-efficient standards to reduce the carbon footprint and promote sustainable energy use.

BUILDING DESIGN REQUIREMENTS.

All new buildings must be designed and constructed to meet minimum energy efficiency standards, including the use of insulation, energy-efficient windows, and heating/cooling systems. The Chief Energy Efficiency Officer shall issue guidelines for the design and construction of energy-efficient buildings.

RENEWABLE ENERGY.

The Chief Energy Efficiency Officer shall promote the use of renewable energy sources, including solar and wind power, in buildings. All new buildings shall be required to install renewable energy systems, such as solar panels or wind turbines, where feasible.

ENERGY AUDITS AND INSPECTIONS.

The Chief Energy Efficiency Officer shall conduct regular energy audits of buildings to ensure compliance with energy efficiency standards. Building owners may be required to implement recommended upgrades to improve energy efficiency.

PENALTIES FOR NON-COMPLIANCE.

Failure to comply with energy efficiency regulations may result in fines, the suspension of operating permits, or mandatory upgrades to meet energy-saving standards.

""")

      transcription17 = Transcription(
        user_id=2, title='Regulations on Air Quality Standards - Official Gazette',
        text="""AIR QUALITY STANDARDS.

The Governor shall appoint a Chief Air Quality Officer who shall be responsible for monitoring and regulating air quality within the Territory. The Chief Air Quality Officer shall set air quality standards and ensure that industries, businesses, and individuals comply with regulations to reduce air pollution.

INDUSTRIAL EMISSIONS.

All industries and businesses that emit pollutants into the air shall be required to obtain an emissions permit from the Department of Environmental Protection. The Chief Air Quality Officer shall enforce emissions limits and ensure that businesses install pollution control technologies to reduce harmful emissions.

VEHICLE EMISSIONS.

All vehicles operating within the Territory shall be required to undergo regular emissions testing to ensure that they meet established air quality standards. The Chief Air Quality Officer shall coordinate with the Department of Transport to ensure that vehicles are properly maintained and emissions are within acceptable limits.

AIR QUALITY MONITORING.

The Chief Air Quality Officer shall oversee the installation of air quality monitoring stations throughout the Territory to assess the levels of pollutants in the air. Regular air quality reports shall be published to inform the public and guide policy decisions.

PENALTIES FOR NON-COMPLIANCE.

Failure to comply with air quality regulations may result in fines, suspension of operating permits, or legal action. The Chief Air Quality Officer shall have the authority to issue citations and enforce penalties.

""")

      transcription18 = Transcription(
        user_id=3, title='Regulations on Coastal Zone Management - Official Gazette',
        text="""COASTAL ZONE MANAGEMENT.

The Governor shall appoint a Chief Coastal Zone Officer to oversee the protection and sustainable development of coastal areas within the Territory. The Chief Coastal Zone Officer shall work to prevent environmental degradation and ensure the sustainable use of coastal resources.

DEVELOPMENT IN COASTAL AREAS.

No person shall engage in development activities in coastal areas without first obtaining approval from the Chief Coastal Zone Officer. Development projects must adhere to environmental standards and ensure that they do not harm marine life, disrupt coastal ecosystems, or lead to erosion.

MARINE CONSERVATION.

The Chief Coastal Zone Officer shall work with local authorities to protect marine ecosystems, including coral reefs, mangroves, and marine reserves. Fishing practices that harm these ecosystems, such as overfishing or the use of destructive fishing methods, are prohibited.

COASTAL EROSION AND FLOODING.

The Chief Coastal Zone Officer shall implement measures to prevent coastal erosion and flooding, including the restoration of wetlands, the planting of mangrove trees, and the construction of protective barriers. Coastal development shall be regulated to minimize environmental impact.

PENALTIES FOR NON-COMPLIANCE.

Failure to comply with coastal zone management regulations may result in fines, suspension of permits, or legal action. The Chief Coastal Zone Officer shall have the authority to issue citations and enforce penalties.

""")

      transcription19 = Transcription(
        user_id=1, title='Regulations on Noise Pollution Control - Official Gazette',
        text="""NOISE POLLUTION CONTROL.

The Governor shall appoint a Chief Noise Control Officer to regulate and control noise pollution within the Territory. The Chief Noise Control Officer shall ensure that noise levels in residential, commercial, and industrial areas remain within acceptable limits to protect public health and well-being.

NOISE LIMITS.

The Chief Noise Control Officer shall set acceptable noise limits for various zones within the Territory, including residential, industrial, and commercial areas. Noise limits shall be based on time of day and the type of activity generating the noise.

NOISE MONITORING AND INSPECTIONS.

The Chief Noise Control Officer shall oversee regular noise monitoring in urban and industrial areas. Inspections may be conducted at businesses, construction sites, and other locations where excessive noise is generated.

COMPLAINTS AND REMEDIES.

Residents or businesses affected by excessive noise may file complaints with the Chief Noise Control Officer. If noise levels exceed established limits, the Chief Noise Control Officer shall take corrective action, which may include issuing fines or ordering noise reduction measures.

PENALTIES FOR NON-COMPLIANCE.

Failure to comply with noise pollution control regulations may result in fines, the suspension of operating permits, or legal action. The Chief Noise Control Officer has the authority to issue citations and enforce penalties.

""")

      transcription20 = Transcription(
        user_id=2, title='Regulations on Wastewater Treatment - Official Gazette',
        text="""WASTEWATER TREATMENT.

The Governor shall appoint a Chief Wastewater Treatment Officer to oversee the regulation of wastewater treatment within the Territory. The Chief Wastewater Treatment Officer shall ensure that wastewater is treated in accordance with environmental standards before being released into water bodies.

WASTEWATER DISPOSAL.

All businesses and industries that discharge wastewater into public sewer systems or directly into water bodies shall be required to install appropriate wastewater treatment systems. The Chief Wastewater Treatment Officer shall monitor and inspect wastewater treatment facilities to ensure compliance with treatment standards.

DOMESTIC WASTEWATER.

Households shall be required to install and maintain septic tanks or connect to municipal sewer systems for the disposal of wastewater. The Chief Wastewater Treatment Officer shall ensure that domestic wastewater is treated and disposed of in an environmentally safe manner.

POLLUTION MONITORING.

The Chief Wastewater Treatment Officer shall oversee the monitoring of water bodies to ensure that wastewater discharge does not harm water quality. Regular water quality reports shall be published to inform the public and guide policy decisions.

PENALTIES FOR NON-COMPLIANCE.

Failure to comply with wastewater treatment regulations may result in fines, suspension of operating permits, or legal action. The Chief Wastewater Treatment Officer has the authority to issue citations and enforce penalties.

""")
        

      db.session.add(transcription01)
      db.session.add(transcription02)
      db.session.add(transcription03)
      db.session.add(transcription04)
      db.session.add(transcription05)
      db.session.add(transcription06)
      db.session.add(transcription07)
      db.session.add(transcription08)
      db.session.add(transcription09)
      db.session.add(transcription10)
      db.session.add(transcription11)
      db.session.add(transcription12)
      db.session.add(transcription13)
      db.session.add(transcription14)
      db.session.add(transcription15)
      db.session.add(transcription16)
      db.session.add(transcription17)
      db.session.add(transcription18)
      db.session.add(transcription19)
      db.session.add(transcription20)
      db.session.commit()



def undo_transcriptions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.transcriptions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM transcriptions"))
        
    db.session.commit()