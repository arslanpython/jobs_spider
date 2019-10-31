import re


def clean(data):
    if isinstance(data, tuple):
        return [e.strip() for e in data if e and e.strip()][0]
    if isinstance(data, list):
        return [e.strip() for seq in data for e in seq if e and e.strip()]
    if isinstance(data, str):
        return data.strip()

data = ["Atomwise (YC W15) Is Hiring a Senior Software Engineer", "BuildZoom (YC W13) is hiring \u2013 help us build better homes",
        "Join YC's Work at a Startup to find your next engineering job", "New Story (YC Nonprofit) Hiring Customer Success Specialist",
        "CoinTracker (YC W18) hiring first generalist to accelerate open financial system",
        "DemandSphere (YC S10) Is Hiring Mid/Senior Front End Developers in Columbus, OH", "The Muse (YC W12) Is Hiring a Senior Product Designer",
        "Tesorio (YC S15) Raised a $10MM Series A and Is Hiring", "Ribbon (YC S17) is hiring data engineers. Help us simplify healthcare",
        "Starsky Robotics Front-End Software Engineer-Teleoperations", "UpCodes is hiring Startup Engineers using Netflix model",
        "Pachyderm Raised $10M and Is Looking for a Senior JavaScript Engineer", "Shoptiques (YC W12) is hiring a client success manager in NYC",
        "Streak \u2013 CRM for Gmail (YC S11) Is Hiring in Vancouver", "Kodable is hiring a Game Developer to help teach millions of kid to code",
        "ZeroCater (YC W11) Is Hiring a Director of Engineer in SF", "Mimir (YC S15) Is Hiring a Product Designer to Help Us Improve CS Education",
        "Impraise (YC S14) Is Hiring a Senior Elixir Developer in Amsterdam, NL", "Starcity (YC S16) Is Hiring a Senior React Native Engineer",
        "Scale AI is hiring engineers to accelerate the development of AI", "Marble (YC S19) Is Hiring iOS & Node+Vue/React Engineers in SF",
        "Shipamax -Hiring Mid or Senior Python Engineers", "Bitmovin (YC S15) Is Hiring an Java Script Software Engineer in Vienna and Denver",
        "Mux (YC W16) is hiring across the board to build the future of online video", "Remix (YC 15) is looking for an engineering manager to better public transit",
        "Mino Games (YC W11) Is Hiring Game Developers in Montreal", "Cloosiv- Is Hiring a Full-Stack Engineer",
        "MTailor (YC S14) Is Hiring for an ML and Back End Engineer", "Coursedog (YC W19) Looking for Back End Engineering Lead", "Taplytics (YC W14) Is Hiring an Engineering Manager in Toronto"
        ,"Flexport is hiring software engineers to work on our trucking apps in  Chicago (flexport.com)"]


for e in data:

    # Job Name
    # result = clean(re.findall(r'(.*)is\s|', e, flags=re.I)[0])
    # result = re.search(r'(.*\))|(.*)\sis|(.*)\s\W|(.*?\s.*?\s)', e, flags=re.I).groups('')
    # result = re.search(r'(.*\))|(.*)\sis|(.*)\s\W|(.*?\s.*?\s)', e, flags=re.I).groups('')
    # result = clean(re.split(r'\W\s|\sis|\s\W', e, flags=re.I)[0])

    # LOCATION
    # result = re.findall(r'\sin\s(.*)|\sat\s(.*)', e, flags=re.I)
    # result = clean(re.findall(r'\sin\s(.*)|\sat\s(.*)', e, flags=re.I))

    # Job positions
    result = re.findall(r'ing\s(.*)\sin|ing\s(.*)', e, flags=re.I)
    # result = clean(re.findall(r'ing\s(.*)\sin|ing\s(.*)', e, flags=re.I))

    print(result)

jobs = [{'job_id': 444, 'name': 'dsfdsf', 'position': 'dsdfd'}]
columns = ', '.join(jobs[0].keys())
placeholders = ', '.join(['%s'] * len(jobs[0]))


