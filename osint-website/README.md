# OSINT Warning Dashboard Prototype

This repository contains a minimal prototype of an OSINT‑powered warning dashboard for monitoring
indicators of Chinese coercion or invasion against Taiwan.  It implements two major
components:

1. **Backend (FastAPI)** – serves indicator definitions and evaluates simulated events using a simple
   rule engine.
2. **Frontend (Next.js)** – displays the list of indicators and allows users to simulate an event and view
   the resulting evaluation.

## Structure

```
osint-website/
├── backend/
│   ├── main.py               # FastAPI app
│   ├── requirements.txt      # Python dependencies
│   ├── rule_engine.py        # Simple rule engine
│   ├── __init__.py           # Makes `backend` a package
│
├── data/
│   └── indicator_definitions.yaml  # YAML indicator definitions

├── frontend/
│   ├── package.json          # Node.js dependencies
│   └── pages/                # Next.js pages

└── README.md
```

## Running the prototype

1. **Backend:**
   ```bash
   cd osint-website/backend
   # Create a virtual environment
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   This starts the FastAPI server on port 8000.  You can access the API documentation at
   `http://localhost:8000/docs`.

2. **Frontend:**
   ```bash
   cd osint-website/frontend
   npm install
   npm run dev
   ```
   This starts the Next.js development server on port 3000.  Navigate to
   `http://localhost:3000` to view the dashboard.  Each indicator links to a detail
   page where you can simulate an event.  The front‑end will POST to the backend’s
   `/event` endpoint and display the returned confidence and recommendation.

## Extending this prototype

This code is a starting point, not a production system.  To turn it into a
fully‑functional OSINT tool you would:

* Replace the dummy rule engine with logic that ingests real sensor data and
  applies thresholds/statistical models to trigger alerts.
* Add a database (e.g., PostgreSQL or DynamoDB) to persist indicators,
  events and analyst annotations.
* Implement WebSockets or server‑sent events so the front‑end can receive live
  updates when new alerts are generated.
* Secure the APIs with authentication and HTTPS.
* Expand the front‑end to include dashboards, heat maps and historical trend
  visualisations.

Nevertheless, this prototype demonstrates the architectural pattern described in the
collection‑management report: a micro‑service back end, a rule engine and a
client‑side application for analysts.

Expanded Taiwan Strait I&W Matrix and Collection Annex
1 Context and aims
You asked for a professional‑grade set of intelligence requirements and indicators with an open‑source intelligence (OSINT) focus. The package I provided earlier followed NATO’s Allied Intelligence Doctrine (AJP‑2.7) and the six‑step intelligence cycle. Here I expand the Indicators & Warnings (I&W) matrix, giving more detail on potential observable events linked to three priority intelligence requirements (PIRs). I then provide a collection annex mapping each indicator to appropriate sensors or data feeds, highlight potential MASINT (measurement and signature intelligence) contributions, and offer practical code and process recommendations for an OSINT‑powered website/agent. Where appropriate I draw on recent open‑source analyses—including Janes’ 2024/2025 warnings, which note that large‑scale PLA mobilization for an invasion has not been observed
janes.com
, and the Institute for the Study of War’s July 2025 update, which stresses the PLA’s “grey‑zone” tactics such as Coast Guard patrols and disinformation while Taiwan concentrates on defensive Han Kuang exercises
understandingwar.org
.

Note: indicators should not be treated in isolation. Multiple indicators firing across disciplines increases confidence; the absence of key indicators reduces the likelihood of imminent conflict. Dates used in this annex reflect the current date (25 July 2025). Any references to “recent” activity are anchored against that date.

