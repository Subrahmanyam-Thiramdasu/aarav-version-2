"""
Aarav Clinics - Complete Services System Builder
This script:
1. Replaces the services listing in services.html with exactly 19 unique services across 3 clinical categories.
2. Generates all 19 individual service pages adhering to the existing cinematic design system with complete, unique clinical content.
3. Creates redirects for legacy URLs so search engines and bookmarks are preserved without 404 errors.
4. Updates shared navigation menus (mega menu, mobile menu) and footers across the site.
5. Updates sitemap.xml with all 19 services.
"""

import os
import re

# The 19 Approved Services Definition
SERVICES = [
    {
        "id": 1,
        "name": "Shockwave Therapy",
        "slug": "shockwave-therapy",
        "category": "Advanced Technology",
        "meta_title": "Shockwave Therapy in Hyderabad | Extracorporeal Acoustic Care | Aarav Clinics",
        "meta_desc": "Advanced radial and focused Shockwave Therapy in Ashok Nagar, Near BHEL, Hyderabad. Non-invasive acoustic pulses accelerating tendon recovery and calcification breakdown.",
        "badge": "Advanced Acoustic Therapy",
        "hero_title": "Acoustic Wave Healing.",
        "hero_subtitle": "Targeted Deep Tissue Relief.",
        "hero_lead": "Accelerate stubborn tendon recovery, dissolve chronic calcifications, and trigger natural cellular repair with medical-grade Extracorporeal Shockwave Therapy (ESWT).",
        "hero_img": "assets/images/shockwave-therapy.jpg",
        "card_icon": "activity",
        "card_desc": "Acoustic pressure waves stimulating cellular repair, microcirculation, and breakdown of stubborn calcifications for chronic plantar fasciitis and tendinopathy.",
        "about_eyebrow": "Cellular Regeneration",
        "about_heading": "Non-invasive acoustic energy activating natural tissue restoration.",
        "about_lead": "Extracorporeal Shockwave Therapy (ESWT) delivers high-energy acoustic pulses directly into chronic, non-healing connective tissues that have stalled in the inflammatory cycle.",
        "about_detail": "When acoustic waves penetrate deep fascia, tendons, and joint capsules, they stimulate localized neovascularization (the growth of new micro-capillaries) and trigger the release of cellular growth factors. This biological cascade accelerates collagen synthesis, reduces substance P (a principal pain neurotransmitter), and breaks down painful fibrous adhesions without injections or surgical incisions.",
        "conditions": [
            {"title": "Plantar Fasciitis & Heel Spurs", "desc": "Chronic morning heel stabbing, thickened plantar fascia, and calcaneal spur irritation resistant to rest.", "icon": "footprints"},
            {"title": "Calcific Shoulder Tendinitis", "desc": "Painful calcium deposits in the rotator cuff tendons restricting arm elevation and night sleep.", "icon": "crosshair"},
            {"title": "Tennis & Golfer's Elbow", "desc": "Chronic lateral or medial epicondylopathy causing persistent forearm weakness and gripping pain.", "icon": "shield"},
            {"title": "Patellar & Achilles Tendinopathy", "desc": "Degenerative overload and pain in the patellar tendon (jumper's knee) or distal Achilles tendon.", "icon": "activity"}
        ],
        "pathway": [
            {"step": "1. Biomechanical Mapping", "desc": "Palpation and anatomical localization of the tender trigger zone to accurately calibrate acoustic frequency and depth.", "icon": "search"},
            {"step": "2. Acoustic Gel Coupling", "desc": "Application of medical conductive gel ensuring frictionless, complete transmission of acoustic energy without surface dissipation.", "icon": "sparkles"},
            {"step": "3. Calibrated Impulse Delivery", "desc": "Targeted application of gentle acoustic waves adjusted to the patient's individual comfort threshold over the target tissue.", "icon": "zap"},
            {"step": "4. Functional Loading Protocols", "desc": "Integration of progressive eccentric loading exercises to structurally align new collagen fibers during tissue remodeling.", "icon": "dumbbell"}
        ],
        "benefits": [
            {"num": "01", "title": "Stimulates Microvascular Flow", "desc": "Promotes new blood vessel formation in avascular tendon tissue to fuel cellular recovery."},
            {"num": "02", "title": "Breaks Down Chronic Fibrosis", "desc": "Mechanically remodels disorganized scar tissue and calcific deposits into pliable, functional collagen."},
            {"num": "03", "title": "Substantial Pain De-escalation", "desc": "Depletes pain-transmitting neurochemicals, offering progressive functional comfort across daily tasks."}
        ],
        "consult_expectations": "During your consultation, our senior physiotherapist performs a comprehensive clinical exam of the affected joint or tendon. We assess symptom duration, palpate precise tender spots, and verify your medical history to ensure ESWT is suitable. A typical session lasts 15 to 25 minutes, feels like deep rhythmic tapping, and requires zero downtime.",
        "precautions": "Shockwave therapy is contraindicated over active malignancies, open growth plates in growing children, acute local infections, deep vein thrombosis, or directly over cardiac pacemakers. Patients taking prescription blood thinners or with bleeding disorders require clinical evaluation prior to initiating acoustic therapy.",
        "related": ["advanced-decompression-therapy", "laser-therapy", "dry-needling-therapy"]
    },
    {
        "id": 2,
        "name": "Advanced Decompression Therapy",
        "slug": "advanced-decompression-therapy",
        "category": "Advanced Technology",
        "meta_title": "Advanced Spinal Decompression Therapy Hyderabad | Aarav Clinics",
        "meta_desc": "Non-surgical computerized spinal decompression in Ashok Nagar, Near BHEL, Hyderabad. Precise negative disc pressure for sciatica, disc bulges, herniations, and neck pain.",
        "badge": "Spinal Care Innovation",
        "hero_title": "Spinal Decompression.",
        "hero_subtitle": "Non-Surgical Disc Relief.",
        "hero_lead": "Gently reduce intra-discal pressure, relieve compressed spinal nerve roots, and promote retraction of herniated disc material with computerized spinal decompression.",
        "hero_img": "assets/images/decompression-therapy.jpg",
        "card_icon": "git-commit",
        "card_desc": "Computerized non-surgical spinal decompression gently relieving intervertebral disc pressure, sciatica, herniated discs, and persistent cervical radiculopathy.",
        "about_eyebrow": "Precision Biomechanics",
        "about_heading": "Creating negative intra-discal pressure to facilitate disc recovery.",
        "about_lead": "Advanced Spinal Decompression is an FDA-cleared computerized traction therapy engineered to overcome the muscle guarding reflex that occurs with conventional traction.",
        "about_detail": "By applying logarithmic tension angles tailored to the exact diseased spinal segment (lumbar or cervical), the system creates sustained negative pressure within the intervertebral disc. This vacuum phenomenon encourages the retraction of bulging or extruded nucleus pulposus material away from sensitive spinal nerve roots, while drawing oxygen, moisture, and healing nutrients back into the avascular disc matrix.",
        "conditions": [
            {"title": "Herniated & Bulging Discs", "desc": "Lumbar or cervical disc protrusions compressing the thecal sac or exiting nerve roots.", "icon": "disc"},
            {"title": "Sciatica & Radiating Nerve Pain", "desc": "Sharp shooting, burning, or tingling pain traveling down the glute, thigh, and calf.", "icon": "zap"},
            {"title": "Cervical Radiculopathy", "desc": "Nerve impingement causing chronic neck stiffness, shoulder blade throbbing, and hand numbness.", "icon": "user-check"},
            {"title": "Degenerative Disc Disease", "desc": "Age-related disc desiccation, loss of disc height, and recurrent mechanical spinal stiffness.", "icon": "activity"}
        ],
        "pathway": [
            {"step": "1. Segmental Spine Evaluation", "desc": "Detailed analysis of MRI reports, neurological dermatomes, and reflexes to verify target vertebrae.", "icon": "search"},
            {"step": "2. Ergonomic Harness Docking", "desc": "Comfortable pelvic or cervical restraint positioning the patient securely without compressive pinch points.", "icon": "shield"},
            {"step": "3. Computerized Pull Cycle", "desc": "Gradual logarithmic distraction cycles allowing spinal muscles to remain relaxed during negative-pressure phase.", "icon": "cpu"},
            {"step": "4. Post-Session Stabilization", "desc": "Guided core stabilization exercises to lock in segmental joint stability following decompression therapy.", "icon": "check-circle"}
        ],
        "benefits": [
            {"num": "01", "title": "Negative Intra-Discal Vacuum", "desc": "Creates negative pressure within disc spaces to encourage centralized retraction of bulges."},
            {"num": "02", "title": "Nerve Root Decongestion", "desc": "Relieves mechanical compression on the sciatic and cervical nerves, dampening radiating pain."},
            {"num": "03", "title": "Enhanced Nutrient Imbibition", "desc": "Draws essential fluids, oxygen, and nutrients into the disc to support cellular maintenance."}
        ],
        "consult_expectations": "Your consultation starts with an examination of spinal range of motion, neurological sensory testing, and MRI correlation. If cleared for decompression, you will lie comfortably on the specialized table. The treatment is gentle and relaxing—many patients even fall asleep during the gentle cyclical distension.",
        "precautions": "Decompression therapy is not suitable for patients with severe spinal instability, spinal fractures, advanced osteoporosis, surgical hardware/rods in the targeted area, spinal tumors, or during pregnancy. Comprehensive clinical assessment is always completed prior to treatment.",
        "related": ["shockwave-therapy", "advanced-physiotherapy", "laser-therapy"]
    },
    {
        "id": 3,
        "name": "Cage Therapy",
        "slug": "cage-therapy",
        "category": "Neuro-Rehabilitation",
        "meta_title": "Cage Therapy & Suspension Rehabilitation Hyderabad | Aarav Clinics",
        "meta_desc": "Universal exercise cage therapy and suspension rehabilitation in Ashok Nagar, Near BHEL, Hyderabad. Dynamic weight-eliminated balance and motor control training.",
        "badge": "Suspension Rehabilitation",
        "hero_title": "Cage Therapy System.",
        "hero_subtitle": "Suspension & Balance Control.",
        "hero_lead": "Universal exercise cage therapy providing dynamic suspension, gravity-eliminated movement, and progressive neuromuscular re-education for balance and gait recovery.",
        "hero_img": "assets/images/cage-therapy.jpg",
        "card_icon": "maximize-2",
        "card_desc": "Structured suspension and universal exercise cage therapy providing gravity-eliminated neuromuscular re-education, postural alignment, and balance stability.",
        "about_eyebrow": "Universal Exercise Unit",
        "about_heading": "Restoring functional independence through structured suspension.",
        "about_lead": "Cage Therapy—utilizing a specialized Universal Exercise Unit (UEU) with elastic suspension cords, supportive slings, and pulley systems—creates a safe, controlled 3D rehabilitation environment.",
        "about_detail": "By selectively offloading gravity or applying multidirectional dynamic resistance, cage therapy enables patients with neurological or motor challenges to practice upright standing, weight shifting, and independent motor patterns without fear of falling. The vestibular and proprioceptive feedback provided by the elastic suspension network re-trains the central nervous system to organize posture and dynamic balance.",
        "conditions": [
            {"title": "Cerebral Palsy & Motor Delays", "desc": "Supporting paediatric patients in developing head control, independent sitting, and upright standing balance.", "icon": "baby"},
            {"title": "Post-Stroke Gait & Balance Deficits", "desc": "Safe weight-supported gait retraining and trunk stability practice following neurological stroke.", "icon": "brain"},
            {"title": "Hypotonia & Muscle Weakness", "desc": "Gravity-eliminated strengthening for individuals with low muscle tone and joint laxity.", "icon": "activity"},
            {"title": "Vestibular & Ataxic Imbalances", "desc": "Proprioceptive retraining for coordination difficulties, tremors, and equilibrium challenges.", "icon": "compass"}
        ],
        "pathway": [
            {"step": "1. Postural & Tonus Assessment", "desc": "Detailed evaluation of baseline trunk stability, muscle tone, postural reflexes, and balance reactions.", "icon": "search"},
            {"step": "2. Sling & Cord Calibration", "desc": "Custom arrangement of elastic suspension cords and padded pelvic/thoracic supports for target body weight support.", "icon": "sliders"},
            {"step": "3. Guided Motor Re-Education", "desc": "Therapist-guided active movement drills including controlled sit-to-stand, single-leg balance, and weight transfers.", "icon": "user-check"},
            {"step": "4. Dynamic Challenge Progression", "desc": "Gradual reduction in suspension assistance to foster real-world independent postural control and confidence.", "icon": "trending-up"}
        ],
        "benefits": [
            {"num": "01", "title": "Zero-Fall Fear Environment", "desc": "Secure suspension builds confidence, allowing patients to push physical boundaries safely."},
            {"num": "02", "title": "Neuromuscular Proprioception", "desc": "Stimulates sensory receptors across joints and muscles to reinforce correct movement patterns."},
            {"num": "03", "title": "Isolated Muscle Activation", "desc": "Enables strengthening of weak muscle groups that cannot otherwise function against full gravity."}
        ],
        "consult_expectations": "Your initial evaluation focuses on motor milestone progression, joint mobility, spasticity grading, and balance control. We introduce the suspension environment gently, ensuring the patient feels completely supported and comfortable before initiating active coordination exercises.",
        "precautions": "Clinical note: Cage therapy protocols are customized to individual clinical evaluations. The treatment requires assessment of bone density, joint subluxation risks, and skin integrity under supportive harnesses. Close, one-on-one therapist supervision is maintained at all times.",
        "related": ["paediatric-adult-rehabilitation", "stroke-rehabilitation", "occupational-therapy"]
    },
    {
        "id": 4,
        "name": "Cupping Therapy",
        "slug": "cupping-therapy",
        "category": "Musculoskeletal",
        "meta_title": "Clinical Cupping Therapy Hyderabad | Myofascial Decompression | Aarav Clinics",
        "meta_desc": "Evidence-based clinical cupping and myofascial decompression in Ashok Nagar, Near BHEL, Hyderabad. Alleviate muscular stiffness, release fascial restrictions, and enhance blood flow.",
        "badge": "Myofascial Decompression",
        "hero_title": "Clinical Cupping Therapy.",
        "hero_subtitle": "Decompress Stiff Fascial Layers.",
        "hero_lead": "Medical-grade negative pressure cupping therapy designed to release dense myofascial restrictions, increase localized microcirculation, and alleviate chronic muscle stiffness.",
        "hero_img": "assets/images/physiotherapy-session.jpg",
        "card_icon": "disc",
        "card_desc": "Medical-grade myofascial cupping utilizing controlled decompression to improve localized blood flow, release fascial restrictions, and alleviate dense muscle stiffness.",
        "about_eyebrow": "Negative Pressure Science",
        "about_heading": "Lifting and decompressing adherent myofascial tissue layers.",
        "about_lead": "While most massage and physical therapy techniques compress muscle tissues downward, clinical cupping therapy works in reverse through therapeutic negative pressure.",
        "about_detail": "Using medical-grade suction cups, our certified physiotherapists gently lift skin and underlying fascia away from the muscle body. This separation draws stagnant interstitial fluid away, encourages rapid influx of oxygenated blood, stimulates lymphatic drainage, and breaks cross-linked collagen adhesions that cause persistent stiffness in desk workers, athletes, and post-injury patients.",
        "conditions": [
            {"title": "Upper Back & Trapezius Spasms", "desc": "Dense shoulder knots, postural fatigue, and tension headaches caused by prolonged computer desk posture.", "icon": "user"},
            {"title": "Lumbar Fascial Tightness", "desc": "Chronic lower back stiffness, limited forward flexion, and thoracolumbar fascial thickening.", "icon": "activity"},
            {"title": "Iliotibial (IT) Band Syndrome", "desc": "Fascial tightness along the lateral thigh and knee common in runners and active individuals.", "icon": "fast-forward"},
            {"title": "Post-Workout Soreness & Stagnation", "desc": "Delayed onset muscle soreness (DOMS) requiring accelerated metabolic waste clearance.", "icon": "refresh-cw"}
        ],
        "pathway": [
            {"step": "1. Fascial Palpation", "desc": "Hands-on assessment to identify localized tissue density, trigger bands, and restrictions in skin gliding.", "icon": "search"},
            {"step": "2. Skin Preparation", "desc": "Application of hypoallergenic emollient oil to facilitate smooth cup movement and protect the dermal barrier.", "icon": "droplet"},
            {"step": "3. Static or Dynamic Cupping", "desc": "Careful application of suction cups, combining stationary placement with active range-of-motion gliding.", "icon": "disc"},
            {"step": "4. Mobility Integration", "desc": "Immediate follow-up stretching and joint mobilization while the myofascial layers are hydrated and pliable.", "icon": "maximize"}
        ],
        "benefits": [
            {"num": "01", "title": "Rapid Fascial Decompression", "desc": "Separates bound fascial layers to restore smooth physiological gliding between muscles."},
            {"num": "02", "title": "Enhanced Microvascular Perfusion", "desc": "Draws fresh blood supply into ischemic, chronically tight muscle knots to speed healing."},
            {"num": "03", "title": "Gentle Nervous System Calming", "desc": "Provides tactile stimulation that helps down-regulate hyperactive motor tone and muscular guarding."}
        ],
        "consult_expectations": "Your session begins with a skin and circulatory evaluation. The suction sensation is typically described as a pleasant, relieving pulling feeling. Temporary circular skin discoloration (ecchymosis) is completely normal and harmless, typically resolving within 3 to 7 days as tissue cleanses.",
        "precautions": "Cupping is contraindicated over open wounds, acute skin rashes, severe varicose veins, areas of active deep vein thrombosis, or in patients with bleeding disorders or severe anaemia. Caution is maintained during pregnancy, avoiding the abdomen and lower lumbar zones.",
        "related": ["dry-needling-therapy", "advanced-physiotherapy", "sports-injury-physiotherapy"]
    },
    {
        "id": 5,
        "name": "Dry Needling Therapy",
        "slug": "dry-needling-therapy",
        "category": "Musculoskeletal",
        "meta_title": "Dry Needling Therapy in Hyderabad | Trigger Point Relief | Aarav Clinics",
        "meta_desc": "Certified intramuscular Dry Needling in Ashok Nagar, Near BHEL, Hyderabad. Precise trigger point release for chronic back pain, tension headaches, sciatica, and muscle knots.",
        "badge": "Intramuscular Therapy",
        "hero_title": "Precision Dry Needling.",
        "hero_subtitle": "Release Deep Trigger Points.",
        "hero_lead": "Targeted intramuscular dry needling by certified physiotherapists to deactivate taut trigger point bands, relieve nerve compression, and restore muscle elasticity.",
        "hero_img": "assets/images/physiotherapy-session.jpg",
        "card_icon": "crosshair",
        "card_desc": "Targeted fine-filament intramuscular needling releasing hyperirritable myofascial trigger points, resetting neuromuscular tension, and relieving referred pain.",
        "about_eyebrow": "Neuro-Muscular Reset",
        "about_heading": "Deactivating chronic neuromuscular contraction knots with fine filaments.",
        "about_lead": "Dry Needling is an evidence-based modern Western physical therapy technique targeting myofascial trigger points—hyperirritable spots within taut bands of skeletal muscle.",
        "about_detail": "Using micro-thin, solid monofilament needles without medication, our certified clinicians penetrate deep into dysfunctional muscle fibers. The needle stimulates a localized twitch response (LTR), which resets dysfunctional motor endplates, normalizes local biochemical acidity, flushes out inflammatory markers (such as bradykinin and substance P), and immediately restores physiological resting muscle length.",
        "conditions": [
            {"title": "Cervicogenic Headaches & Neck Spasm", "desc": "Referred tension radiating into the temples and base of the skull from upper trapezius trigger points.", "icon": "zap"},
            {"title": "Piriformis Syndrome & Gluteal Pain", "desc": "Deep buttock trigger points compressing the sciatic nerve pathway, mimicking lumbar disc pain.", "icon": "activity"},
            {"title": "Myofascial Back & Quadratus Pain", "desc": "Deep lower back muscular spasms that restrict twisting, bending, and comfortable sitting.", "icon": "shield"},
            {"title": "Rotator Cuff & Shoulder Impingement", "desc": "Infraspinatus and supraspinatus knots preventing smooth overhead reaching and arm rotation.", "icon": "crosshair"}
        ],
        "pathway": [
            {"step": "1. Palpatory Trigger Identification", "desc": "Precise flat or pincer palpation isolating the taut band and eliciting patient-recognized referred pain.", "icon": "search"},
            {"step": "2. Sterile Skin Preparation", "desc": "Medical alcohol sanitization and single-use, sterile disposable surgical-grade monofilament needles.", "icon": "check-circle"},
            {"step": "3. Precision Intramuscular Needling", "desc": "Gentle needle insertion eliciting a brief, therapeutic local twitch response to release the contraction.", "icon": "target"},
            {"step": "4. Passive Elongation & Movement", "desc": "Immediate post-needling gentle stretching and active mobility drills to cement lengthened muscle memory.", "icon": "maximize"}
        ],
        "benefits": [
            {"num": "01", "title": "Immediate Local Twitch Release", "desc": "Deactivates sustained muscular contractions that cannot be reached through superficial massage."},
            {"num": "02", "title": "Normalizes Local Biochemistry", "desc": "Neutralizes acidic tissue pH and disperses accumulated inflammatory neurotransmitters."},
            {"num": "03", "title": "Restores Full Functional Length", "desc": "Permits joints to move through their natural, pain-free anatomical range of motion."}
        ],
        "consult_expectations": "Your therapist will walk you through the procedure, palpating the exact muscle group before beginning. The needle entry is generally unfelt; when the trigger point releases, a brief dull ache or twitch is experienced. Mild muscular soreness lasting 24 to 48 hours is normal, followed by significant freedom of movement.",
        "precautions": "Dry needling is conducted only after strict clinical screening. It is avoided in areas of active infection, in patients with severe needle phobia, uncontrolled lymphedema, or acute bleeding disorders. Pregnancy considerations require avoidance of specific acupuncture-sensitive trigger points.",
        "related": ["cupping-therapy", "advanced-physiotherapy", "sports-injury-physiotherapy"]
    },
    {
        "id": 6,
        "name": "Prenatal and Postnatal Exercise Therapy",
        "slug": "prenatal-postnatal-exercise-therapy",
        "category": "Maternal Rehabilitation",
        "meta_title": "Prenatal and Postnatal Exercise Therapy Hyderabad | Aarav Clinics",
        "meta_desc": "Expert Prenatal and Postnatal Exercise Therapy in Ashok Nagar, Near BHEL, Hyderabad. Pelvic floor strengthening, diastasis recti recovery, and safe pregnancy fitness.",
        "badge": "Maternal Health Physiotherapy",
        "hero_title": "Maternal Wellness Care.",
        "hero_subtitle": "Prenatal & Postnatal Therapy.",
        "hero_lead": "Evidence-based physiotherapy for expectant and new mothers. Gentle pelvic floor conditioning, diastasis recti recovery, ergonomic support, and safe functional rehabilitation.",
        "hero_img": "assets/images/hero-clinic.jpg",
        "card_icon": "heart",
        "card_desc": "Specialized physical therapy guiding expectant and new mothers through safe pelvic floor conditioning, diastasis recti recovery, and spinal support.",
        "about_eyebrow": "Safe Maternal Rehabilitation",
        "about_heading": "Supporting maternal musculoskeletal health through every trimester and beyond.",
        "about_lead": "Pregnancy and childbirth bring profound biomechanical, hormonal, and postural changes. Our specialized maternal physiotherapy programs ensure safety, comfort, and restorative healing.",
        "about_detail": "During pregnancy, increased relaxin levels soften ligaments, altering pelvic alignment and loading the lumbar spine. Following childbirth, women frequently experience abdominal separation (diastasis recti), pelvic girdle instability, and postural strain from nursing. Our certified therapists provide individualized, doctor-coordinated exercise protocols that protect the core, strengthen the pelvic floor, and promote gradual, sustainable recovery.",
        "conditions": [
            {"title": "Pregnancy Pelvic Girdle & SIJ Pain", "desc": "Asymmetrical pelvic joint pain, pubic symphysis discomfort, and sacroiliac strain while walking.", "icon": "activity"},
            {"title": "Diastasis Recti Abdominis", "desc": "Separation of the rectus abdominis muscles post-delivery requiring structured transverse abdominis activation.", "icon": "shield"},
            {"title": "Pelvic Floor Weakness & Incontinence", "desc": "Stress urinary leakage, feelings of pelvic heaviness, and core coordinator weakness.", "icon": "heart"},
            {"title": "Postural Neck & Upper Back Fatigue", "desc": "Thoracic kyphosis and trapezius strain stemming from newborn feeding and prolonged carrying.", "icon": "user"}
        ],
        "pathway": [
            {"step": "1. Comprehensive Maternal Assessment", "desc": "Gentle screening of pelvic alignment, spinal curvature, breathing mechanics, and obstetric history.", "icon": "search"},
            {"step": "2. Core & Diastasis Recti Mapping", "desc": "Palpation of inter-recti distance and assessment of deep transverse abdominis recruitment efficiency.", "icon": "check-circle"},
            {"step": "3. Tailored Trimester-Safe Exercises", "desc": "Low-impact pelvic floor coordination, breathing synergy, and joint-stabilizing resistance routines.", "icon": "activity"},
            {"step": "4. Ergonomic & Baby-Care Coaching", "desc": "Practical guidance on safe lifting, nursing postures, and ergonomic stroller mechanics to avoid repetitive strain.", "icon": "compass"}
        ],
        "benefits": [
            {"num": "01", "title": "Pelvic Stability & Comfort", "desc": "Alleviates sacroiliac and lower back tension while promoting comfortable daily mobility."},
            {"num": "02", "title": "Safe Diastasis Recti Healing", "desc": "Restores deep abdominal wall integrity without increasing intra-abdominal pressures inappropriately."},
            {"num": "03", "title": "Postpartum Stamina & Recovery", "desc": "Rebuilds overall endurance, pelvic support, and confidence to return to active life smoothly."}
        ],
        "consult_expectations": "Your initial consultation is conducted in a relaxed, private setting. We discuss your obstetrician's recommendations, delivery details, and current functional comfort. Exercises are introduced gradually, with continuous monitoring of comfort and breathing mechanics.",
        "precautions": "Clinical safety note: Prenatal exercise therapy requires medical clearance from your obstetrician or gynaecologist. Exercises are adapted per trimester, avoiding supine positioning past the first trimester, avoiding heavy valsalva maneuvers, and respecting individual physiological boundaries.",
        "related": ["advanced-physiotherapy", "paediatric-adult-rehabilitation", "geriatric-rehabilitation"]
    },
    {
        "id": 7,
        "name": "Speech Therapy for Paediatric and Adult Patients",
        "slug": "speech-therapy-paediatric-adult",
        "category": "Speech & Communication",
        "meta_title": "Speech Therapy for Paediatric and Adult Patients Hyderabad | Aarav Clinics",
        "meta_desc": "Certified speech-language pathology in Ashok Nagar, Near BHEL, Hyderabad. Expert care for child speech delay, stammering, adult stroke aphasia, and swallowing disorders.",
        "badge": "Speech & Language Pathology",
        "hero_title": "Clear Communication.",
        "hero_subtitle": "Paediatric & Adult Care.",
        "hero_lead": "Evidence-based speech, language, voice, and swallowing rehabilitation. Helping children unlock developmental communication milestones and adults regain confidence after neurological events.",
        "hero_img": "assets/images/child-therapy.jpg",
        "card_icon": "mic",
        "card_desc": "Expert speech-language pathology addressing developmental speech delays, articulation, fluency, voice, and adult post-stroke swallowing or aphasia challenges.",
        "about_eyebrow": "Voice & Communication",
        "about_heading": "Unlocking articulate expression and safe swallowing across all ages.",
        "about_lead": "Communication is fundamental to connection, learning, and independence. Our licensed speech-language pathologists provide individualized intervention tailored to distinct developmental and neurological needs.",
        "about_detail": "For paediatric patients, therapy focuses on developmental delays, clarity of speech sounds (articulation), stammering/fluency, vocabulary development, and social pragmatics through interactive, play-based strategies. For adults recovering from stroke, head trauma, or progressive conditions, our therapy targets aphasia (word retrieval), dysarthria (motor speech clarity), voice modulation, and dysphagia (swallowing safety) using structured clinical protocols.",
        "conditions": [
            {"title": "Paediatric Speech & Language Delay", "desc": "Toddlers and young children experiencing delayed expressive vocabulary, sentence formation, or comprehension.", "icon": "baby"},
            {"title": "Stammering & Stuttering (Fluency)", "desc": "Repetitions, prolongations, or speech blocks in children and adults, addressing both mechanics and confidence.", "icon": "mic"},
            {"title": "Adult Post-Stroke Aphasia & Dysarthria", "desc": "Difficulty speaking clearly, finding words, or comprehending conversations following a cerebrovascular event.", "icon": "brain"},
            {"title": "Dysphagia & Swallowing Difficulties", "desc": "Choking, coughing during meals, or oral-motor weakness requiring safe swallow conditioning.", "icon": "shield"}
        ],
        "pathway": [
            {"step": "1. Standardized Speech-Language Battery", "desc": "Formal assessment of expressive language, receptive comprehension, oral-motor mechanics, and speech clarity.", "icon": "search"},
            {"step": "2. Oral-Motor & Acoustic Screening", "desc": "Evaluating tongue strength, lip seal, soft palate elevation, and vocal cord resonance parameters.", "icon": "user-check"},
            {"step": "3. Targeted Structured Intervention", "desc": "Weekly clinical sessions using play-based milestone drills for children or cognitive-linguistic retraining for adults.", "icon": "sparkles"},
            {"step": "4. Home Communication Coaching", "desc": "Equipping family members with conversational strategies and carryover exercises for real-world reinforcement.", "icon": "users"}
        ],
        "benefits": [
            {"num": "01", "title": "Enhanced Expressive Clarity", "desc": "Improves articulation and speech sound accuracy so individuals are understood clearly by peers and family."},
            {"num": "02", "title": "Confident Social Interaction", "desc": "Reduces communication anxiety, enabling active participation in school, work, and community settings."},
            {"num": "03", "title": "Safe, Dignified Swallowing", "desc": "Strengthens pharyngeal muscles to reduce aspiration risks and ensure safe oral nutrition."}
        ],
        "consult_expectations": "Your initial speech-language evaluation is welcoming, supportive, and non-intimidating. For children, it involves engaging interactive play and picture-naming tasks. For adults, it includes conversational analysis, word-retrieval tests, and a thorough oral-motor examination.",
        "precautions": "Therapy goals are established collaboratively based on standardized clinical assessments. For dysphagia cases, close coordination with the patient's primary physician and instrumental swallow studies (such as FEES or videofluoroscopy) may be incorporated as medically indicated.",
        "related": ["occupational-therapy", "behavioural-therapy", "parental-training"]
    },
    {
        "id": 8,
        "name": "Occupational Therapy",
        "slug": "occupational-therapy",
        "category": "Developmental & Functional",
        "meta_title": "Occupational Therapy in Hyderabad | Sensory Integration | Aarav Clinics",
        "meta_desc": "Certified Occupational Therapy and sensory integration in Ashok Nagar, Near BHEL, Hyderabad. Fine motor skills, sensory processing, handwriting, and daily independence.",
        "badge": "Sensory & Functional Care",
        "hero_title": "Occupational Therapy.",
        "hero_subtitle": "Empowering Independence.",
        "hero_lead": "Evidence-based occupational therapy cultivating sensory processing, fine motor dexterity, bilateral coordination, and daily functional living skills for children and adults.",
        "hero_img": "assets/images/child-therapy.jpg",
        "card_icon": "puzzle",
        "card_desc": "Sensory integration, handwriting coordination, bilateral motor skills, and self-care independence helping children and adults excel in daily activities.",
        "about_eyebrow": "Meaningful Daily Living",
        "about_heading": "Enabling participation and success in the occupations of everyday life.",
        "about_lead": "Occupational therapy helps individuals of all ages participate in the activities they need and want to do—from school and play for children, to self-care and work for adults.",
        "about_detail": "At Aarav Clinics, our occupational therapy department features a fully equipped sensory integration gym and fine motor training area. For paediatric patients with sensory processing differences, autism, ADHD, or developmental coordination disorder, we build sensory regulation, handwriting grasp, and emotional focus. For adults recovering from injury or neurological events, we retrain activities of daily living (ADLs), hand function, and adaptive task strategies.",
        "conditions": [
            {"title": "Sensory Processing Differences", "desc": "Hypersensitivity or hyposensitivity to touch, sound, or movement affecting attention and calm in everyday environments.", "icon": "sparkles"},
            {"title": "Fine Motor & Handwriting Challenges", "desc": "Pencil grip fatigue, illegible handwriting, buttoning difficulties, and poor bilateral hand coordination.", "icon": "edit-3"},
            {"title": "Attention & Executive Function", "desc": "Difficulty organizing tasks, transitioning between activities, and sustaining focus in classroom or home settings.", "icon": "clock"},
            {"title": "Adult Activities of Daily Living (ADLs)", "desc": "Loss of independent upper limb function for dressing, eating, or grooming post-stroke or injury.", "icon": "user-check"}
        ],
        "pathway": [
            {"step": "1. Sensory & Motor Profile Assessment", "desc": "Comprehensive evaluation using standardized developmental motor batteries and sensory profile questionnaires.", "icon": "search"},
            {"step": "2. Sensory Gym Integration", "desc": "Therapeutic swinging, textured tactile inputs, and deep proprioceptive obstacle courses to regulate the nervous system.", "icon": "activity"},
            {"step": "3. Fine Motor & Perceptual Drills", "desc": "Graded bilateral coordination, scissor skills, finger dissociation, and visual-motor integration tasks.", "icon": "puzzle"},
            {"step": "4. Routine & Environmental Adaptation", "desc": "Developing realistic sensory diets and modified task strategies for smooth independence at school and home.", "icon": "check-circle"}
        ],
        "benefits": [
            {"num": "01", "title": "Sensory Emotional Self-Regulation", "desc": "Helps the nervous system adapt to sensory inputs, reducing distress and meltdowns."},
            {"num": "02", "title": "Enhanced Classroom & Writing Skills", "desc": "Strengthens hand musculature and motor planning for comfortable, fluent pencil control."},
            {"num": "03", "title": "Everyday Self-Care Confidence", "desc": "Promotes mastery of buttoning, shoelaces, utensil use, and personal grooming independence."}
        ],
        "consult_expectations": "The initial evaluation includes an observation of gross and fine motor skills, motor planning, and sensory responses. Parents and caregivers actively participate in discussing daily routines, sensory sensitivities, and developmental goals.",
        "precautions": "Therapy activities are individually calibrated to prevent sensory overload or fatigue. Equipment like suspension swings and deep-pressure tools are utilized under continuous, direct clinician supervision.",
        "related": ["speech-therapy-paediatric-adult", "vision-therapy", "behavioural-therapy"]
    },
    {
        "id": 9,
        "name": "Vision Therapy",
        "slug": "vision-therapy",
        "category": "Neuro-Developmental",
        "meta_title": "Vision Therapy in Hyderabad | Visual Processing & Eye Tracking | Aarav Clinics",
        "meta_desc": "Specialized Vision Therapy in Ashok Nagar, Near BHEL, Hyderabad. Evidence-based care for convergence insufficiency, eye tracking delays, amblyopia, and visual-motor integration.",
        "badge": "Visual-Motor Rehabilitation",
        "hero_title": "Clinical Vision Therapy.",
        "hero_subtitle": "Retraining the Visual Brain.",
        "hero_lead": "Specialized visual-motor and neuro-developmental therapy improving eye tracking, binocular convergence, visual-spatial perception, and reading visual endurance.",
        "hero_img": "assets/images/child-therapy.jpg",
        "card_icon": "eye",
        "card_desc": "Clinical neuro-developmental visual exercises enhancing binocular convergence, ocular motor tracking, visual-spatial perception, and visual-motor integration.",
        "about_eyebrow": "Neuro-Optometric Rehabilitation",
        "about_heading": "Vision is more than 20/20 eyesight—it is how the brain processes the world.",
        "about_lead": "A person can have sharp 20/20 visual acuity and still suffer from severe visual-processing or ocular-motor dysfunction that impairs learning, reading, and coordination.",
        "about_detail": "Vision therapy is a personalized program of progressive visual activities designed to correct binocular vision problems, eye movement disorders, and visual-perceptual deficits. By strengthening the neural connections between the eyes and the brain's visual cortex, vision therapy resolves issues such as convergence insufficiency (eyes struggling to team together for close work), skipping lines while reading, double vision, and post-concussion visual fatigue.",
        "conditions": [
            {"title": "Convergence Insufficiency (CI)", "desc": "Eyes struggling to turn inward together during reading, causing eye strain, headaches, and words blurring.", "icon": "eye"},
            {"title": "Ocular Motor Tracking Deficits", "desc": "Losing place while reading, skipping words, using a finger to track, or slow visual scanning across lines.", "icon": "navigation"},
            {"title": "Visual-Spatial & Perceptual Delays", "desc": "Difficulty distinguishing reversals (b/d, p/q), poor visual memory, and spatial orientation challenges.", "icon": "grid"},
            {"title": "Post-Concussion & Stroke Vision Strain", "desc": "Visual crowding, sensitivity to visual motion, and double vision following neurological trauma.", "icon": "zap"}
        ],
        "pathway": [
            {"step": "1. Binocular & Tracking Screening", "desc": "Assessment of smooth pursuits, saccades, near point of convergence (NPC), and binocular stereopsis.", "icon": "search"},
            {"step": "2. Monocular Fixation & Control", "desc": "Targeted ocular exercises establishing steady individual eye fixation and pursuit precision.", "icon": "target"},
            {"step": "3. Binocular Teaming & Fusion", "desc": "Utilizing specialized prism lenses, polarized targets, and stereograms to foster simultaneous binocular perception.", "icon": "eye"},
            {"step": "4. Visual-Vestibular-Motor Integration", "desc": "Combining visual tracking tasks with balance and whole-body coordination for real-world integration.", "icon": "activity"}
        ],
        "benefits": [
            {"num": "01", "title": "Effortless Reading Comfort", "desc": "Eliminates eye fatigue, blurred text, and persistent headaches during schoolwork or desk tasks."},
            {"num": "02", "title": "Accurate Eye Movement & Tracking", "desc": "Ensures smooth transitions across pages without skipping sentences or losing reading comprehension."},
            {"num": "03", "title": "Enhanced Hand-Eye Coordination", "desc": "Sharpens spatial visual judgment for handwriting, sports participation, and spatial awareness."}
        ],
        "consult_expectations": "Your evaluation entails a series of visual-motor and tracking assessments using specialized charts, optical targets, and binocular alignment tools. We explain the findings clearly and outline whether clinic-based therapy, home exercises, or coordination with your ophthalmologist is recommended.",
        "precautions": "Vision therapy does not replace standard ophthalmological examinations or prescription corrective lenses for refractive errors. It is designed specifically for visual function, ocular motility, and neuro-visual processing.",
        "related": ["occupational-therapy", "special-education-therapy", "behavioural-therapy"]
    },
    {
        "id": 10,
        "name": "Behavioural Therapy",
        "slug": "behavioural-therapy",
        "category": "Child Development",
        "meta_title": "Behavioural Therapy for Children in Hyderabad | Aarav Clinics",
        "meta_desc": "Empathetic, evidence-based Behavioural Therapy in Ashok Nagar, Near BHEL, Hyderabad. Positive behavioral support, emotional regulation, and social skill development.",
        "badge": "Positive Behavior Support",
        "hero_title": "Behavioural Therapy.",
        "hero_subtitle": "Emotional Regulation & Growth.",
        "hero_lead": "Compassionate, evidence-informed behavioral intervention helping children develop emotional regulation, positive social communication, routine adaptability, and lasting confidence.",
        "hero_img": "assets/images/child-therapy.jpg",
        "card_icon": "smile",
        "card_desc": "Evidence-based behavioral support fostering emotional regulation, social-communication skills, routine adaptation, and positive behavioral milestones.",
        "about_eyebrow": "Positive Reinforcement",
        "about_heading": "Understanding the function of behavior to build constructive coping strategies.",
        "about_lead": "Challenging behaviors in children are almost always forms of communication—signaling unmet sensory, emotional, communicative, or developmental needs.",
        "about_detail": "At Aarav Clinics, our behavioural therapists use positive, relationship-centered behavioral techniques to identify what triggers distress, tantrums, anxiety, or defiance. We work collaboratively with the child to teach replacement behaviors, self-soothing strategies, functional communication, and emotional vocabulary. By structuring the child's environment and reinforcing positive adaptations, we help create calm, fulfilling relationships at home and school.",
        "conditions": [
            {"title": "Emotional Dysregulation & Meltdowns", "desc": "Intense, prolonged emotional outbursts when frustrated, overwhelmed, or asked to transition tasks.", "icon": "alert-circle"},
            {"title": "Social Communication Difficulties", "desc": "Challenges with turn-taking, peer interaction, sharing, and understanding non-verbal social cues.", "icon": "users"},
            {"title": "Anxiety & Routine Rigidity", "desc": "Severe distress during unexpected routine changes, separation anxiety, or situational avoidance.", "icon": "shield"},
            {"title": "ADHD-Related Impulsivity & Inattention", "desc": "Difficulty waiting turns, following multi-step directions, or managing impulses in group settings.", "icon": "zap"}
        ],
        "pathway": [
            {"step": "1. Functional Behavior Assessment (FBA)", "desc": "Analyzing antecedents, specific behaviors, and consequences to identify what drives the behavioral pattern.", "icon": "search"},
            {"step": "2. Positive Reinforcement Structuring", "desc": "Establishing clear, motivating reward schedules and visual schedules that celebrate small successes.", "icon": "award"},
            {"step": "3. Replacement Skill Coaching", "desc": "Teaching the child functional communication phrases, self-calming breathing, and alternative responses.", "icon": "smile"},
            {"step": "4. Caregiver Strategy Alignment", "desc": "Guiding parents and teachers with consistent, calm boundary setting and positive reinforcement at home.", "icon": "users"}
        ],
        "benefits": [
            {"num": "01", "title": "Constructive Coping Mechanisms", "desc": "Equips the child with calm strategies to handle frustration and disappointment constructively."},
            {"num": "02", "title": "Improved Family Harmony", "desc": "Reduces daily power struggles, mealtime resistance, and bedtime difficulties through clear routines."},
            {"num": "03", "title": "Thriving Social Peer Connections", "desc": "Fosters cooperative play, empathy, sharing, and reciprocal friendships in school and community."}
        ],
        "consult_expectations": "The initial assessment begins with an in-depth conversation with parents about daily patterns, triggers, and family strengths, followed by a playful observation session with the child. We formulate a customized positive behavioral plan with measurable, realistic milestone goals.",
        "precautions": "Our clinical approach strictly utilizes positive reinforcement, empathy, and developmental support. We never employ punitive or shaming methods. Individual plans are monitored continually to ensure the child feels safe, respected, and understood.",
        "related": ["parental-training", "special-education-therapy", "occupational-therapy"]
    },
    {
        "id": 11,
        "name": "Special Education Therapy",
        "slug": "special-education-therapy",
        "category": "Child Development",
        "meta_title": "Special Education Therapy in Hyderabad | Remedial Learning | Aarav Clinics",
        "meta_desc": "Individualized Special Education and remedial therapy in Ashok Nagar, Near BHEL, Hyderabad. Structured academic support for dyslexia, learning differences, and developmental delays.",
        "badge": "Remedial & Developmental Learning",
        "hero_title": "Special Education.",
        "hero_subtitle": "Personalized Learning Pathways.",
        "hero_lead": "Individualized remedial educational therapy supporting children with learning differences, dyslexia, processing challenges, and academic developmental milestones.",
        "hero_img": "assets/images/child-therapy.jpg",
        "card_icon": "book-open",
        "card_desc": "Individualized educational interventions for children with learning differences, dyslexia, attention difficulties, and academic processing challenges.",
        "about_eyebrow": "Individualized Learning",
        "about_heading": "Every child learns differently—we adapt teaching to how their brain thrives.",
        "about_lead": "Traditional classrooms often rely on uniform instructional methods that leave children with learning differences feeling overwhelmed, anxious, and discouraged.",
        "about_detail": "Special Education Therapy at Aarav Clinics is designed to identify each child's cognitive learning style, perceptual strengths, and areas requiring structured support. Using multi-sensory instruction (Orton-Gillingham principles, tactile manipulatives, and visual modeling), our special educators address reading decoding, phonetic awareness, mathematical concepts, working memory, and study organization, restoring academic self-esteem and a love of learning.",
        "conditions": [
            {"title": "Dyslexia & Reading Challenges", "desc": "Difficulty with letter-sound correspondence, phonetic decoding, reading fluency, and comprehension.", "icon": "book-open"},
            {"title": "Dyscalculia & Math Processing", "desc": "Challenges grasping number sense, spatial math relationships, telling time, or remembering math facts.", "icon": "hash"},
            {"title": "Dysgraphia & Written Expression", "desc": "Struggles putting thoughts into organized writing, severe spelling challenges, and motor fatigue.", "icon": "edit"},
            {"title": "Slow Processing & Working Memory", "desc": "Needing extra time to absorb multi-step directions, retain sequences, and retrieve learned concepts.", "icon": "cpu"}
        ],
        "pathway": [
            {"step": "1. Psycho-Educational Profile Review", "desc": "Reviewing school performance, developmental history, and cognitive strengths through standardized screening.", "icon": "search"},
            {"step": "2. Multi-Sensory Concept Introduction", "desc": "Teaching phonics, reading, and numeracy through touch, sight, sound, and movement simultaneously.", "icon": "sparkles"},
            {"step": "3. Executive Function & Study Habits", "desc": "Structuring graphic organizers, color-coded task breakdowns, and working memory strategies.", "icon": "check-square"},
            {"step": "4. School Accommodation Collaboration", "desc": "Assisting parents in advocating for appropriate classroom accommodations, extra time, and IEP support.", "icon": "users"}
        ],
        "benefits": [
            {"num": "01", "title": "Stronger Academic Foundations", "desc": "Builds solid phonetic, reading comprehension, and numerical reasoning skills step-by-step."},
            {"num": "02", "title": "Restored Self-Confidence", "desc": "Transforms academic frustration into pride and self-efficacy as concepts click into place."},
            {"num": "03", "title": "Independent Study Strategies", "desc": "Provides lifelong organizational tools that enable students to manage homework and exams with ease."}
        ],
        "consult_expectations": "Your consultation starts with an evaluation of your child's current academic skills, reading samples, and school reports in a low-pressure, encouraging environment. We outline a clear learning roadmap tailored to your child's pace and specific learning differences.",
        "precautions": "Special education therapy is tailored to individual developmental profiles. It complements, but does not replace, formal neurological or psycho-educational diagnostic assessments conducted by licensed clinical psychologists where formal educational exemptions are sought.",
        "related": ["behavioural-therapy", "vision-therapy", "speech-therapy-paediatric-adult"]
    },
    {
        "id": 12,
        "name": "Parental Training",
        "slug": "parental-training",
        "category": "Child Development",
        "meta_title": "Parental Training & Coaching in Hyderabad | Aarav Clinics",
        "meta_desc": "Compassionate, structured Parental Training in Ashok Nagar, Near BHEL, Hyderabad. Equipping families with evidence-based home therapy routines, positive communication, and guidance.",
        "badge": "Family Coaching & Guidance",
        "hero_title": "Parental Training.",
        "hero_subtitle": "Empowering Families to Lead.",
        "hero_lead": "Structured parent coaching programs equipping families with practical home-based therapy techniques, positive communication tools, and calm developmental guidance.",
        "hero_img": "assets/images/child-therapy.jpg",
        "card_icon": "users",
        "card_desc": "Empowering parents with hands-on therapeutic techniques, positive communication strategies, and home-based developmental guidance for lasting progress.",
        "about_eyebrow": "Collaborative Care",
        "about_heading": "Parents are the most powerful therapists in a child's everyday world.",
        "about_lead": "A clinic session lasts an hour, but family life continues around the clock. The greatest developmental gains happen when therapy principles are woven seamlessly into daily home routines.",
        "about_detail": "At Aarav Clinics, Parental Training is an essential pillar of our child development ecosystem. We partner with parents of children undergoing speech, occupational, vision, or behavioral therapy to provide clear, actionable coaching. From setting up calming sensory corners and managing public meltdowns, to facilitating speech during mealtime and establishing consistent sleep routines, we give parents the tools, confidence, and emotional support they deserve.",
        "conditions": [
            {"title": "Navigating a New Developmental Diagnosis", "desc": "Helping families understand autism, ADHD, sensory differences, or speech delay with clarity and hope.", "icon": "compass"},
            {"title": "Home Sensory & Meltdown Strategies", "desc": "Creating low-stress home environments and co-regulation tools to de-escalate emotional distress.", "icon": "shield"},
            {"title": "Daily Living & Milestone Routines", "desc": "Step-by-step coaching for stress-free mealtime, toilet training, tooth brushing, and bedtime transitions.", "icon": "clock"},
            {"title": "Parent Burnout & Emotional Fatigue", "desc": "Providing emotional support, self-care strategies, and realistic expectations to sustain family wellness.", "icon": "heart"}
        ],
        "pathway": [
            {"step": "1. Family Lifestyle & Routine Mapping", "desc": "Understanding daily pain points, sibling dynamics, work-life schedules, and primary family priorities.", "icon": "search"},
            {"step": "2. Co-Therapy Hands-On Observation", "desc": "Parents observe and participate alongside senior therapists to master hands-on techniques in real time.", "icon": "eye"},
            {"step": "3. Home Action Blueprint", "desc": "Developing concise visual charts, simplified verbal prompts, and 10-minute micro-routines for home life.", "icon": "file-text"},
            {"step": "4. Ongoing Progress & Problem-Solving", "desc": "Regular check-ins to celebrate breakthroughs, troubleshoot emerging challenges, and adjust strategies.", "icon": "refresh-cw"}
        ],
        "benefits": [
            {"num": "01", "title": "Confident Caregiver Leadership", "desc": "Replaces feeling overwhelmed with clear, predictable action steps for daily challenges."},
            {"num": "02", "title": "Accelerated Child Progress", "desc": "Reinforces clinic gains 24/7 in natural settings, speeding milestone achievement dramatically."},
            {"num": "03", "title": "Strengthened Emotional Bond", "desc": "Replaces disciplinary frustration with deep, positive connection between parent and child."}
        ],
        "consult_expectations": "Parental training sessions are private, empathetic, and judgment-free. Both parents, grandparents, and primary caregivers are warmly welcomed. Sessions can be conducted in-clinic or through interactive video consultations for busy schedules.",
        "precautions": "Our coaching philosophy is anchored in empathy, practicality, and realistic pacing. We design strategies around your existing family life rather than creating exhausting additional burdens.",
        "related": ["behavioural-therapy", "occupational-therapy", "speech-therapy-paediatric-adult"]
    },
    {
        "id": 13,
        "name": "Advanced Physiotherapy",
        "slug": "advanced-physiotherapy",
        "category": "Musculoskeletal",
        "meta_title": "Advanced Physiotherapy Clinic Hyderabad | Aarav Clinics",
        "meta_desc": "Leading evidence-based Advanced Physiotherapy in Ashok Nagar, Near BHEL, Hyderabad. Expert manual therapy, spinal rehab, joint mobilization, and long-term functional recovery.",
        "badge": "Musculoskeletal Clinical Excellence",
        "hero_title": "Advanced Physiotherapy.",
        "hero_subtitle": "Root-Cause Functional Recovery.",
        "hero_lead": "Comprehensive physical therapy integrating precise joint mobilization, myofascial release, advanced modalities, and progressive functional loading for lasting pain relief.",
        "hero_img": "assets/images/physiotherapy-session.jpg",
        "card_icon": "zap",
        "card_desc": "Comprehensive clinical physiotherapy combining manual mobilization, postural re-education, and tailored exercise therapy for back, neck, and joint disorders.",
        "about_eyebrow": "Root-Cause Care",
        "about_heading": "Moving beyond temporary symptom masking to rebuild biomechanical integrity.",
        "about_lead": "At Aarav Clinics, advanced physiotherapy begins with identifying why an injury occurred, rather than simply treating where it hurts.",
        "about_detail": "We evaluate kinetic chains, spinal alignment, neuromuscular coordination, and daily workplace ergonomics to craft a structured, 4-phase clinical recovery plan. By pairing hands-on manual techniques—such as Maitland and Mulligan joint mobilizations—with targeted electrotherapy and progressive resistance training, we eliminate pain, rebuild functional strength, and prevent recurrent injury.",
        "conditions": [
            {"title": "Lumbar Spondylosis & Sciatica", "desc": "Herniated discs, facet joint arthropathy, and radiating nerve pain down the leg and foot.", "icon": "activity"},
            {"title": "Cervical Spondylosis & Tech Neck", "desc": "Chronic neck stiffness, postural trapezius spasm, and tension radiating into the upper limbs.", "icon": "user-check"},
            {"title": "Frozen Shoulder & Rotator Cuff Pain", "desc": "Adhesive capsulitis, subacromial impingement, and painful limitation of overhead reaching.", "icon": "shield"},
            {"title": "Knee Osteoarthritis & Patellofemoral Pain", "desc": "Cartilage wear, crepitus, joint effusion, and difficulty climbing stairs or standing from chairs.", "icon": "footprints"}
        ],
        "pathway": [
            {"step": "1. Multi-Point Biomechanical Exam", "desc": "Postural photography, joint range of motion (ROM), neurological testing, and palpation of tissue origin.", "icon": "search"},
            {"step": "2. Skilled Hands-On Manual Therapy", "desc": "Joint gliding, myofascial release, and passive neural mobilization to restore pain-free movement play.", "icon": "hand"},
            {"step": "3. Advanced Therapeutic Modalities", "desc": "Integration of therapeutic laser, IFT, or ultrasound to control deep inflammation at the cellular level.", "icon": "zap"},
            {"step": "4. Kinetic Chain Strengthening", "desc": "Progressive resistance exercises restoring deep postural stabilizers and shielding against future injury.", "icon": "dumbbell"}
        ],
        "benefits": [
            {"num": "01", "title": "Rapid Pain De-Escalation", "desc": "Relieves acute mechanical nerve and joint pressure through targeted hands-on mobilization."},
            {"num": "02", "title": "Restored Full Range of Motion", "desc": "Eliminates protective muscle guarding, enabling smooth, unrestricted daily movement."},
            {"num": "03", "title": "Reduced Medication Dependence", "desc": "Helps patients safely step down reliance on NSAIDs and temporary pain-masking pharmaceuticals."}
        ],
        "consult_expectations": "Your first session includes a thorough 45-minute clinical evaluation of your posture, spine, joint mechanics, and functional pain triggers. You will receive immediate hands-on treatment and a clear, transparent explanation of your diagnosis and recovery timeline.",
        "precautions": "Treatment intensity is tailored to your acute or chronic status. Patients with recent trauma, suspected fractures, severe osteoporosis, or progressive neurological deficits undergo detailed clinical screening to ensure safety.",
        "related": ["shockwave-therapy", "laser-therapy", "advanced-decompression-therapy"]
    },
    {
        "id": 14,
        "name": "Stroke Rehabilitation",
        "slug": "stroke-rehabilitation",
        "category": "Neuro-Rehabilitation",
        "meta_title": "Stroke Rehabilitation in Hyderabad | Neuro Physiotherapy | Aarav Clinics",
        "meta_desc": "Specialized Stroke & Neurological Rehabilitation in Ashok Nagar, Near BHEL, Hyderabad. Neuroplasticity retraining, hemiplegia recovery, gait re-education, and functional independence.",
        "badge": "Neurological Excellence",
        "hero_title": "Stroke Rehabilitation.",
        "hero_subtitle": "Rewiring Neural Pathways.",
        "hero_lead": "Evidence-based neurological physiotherapy dedicated to neuroplasticity retraining, hemiplegic motor recovery, balance stabilization, and restoring functional independence after stroke.",
        "hero_img": "assets/images/blog-stroke.jpg",
        "card_icon": "brain",
        "card_desc": "Specialized neuro-physiotherapy retraining motor pathways, restoring balance and gait coordination, managing spasticity, and fostering functional independence.",
        "about_eyebrow": "Neuroplastic Potential",
        "about_heading": "Harnessing the brain's capacity to reorganize and rebuild motor function.",
        "about_lead": "A stroke interrupts blood flow to the brain, but the brain possesses an extraordinary lifelong ability to rewire itself through dedicated neuroplastic rehabilitation.",
        "about_detail": "At Aarav Clinics, our neuro-physiotherapists utilize task-oriented training, Bobath/NDT concepts, and progressive balance protocols to stimulate dormant motor pathways. We treat hemiparesis (one-sided weakness), abnormal spastic muscle tone, foot drop, and balance insecurity. Every session is structured to translate clinical exercises directly into daily functional living—sitting safely, standing confidently, walking with stability, and regaining upper limb function.",
        "conditions": [
            {"title": "Hemiplegia & One-Sided Weakness", "desc": "Loss of active motor control and strength in the arm and leg following ischemic or hemorrhagic stroke.", "icon": "activity"},
            {"title": "Spasticity & Muscle Hypertonicity", "desc": "Involuntary muscle stiffness and tight flexor synergy patterns in the arm or extensor patterns in the leg.", "icon": "shield"},
            {"title": "Gait Ataxia & Balance Loss", "desc": "Unsteady, asymmetrical walking, foot drop, and significant fear of falling during household ambulation.", "icon": "navigation"},
            {"title": "Upper Limb & Hand Functional Deficits", "desc": "Difficulty opening the hand, grasping utensils, or coordinating fine finger movements for daily tasks.", "icon": "hand"}
        ],
        "pathway": [
            {"step": "1. Standardized Neuro Evaluation", "desc": "Assessment using Brunnstrom stages of recovery, Berg Balance Scale, and spasticity grading (Modified Ashworth).", "icon": "search"},
            {"step": "2. Tone Normalization & Inhibition", "desc": "Hands-on neuro-facilitation techniques to reduce spasticity and release pathological muscular posturing.", "icon": "hand"},
            {"step": "3. High-Repetition Task Training", "desc": "Meaningful, goal-directed exercises like weight shifting, sit-to-stand repetitions, and reach-and-grasp drills.", "icon": "refresh-cw"},
            {"step": "4. Overground Gait Re-Education", "desc": "Structured walking re-education with orthotic support and rhythmic auditory cues to foster safe, symmetrical steps.", "icon": "footprints"}
        ],
        "benefits": [
            {"num": "01", "title": "Stimulates Neuroplastic Rewiring", "desc": "Repetitive, task-specific practice promotes synaptic connections around injured brain territories."},
            {"num": "02", "title": "Restores Safe Household Ambulation", "desc": "Improves balance reactions, gait symmetry, and weight bearing on the affected lower extremity."},
            {"num": "03", "title": "Regains Activities of Daily Living", "desc": "Progresses patients toward independent transfers, dressing, and personal autonomy."}
        ],
        "consult_expectations": "Your initial evaluation is gentle, patient, and comprehensive. We review hospital discharge summaries, current medications, cardiovascular status, and cognitive alertness, involving family members directly in defining meaningful recovery goals.",
        "precautions": "Stroke rehabilitation plans depend on individual assessment and medical stability. Blood pressure and heart rate are monitored closely during sessions. Precautions are taken regarding shoulder subluxation and sensory loss in the hemiplegic limb.",
        "related": ["advanced-physiotherapy", "cage-therapy", "occupational-therapy"]
    },
    {
        "id": 15,
        "name": "Paediatric and Adult Rehabilitation",
        "slug": "paediatric-adult-rehabilitation",
        "category": "Multidisciplinary",
        "meta_title": "Paediatric and Adult Rehabilitation in Hyderabad | Aarav Clinics",
        "meta_desc": "Comprehensive Paediatric and Adult Rehabilitation in Ashok Nagar, Near BHEL, Hyderabad. Lifelong restorative care for congenital delays, trauma, and neurological conditions.",
        "badge": "Continuum of Care",
        "hero_title": "Paediatric & Adult Care.",
        "hero_subtitle": "Restorative Therapy for All Ages.",
        "hero_lead": "A unified continuum of restorative care addressing congenital conditions, developmental motor challenges, adult traumatic injuries, and complex neurological recovery.",
        "hero_img": "assets/images/hero-clinic.jpg",
        "card_icon": "life-buoy",
        "card_desc": "Integrated developmental and restorative rehabilitation addressing congenital conditions, motor milestone delays, adult trauma, and complex neuromuscular needs.",
        "about_eyebrow": "Integrated Clinical Excellence",
        "about_heading": "Tailored restorative care across every stage of human development.",
        "about_lead": "Human movement evolves across a lifetime. Whether addressing an infant learning to roll over or an adult recovering from severe trauma, rehabilitation requires deep clinical insight.",
        "about_detail": "At Aarav Clinics, our Paediatric and Adult Rehabilitation department bridges developmental pediatric therapy and adult physical medicine under one coordinated roof. Children with conditions such as torticollis, cerebral palsy, and hypotonia receive gentle, play-infused motor milestone facilitation. Adults recovering from polytrauma, peripheral nerve injuries, or prolonged illness receive phased conditioning that rebuilds stamina, joint mobility, and functional dignity.",
        "conditions": [
            {"title": "Infant & Child Motor Delay", "desc": "Delayed rolling, sitting, crawling, or walking requiring neuro-developmental physical therapy.", "icon": "baby"},
            {"title": "Congenital Musculoskeletal Conditions", "desc": "Infant torticollis, plagiocephaly, clubfoot follow-up, and generalized joint hypermobility.", "icon": "shield"},
            {"title": "Adult Traumatic & Orthopaedic Injuries", "desc": "Complex fractures, ligament reconstructions, and prolonged immobilization requiring phased re-mobilization.", "icon": "activity"},
            {"title": "Neuromuscular & Chronic Impairments", "desc": "Long-term rehabilitation for muscular dystrophies, neuropathies, and multi-system motor fatigue.", "icon": "user-check"}
        ],
        "pathway": [
            {"step": "1. Age-Specific Baseline Evaluation", "desc": "Standardized developmental milestone checks for children or functional independence measures for adults.", "icon": "search"},
            {"step": "2. Developmental / Joint Mobilization", "desc": "Gentle hands-on facilitation guiding proper joint alignment and stimulating postural equilibrium.", "icon": "hand"},
            {"step": "3. Play-Based or Functional Drills", "desc": "Engaging sensory games for children and functional task-simulation training for adults.", "icon": "sparkles"},
            {"step": "4. Ongoing Family & Lifestyle Support", "desc": "Adaptive equipment selection, ergonomic positioning, and practical home exercise progression.", "icon": "home"}
        ],
        "benefits": [
            {"num": "01", "title": "Milestone Achievement for Children", "desc": "Encourages natural physical progression toward sitting, crawling, and independent walking."},
            {"num": "02", "title": "Restored Adult Functional Independence", "desc": "Rebuilds joint motion, muscular strength, and endurance following trauma or illness."},
            {"num": "03", "title": "Coordinated Family-Centered Care", "desc": "Provides unified treatment plans that grow and adapt with the patient's individual progress."}
        ],
        "consult_expectations": "Our multi-disciplinary team conducts a detailed assessment respecting the patient's age and comfort level. We review medical records, discuss daily lifestyle barriers, and co-create an encouraging, realistic rehabilitation plan.",
        "precautions": "Treatment intensity is closely adjusted according to individual diagnostic profiles. Pediatric sessions prioritize gentle handling and play, while adult post-trauma plans adhere strictly to orthopedic surgeon weight-bearing guidelines.",
        "related": ["cage-therapy", "advanced-physiotherapy", "stroke-rehabilitation"]
    },
    {
        "id": 16,
        "name": "Geriatric Rehabilitation",
        "slug": "geriatric-rehabilitation",
        "category": "Senior Mobility",
        "meta_title": "Geriatric Rehabilitation in Hyderabad | Fall Prevention | Aarav Clinics",
        "meta_desc": "Specialized Geriatric Rehabilitation in Ashok Nagar, Near BHEL, Hyderabad. Safe balance training, fall prevention, arthritis management, and mobility support for senior citizens.",
        "badge": "Senior Health & Longevity",
        "hero_title": "Geriatric Rehabilitation.",
        "hero_subtitle": "Safe, Confident Senior Mobility.",
        "hero_lead": "Compassionate, evidence-based senior physical therapy focused on balance stabilization, fall prevention, joint flexibility, bone health, and maintaining daily independence.",
        "hero_img": "assets/images/hero-clinic.jpg",
        "card_icon": "user-check",
        "card_desc": "Compassionate senior physical therapy improving balance confidence, joint flexibility, bone health, and fall prevention for active, safe living.",
        "about_eyebrow": "Healthy Active Aging",
        "about_heading": "Preserving autonomy, strength, and confidence in the golden years.",
        "about_lead": "Aging should not mean accepting a loss of independence, constant joint pain, or the perpetual fear of falling.",
        "about_detail": "Geriatric Rehabilitation at Aarav Clinics is tailored to the physiological changes of senior adults. We address age-related sarcopenia (muscle loss), joint stiffness from osteoarthritis, spinal stenosis, and vestibular balance decline. Our clinicians design gentle, dignified exercise programs that enhance bone density, improve gait stability, prevent dangerous slips and falls, and keep senior citizens actively engaged in the activities they love.",
        "conditions": [
            {"title": "Balance Insecurity & Fall Prevention", "desc": "Unsteadiness while walking, dizziness when turning, or recovering from a previous frightening fall.", "icon": "shield-alert"},
            {"title": "Degenerative Osteoarthritis & Stiffness", "desc": "Severe joint pain and stiffness in the knees, hips, and spine making standing and stair climbing painful.", "icon": "activity"},
            {"title": "Osteopenia & Osteoporosis Support", "desc": "Safe bone-loading and postural exercises designed to reduce vertebral compression fracture risks.", "icon": "shield"},
            {"title": "Post-Hospitalization Deconditioning", "desc": "Generalized weakness and stamina loss following medical illness, surgery, or prolonged bed rest.", "icon": "refresh-cw"}
        ],
        "pathway": [
            {"step": "1. Fall Risk & Mobility Audit", "desc": "Comprehensive screening of balance, gait speed, joint flexibility, vision, and footwear safety.", "icon": "search"},
            {"step": "2. Joint Mobilization & Pain Relief", "desc": "Gentle manual therapy, warmth, and safe modalities to ease arthritic morning stiffness.", "icon": "hand"},
            {"step": "3. Static & Dynamic Balance Training", "desc": "Weight-shifting exercises, tandem standing, and obstacle stepping supported by sturdy safety rails.", "icon": "compass"},
            {"step": "4. Home Safety & Assistive Advice", "desc": "Guidance on cane/walker sizing, bathroom grab bars, non-slip flooring, and everyday ergonomic safety.", "icon": "home"}
        ],
        "benefits": [
            {"num": "01", "title": "Significant Fall Risk Reduction", "desc": "Strengthens ankle proprioception and core postural reflexes to prevent disastrous slips and trips."},
            {"num": "02", "title": "Long-Term Living Autonomy", "desc": "Maintains ability to stand up from chairs, walk to the market, and manage self-care without relying on others."},
            {"num": "03", "title": "Safe Cardiovascular Stamina", "desc": "Rebuilds cardiopulmonary endurance through low-impact, supervised physical conditioning."}
        ],
        "consult_expectations": "We welcome senior patients with warmth, respect, and patience. The initial consultation moves at a comfortable pace, checking vital signs, reviewing medication lists, and identifying personal mobility goals without physical strain.",
        "precautions": "Safety is paramount. Exercises are conducted with close therapist contact and support rails. Vital signs (blood pressure, pulse oximetry) are checked when indicated, and exercises avoid sudden rotational strain on osteoporotic spines.",
        "related": ["advanced-physiotherapy", "tkr-thr-physiotherapy", "stroke-rehabilitation"]
    },
    {
        "id": 17,
        "name": "Sports Injury Physiotherapy",
        "slug": "sports-injury-physiotherapy",
        "category": "Sports Rehabilitation",
        "meta_title": "Sports Injury Physiotherapy in Hyderabad | Aarav Clinics",
        "meta_desc": "Elite Sports Injury Physiotherapy in Ashok Nagar, Near BHEL, Hyderabad. Accelerated recovery for ACL tears, rotator cuff injuries, ankle sprains, runner's knee, and return-to-sport training.",
        "badge": "Athletic Performance Recovery",
        "hero_title": "Sports Injury Physiotherapy.",
        "hero_subtitle": "Accelerated Return to Play.",
        "hero_lead": "Advanced athletic rehabilitation combining biomechanical video analysis, targeted tissue repair, sport-specific conditioning, and re-injury prevention protocols.",
        "hero_img": "assets/images/physiotherapy-session.jpg",
        "card_icon": "award",
        "card_desc": "Biomechanical evaluation, ligament and tendon recovery protocols, and progressive return-to-sport physical conditioning for athletes.",
        "about_eyebrow": "Athletic Science",
        "about_heading": "Rebuilding athletes stronger, faster, and more resilient than before.",
        "about_lead": "Sports injuries demand more than resting on the sidelines—they require aggressive, scientifically phased functional rehabilitation to restore peak performance.",
        "about_detail": "At Aarav Clinics, our sports physiotherapists treat athletes across all levels—from recreational badminton and weekend cricket players to competitive runners and gym enthusiasts. We analyze kinetic chain dysfunctions, muscle imbalances, and movement mechanics that predispose tissues to failure. By integrating manual therapy, dry needling, therapeutic laser, and progressive plyometric loading, we ensure you return to your sport with complete confidence.",
        "conditions": [
            {"title": "Ligament Tears (ACL, PCL, MCL, ATFL)", "desc": "Pre-hab and post-operative functional rehabilitation for knee and ankle ligament reconstructions.", "icon": "activity"},
            {"title": "Rotator Cuff & Shoulder Labrum Tears", "desc": "Overhead throwing injuries, shoulder impingement, and swimming/badminton rotator cuff strains.", "icon": "crosshair"},
            {"title": "Muscle Strains (Hamstring, Groin, Calf)", "desc": "Acute and recurrent muscle tears requiring guided eccentric loading and scar remodeling.", "icon": "zap"},
            {"title": "Meniscus Tears & Runner's Knee", "desc": "Patellofemoral pain syndrome, IT band friction, and meniscus irritation from running and jumping.", "icon": "footprints"}
        ],
        "pathway": [
            {"step": "1. Biomechanical Kinetic Analysis", "desc": "Evaluating jumping mechanics, landing alignment, joint stability, and muscle asymmetry.", "icon": "search"},
            {"step": "2. Acute Tissue Decongestion", "desc": "Targeted manual therapy, ice compression, and Class IV laser to clear swelling and spasm.", "icon": "shield"},
            {"step": "3. Progressive Strength & Eccentric Load", "desc": "Rebuilding tensile tissue capacity with heavy-slow resistance and eccentric muscle loading.", "icon": "dumbbell"},
            {"step": "4. Agility & Return-to-Sport Testing", "desc": "Sport-specific drills, cutting maneuvers, and objective clearance testing before match return.", "icon": "award"}
        ],
        "benefits": [
            {"num": "01", "title": "Accelerated Tissue Remodeling", "desc": "Stimulates dense, parallel collagen fiber alignment for resilient tendon and ligament recovery."},
            {"num": "02", "title": "Corrects Kinetic Chain Deficits", "desc": "Eliminates compensatory weaknesses in the hips and core that cause recurrent joint breakdown."},
            {"num": "03", "title": "Objective Return-to-Play Criteria", "desc": "Uses validated functional hop and strength tests so you step back onto the field without fear."}
        ],
        "consult_expectations": "Your evaluation entails a physical examination of joint laxity, muscle firing patterns, and functional movement screens. We outline your exact timeline, phasing your recovery from acute protection to full athletic performance.",
        "precautions": "Athletic rehabilitation adheres to strict biological healing timelines. We never accelerate return-to-sport clearance prematurely before objective strength and neuromuscular criteria are verified.",
        "related": ["advanced-physiotherapy", "shockwave-therapy", "dry-needling-therapy"]
    },
    {
        "id": 18,
        "name": "Pre- and Post-TKR and THR Physiotherapy",
        "slug": "tkr-thr-physiotherapy",
        "category": "Joint Replacement",
        "meta_title": "Pre- and Post-TKR and THR Physiotherapy Hyderabad | Aarav Clinics",
        "meta_desc": "Specialized Pre- and Post-Total Knee Replacement (TKR) & Total Hip Replacement (THR) physiotherapy in Ashok Nagar, Near BHEL, Hyderabad. Safe phased recovery and mobility.",
        "badge": "Joint Replacement Rehabilitation",
        "hero_title": "TKR & THR Physiotherapy.",
        "hero_subtitle": "Pre- & Post-Surgical Recovery.",
        "hero_lead": "Dedicated clinical rehabilitation for Total Knee Replacement (TKR) and Total Hip Replacement (THR). Pre-operative conditioning and phased post-surgical functional recovery.",
        "hero_img": "assets/images/physiotherapy-session.jpg",
        "card_icon": "shield-check",
        "card_desc": "Phased pre-operative conditioning and post-surgical rehabilitation for Total Knee Replacement (TKR) and Total Hip Replacement (THR) procedures.",
        "about_eyebrow": "Surgical Rehabilitation Protocol",
        "about_heading": "Maximizing the outcome of your Total Knee and Total Hip Replacement surgery.",
        "about_lead": "The surgical success of a Total Knee Replacement (TKR) or Total Hip Replacement (THR) is realized through disciplined, expert postoperative rehabilitation.",
        "about_detail": "At Aarav Clinics, our joint replacement physiotherapy begins before your procedure with 'pre-habilitation'—building quadriceps strength, hip stability, and teaching safe post-surgical crutch and walker ambulation. Following surgery, our phased protocol manages postoperative swelling, restores knee flexion and extension, activates dormant gluteal muscles, prevents scar contractures, and transitions you smoothly from walking aids to independent, pain-free strides.",
        "conditions": [
            {"title": "Pre-Operative Conditioning (Pre-Hab)", "desc": "Strengthening knee and hip musculature prior to surgery to accelerate post-operative discharge recovery.", "icon": "shield"},
            {"title": "Post-TKR Knee Flexion & Extension", "desc": "Safely achieving 90° to 120° knee bend, full terminal extension, and patellar mobility.", "icon": "maximize"},
            {"title": "Post-THR Hip Precautions & Gait", "desc": "Safe hip mobilization, preventing dislocation risks, and rebuilding abductor stability.", "icon": "check-circle"},
            {"title": "Weaning from Walkers to Independent Steps", "desc": "Gradual progression from walker to quad-cane to natural, unassisted gait without limping.", "icon": "footprints"}
        ],
        "pathway": [
            {"step": "1. Post-Op Wound & Swelling Protocol", "desc": "Cryotherapy, gentle passive ankle pumps, and lymphatic elevation to reduce acute joint effusion.", "icon": "shield"},
            {"step": "2. Guided Joint Range Restoration", "desc": "Gentle manual patellar mobilization and active-assisted knee/hip slides to prevent scar adhesions.", "icon": "sliders"},
            {"step": "3. Quadriceps & Glute Re-Activation", "desc": "Isometric quad sets, straight leg raises, and glute bridges overcoming postoperative muscle inhibition.", "icon": "activity"},
            {"step": "4. Functional Gait & Stair Mastery", "desc": "Step-by-step training on level ground, stairs, and sit-to-stand transitions for complete self-reliance.", "icon": "trending-up"}
        ],
        "benefits": [
            {"num": "01", "title": "Full Functional Joint Mobility", "desc": "Prevents joint stiffness and arthrofibrosis, ensuring maximum bend and straight knee extension."},
            {"num": "02", "title": "Confident Limp-Free Ambulation", "desc": "Rebuilds hip abductor strength to eliminate post-surgical Trendelenburg limping."},
            {"num": "03", "title": "Safe Return to Active Daily Life", "desc": "Empowers patients to climb stairs, travel, and enjoy daily walks without fear of joint failure."}
        ],
        "consult_expectations": "We coordinate directly with your orthopedic surgeon's post-op protocol. Your initial session includes an inspection of incision healing, measurement of joint angles with a goniometer, and a gentle, supportive start to mobility exercises.",
        "precautions": "Strict adherence to your orthopedic surgeon's weight-bearing orders and hip precautions (such as avoiding flexion past 90 degrees or crossing legs in posterior THR) is rigorously maintained throughout treatment.",
        "related": ["advanced-physiotherapy", "geriatric-rehabilitation", "laser-therapy"]
    },
    {
        "id": 19,
        "name": "Laser Therapy",
        "slug": "laser-therapy",
        "category": "Advanced Technology",
        "meta_title": "Class IV Laser Therapy in Hyderabad | Aarav Clinics",
        "meta_desc": "High-intensity Class IV Laser Therapy in Ashok Nagar, Near BHEL, Hyderabad. Rapid non-invasive pain relief for osteoarthritis, plantar fasciitis, tendonitis, and sports injuries.",
        "badge": "Advanced Photobiomodulation",
        "hero_title": "Deep Tissue Laser.",
        "hero_subtitle": "Cellular-Level Phototherapy.",
        "hero_lead": "Accelerate cellular repair, resolve stubborn deep-tissue inflammation, and conquer chronic joint pain with medical-grade Class IV therapeutic laser technology.",
        "hero_img": "assets/images/hero-clinic.jpg",
        "card_icon": "sun",
        "card_desc": "Class IV deep-penetrating therapeutic laser delivering targeted light photons into deep tissues, rapidly resolving inflammation and stimulating mitochondrial repair.",
        "about_eyebrow": "Targeted Energy",
        "about_heading": "Healing injured tissue at the cellular mitochondrial level.",
        "about_lead": "Class IV Therapeutic Laser Therapy delivers specific therapeutic wavelengths of red and near-infrared light deep into damaged subcutaneous tissues.",
        "about_detail": "When light photons interact with cytochrome c oxidase within your cells' mitochondria, they trigger a surge in adenosine triphosphate (ATP) production. This cellular energy surge accelerates natural tissue repair, enhances local microcirculation, rapidly down-regulates inflammatory cytokines, and desensitizes pain receptors—penetrating arthritic joint capsules and dense tendon insertions that standard superficial modalities cannot reach.",
        "conditions": [
            {"title": "Plantar Fasciitis & Heel Pain", "desc": "Intense morning heel throbbing, thick plantar fascia inflammation, and calcaneal sensitivity.", "icon": "footprints"},
            {"title": "Knee Osteoarthritis & Synovitis", "desc": "Cartilage wear, chronic joint effusion, crepitus, and stiff knees upon standing.", "icon": "activity"},
            {"title": "Tendinopathies & Overuse Injuries", "desc": "Tennis elbow, Achilles tendinitis, supraspinatus rotator cuff strains, and wrist tendinopathy.", "icon": "crosshair"},
            {"title": "Frozen Shoulder & Acute Bursitis", "desc": "Severe night shoulder throbbing, adhesive capsulitis, and acute subacromial bursitis.", "icon": "shield"}
        ],
        "pathway": [
            {"step": "1. Diagnostic Anatomical Mapping", "desc": "Pinpointing target tissue depth, chronicity, and anatomical perimeter to calibrate laser dosage parameters.", "icon": "search"},
            {"step": "2. Certified Optical Safety", "desc": "Both patient and clinician wear wavelength-specific optical safety glasses for complete eye protection.", "icon": "glasses"},
            {"step": "3. Dynamic Laser Administration", "desc": "The laser handpiece sweeps smoothly over the target joint, delivering a soothing, therapeutic warmth.", "icon": "sun"},
            {"step": "4. Immediate Manual Integration", "desc": "Following laser application while tissue is relaxed, your therapist performs gentle joint mobilization.", "icon": "hand"}
        ],
        "benefits": [
            {"num": "01", "title": "Accelerates Cellular ATP Synthesis", "desc": "Energizes damaged cells to double their metabolic repair rate and collagen reconstruction."},
            {"num": "02", "title": "Rapid Anti-Inflammatory Action", "desc": "Flushes localized fluid edema and inhibits pro-inflammatory enzymes for immediate relief."},
            {"num": "03", "title": "Completely Non-Invasive & Soothing", "desc": "Delivers deep biological healing with zero needles, zero medication, and a comforting warm sensation."}
        ],
        "consult_expectations": "During your consultation, our certified laser therapist evaluates the depth and chronicity of your pain. You will be seated comfortably and provided with protective glasses. The laser wand glides smoothly over the area, producing a gentle, soothing warmth. Treatments last 10 to 20 minutes with zero post-session downtime.",
        "precautions": "Class IV Laser is contraindicated directly over active malignant lesions, directly over the gravid uterus during pregnancy, over the thyroid gland, or directly into the eyes. Protective wavelength eyewear is mandatory for everyone present during treatment.",
        "related": ["shockwave-therapy", "advanced-decompression-therapy", "advanced-physiotherapy"]
    }
]

