import re

# Class for a Course
class Course:
    def __init__(self, SUBJECT, CODE, NAME = None):
        self.SUBJECT = SUBJECT
        self.CODE = CODE
        self.NAME = NAME
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return '{} {}'.format(self.SUBJECT, self.CODE)
        #return '{} {}: {}'.format(self.SUBJECT, self.CODE, self.NAME)
        

# Course Subjects List
CourseSubjects = [['AAS', 'Asian American Studies'],
 ['ABUS', 'Applied Business'],
 ['ACCT', 'Accounting'],
 ['ACL', 'Arts and Cultural Leadership'],
 ['ADDS', 'Addiction Studies'],
 ['ADES', 'Apparel Design'],
 ['ADPY', 'Adult Psychiatry'],
 ['AECM', 'Ag Educ, Comm & Mktg'],
 ['AEM', 'Aerospace Engineering and Mech'],
 ['AFEE', 'Agri, Food, and Environ Educ'],
 ['AFRO', 'African Amer & African Studies'],
 ['AGRO', 'Agronomy and Plant Genetics'],
 ['AHS', 'Academic Health Center Shared'],
 ['AIR', 'Aerospace Studies'],
 ['AKKA', 'Akkadian'],
 ['ALL', 'Asian Languages and Literature'],
 ['AMES', 'Asian & Middle Eastern Studies'],
 ['AMIN', 'American Indian Studies'],
 ['AMST', 'American Studies'],
 ['ANAT', 'Anatomy'],
 ['ANES', 'Anesthesiology'],
 ['ANSC', 'Animal Science'],
 ['ANTH', 'Anthropology'],
 ['APEC', 'Applied Economics'],
 ['APS', 'Applied Professional Studies'],
 ['APSC', 'Applied Plant Sciences'],
 ['APST', 'Apparel Studies'],
 ['ARAB', 'Arabic'],
 ['ARCH', 'Architecture'],
 ['ARGN', 'Study Abroad in Argentina'],
 ['ARTH', 'Art History'],
 ['ARTS', 'Art'],
 ['ASL', 'American Sign Language'],
 ['AST', 'Astronomy'],
 ['BA', 'Business Administration'],
 ['BBE', 'Bioproducts and Biosystems Eng'],
 ['BIOC', 'Biochemistry'],
 ['BIOL', 'Biology'],
 ['BLAW', 'Business Law'],
 ['BMEN', 'Biomedical Engineering'],
 ['BSE', 'Biology, Society, and Environ'],
 ['BTHX', 'Bioethics, Center for'],
 ['CAPY', 'Child & Adolescent Psychiatry'],
 ['CDED', 'Continuing Dental Education'],
 ['CEGE', 'Civil, Environ, and Geo-Engin'],
 ['CESP', 'Commun Engage Scholars Program'],
 ['CFAN', 'Col of Food, Agr & Nat Res Sci'],
 ['CGSC', 'Cognitive Science'],
 ['CHEM', 'Chemistry'],
 ['CHEN', 'Chemical Engineering'],
 ['CHIC', 'Chicano Studies'],
 ['CHMB', 'China Executive MBA'],
 ['CHN', 'Chinese'],
 ['CHPH', 'Chemical Physics'],
 ['CI', 'Curriculum and Instruction'],
 ['CL', 'Comparative Literature'],
 ['CLA', 'College of Liberal Arts'],
 ['CMB', 'Comparative & Molecular Biosci'],
 ['CMBA', 'Carlson Executive MBA'],
 ['CMGT', 'Construction Management'],
 ['CNES', 'Classical and Near Eastern Std'],
 ['COMM', 'Communication Studies'],
 ['CONS', 'Conservation Sciences'],
 ['COP', 'Cellular/Organismal Physiology'],
 ['CPSY', 'Child Psychology'],
 ['CSCI', 'Computer Science'],
 ['CSCL', 'Cultural Stdy/Comparative Lit'],
 ['CSDS', 'Compar Study in Discourse/Soc'],
 ['CSE', 'Coll of Science, Engineering'],
 ['CSOM', 'Carlson School of Management'],
 ['CSPH', 'Ctr for Spirituality/Healing'],
 ['CVM', 'Veterinary Medicine'],
 ['DAKO', 'Dakota'],
 ['DDS', 'Doctor of Dental Surgery'],
 ['DENT', 'Dentistry'],
 ['DERM', 'Dermatology'],
 ['DES', 'Design'],
 ['DH', 'Dental Hygiene'],
 ['DNCE', 'Dance'],
 ['DSCI', 'Data Science'],
 ['DSSC', 'Develpmt Std and Soc Change'],
 ['DT', 'Dental Therapy'],
 ['DTCH', 'Dutch'],
 ['EAS', 'East Asian Studies'],
 ['ECON', 'Economics'],
 ['ECP', 'Experimental and Clinical Phar'],
 ['EDHD', 'Educational/Human Development'],
 ['EDUC', 'Education'],
 ['EE', 'Electrical & Computer Eng'],
 ['EEB', 'Ecology, Evolution, and Behav'],
 ['EMMD', 'Emergency Medicine'],
 ['EMS', 'Early Modern Studies'],
 ['ENDO', 'Endodontics'],
 ['ENGL', 'English:  Literature'],
 ['ENGW', 'English: Creative Writing'],
 ['ENT', 'Entomology'],
 ['ENTR', 'Entrepreneurship'],
 ['EPSY', 'Educational Psychology'],
 ['ESCI', 'Earth Sciences'],
 ['ESL', 'English as a Second Language'],
 ['ESPM', 'Environment Sci, Policy, Mgmt'],
 ['FDSY', 'Food Systems'],
 ['FIN', 'Finnish'],
 ['FINA', 'Finance'],
 ['FM', 'Financial Mathematics'],
 ['FMCH', 'Family Med & Community Health'],
 ['FNRM', 'Forest and Natural Res. Mgmt.'],
 ['FOST', 'Foreign Study'],
 ['FREN', 'French'],
 ['FRIT', 'French and Italian'],
 ['FSCN', 'Food Science and Nutrition'],
 ['FSOS', 'Family Social Science'],
 ['FW', 'Fisheries and Wildlife'],
 ['GCC', 'Grand Challenge Curriculum'],
 ['GCD', 'Genetics, Cell Biol/Developmnt'],
 ['GDBA', 'Global Doctorate of Business'],
 ['GDES', 'Graphic Design'],
 ['GEND', 'General Dentistry'],
 ['GEOG', 'Geography'],
 ['GER', 'German'],
 ['GERI', 'Geriatrics'],
 ['GERO', 'Gerontology'],
 ['GIS', 'Geographic Information Science'],
 ['GLBT', 'Gay, Lesbian, Bisexual, Transg'],
 ['GLOS', 'Global Studies'],
 ['GRAD', 'Graduate School'],
 ['GRK', 'Greek'],
 ['GSD', 'German,Scandinavian, and Dutch'],
 ['GWSS', 'Gender, Women, & Sexuality Std'],
 ['HCOL', 'Honors Colloquia'],
 ['HEBR', 'Hebrew'],
 ['HECU', 'Higher Ed Consortium Urban Aff'],
 ['HINF', 'Health Informatics'],
 ['HIST', 'History'],
 ['HMED', 'History of Medicine'],
 ['HMNG', 'Hmong'],
 ['HNDI', 'Hindi'],
 ['HORT', 'Horticultural Science'],
 ['HRIR', 'Human Resources/Indus Rel'],
 ['HSCI', 'History of Science and Tech'],
 ['HSEM', 'Honors Seminar'],
 ['HSEX', 'Human Sexuality'],
 ['HSG', 'Housing Studies'],
 ['HSM', 'Health Services Management'],
 ['HSPH', 'Heritage Studies & Public Hist'],
 ['HUMF', 'Human Factors'],
 ['IBH', 'Integrated Behavioral Health'],
 ['IBUS', 'International Business'],
 ['ICP', 'Inter-College Program'],
 ['ID', 'Interdepartmental Study'],
 ['IDES', 'Interior Design'],
 ['IDSC', 'Information and Decision Sci'],
 ['IE', 'Industrial Engineering'],
 ['IFSL', 'Integrated Food Systems Ldrshp'],
 ['INAR', 'Interdisciplinary Archaeologic'],
 ['INET', 'Information Networking'],
 ['INMD', 'Interdisciplinary Medicine'],
 ['INS', 'Insurance and Risk Management'],
 ['IREL', 'Interprsnl Relations Research'],
 ['ISG', 'Introduced Species, Genotypes'],
 ['ITAL', 'Italian'],
 ['JOUR', 'Journalism & Mass Communicat'],
 ['JPN', 'Japanese'],
 ['JWST', 'Jewish Studies'],
 ['KIN', 'Kinesiology'],
 ['KOR', 'Korean'],
 ['LA', 'Landscape Architecture'],
 ['LAAS', 'Land and Atmospheric Science'],
 ['LAMP', 'Laboratory Medicine and Path'],
 ['LANG', 'Language Centr CLA Courseshare'],
 ['LAS', 'Latin American Studies'],
 ['LASK', 'Learning and Academic Skills'],
 ['LAT', 'Latin'],
 ['LAW', 'Law School'],
 ['LEAD', 'Leadership Education'],
 ['LING', 'Linguistics'],
 ['LS', 'Liberal Studies'],
 ['MATH', 'Mathematics'],
 ['MATS', 'Materials Science'],
 ['MBA', 'Master of Business Admin'],
 ['MBS', 'Master of Biological Sciences'],
 ['MBT', 'Master of Business Taxation'],
 ['MCDG', 'Mol Cell Devlpmental Biol/Gene'],
 ['MCOM', 'Managerial Communications'],
 ['MDI', 'Medical Device Innovation'],
 ['MDP', 'Master of Development Practice'],
 ['MDS', 'Multidisciplinary Studies'],
 ['ME', 'Mechanical Engineering'],
 ['MED', 'Medicine'],
 ['MEDC', 'Medicinal Chemistry'],
 ['MEST', 'Medieval Studies'],
 ['MGMT', 'Management'],
 ['MICA', 'Microbiol/Immun/Cancer Biology'],
 ['MICB', 'Microbiology'],
 ['MICE', 'Microbial Engineering'],
 ['MIL', 'Military Science'],
 ['MILI', 'Medical Industry Leadrshp Inst'],
 ['MIMS', 'Moving Image Studies'],
 ['MKTG', 'Marketing'],
 ['MLSP', 'Medical Laboratory Sciences Pr'],
 ['MM', 'Manufacturing Operations Mgmt'],
 ['MORT', 'Mortuary Science'],
 ['MOT', 'Management of Technology'],
 ['MPHY', 'Medical Physics'],
 ['MSBA', 'Masters of Business Analytics'],
 ['MSF', 'Master of Science in Finance'],
 ['MST', 'Museum Studies'],
 ['MTHE', 'Mathematics Education'],
 ['MUED', 'Music Education'],
 ['MULT', 'Multi-Inst Cross Registration'],
 ['MUS', 'Music'],
 ['MUSA', 'Music Applied'],
 ['NAV', 'Naval Science'],
 ['NEUR', 'Neurology'],
 ['NOR', 'Norwegian'],
 ['NPSE', 'Nanoparticle Science and Eng'],
 ['NR', 'Natural Resources Sci and Mgmt'],
 ['NSC', 'Neuroscience'],
 ['NSCI', 'Neuroscience Department'],
 ['NSU', 'Neurosurgery'],
 ['NURS', 'Nursing'],
 ['NUTR', 'Nutrition'],
 ['OBIO', 'Oral Biology'],
 ['OBST', 'Obstetrics and Gynecology'],
 ['OCS', 'Off-Campus Study'],
 ['OJIB', 'Ojibwe'],
 ['OLPD', 'Org Leadership, Policy & Dev'],
 ['OPH', 'Ophthalmology'],
 ['ORSU', 'Orthopaedic Surgery'],
 ['OSUR', 'Oral and Maxillofacial Surgery'],
 ['OT', 'Occupational Therapy'],
 ['OTHO', 'Orthodontics'],
 ['OTOL', 'Otolaryngology'],
 ['OUE', 'Office of Undergrad Education'],
 ['PA', 'Public Affairs'],
 ['PATH', 'Pathology'],
 ['PDEN', 'Pediatric Dentistry'],
 ['PDES', 'Product Design'],
 ['PE', 'Physical Education'],
 ['PED', 'Pediatrics'],
 ['PERO', 'Periodontics'],
 ['PHAR', 'Pharmacy'],
 ['PHCL', 'Pharmacology'],
 ['PHIL', 'Philosophy'],
 ['PHM', 'Pharmaceutics'],
 ['PHSL', 'Physiology'],
 ['PHYS', 'Physics'],
 ['PLPA', 'Plant Pathology'],
 ['PLSC', 'Plant Science'],
 ['PMB', 'Plant and Microbial Biology'],
 ['PMED', 'Physical Med & Rehabilitation'],
 ['POL', 'Political Science'],
 ['PORT', 'Portuguese'],
 ['PREV', 'Preventive Science Minor'],
 ['PROS', 'Prosthodontics'],
 ['PSTL', 'Postsecondary Tchg and Lrng'],
 ['PSY', 'Psychology'],
 ['PT', 'Physical Therapy'],
 ['PUBH', 'Public Health'],
 ['RAD', 'Radiology'],
 ['REC', 'Rec, Park, and Leisure Studies'],
 ['RELS', 'Religious Studies'],
 ['RM', 'Retail Merchandising'],
 ['RSC', 'Rehabilitation Science'],
 ['RUSS', 'Russian'],
 ['SACP', 'Social, Adm, and Clinical Phar'],
 ['SAGR', 'Sustainable Agricultural Syst'],
 ['SAPH', 'Social/Administrative Pharmacy'],
 ['SCAN', 'Scandinavian'],
 ['SCB', 'Stem Cell Biology'],
 ['SCIC', 'Scientific Computation'],
 ['SCMC', 'Studies in Cinema Media Cultur'],
 ['SCO', 'Supply Chain and Operations'],
 ['SENG', 'Software Engineering'],
 ['SLHS', 'Speech-Language-Hearing Sci'],
 ['SMGT', 'Sport Management'],
 ['SMLI', 'Somali'],
 ['SOC', 'Sociology'],
 ['SOIL', 'Soil, Water, and Climate'],
 ['SPAN', 'Spanish'],
 ['SPPT', 'Spanish and Portuguese'],
 ['SSM', 'Sustainable Systems Management'],
 ['SST', 'Studies of Science and Tech'],
 ['ST', 'Security Technologies'],
 ['STAT', 'Statistics'],
 ['SURG', 'Surgery'],
 ['SUST', 'Sustainability Studies'],
 ['SW', 'Social Work'],
 ['SWAH', 'Swahili'],
 ['SWED', 'Swedish'],
 ['TH', 'Theatre Arts'],
 ['TMDP', 'TMD & Orofacial Pain'],
 ['TRAD', 'Therapeutic Radiology'],
 ['TRIN', 'Translation and Interpreting'],
 ['TXCL', 'Toxicology'],
 ['UC', 'University College'],
 ['URBS', 'Urban Studies'],
 ['URDU', 'Urdu'],
 ['UROL', 'Urologic Surgery'],
 ['VBS', 'Veterinary & Biomedical Sci'],
 ['VCS', 'Veterinary Clinical Sciences'],
 ['VMBA', 'Vienna Executive MBA'],
 ['VMED', 'Veterinary Medicine, Graduate'],
 ['VPM', 'Veterinary Population Medicine'],
 ['WRIT', 'Writing Studies'],
 ['WRS', 'Water Resources Science'],
 ['YOST', 'Youth Development and Research']]        