2 Expanded indicators by PIR and course of action
PIR 1 – Will the CCP leadership issue an irrevocable order to initiate armed unification within the next 90 days?
Course of action (COA)	Indicator (I&W)	Rationale & comments	Likely collection discipline
Most‐Likely COA (MLCOA): Coercive quarantine and political pressure	A1 – Politburo Standing Committee (PSC) travel freeze – sudden cancellation of all PSC members’ foreign travel and unexplained extensions of the annual Beidaihe retreat.	Janes warns that there has been no significant hostile rhetoric or mobilisation orders from the Chinese leadership through late 2024
janes.com
. A sudden travel ban would therefore be abnormal and suggest a shift to crisis footing.	HUMINT via diplomatic contacts; OSINT scraping of flight manifests, PSC public schedule.
A2 – Partial wartime economic controls – State Council introduces fuel rationing or “joint supply drills” in coastal provinces.	Such measures would prepare the economy for a blockade while keeping below full mobilisation.	OSINT monitoring of PRC official pronouncements; social media chatter on rationing and panic buying.
A3 – Maritime militia mobilisation – fishing cooperatives in Pingtan, Xiamen and Shantou ordered to deliver crews for “research” trips.	The maritime militia forms the front line of a blockade; unusual convoys would hint at a quarantine rather than normal fishing.	AIS/Satellite imaging of harbour outflows; human reporting from port workers; Chinese social media.
A4 – Cyber harassment surge – increased probing of Taiwan’s power grid, telecoms and news websites without destructive payloads.	A quarantine would involve psychological pressure and intermittent outages; the ISW notes that Taiwan officials have been preparing citizens for disinformation campaigns
understandingwar.org
.	CYBINT via open‑source threat feeds (GreyNoise, Shodan), MITRE ATT&CK pattern tracking.
A5 – Strategic messaging – People’s Daily and Xinhua run editorials insisting on “peaceful reunification” but warn of “law enforcement operations” around Taiwan; envoys to the UN push for acceptance of PRC quarantine zones.	Coercive pressure often starts with legal justifications. In 2025 the PRC has been normalising Coast Guard “law‑enforcement” patrols around outlying Taiwanese islands
understandingwar.org
.	OSINT media scraping, official statements, UN transcripts.
A6 – Targeted sanctions threats against allied firms – PRC threatens economic retaliation against Australian/Japanese companies for “interference in Taiwan affairs.”	This would aim to fracture alliance cohesion without committing to war.	OSINT monitoring of PRC Ministry of Commerce and state media; trade press.
A7 – Limited mobilisation – reserve call‑ups in Fujian and Zhejiang disguised as “flood relief” or “summer training.”	Small‑scale call‑ups are harder to detect but would hint at preparations for blockades; Janes notes that in 2024 no extra recruitment campaigns were observed
janes.com
.	HUMINT from local officials; social media videos of reserve units; overhead imagery of barracks.
A8 – Diplomatic freeze – recall of PRC ambassadors from Washington, Tokyo and Canberra for “consultations.”	Pulling ambassadors would signal intent to initiate coercive action but stop short of war.	Diplomatic traffic, open‑source watch of embassy activities, flight departures.
Most‐Dangerous COA (MDCOA): 48‑h missile/cyber strike then amphibious landing	B1 – CMC mobilisation order (JX‑20) – SIGINT surge on microwave links from Beijing to Eastern and Southern Theatre Commands; new daily code words.	A decisive invasion would require a national mobilisation order. This remains absent; Janes notes no mobilisation orders as of December 2024
janes.com
.	SIGINT collection by NSA/ASD; OSINT from amateur radio interceptors.
B2 – Full national mobilisation announcements – provincial governments order reserve and medical personnel to report; People’s Daily runs front‑page call‑ups.	Only a full assault requires such overt mobilisation.	HUMINT, PRC government websites, social media.
B3 – Widespread wartime economic measures – PRC imposes rationing of petrol, food and electricity and converts factories to military output.	A full‑scale invasion would necessitate emergency economic controls far beyond MLCOA measures.	Economic OSINT (customs data, port throughput), Chinese media monitoring.
B4 – Strategic Support Force (SSF) dispersal – large convoys of SSF vehicles carrying anti‑satellite (ASAT) and electronic‑warfare gear move to remote desert launch sites.	The MDCOA requires neutralising US space assets. Dispersal of SSF units would be visible in commercial SAR.	GEOINT via Planet, ICEYE; radio‑frequency mapping by commercial RF geolocation.
B5 – Rocket Force bases go to combat duty – DF‑17/DF‑26 transporter‑erector‑launchers (TELs) leave garrisons at night and disperse across highways.	A key indicator of imminent strikes; would be captured by synthetic‑aperture radar.	SAR imagery; road‑network traffic analysis.
B6 – National propaganda for total war – CCTV broadcasts martial songs; authorities warn citizens to prepare for “long war.”	MDCOA would require preparing public opinion for casualties and economic hardship.	Media analysis; Chinese social‑media sentiment tracking.
B7 – Diplomats evacuated – PRC orders families of diplomats home from Western capitals.	Evacuations would precede war to avoid hostages.	Travel manifests; consular notices.
B8 – Coastal SAM redeployment – HQ‑9B/HQ‑22 brigades move from permanent sites to camouflaged positions along Fujian coast; camouflage removed and radars activated.	Janes notes that as of late 2024 no such SAM redeployments were seen
janes.com
; movement would signal preparation for high‑intensity conflict.	IMINT/GEOINT (commercial EO and SAR).
B9 – Missile‐cyber pre‑strike – widespread cyber disruptions to Taiwanese critical infrastructure hours before kinetic strikes.	MDCOA begins with paralysing cyber operations. Taiwan’s 2025 Han Kuang exercises emphasised resilience against such attacks
understandingwar.org
.	CYBINT, telemetry from Taiwan’s National Cyber Security Centre.
B10 – Elite travel ban + arrest of dove politicians – internal purge of CCP elites who oppose war.	Historically, major wars follow consolidations of power; arrests would leak via elite networks.	HUMINT, Chinese legal notices, gossip on Weibo/Reddit clones.