print(f"Loaded {len(SERVICES)} approved services.")

# Dictionary lookup by slug
SERVICES_BY_SLUG = {s["slug"]: s for s in SERVICES}

# Icon SVG definitions for inline rendering
ICON_SVGS = {
    "activity": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
    "git-commit": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><line x1="1.05" y1="12" x2="7" y2="12"/><line x1="17.01" y1="12" x2="22.96" y2="12"/><line x1="12" y1="1.05" x2="12" y2="7"/><line x1="12" y1="17.01" x2="12" y2="22.96"/></svg>',
    "maximize-2": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>',
    "disc": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/></svg>',
    "crosshair": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="22" y1="12" x2="18" y2="12"/><line x1="6" y1="12" x2="2" y2="12"/><line x1="12" y1="6" x2="12" y2="2"/><line x1="12" y1="22" x2="12" y2="18"/></svg>',
    "heart": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
    "mic": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>',
    "puzzle": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19.439 7.85c-.049-.322-.28-.61-.62-.774a2.913 2.913 0 0 1-1.637-2.618A2.92 2.92 0 0 1 20.1 1.54c.348-.163.58-.452.628-.774a.836.836 0 0 0-.256-.732.844.844 0 0 0-.74-.184 7.07 7.07 0 0 0-5.732 5.732.846.846 0 0 0 .184.74.836.836 0 0 0 .732.256c.322-.048.611-.28.774-.628a2.914 2.914 0 0 1 2.618-1.637 2.92 2.92 0 0 1 2.918 2.918c0 .647-.215 1.25-.578 1.74a.836.836 0 0 0-.087.778z"/><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "eye": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>',
    "smile": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>',
    "book-open": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    "users": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "zap": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "brain": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 4.44-2.04z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-4.44-2.04z"/></svg>',
    "life-buoy": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><line x1="4.93" y1="4.93" x2="9.17" y2="9.17"/><line x1="14.83" y1="14.83" x2="19.07" y2="19.07"/><line x1="14.83" y1="9.17" x2="19.07" y2="4.93"/><line x1="14.83" y1="9.17" x2="19.07" y2="4.93"/><line x1="4.93" y1="19.07" x2="9.17" y2="14.83"/></svg>',
    "user-check": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>',
    "award": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>',
    "shield-check": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>',
    "sun": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>'
}