#Catalog = [Course('MUS', 3603, 'History of Western Music III'),
#            Course('MATH', 2283, 'Sequences, Series, and Foundations'),
#            Course('LAT', 5200, 'Advanced Reading in Later Latin')]

#Cleaning Function (takes string to Course Object)
def clean(course):
    if isinstance(course, str):
        course = course.upper().replace(' ','').rstrip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*`~,./;<>?:-=_+')
    
    n = 0
    while not course[n:].isnumeric():
        n+=1
    
#Searches Subject List
    if course[:n] in [x[0] for x in CourseSubjects]:
        SUBJECT = course[:n]
    else:
        print('Subject Not Found')
        raise ValueError()
        return False
    
#Checks for 4 digit class code    
    if len(course[n:]) == 4:
        CODE = course[n:]
    else:
        print('Number Not Found')
        raise ValueError()
        return False
    
    return Course(SUBJECT,CODE)
	
def clean_str(course):
    try:
        c = clean(course).__str__()
    except ValueError:
        c = "INVALID"
    finally:
        return c
		

#Class for request space
class SearchSpace:
    def __init__(self):
        self.requests = {}
        
    def add_request(self, USER, COURSE):
        if COURSE:
            if str(COURSE) not in self.requests.keys():
                self.requests[str(COURSE)] = [USER]
            else:
                self.requests[str(COURSE)].append(USER)
                self.send_notification(COURSE)
        else:
            print('Request Failed. Class Not Found.')
            return False
    
    def send_notification(self, COURSE):
        print('MATCH FOUND:')
        print('Course: {}'.format(COURSE))
        print(self.requests[str(COURSE)])
        