PIR 2 – Is the PLA assembling forces for a quarantine or for a full‑scale landing?
Course of action	Indicator	Rationale & comments	Likely discipline
MLCOA	C1 – Surge of China Coast Guard (CCG) cutters and white‑hulled maritime militia convoys departing Ningbo, Guangzhou and Xiamen.	The ISW notes that PRC Coast Guard vessels have been conducting “dark” patrols around Pratas and Kinmen islands, often turning off AIS
understandingwar.org
. A sustained surge would indicate a blockade rather than a landing.	AIS and SAR tracking; OSINT from ship‑spotter social media; PRC maritime safety notices.
C2 – Limited amphibious shipping load‑outs – Type 071/075 amphibious assault ships conduct drills but return to port without full equipment.	Show of force for coercion rather than invasion.	PlanetScope imagery of dockyards; Chinese navy social media.
C3 – Maritime exclusion notices – PRC issues NOTAMs and navigation warnings in Bashi Channel and Taiwan Strait citing “joint law enforcement.”	Partial quarantines will be signalled through official notices.	OSINT scraping of MSA (Maritime Safety Administration) and civil aviation NOTAM feeds.
C4 – No mass airborne deployments – PLAAF airborne brigades remain at home bases; only small drills occur.	A quarantine does not require large airborne landings.	ADS‑B Exchange and MLAT tracking; commercial satellite imagery of airfields.
C5 – Rocket Force on alert but not dispersed – garrison activities intensify (training), but TELs remain inside bases.	Indicates posture for deterrence rather than assault.	SAR imagery; thermal imaging.
C6 – PLA logistics movements limited to Eastern TC – trains carrying supplies move to Fujian but not beyond; no bridging equipment observed.	Suggests preparation for blockade rather than cross‑strait landing.	OSINT train‑spotters; Sentinel‑2 imaging; social media.
C7 – Absence of large‑scale civilian ferry conversion – no ro‑ro passenger ferries are stripped for vehicle transport.	A landing would require mobilising civilian ro‑ro fleet.	Port observations, shipping manifests, ferry websites.
C8 – Coastal SAM batteries remain garrisoned – HQ‑9/HQ‑22 units stay at peacetime sites
janes.com
.	MLCOA does not need full air defence repositioning.	IMINT.
MDCOA	D1 – Amphibious assault ships fully loaded – Type 075 and Type 071 LPDs observed embarking armour, artillery and supplies, then sailing towards staging points such as Dachan Bay and Yulin.	A necessary precursor to an amphibious invasion.	High‑resolution commercial imagery; port photography; SAR.
D2 – Rapid airborne deployment – multiple PLAAF Y‑20 and Il‑76 aircraft ferry airborne troops to forward bases at Sanming, Xi’an and Fuzhou; temporary forward strips constructed on expressways.	Airborne assault on key nodes is central to MDCOA.	ADS‑B Exchange, crowdsourced flight tracking, satellite imagery.
D3 – Mass mobilisation of civilian shipping – ro‑ro ferries and container ships chartered; ports issue “fishing bans.”	Provides lift capacity for heavy equipment and troops.	AIS anomalies (new voyage patterns), PRC port notices, shipping industry press.
D4 – Coastal SAM deployment – HQ‑9B and HQ‑22 brigades move to open positions along Fujian coast; radars active 24/7
janes.com
.	Prepares for allied air strikes.	IMINT/SAR.
D5 – Logistics build‑up at marshalling areas – large numbers of flatbed trucks and fuel bowsers gather near Fuzhou and Xiamen; bridging units assemble pontoon equipment.	High capacity indicates imminent cross‑strait operations.	Planet imagery, highway traffic cameras.
D6 – Engineering dredging of Pingtan and Quanzhou – dredgers and pontoon causeways built to support amphibious operations.	Allows rapid embarkation of armour.	Satellite imagery; ship‑spotting.
D7 – Wide NOTAMs & closure of civilian airspace – PRC issues blanket NOTAMs over East China Sea and South China Sea citing “military exercises.”	Precedes ballistic missile launches.	Aviation OSINT; NOTAM watchers.
D8 – All‑domain drills with civilian assets – large‑scale integrated exercises using civilian ferries, fishing vessels and cargo aircraft; assimilation of militia into PLA chain of command.	A sharp contrast to the limited exercises observed up to 2024
janes.com
.	Observers on Chinese social media; port videos; local news.
D9 – Electronic suppression – SSF deploys jammers along the coast; GPS spoofing in Taiwan Strait.	Aims to disrupt allied navigation.	RF sensing (HawkEye 360), GNSS spoof detection, maritime reports.
D10 – Establishment of forward field hospitals – tented medical facilities set up in Fujian, Zhejiang; blood supply shipments surge.	Prepares for casualties; would be conspicuous.	Satellite imagery; procurement data; local social media.