# Standard Navigation Header Component (Desktop + Mobile)
NAV_HEADER_HTML = """<header class="site-header theme-transparent theme-dark" id="siteHeader">
    <div class="wrap header-inner">
      <a class="brand" href="index.html" aria-label="Aarav Clinics — Home">
        <img src="assets/images/logo.png" alt="Aarav Clinics — A Complete Family Therapy Care" class="brand-logo"
          width="200" height="60">
      </a>

      <!-- Desktop Nav -->
      <nav class="main-nav" aria-label="Primary navigation">
        <ul class="main-nav" style="display:flex;align-items:center;gap:var(--space-1);list-style:none;">
          <li class="nav-item">
            <a href="index.html" class="nav-link">Home</a>
          </li>
          <li class="nav-item">
            <a href="about.html" class="nav-link">About</a>
          </li>
          <li class="nav-item">
            <a href="services.html" class="nav-link is-active" aria-haspopup="true">
              Services
                <!-- <svg class="nav-caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"
                aria-hidden="true">
                <polyline points="6 9 12 15 18 9" />
              </svg> -->
            </a>
   <!-- <div class="nav-drop nav-drop--mega" role="region" aria-label="Services menu">
              <div class="mega-cols">
                <div>
                  <p class="mega-group-title">Advanced Therapies</p>
                  <a href="shockwave-therapy.html" class="nav-drop-link">Shockwave Therapy</a>
                  <a href="advanced-decompression-therapy.html" class="nav-drop-link">Advanced Decompression</a>
                  <a href="cage-therapy.html" class="nav-drop-link">Cage Therapy</a>
                  <a href="cupping-therapy.html" class="nav-drop-link">Cupping Therapy</a>
                  <a href="dry-needling-therapy.html" class="nav-drop-link">Dry Needling Therapy</a>
                  <a href="laser-therapy.html" class="nav-drop-link">Laser Therapy</a>
                </div>
                <div>
                  <p class="mega-group-title">Rehabilitation Care</p>
                  <a href="advanced-physiotherapy.html" class="nav-drop-link">Advanced Physiotherapy</a>
                  <a href="stroke-rehabilitation.html" class="nav-drop-link">Stroke Rehabilitation</a>
                  <a href="paediatric-adult-rehabilitation.html" class="nav-drop-link">Paediatric &amp; Adult Rehab</a>
                  <a href="geriatric-rehabilitation.html" class="nav-drop-link">Geriatric Rehabilitation</a>
                  <a href="sports-injury-physiotherapy.html" class="nav-drop-link">Sports Injury Physiotherapy</a>
                  <a href="tkr-thr-physiotherapy.html" class="nav-drop-link">Pre- &amp; Post-TKR &amp; THR</a>
                  <a href="prenatal-postnatal-exercise-therapy.html" class="nav-drop-link">Prenatal &amp; Postnatal</a>
                </div>
                <div>
                  <p class="mega-group-title">Child Development</p>
                  <a href="speech-therapy-paediatric-adult.html" class="nav-drop-link">Speech Therapy</a>
                  <a href="occupational-therapy.html" class="nav-drop-link">Occupational Therapy</a>
                  <a href="vision-therapy.html" class="nav-drop-link">Vision Therapy</a>
                  <a href="behavioural-therapy.html" class="nav-drop-link">Behavioural Therapy</a>
                  <a href="special-education-therapy.html" class="nav-drop-link">Special Education Therapy</a>
                  <a href="parental-training.html" class="nav-drop-link">Parental Training</a>
                  <a href="services.html" class="nav-drop-link" style="font-weight:700;color:var(--teal);">All 19 Services &rarr;</a>
                </div>
              </div>
            </div> -->
          
          
          </li>
          <li class="nav-item">
            <a href="child-development.html" class="nav-link">Child Development</a>
          </li>
          <li class="nav-item">
            <a href="team.html" class="nav-link">Our Team</a>
          </li>
          <li class="nav-item">
            <a href="blog.html" class="nav-link">Blog</a>
          </li>
          <li class="nav-item">
            <a href="contact.html" class="nav-link">Contact</a>
          </li>
        </ul>
      </nav>

      <a href="contact.html#appointment" class="btn btn-primary nav-cta" style="margin-left:auto;">
        Book Appointment
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"
          class="btn-arrow" aria-hidden="true">
          <path d="M5 12h14M12 5l7 7-7 7" />
        </svg>
      </a>

      <!-- Mobile toggle -->
      <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Mobile Menu -->
  <nav class="mobile-menu" id="mobileMenu" aria-label="Mobile navigation" aria-hidden="true">
    <div class="mobile-menu-inner">
      <a href="index.html" class="mobile-nav-link">Home</a>
      <a href="about.html" class="mobile-nav-link">About</a>

      <button class="mobile-nav-link" data-mobile-toggle="mobileServSub" aria-expanded="false"
        style="width:100%;text-align:left;border:none;background:none;cursor:pointer;font:inherit;font-size:var(--text-lg);font-weight:600;color:var(--text-heading);">
        Services (19)
        <svg class="mobile-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
          stroke-width="2.5" style="transition:transform 0.3s" aria-hidden="true">
          <polyline points="6 9 12 15 18 9" />
        </svg>
      </button>
      <div id="mobileServSub" class="mobile-nav-sub">
        <a href="services.html" style="font-weight:700;color:var(--teal);">All 19 Clinical Services</a>
        <a href="shockwave-therapy.html">Shockwave Therapy</a>
        <a href="advanced-decompression-therapy.html">Advanced Decompression Therapy</a>
        <a href="cage-therapy.html">Cage Therapy</a>
        <a href="cupping-therapy.html">Cupping Therapy</a>
        <a href="dry-needling-therapy.html">Dry Needling Therapy</a>
        <a href="prenatal-postnatal-exercise-therapy.html">Prenatal &amp; Postnatal Exercise</a>
        <a href="speech-therapy-paediatric-adult.html">Speech Therapy (Paediatric &amp; Adult)</a>
        <a href="occupational-therapy.html">Occupational Therapy</a>
        <a href="vision-therapy.html">Vision Therapy</a>
        <a href="behavioural-therapy.html">Behavioural Therapy</a>
        <a href="special-education-therapy.html">Special Education Therapy</a>
        <a href="parental-training.html">Parental Training</a>
        <a href="advanced-physiotherapy.html">Advanced Physiotherapy</a>
        <a href="stroke-rehabilitation.html">Stroke Rehabilitation</a>
        <a href="paediatric-adult-rehabilitation.html">Paediatric &amp; Adult Rehabilitation</a>
        <a href="geriatric-rehabilitation.html">Geriatric Rehabilitation</a>
        <a href="sports-injury-physiotherapy.html">Sports Injury Physiotherapy</a>
        <a href="tkr-thr-physiotherapy.html">Pre- and Post-TKR &amp; THR</a>
        <a href="laser-therapy.html">Laser Therapy</a>
      </div>

      <a href="child-development.html" class="mobile-nav-link">Child Development</a>
      <a href="team.html" class="mobile-nav-link">Our Team</a>
      <a href="blog.html" class="mobile-nav-link">Blog</a>
      <a href="contact.html" class="mobile-nav-link">Contact</a>
    </div>
    <div class="mobile-menu-ctas">
      <a href="contact.html#appointment" class="btn btn-primary btn--block">Book an Appointment</a>
      <a href="https://wa.me/916302882910?text=Hi%20Aarav%20Clinics%2C%20I%20would%20like%20to%20book%20an%20appointment"
        target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn--block">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 0 1 8.413 3.488 11.82 11.82 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.513 5.26l-.999 3.648 3.985-1.045zm6.11-3.336c-.29-.145-1.71-.845-1.975-.94-.265-.1-.46-.145-.65.145-.195.29-.745.94-.915 1.135-.165.195-.335.22-.625.075-.29-.145-1.225-.45-2.335-1.44-.86-.77-1.44-1.72-1.61-2.01-.165-.29-.018-.445.125-.59.128-.128.29-.335.435-.5.145-.165.193-.29.29-.485.1-.195.048-.365-.025-.51-.072-.145-.65-1.565-.89-2.145-.235-.565-.475-.49-.65-.5-.167-.008-.36-.01-.55-.01-.19 0-.5.072-.765.36-.265.29-1.01.985-1.01 2.4s1.035 2.785 1.18 2.98c.145.195 2.035 3.105 4.935 4.355.69.298 1.23.475 1.65.605.693.219 1.325.188 1.824.114.556-.082 1.71-.7 1.95-1.376.24-.676.24-1.255.168-1.376-.073-.12-.265-.193-.555-.336z" />
        </svg>
        WhatsApp Us
      </a>
    </div>
  </nav>"""