PIR 3 – Are PRC strike assets preparing to paralyse Taiwan and interdict allied response?
Indicator (common to both COAs unless stated)	Rationale & comments	Discipline
E1 – Mass NOTAMs/exclusion zones – PRC issues large maritime and airspace closures around Taiwan Strait, Bashi Channel and Luzon Strait. NOTAM watchers have previously observed such notices before grey‑zone drills
understandingwar.org
.	Signals live‑fire tests or strikes.	NOTAM scraping; maritime safety websites.
E2 – Heavy PLAAF flight windows – increased night‑time training sorties by H‑6K bomber regiments and J‑20 fighter units over East China Sea.	Suggests rehearsals for long‑range strike.	ADS‑B Exchange (military transponders may squawk occasionally), satellite imaging of bases.
E3 – Rocket Force “track loading” – commercial SAR detects DF‑17/DF‑26 TEL convoys on highways after dusk; garrisons show empty garages.	Precursor to ballistic or hypersonic missile launches.	SAR imagery (ICEYE, Capella); highways monitored by open‑source enthusiasts.
E4 – Warhead and fuel transport – unusual rail shipments of solid‑rocket propellant and warheads to coastal ammunition depots.	Without warheads, TEL dispersal may be deception.	Rail‑spotter OSINT; thermal imaging of storage sites.
E5 – Armament of PLAAF bomber regiments – H‑6K/N bombers at Fuzhou and Ganzhou loaded with CJ‑20 cruise missiles.	Differentiates training from actual attack posture.	Satellite imagery; high‑resolution EO; analysis of payload mounts.
E6 – Mine‑laying preparations – Type 022 missile boats and YJ‑mine conversion kits loaded onto civilian trawlers.	Used to deny strait crossing and allied entry.	AIS anomalies; optical imagery of ports.
E7 – Cyber pre‑positioning – malware implants discovered in Taiwan’s power grid and US/Japanese early‑warning radars; PRC hackers pivot from espionage to destructive commands.	Prepares to paralyse communications and radars; Taiwan’s 2025 drills emphasised resilience
understandingwar.org
.	CYBINT from dark‑web sources; malware telemetry; cooperation with Taiwan/US CERTs.
E8 – Space & EW surge – SSF units deploy mobile ground‑based ASAT lasers and jammers to remote deserts; increased frequency of Chinese satellite launches with rendezvous‐proximity payloads.	Aimed at degrading US and Taiwanese space situational awareness.	Space surveillance networks (Space‑Track), optical telescopes; RF detection.
E9 – Targeting data flows – abnormal bursts of encrypted transmissions from PRC targeting networks to missile units; cross‑correlated with satellite pass‑over times.	Suggests final targeting updates.	SIGINT; analysis of Chinese launch control networks.
E10 – Live‑fire anti‑ship cruise missile drills – PRC releases footage of YJ‑12B launches from coastal batteries; maritime militia posts videos of tests.	May serve both training and deterrence roles.	Media analysis; geolocation of test videos; open‑source defence forums.
Unique MDCOA escalations		
E11 – Multi‑axis ballistic missile launches – simultaneous launches from multiple Rocket Force bases to overwhelm THAAD/Patriot defences.	Central to MDCOA.	Missile‑warning satellites, infrared sensors; commercial sensors.
E12 – High‑tempo bomber deployments – H‑6N bombers forward deploy to Fuzhou and Ganzhou with full munitions loads; flights extend into Philippine Sea.	Used to strike Guam and allied bases.	IMINT; open‑source flight tracking; Japanese MOD reporting.
E13 – SSF cyber & space denial – mass denial of GPS and BeiDou signals across the Western Pacific; kinetic ASAT engagement against allied satellites.	Would mark escalation to regional war.	GNSS monitoring networks; space surveillance.
E14 – Coordinated maritime and air decoys – use of unmanned surface vessels and drone swarms to saturate Taiwanese and allied radars.	A new tactic to paralyse defences.	OSINT from fishermen and shipping; sensor networks; open‑source videos.