# Standard Premium Footer Component
PREMIUM_FOOTER_HTML = """<footer class="premium-footer">
    <div class="footer-ambient-glow"></div>
    <div class="wrap footer-grid">
      <div class="footer-brand-col">
        <img src="assets/images/logo.png" alt="Aarav Clinics" width="180">
        <p class="footer-desc">Advanced physiotherapy, rehabilitation, and pediatric therapy in Hyderabad, delivering
          evidence-based clinical excellence.</p>
        <div class="footer-social">
          <a href="https://www.google.com/maps?cid=10521016619599487601" target="_blank" rel="noopener noreferrer" class="social-btn" aria-label="Google Maps"><i data-lucide="map-pin"></i></a>
          <a href="https://wa.me/916302882910" target="_blank" rel="noopener noreferrer" class="social-btn" aria-label="WhatsApp"><i data-lucide="message-circle"></i></a>
        </div>
      </div>

      <div class="footer-links-col">
        <h4>Clinical Services</h4>
        <a href="advanced-physiotherapy.html">Advanced Physiotherapy</a>
        <a href="shockwave-therapy.html">Shockwave Therapy</a>
        <a href="advanced-decompression-therapy.html">Advanced Decompression</a>
        <a href="stroke-rehabilitation.html">Stroke Rehabilitation</a>
        <a href="laser-therapy.html">Laser Therapy</a>
        <a href="sports-injury-physiotherapy.html">Sports Injury Physiotherapy</a>
        <a href="tkr-thr-physiotherapy.html">Pre- &amp; Post-TKR and THR</a>
        <a href="services.html">All 19 Clinical Services</a>
      </div>

      <div class="footer-links-col">
        <h4>Child Development</h4>
        <a href="speech-therapy-paediatric-adult.html">Speech Therapy</a>
        <a href="occupational-therapy.html">Occupational Therapy</a>
        <a href="vision-therapy.html">Vision Therapy</a>
        <a href="behavioural-therapy.html">Behavioural Therapy</a>
        <a href="special-education-therapy.html">Special Education Therapy</a>
        <a href="parental-training.html">Parental Training</a>
        <a href="cage-therapy.html">Cage Therapy</a>
        <a href="paediatric-adult-rehabilitation.html">Paediatric &amp; Adult Rehab</a>
      </div>

      <div class="footer-contact-col">
        <h4>Reach Us</h4>
        <p>HIG, 2nd Floor, Sai Sadan Enclave, Ashok Nagar, Near BHEL, Hyderabad - 502032</p>
        <a href="tel:+916302882910" class="footer-contact-link"><i data-lucide="phone"></i> +91 63028 82910</a>
        <a href="mailto:aaravphysioclinics@gmail.com" class="footer-contact-link"><i data-lucide="mail"></i>
          aaravphysioclinics@gmail.com</a>
        <div class="footer-hours">
          <span>Mon - Sat: 9:00 AM - 6:00 PM</span>
          <span>Sunday: By Appointment</span>
        </div>
      </div>
    </div>

    <div class="footer-bottom wrap">
      <p>&copy; 2026 Aarav Clinics. All rights reserved. Ashok Nagar, Near BHEL, Hyderabad.</p>
      <div style="display:flex;gap:1.5rem;">
        <a href="privacy-policy.html" style="color:var(--text-muted);text-decoration:none;">Privacy Policy</a>
        <a href="terms.html" style="color:var(--text-muted);text-decoration:none;">Terms of Service</a>
      </div>
    </div>
  </footer>"""

def build_individual_service_page(service):
    slug = service["slug"]
    name = service["name"]
    meta_title = service["meta_title"]
    meta_desc = service["meta_desc"]
    badge = service["badge"]
    hero_title = service["hero_title"]
    hero_subtitle = service["hero_subtitle"]
    hero_lead = service["hero_lead"]
    hero_img = service["hero_img"]
    about_eyebrow = service["about_eyebrow"]
    about_heading = service["about_heading"]
    about_lead = service["about_lead"]
    about_detail = service["about_detail"]
    conditions = service["conditions"]
    pathway = service["pathway"]
    benefits = service["benefits"]
    consult_expectations = service["consult_expectations"]
    precautions = service["precautions"]
    related_slugs = service["related"]

    # Bento condition cards HTML
    bento_html = ""
    for cond in conditions:
        bento_html += f"""
        <div class="bento-card bento-small gsap-item">
          <div class="bento-content-solid" style="border-top: 3px solid var(--color-teal);">
            <i data-lucide="{cond['icon']}" class="bento-icon" style="color:var(--color-teal);"></i>
            <h4>{cond['title']}</h4>
            <p style="font-size: 0.875rem; line-height: 1.5; color: #64748b;">{cond['desc']}</p>
          </div>
        </div>"""

    # 4-step pathway HTML
    pathway_html = ""
    for p in pathway:
        pathway_html += f"""
        <div class="tech-card gsap-item">
          <div class="tech-content">
            <div class="tech-icon"><i data-lucide="{p['icon']}"></i></div>
            <h3>{p['step']}</h3>
            <p>{p['desc']}</p>
          </div>
        </div>"""

    # Benefits rows HTML
    benefits_html = ""
    for b in benefits:
        benefits_html += f"""
        <div class="benefit-row">
          <div class="benefit-number">{b['num']}</div>
          <div class="benefit-desc">
            <h3>{b['title']}</h3>
            <p>{b['desc']}</p>
          </div>
        </div>"""

    # Related services cards HTML
    related_cards_html = ""
    for r_slug in related_slugs:
        r_svc = SERVICES_BY_SLUG.get(r_slug)
        if r_svc:
            icon_markup = ICON_SVGS.get(r_svc["card_icon"], f'<i data-lucide="{r_svc["card_icon"]}"></i>')
            related_cards_html += f"""
          <a href="{r_svc['slug']}.html" class="svc-card">
            <div class="svc-icon">
              {icon_markup}
            </div>
            <h3>{r_svc['name']}</h3>
            <p>{r_svc['card_desc']}</p>
            <span class="svc-learn">
              Explore Service
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M5 12h14M12 5l7 7-7 7" />
              </svg>
            </span>
          </a>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{meta_title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://aaravhealthcare.com/{slug}.html">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://aaravhealthcare.com/{slug}.html">
  <meta property="og:title" content="{meta_title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:image" content="https://aaravhealthcare.com/{hero_img}">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@200;300;400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Scripts -->
  <script src="https://unpkg.com/lucide@0.344.0/dist/umd/lucide.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js" defer></script>
  <script src="js/particle-bg.js" defer></script>

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="assets/images/logo.png">

  <!-- CSS -->
  <link rel="stylesheet" href="css/variables.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/layout.css">
  <link rel="stylesheet" href="css/buttons.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/hero.css">
  <link rel="stylesheet" href="css/sections.css">
  <link rel="stylesheet" href="css/inner.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/bg-animations.css">

  <!-- Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "MedicalWebPage",
    "name": "{name} - Aarav Clinics",
    "url": "https://aaravhealthcare.com/{slug}.html",
    "description": "{meta_desc}",
    "provider": {{
      "@type": "MedicalClinic",
      "name": "Aarav Clinics",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "HIG, 2nd Floor, Sai Sadan Enclave, Ashok Nagar",
        "addressLocality": "Hyderabad",
        "postalCode": "502032",
        "addressCountry": "IN"
      }},
      "telephone": "+916302882910"
    }}
  }}
  </script>
</head>
<body class="premium-theme">

<!-- Page Loader -->
<div class="premium-loader" id="pageLoader">
  <div class="premium-loader-brand">Aarav Clinics</div>
  <div class="premium-loader-bar"><div class="premium-loader-progress"></div></div>
</div>

{NAV_HEADER_HTML}

<main id="main">

  <!-- CINEMATIC HERO -->
  <section class="cinematic-hero hero--dark particle-canvas-container" style="background:#0f172a;">
    <div class="cinematic-hero-bg">
      <img src="{hero_img}" alt="{name} Session at Aarav Clinics" class="hero-parallax-img" style="filter: brightness(0.4) contrast(1.1);" onerror="this.src='assets/images/hero-clinic.jpg'">
      <div class="cinematic-overlay" style="background: radial-gradient(circle at 70% 30%, rgba(13, 148, 136, 0.25) 0%, rgba(15,23,42,1) 85%);"></div>
      <div class="cinematic-gradient"></div>
    </div>
    
    <div class="cinematic-hero-content wrap">
      <div class="hero-text-block">
        <div class="hero-badge gsap-reveal-up" style="border-color:rgba(13, 148, 136, 0.4); color:var(--color-teal);">
          <i data-lucide="activity"></i> {badge}
        </div>
        
        <h1 class="hero-giant-title">
          <span class="mask-line"><span class="gsap-title-reveal">{hero_title}</span></span>
          <span class="mask-line"><span class="gsap-title-reveal text-champagne">{hero_subtitle}</span></span>
        </h1>
        
        <p class="hero-editorial-desc gsap-reveal-up">
          {hero_lead}
        </p>
        
        <div class="hero-cta-group gsap-reveal-up">
          <a href="contact.html#appointment" class="btn btn-premium-solid btn-large">
            Book Consultation <i data-lucide="arrow-right"></i>
          </a>
          <a href="https://wa.me/916302882910?text=Hi%20Aarav%20Clinics%2C%20I%20would%20like%20to%20consult%20about%20{name}" target="_blank" rel="noopener noreferrer" class="btn btn-premium-outline btn-large">
            <i data-lucide="message-circle"></i> WhatsApp Us
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- EDITORIAL OVERVIEW: What the therapy involves -->
  <section class="editorial-about">
    <div class="wrap editorial-about-grid">
      <div class="about-content">
        <span class="premium-eyebrow accent-teal gsap-reveal-up">{about_eyebrow}</span>
        <h2 class="editorial-title gsap-word-reveal">{about_heading}</h2>
        <p class="editorial-lead gsap-text-progress">
          {about_lead}
        </p>
        <p class="gsap-reveal-up" style="color:#64748b; font-size:clamp(0.9rem, 1.1vw, 1.05rem); line-height:1.75; margin-bottom:2rem;">
          {about_detail}
        </p>
        <a href="#methodology" class="link-arrow">Explore Clinical Methodology <i data-lucide="arrow-right"></i></a>
      </div>
      
      <div class="about-visuals gsap-clip-reveal">
        <div class="img-frame img-primary" style="box-shadow: -20px 20px 60px rgba(13, 148, 136, 0.1);">
          <img src="{hero_img}" alt="{name} Treatment at Aarav Clinics" onerror="this.src='assets/images/physiotherapy-session.jpg'">
        </div>
        <div class="experience-badge" style="background:var(--color-navy);">
          <span class="exp-number" style="color:var(--color-champagne);">19</span>
          <span class="exp-text">Specialised<br>Services</span>
        </div>
      </div>
    </div>
  </section>

  <!-- CONDITIONS TREATED BENTO: Who may benefit -->
  <section class="services-bento-section">
    <div class="wrap">
      <div class="section-header-centered gsap-reveal-up">
        <span class="premium-eyebrow accent-teal">Clinical Indications</span>
        <h2 class="editorial-title">Who benefits most from {name}</h2>
        <p class="editorial-lead" style="margin-inline:auto;">Tailored clinical protocols addressing acute limitations, chronic restrictions, and functional rehabilitation goals.</p>
      </div>
      
      <div class="services-bento gsap-stagger-group">
        {bento_html}
      </div>
    </div>
  </section>

  <!-- METHODOLOGY / 4-PHASE CLINICAL PATHWAY -->
  <section id="methodology" class="advanced-therapy-section" style="background:#050d18;">
    <div class="wrap">
      <div class="section-header-dark gsap-reveal-up">
        <span class="premium-eyebrow" style="color:var(--color-champagne);">Clinical Pathway</span>
        <h2 class="editorial-title text-white gsap-word-reveal">How the treatment process works</h2>
        <p class="editorial-lead text-gray-400" style="margin-inline:auto;">Structured for meticulous assessment, comfortable delivery, and long-term functional stability.</p>
      </div>
      
      <div class="tech-bento-grid gsap-stagger-group">
        {pathway_html}
      </div>
    </div>
  </section>

  <!-- MEASURABLE BENEFITS & CONSULTATION EXPECTATIONS -->
  <section class="benefits-editorial">
    <div class="wrap">
      <div class="benefits-layout">
        <div class="benefits-intro gsap-reveal-up">
          <span class="premium-eyebrow accent-teal">Treatment Outcomes</span>
          <h2 class="giant-editorial-text">Measurable goals you can expect.</h2>
          <p style="color:#64748b; margin-top:1.5rem; line-height:1.7;">
            Our evidence-based protocols are designed around concrete functional milestones—helping you move easier, build stability, and restore independence.
          </p>
        </div>
        
        <div class="benefits-list gsap-stagger-list">
          {benefits_html}
        </div>
      </div>

      <!-- Consultation Expectations & Precautions Box -->
      <div style="margin-top: clamp(3rem, 5vw, 5rem); display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: var(--space-6);">
        <div style="background:var(--white); border:1px solid var(--border-card); border-radius:var(--radius-xl); padding:var(--space-8); box-shadow:var(--shadow-sm);">
          <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1rem;color:var(--teal);">
            <i data-lucide="clipboard-check" style="width:24px;height:24px;"></i>
            <h3 style="margin:0;font-size:var(--text-lg);font-weight:700;color:var(--text-heading);">What to Expect in Your Consultation</h3>
          </div>
          <p style="color:var(--text-body);font-size:var(--text-sm);line-height:1.7;margin:0;">
            {consult_expectations}
          </p>
        </div>

        <div style="background:#faf8f5; border:1px solid rgba(208, 167, 106, 0.3); border-radius:var(--radius-xl); padding:var(--space-8); box-shadow:var(--shadow-sm);">
          <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1rem;color:#b45309;">
            <i data-lucide="alert-circle" style="width:24px;height:24px;"></i>
            <h3 style="margin:0;font-size:var(--text-lg);font-weight:700;color:var(--text-heading);">Clinical Precautions &amp; Suitability</h3>
          </div>
          <p style="color:#78350f;font-size:var(--text-sm);line-height:1.7;margin:0;">
            {precautions}
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- CINEMATIC APPOINTMENT -->
  <section class="appointment-cinematic">
    <div class="wrap appointment-split">
      <div class="appointment-visual gsap-reveal-up" style="padding-left:5%;">
        <span class="premium-eyebrow">Expert Consultation</span>
        <h2>Begin your healing journey today.</h2>
        <p>Book your clinical evaluation at our Ashok Nagar clinic or request home-based therapy support across Hyderabad.</p>
        
        <div class="contact-methods">
          <div class="contact-method">
            <i data-lucide="phone"></i>
            <div>
              <strong>+91 63028 82910</strong>
              <span>Front Desk &amp; Appointment Desk</span>
            </div>
          </div>
          <div class="contact-method">
            <i data-lucide="map-pin"></i>
            <div>
              <strong>Sai Sadan Enclave, Ashok Nagar</strong>
              <span>Hyderabad - 502032</span>
            </div>
          </div>
          <div class="contact-method">
            <i data-lucide="clock"></i>
            <div>
              <strong>Mon - Sat: 9:00 AM - 6:00 PM</strong>
              <span>Sunday: By Prior Appointment</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="appointment-form-container gsap-scale-up">
        <form class="premium-form" id="apptForm">
          <h3 class="form-title">Consult for {name}</h3>
          
          <div class="form-group">
            <label for="name">Patient Full Name</label>
            <input type="text" id="name" class="premium-input" placeholder="e.g. Rahul Sharma" required>
          </div>

          <div class="form-group">
            <label for="phone">Contact Number</label>
            <input type="tel" id="phone" class="premium-input" placeholder="10-digit mobile number" required>
          </div>
          
          <div class="form-group">
            <label for="service">Requested Service</label>
            <select id="service" class="premium-input">
              <option selected>{name}</option>
              <option>Advanced Physiotherapy</option>
              <option>Shockwave Therapy</option>
              <option>Advanced Decompression Therapy</option>
              <option>Laser Therapy</option>
              <option>Speech Therapy</option>
              <option>Occupational Therapy</option>
              <option>Child Development Consultation</option>
            </select>
          </div>
          
          <div class="form-group">
            <label for="message">Symptoms or Notes (Optional)</label>
            <textarea id="message" class="premium-input" rows="3" placeholder="Briefly describe your condition or duration of symptoms"></textarea>
          </div>
          
          <button type="submit" class="btn btn-whatsapp-solid btn-block" style="width:100%;">
            <i data-lucide="message-circle"></i> Continue to WhatsApp Booking
          </button>
          <p class="form-disclaimer">Instant front desk connection. Opens WhatsApp with your pre-filled inquiry details.</p>
        </form>
      </div>
    </div>
  </section>

  <!-- RELATED SERVICES SECTION (From Approved 19 Only) -->
  <section class="related-services-section">
    <div class="wrap">
      <div class="section-head reveal" style="text-align:left;max-width:none;margin-inline:0;">
        <span class="eyebrow">Complementary Care</span>
        <h2 class="section-title">Related Clinical Specialties</h2>
        <p class="lead">Explore coordinated multidisciplinary rehabilitation options offered at Aarav Clinics.</p>
      </div>
      
      <div class="grid-3 stagger">
        {related_cards_html}
      </div>
    </div>
  </section>

</main>

{PREMIUM_FOOTER_HTML}

<!-- Scripts -->
<script src="js/navigation.js"></script>
<script src="js/animations.js"></script>
<script>
  // Initialize Lucide icons
  lucide.createIcons();

  // Handle WhatsApp Form Submit
  document.getElementById('apptForm')?.addEventListener('submit', function(e) {{
    e.preventDefault();
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone')?.value || '';
    const service = document.getElementById('service').value;
    const notes = document.getElementById('message')?.value || '';
    const msg = `Hi Aarav Clinics, I would like to book a consultation for ${{service}}.\\nPatient Name: ${{name}}\\nPhone: ${{phone}}\\nNotes: ${{notes}}`;
    const url = `https://wa.me/916302882910?text=${{encodeURIComponent(msg)}}`;
    window.open(url, '_blank');
  }});
</script>

</body>
</html>
"""
    return html