3 Collection and platform annex
Below is a collector‑by‑collector overview aligned to the indicators above. Where possible I prioritise publicly accessible or commercial sources so an OSINT‑focused organisation can start cheaply and scale up. Classified collectors (NSA/ASD, National Technical Means) are listed to show how an all‑source agency would fill gaps. Frequency recommendations assume 24/7 operations when tensions rise.

Discipline	Collector/Platform	Indicators addressed	Notes & Tasking priority
HUMINT	Diplomats/liaison officers in Beijing; Chinese academic contacts; port workers; maritime militia families; PRC diaspora in Australia.	A1, A2, A3, A7, A8, B1–B3, B10, C6, C7, D9–D10.	Build trusted networks early; provide anonymised reporting channels; cross‑check for disinformation. Liaison with Taiwanese and Japanese counterparts is vital.
Cyber/OSINT	GreyNoise, Shodan, Recorded Future’s free feeds, dark‑web forums.	A4, E7.	Automate scraping for malware indicators; map to MITRE ATT&CK.
Media monitoring	Xinhua/People’s Daily, Global Times, CCTV; UN transcripts; Chinese social media (Weibo, Douyin), Telegram channels for ship‑spotters.	A5, A6, B6, C1, C3, D3, D8, E10.	Use NLP to detect shifts in tone; watch for censorship of rumours.
SIGINT	Menwith Hill, Pine Gap, Shoal Bay; US and allied airborne collection (RC‑135); mobile intercept ships; open amateur radio intercepts.	B1, B2, E9.	Classified sources will provide early warning of mobilisation orders and targeting data flows; OSINT interceptors can sometimes detect microwave bursts.
IMINT/GEOINT	Commercial EO (PlanetScope 3 m daily; Sentinel‑2 10 m weekly); Capella/ICEYE SAR; high‑resolution (Maxar, BlackSky) for tip‑off tasks; European Copernicus Sentinel‑1 for free SAR.	C2, C5, C6, C8, D1–D7, E3–E6, E8, D10, B4, B5.	SAR is invaluable because it sees through cloud and darkness; cross‑cue high‑res optical when SAR shows movement. Use change detection on ports and bases.
AIS/Maritime	MarineTraffic, Spire, Starboard Maritime Intelligence; PRC port authority notices (MEE, MSA).	C1, C3, C7, C8, D1–D3, E1, E6.	Combine AIS with SAR: AIS “dark” ships may still be visible on SAR. Monitor call‑sign changes or AIS spoofs around Pratas and Kinmen
understandingwar.org
.
Aviation tracking	ADS‑B Exchange, Flightradar24, PlaneFinder; open‑source MLAT networks.	C4, D2, E2, E5.	Military aircraft often turn off transponders, but tankers or transports may squawk; watch for unusual routes and long‑distance flights.
GEOINT/RF geolocation	HawkEye 360 (commercial RF), Aurora Insight.	D9, E8, E9.	Detect radar and jammer emissions; confirm SSF dispersal and EW operations.
MASINT	Infrared and hyperspectral sensors (e.g., NASA’s VIIRS, Sentinel‑3 SLSTR); acoustic sensors via underwater hydrophones; gravimetric sensors.	B5, E3 (TEL launches), E11, E12, E13.	VIIRS can detect rocket motor heat signatures; hydrophones detect submarine and torpedo activity; gravimetric anomalies may reveal tunnelling.
Analyst toolchain	Kafka event bus with micro‑services (FastAPI) to ingest data; YAML indicator definitions; ChatGPT agent for summarisation.	All indicators.	See Section 4 for code recommendations.