def build_services_listing_page():
    # Build the 19 cards across 3 sections
    # Section 1: Advanced Technologies (6 cards: Shockwave, Decompression, Cage, Cupping, Dry Needling, Laser)
    # Section 2: Musculoskeletal & Neurological Rehabilitation (7 cards: Advanced Physio, Stroke, Paediatric & Adult, Geriatric, Sports Injury, Pre/Post-TKR & THR, Prenatal & Postnatal)
    # Section 3: Child Development & Cognitive-Behavioral (6 cards: Speech, OT, Vision, Behavioural, Special Education, Parental Training)

    cat1_ids = [1, 2, 3, 4, 5, 19]
    cat2_ids = [13, 14, 15, 16, 17, 18, 6]
    cat3_ids = [7, 8, 9, 10, 11, 12]

    def render_cards(id_list):
        out = ""
        for s_id in id_list:
            s = next(item for item in SERVICES if item["id"] == s_id)
            icon_markup = ICON_SVGS.get(s["card_icon"], f'<i data-lucide="{s["card_icon"]}"></i>')
            out += f"""
          <!-- {s['name']} -->
          <a href="{s['slug']}.html" class="svc-card reveal">
            <div class="svc-icon">
              {icon_markup}
            </div>
            <h3>{s['name']}</h3>
            <p>{s['card_desc']}</p>
            <span class="svc-learn">
              Explore Service
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true">
                <path d="M5 12h14M12 5l7 7-7 7" />
              </svg>
            </span>
          </a>"""
        return out

    cards_cat1 = render_cards(cat1_ids)
    cards_cat2 = render_cards(cat2_ids)
    cards_cat3 = render_cards(cat3_ids)

    html = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>19 Specialised Clinical Services &amp; Rehabilitation Care – Aarav Clinics Hyderabad</title>
  <meta name="description"
    content="Explore the complete directory of 19 specialised clinical rehabilitation services at Aarav Clinics Hyderabad: advanced physiotherapy, shockwave, decompression, stroke recovery, and child development therapies.">
  <link rel="canonical" href="https://aaravhealthcare.com/services.html">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://aaravhealthcare.com/services.html">
  <meta property="og:title" content="19 Specialised Clinical Services – Aarav Clinics">
  <meta property="og:description"
    content="Personalized physiotherapy, advanced technology therapies, stroke rehabilitation, and child development in Ashok Nagar, Near BHEL, Hyderabad.">
  <meta property="og:image" content="https://aaravhealthcare.com/assets/images/physiotherapy-session.jpg">

  <!-- Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
    rel="stylesheet">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="assets/images/logo.png">

  <!-- CSS -->
  <link rel="stylesheet" href="css/variables.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/layout.css">
  <link rel="stylesheet" href="css/buttons.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/hero.css">
  <link rel="stylesheet" href="css/sections.css">
  <link rel="stylesheet" href="css/inner.css">
  <link rel="stylesheet" href="css/footer.css">
  <link rel="stylesheet" href="css/animations.css">
  <link rel="stylesheet" href="css/bg-animations.css">

  <!-- Schema.org -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "MedicalWebPage",
    "name": "Aarav Clinics Specialised Therapy Services",
    "url": "https://aaravhealthcare.com/services.html",
    "description": "Complete catalog of 19 adult and paediatric clinical therapy services provided by Aarav Clinics in Ashok Nagar, Near BHEL, Hyderabad."
  }}
  </script>
  <script src="js/particle-bg.js" defer></script>
</head>

<body>

  <!-- Skip link -->
  <a class="skip-link" href="#main">Skip to main content</a>

  {NAV_HEADER_HTML}

  <!-- Main -->
  <main id="main">

    <!-- Page Hero -->
    <section class="page-hero particle-canvas-container" aria-label="Aarav Clinics Services">
      <div class="wrap page-hero-inner">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb-separator">/</span>
          <span class="breadcrumb-current">All Services</span>
        </nav>

        <div class="page-hero-badge">Comprehensive Clinical Directory · 19 Specialised Services</div>
        <h1 class="page-hero-title">Evidence-Based Rehabilitation &amp; Child Development</h1>
        <p class="page-hero-lead">
          From advanced pain technology and stroke neuro-rehabilitation to comprehensive paediatric developmental milestones, our specialized
          departments provide expert, coordinated care for your entire family.
        </p>

        <div class="page-hero-actions">
          <a href="contact.html#appointment" class="btn btn-primary">Book Consultation</a>
          <a href="https://wa.me/916302882910?text=Hi%20Aarav%20Clinics%2C%20I%20need%20guidance%20on%20choosing%20a%20service"
            target="_blank" rel="noopener noreferrer" class="btn btn-ghost">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path
                d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 0 1 8.413 3.488 11.82 11.82 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.513 5.26l-.999 3.648 3.985-1.045zm6.11-3.336c-.29-.145-1.71-.845-1.975-.94-.265-.1-.46-.145-.65.145-.195.29-.745.94-.915 1.135-.165.195-.335.22-.625.075-.29-.145-1.225-.45-2.335-1.44-.86-.77-1.44-1.72-1.61-2.01-.165-.29-.018-.445.125-.59.128-.128.29-.335.435-.5.145-.165.193-.29.29-.485.1-.195.048-.365-.025-.51-.072-.145-.65-1.565-.89-2.145-.235-.565-.475-.49-.65-.5-.167-.008-.36-.01-.55-.01-.19 0-.5.072-.765.36-.265.29-1.01.985-1.01 2.4s1.035 2.785 1.18 2.98c.145.195 2.035 3.105 4.935 4.355.69.298 1.23.475 1.65.605.693.219 1.325.188 1.824.114.556-.082 1.71-.7 1.95-1.376.24-.676.24-1.255.168-1.376-.073-.12-.265-.193-.555-.336z" />
            </svg>
            Ask on WhatsApp
          </a>
        </div>

        <div class="page-hero-pills">
          <span class="hero-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M20 6L9 17l-5-5" />
            </svg>
            Exactly 19 Clinical Services
          </span>
          <span class="hero-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M20 6L9 17l-5-5" />
            </svg>
            Ashok Nagar, Near BHEL, Hyderabad
          </span>
          <span class="hero-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M20 6L9 17l-5-5" />
            </svg>
            Personalised Care Plans
          </span>
        </div>
      </div>
    </section>

    <!-- Section 1: Advanced Technologies & Specialized Therapies (6 Services) -->
    <section class="section section--white" id="advanced-therapies">
      <div class="wrap">
        <div class="section-head reveal" style="text-align:left;max-width:none;margin-inline:0;">
          <span class="eyebrow">Advanced Clinical Technologies</span>
          <h2 class="section-title">Specialized Medical Technologies</h2>
          <p class="lead">Non-invasive therapeutic equipment operating at the cellular level to accelerate deep tissue healing, reduce chronic nerve compression, and break calcifications.</p>
        </div>

        <div class="grid-3 stagger">
          {cards_cat1}
        </div>
      </div>
    </section>

    <!-- Section 2: Physical & Neurological Rehabilitation (7 Services) -->
    <section class="section section--surface" id="rehabilitation">
      <div class="wrap">
        <div class="section-head reveal" style="text-align:left;max-width:none;margin-inline:0;">
          <span class="eyebrow">Physical &amp; Neurological Recovery</span>
          <h2 class="section-title">Comprehensive Rehabilitation Programs</h2>
          <p class="lead">Restoring mobility, relieving acute pain, and rebuilding strength through evidence-based musculoskeletal, post-operative, and neuro therapies.</p>
        </div>

        <div class="grid-3 stagger">
          {cards_cat2}
        </div>
      </div>
    </section>

    <!-- Section 3: Child Development & Cognitive-Behavioral Therapies (6 Services) -->
    <section class="section section--white" id="child-development">
      <div class="wrap">
        <div class="section-head reveal" style="text-align:left;max-width:none;margin-inline:0;">
          <span class="eyebrow">Child Development &amp; Family Care</span>
          <h2 class="section-title">Pediatric Therapy &amp; Family Coaching</h2>
          <p class="lead">Early identification, play-based therapy, and compassionate family coaching helping every child flourish across speech, sensory, learning, and behavioral milestones.</p>
        </div>

        <div class="grid-3 stagger">
          {cards_cat3}
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="section cta-section" aria-label="Book an appointment">
      <div class="wrap">
        <div class="cta-inner reveal">
          <span class="eyebrow">Ready to Move Better?</span>
          <h2>Consult with our specialists today</h2>
          <p>Book an appointment at our Ashok Nagar clinic or connect directly with our therapists for guidance on the right therapy for your needs.</p>
          <div class="cta-actions">
            <a href="contact.html#appointment" class="btn btn-primary btn--lg">Book an Appointment</a>
            <a href="https://wa.me/916302882910?text=Hi%20Aarav%20Clinics%2C%20I%20would%20like%20to%20book%20an%20appointment"
              target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn--lg">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path
                  d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 0 1 8.413 3.488 11.82 11.82 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.513 5.26l-.999 3.648 3.985-1.045zm6.11-3.336c-.29-.145-1.71-.845-1.975-.94-.265-.1-.46-.145-.65.145-.195.29-.745.94-.915 1.135-.165.195-.335.22-.625.075-.29-.145-1.225-.45-2.335-1.44-.86-.77-1.44-1.72-1.61-2.01-.165-.29-.018-.445.125-.59.128-.128.29-.335.435-.5.145-.165.193-.29.29-.485.1-.195.048-.365-.025-.51-.072-.145-.65-1.565-.89-2.145-.235-.565-.475-.49-.65-.5-.167-.008-.36-.01-.55-.01-.19 0-.5.072-.765.36-.265.29-1.01.985-1.01 2.4s1.035 2.785 1.18 2.98c.145.195 2.035 3.105 4.935 4.355.69.298 1.23.475 1.65.605.693.219 1.325.188 1.824.114.556-.082 1.71-.7 1.95-1.376.24-.676.24-1.255.168-1.376-.073-.12-.265-.193-.555-.336z" />
              </svg>
              WhatsApp Us
            </a>
          </div>
        </div>
      </div>
    </section>

  </main>

  {PREMIUM_FOOTER_HTML}

  <!-- Mobile FAB -->
  <div class="mobile-fab-bar" aria-label="Quick contact actions">
    <a href="tel:+916302882910" class="mobile-fab-btn mobile-fab-btn--call" aria-label="Call Aarav Clinics">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"
        aria-hidden="true">
        <path
          d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z" />
      </svg>
      Call
    </a>
    <a href="https://wa.me/916302882910?text=Hi%20Aarav%20Clinics%2C%20I%20would%20like%20to%20book%20an%20appointment"
      target="_blank" rel="noopener noreferrer" class="mobile-fab-btn mobile-fab-btn--wa"
      aria-label="WhatsApp Aarav Clinics">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path
          d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 0 1 8.413 3.488 11.82 11.82 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.513 5.26l-.999 3.648 3.985-1.045zm6.11-3.336c-.29-.145-1.71-.845-1.975-.94-.265-.1-.46-.145-.65.145-.195.29-.745.94-.915 1.135-.165.195-.335.22-.625.075-.29-.145-1.225-.45-2.335-1.44-.86-.77-1.44-1.72-1.61-2.01-.165-.29-.018-.445.125-.59.128-.128.29-.335.435-.5.145-.165.193-.29.29-.485.1-.195.048-.365-.025-.51-.072-.145-.65-1.565-.89-2.145-.235-.565-.475-.49-.65-.5-.167-.008-.36-.01-.55-.01-.19 0-.5.072-.765.36-.265.29-1.01.985-1.01 2.4s1.035 2.785 1.18 2.98c.145.195 2.035 3.105 4.935 4.355.69.298 1.23.475 1.65.605.693.219 1.325.188 1.824.114.556-.082 1.71-.7 1.95-1.376.24-.676.24-1.255.168-1.376-.073-.12-.265-.193-.555-.336z" />
      </svg>
      WhatsApp
    </a>
    <a href="contact.html#appointment" class="mobile-fab-btn mobile-fab-btn--book" aria-label="Book appointment">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"
        aria-hidden="true">
        <rect x="3" y="4" width="18" height="18" rx="2" />
        <line x1="16" y1="2" x2="16" y2="6" />
        <line x1="8" y1="2" x2="8" y2="6" />
        <line x1="3" y1="10" x2="21" y2="10" />
      </svg>
      Book
    </a>
  </div>

  <!-- Scripts -->
  <script src="js/navigation.js"></script>
  <script src="js/animations.js"></script>