MASINT annex (heavier)
Thermal anomaly detection: Use VIIRS (Visible Infrared Imaging Radiometer Suite) to spot heat signatures from rocket launches (E11) and from TEL vehicles idling at dispersal sites. Combine with thermal cameras on high‑altitude drones.

Spectral analysis: Deploy hyperspectral sensors to identify camouflage nets and freshly disturbed soil at SAM and artillery positions (D4, D5). Hyperspectral data can differentiate paint and vegetation, highlighting decoys.

Acoustic sensing: Undersea hydrophone arrays can detect increased PLAN submarine traffic near Pingtan and Bashi Channel (E11). OSINT may not access these directly, but declassified detections could tip off analysts.

Gravimetric & magnetic: Monitoring subtle changes in gravity or magnetic fields in Fujian may reveal tunnelling for underground missile storage or command posts (B5). This typically requires classified sensors but could be complemented by satellite altimetry.

4 Practical blueprint for an OSINT‑powered website/agent
Below are actionable steps to transform the I&W matrix into a living OSINT application. This extends the outline previously provided.

Indicator schema: Create a YAML or JSON schema where each indicator has fields: pir, coa (mlcoa/mdcoa), description, data_signals (list of data feeds), threshold (logic for trigger), and confidence. Example:

yaml
Copy
Edit
id: B5
pir: 1
coa: mdcoa
description: Rocket Force TELs leave garrisons at night and disperse across highways.
data_signals:
  - iceye_sar
  - hawkeye360_rf
threshold:
  type: occurrence
  occurrences_required: 2
  time_window_hours: 24
confidence_model: simple_weighted_sum
Micro‑services: Write Python/FastAPI micro‑services for each data feed. For example, a sar_collector.py could query Capella/ICEYE APIs for imagery over pre‑defined polygons (Rocket Force bases) every six hours. Use asynchronous tasks (e.g., Celery) to parallelise downloads.

Rule engine: Implement a rule engine that reads incoming JSON events from Kafka, matches them against indicator definitions, and scores each indicator. For simple thresholds use boolean logic; for ambiguous signals use Bayesian updating or logistic regression.

ChatGPT agent: Deploy a GPT‑based agent with a system prompt that embeds the I&W matrix and doctrinal context. When the rule engine triggers an indicator, the agent receives a JSON blob and outputs:

confidence (0‑1): a subjective probability that the indicator is genuine.

which_indicator: the ID(s) matched.

analysis: a brief narrative linking the event to broader PIR/COA.

recommended_task: e.g., “task SAR on marshalling area X” or “increase cyber monitoring.”

The agent can also summarise the last 24 hours of activity per PIR when queried by analysts.

Front‑end: Use React or Next.js with a heat‑map dashboard. Each tile represents an indicator; colour intensity corresponds to the confidence score. Clicking a tile shows underlying data (images, AIS tracks) and the GPT agent’s narrative. Provide a page per PIR with aggregated trends.

Human‑in‑the‑loop: Analysts should review each high‑confidence alert before sending it to decision‑makers. Include an override button to veto false positives or request additional collection. Maintain an audit log (NIST SP 800‑53 moderate) of indicator evaluations.

Cost management: Start with free/public feeds—Sentinel‑2, Sentinel‑1, AIS/ADS‑B hobbyist networks—and a small Planet education account. Use paid SAR only when simple indicators (like AIS anomalies) trigger a need. Event filtering ensures ChatGPT tokens are used only on relevant data, keeping costs manageable.

Continuous evaluation: Treat this OSINT system as a living product. Conduct regular red‑team exercises to test whether the rule engine can detect simulated indicators. Compare outputs to authoritative assessments, such as Janes or the Institute for the Study of War reports. Iterate the indicator definitions and thresholds accordingly.

5 Closing remarks
This expanded matrix and annex should allow a Western collection‑management cell—or a GPT‑powered agent—to systematically watch for signals of PRC coercion or invasion. The key to success is balancing breadth of coverage with depth of analysis: use wide‑area sensors to detect anomalies, then cue high‑resolution assets and human analysts. Recent open‑source assessments underscore the value of context: Janes notes that through late 2024 no mobilisation orders or massed amphibious drills were evident
janes.com
, while the July 2025 Han Kuang exercises demonstrated Taiwan’s focus on resilience rather than panic
understandingwar.org
. Indicators must therefore be interpreted in sequence; a single event rarely justifies alarm. By codifying these indicators in software and coupling them with rigorous analytic tradecraft, intelligence teams can move from ad‑hoc OSINT scraping to a structured, doctrine‑aligned warning system.