</body>

</html>
"""
    return html

def build_redirect_page(target_slug, service_name):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={target_slug}.html">
  <title>Redirecting to {service_name} | Aarav Clinics</title>
  <link rel="canonical" href="https://aaravhealthcare.com/{target_slug}.html">
  <script>window.location.href = "{target_slug}.html";</script>
</head>
<body style="font-family:sans-serif;text-align:center;padding:50px;">
  <h2>Page Moved</h2>
  <p>This service page has been updated to <a href="{target_slug}.html">{service_name}</a>.</p>
  <p>Redirecting you now...</p>
</body>
</html>
"""

def update_sitemap():
    sitemap_path = "sitemap.xml"
    if not os.path.exists(sitemap_path):
        return

    # Create fresh sitemap with all 19 services
    service_urls_xml = ""
    for s in SERVICES:
        service_urls_xml += f"""  <url>
    <loc>https://aaravhealthcare.com/{s['slug']}.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>
"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Core Pages -->
  <url>
    <loc>https://aaravhealthcare.com/</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/about.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/services.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/child-development.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/team.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/blog.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/contact.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- 19 Specialised Clinical Services -->
{service_urls_xml}
  <!-- Team & Legal -->
  <url>
    <loc>https://aaravhealthcare.com/dr-sneha-reddy.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/dr-karthik-varma.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/dr-ananya-iyer.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/privacy-policy.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://aaravhealthcare.com/terms.html</loc>
    <lastmod>2026-10-15</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
</urlset>
"""
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Updated sitemap.xml with all 19 services.")

def update_shared_navigation_and_footers():
    # Update mega menu and footer across other shared pages
    pages = [
        "index.html", "about.html", "child-development.html", "team.html", 
        "blog.html", "contact.html", "privacy-policy.html", "terms.html",
        "dr-sneha-reddy.html", "dr-karthik-varma.html", "dr-ananya-iyer.html"
    ]

    mega_regex = re.compile(r'<div class="nav-drop nav-drop--mega"[^>]*>.*?</div>\s*</div>\s*</div>', re.DOTALL)
    mobile_sub_regex = re.compile(r'<div id="mobileServSub" class="mobile-nav-sub">.*?</div>', re.DOTALL)

    new_mega_content = """<div class="nav-drop nav-drop--mega" role="region" aria-label="Services menu">
              <div class="mega-cols">
                <div>
                  <p class="mega-group-title">Advanced Therapies</p>
                  <a href="shockwave-therapy.html" class="nav-drop-link">Shockwave Therapy</a>
                  <a href="advanced-decompression-therapy.html" class="nav-drop-link">Advanced Decompression</a>
                  <a href="cage-therapy.html" class="nav-drop-link">Cage Therapy</a>
                  <a href="cupping-therapy.html" class="nav-drop-link">Cupping Therapy</a>
                  <a href="dry-needling-therapy.html" class="nav-drop-link">Dry Needling Therapy</a>
                  <a href="laser-therapy.html" class="nav-drop-link">Laser Therapy</a>
                </div>
                <div>
                  <p class="mega-group-title">Rehabilitation Care</p>
                  <a href="advanced-physiotherapy.html" class="nav-drop-link">Advanced Physiotherapy</a>
                  <a href="stroke-rehabilitation.html" class="nav-drop-link">Stroke Rehabilitation</a>
                  <a href="paediatric-adult-rehabilitation.html" class="nav-drop-link">Paediatric &amp; Adult Rehab</a>
                  <a href="geriatric-rehabilitation.html" class="nav-drop-link">Geriatric Rehabilitation</a>
                  <a href="sports-injury-physiotherapy.html" class="nav-drop-link">Sports Injury Physiotherapy</a>
                  <a href="tkr-thr-physiotherapy.html" class="nav-drop-link">Pre- &amp; Post-TKR &amp; THR</a>
                  <a href="prenatal-postnatal-exercise-therapy.html" class="nav-drop-link">Prenatal &amp; Postnatal</a>
                </div>
                <div>
                  <p class="mega-group-title">Child Development</p>
                  <a href="speech-therapy-paediatric-adult.html" class="nav-drop-link">Speech Therapy</a>
                  <a href="occupational-therapy.html" class="nav-drop-link">Occupational Therapy</a>
                  <a href="vision-therapy.html" class="nav-drop-link">Vision Therapy</a>
                  <a href="behavioural-therapy.html" class="nav-drop-link">Behavioural Therapy</a>
                  <a href="special-education-therapy.html" class="nav-drop-link">Special Education Therapy</a>
                  <a href="parental-training.html" class="nav-drop-link">Parental Training</a>
                  <a href="services.html" class="nav-drop-link" style="font-weight:700;color:var(--teal);">All 19 Services &rarr;</a>
                </div>
              </div>
            </div>"""

    new_mobile_sub_content = """<div id="mobileServSub" class="mobile-nav-sub">
        <a href="services.html" style="font-weight:700;color:var(--teal);">All 19 Clinical Services</a>
        <a href="shockwave-therapy.html">Shockwave Therapy</a>
        <a href="advanced-decompression-therapy.html">Advanced Decompression Therapy</a>
        <a href="cage-therapy.html">Cage Therapy</a>
        <a href="cupping-therapy.html">Cupping Therapy</a>
        <a href="dry-needling-therapy.html">Dry Needling Therapy</a>
        <a href="prenatal-postnatal-exercise-therapy.html">Prenatal &amp; Postnatal Exercise</a>
        <a href="speech-therapy-paediatric-adult.html">Speech Therapy (Paediatric &amp; Adult)</a>
        <a href="occupational-therapy.html">Occupational Therapy</a>
        <a href="vision-therapy.html">Vision Therapy</a>
        <a href="behavioural-therapy.html">Behavioural Therapy</a>
        <a href="special-education-therapy.html">Special Education Therapy</a>
        <a href="parental-training.html">Parental Training</a>
        <a href="advanced-physiotherapy.html">Advanced Physiotherapy</a>
        <a href="stroke-rehabilitation.html">Stroke Rehabilitation</a>
        <a href="paediatric-adult-rehabilitation.html">Paediatric &amp; Adult Rehabilitation</a>
        <a href="geriatric-rehabilitation.html">Geriatric Rehabilitation</a>
        <a href="sports-injury-physiotherapy.html">Sports Injury Physiotherapy</a>
        <a href="tkr-thr-physiotherapy.html">Pre- and Post-TKR &amp; THR</a>
        <a href="laser-therapy.html">Laser Therapy</a>
      </div>"""

    for page in pages:
        if not os.path.exists(page):
            continue
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()

        # Update mega menu
        if mega_regex.search(content):
            content = mega_regex.sub(new_mega_content, content)
        
        # Update mobile nav sub
        if mobile_sub_regex.search(content):
            content = mobile_sub_regex.sub(new_mobile_sub_content, content)

        # Update footer clinical services links if present
        # In pages with .footer-links-col
        content = re.sub(
            r'<h4>Clinical Services</h4>.*?</div>\s*<div class="footer-links-col">',
            """<h4>Clinical Services</h4>
        <a href="advanced-physiotherapy.html">Advanced Physiotherapy</a>
        <a href="shockwave-therapy.html">Shockwave Therapy</a>
        <a href="advanced-decompression-therapy.html">Advanced Decompression</a>
        <a href="stroke-rehabilitation.html">Stroke Rehabilitation</a>
        <a href="laser-therapy.html">Laser Therapy</a>
        <a href="sports-injury-physiotherapy.html">Sports Injury Physiotherapy</a>
        <a href="tkr-thr-physiotherapy.html">Pre- &amp; Post-TKR &amp; THR</a>
        <a href="services.html">All 19 Services</a>
      </div>
      <div class="footer-links-col">""",
            content,
            flags=re.DOTALL
        )

        with open(page, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated navigation and footer links in {page}")

def main():
    print("Beginning Services System Transformation...")

    # 1. Generate all 19 individual service pages
    print("\n--- Generating 19 Individual Service Pages ---")
    for svc in SERVICES:
        slug = svc["slug"]
        filename = f"{slug}.html"
        html = build_individual_service_page(svc)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created/Updated: {filename} -> {svc['name']}")

    # 2. Build and write the updated services listing page
    print("\n--- Building Services Listing Page (services.html) ---")
    services_html = build_services_listing_page()
    with open("services.html", "w", encoding="utf-8") as f:
        f.write(services_html)
    print("services.html updated with exactly 19 unique services across 3 sections.")

    # 3. Create redirect files for legacy URLs to preserve backlinks / bookmarks
    print("\n--- Creating Legacy Redirects ---")
    legacy_redirects = {
        "physiotherapy.html": ("advanced-physiotherapy", "Advanced Physiotherapy"),
        "sports-rehabilitation.html": ("sports-injury-physiotherapy", "Sports Injury Physiotherapy"),
        "post-surgical-rehabilitation.html": ("tkr-thr-physiotherapy", "Pre- and Post-TKR and THR Physiotherapy"),
        "speech-therapy.html": ("speech-therapy-paediatric-adult", "Speech Therapy for Paediatric and Adult Patients"),
        "pediatric-physiotherapy.html": ("paediatric-adult-rehabilitation", "Paediatric and Adult Rehabilitation"),
        "autism-therapy.html": ("behavioural-therapy", "Behavioural Therapy"),
        "chiropractic.html": ("advanced-decompression-therapy", "Advanced Decompression Therapy")
    }

    for leg_file, (target_slug, name) in legacy_redirects.items():
        redirect_html = build_redirect_page(target_slug, name)
        with open(leg_file, "w", encoding="utf-8") as f:
            f.write(redirect_html)
        print(f"Created redirect: {leg_file} -> {target_slug}.html ({name})")

    # 4. Update shared navigation & footers
    print("\n--- Updating Shared Navigation & Footers Across Website ---")
    update_shared_navigation_and_footers()

    # 5. Update Sitemap
    print("\n--- Updating sitemap.xml ---")
    update_sitemap()

    print("\nTransformation Complete! 19 Services Fully Active.")

if __name__ == "__main__":
    main()
