from django.core.management.base import BaseCommand
from pandals.models import Pandal

class Command(BaseCommand):
    help = "Load REAL famous Durga Puja pandals"

    def handle(self, *args, **kwargs):

        Pandal.objects.all().delete()

        pandals = [

            # NORTH KOLKATA
            ("Bagbazar Sarbojanin","North Kolkata",22.6031,88.3650,"Heritage",4.9),
            ("Kumartuli Park","North Kolkata",22.6023,88.3624,"Traditional",4.8),
            ("Ahiritola Sarbojanin","North Kolkata",22.5997,88.3633,"Theme",4.7),

            # CENTRAL
            ("College Square","Central Kolkata",22.5735,88.3636,"Lighting",4.9),
            ("Md Ali Park","Central Kolkata",22.5724,88.3545,"Theme",4.7),
            ("Santosh Mitra Square","Central Kolkata",22.5885,88.3663,"Theme",4.8),

            # SOUTH
            ("Deshapriya Park","South Kolkata",22.5173,88.3522,"Theme",4.9),
            ("Ekdalia Evergreen","South Kolkata",22.5176,88.3631,"Heritage",4.8),
            ("Tridhara Sammilani","South Kolkata",22.5166,88.3654,"Theme",4.8),
            ("Suruchi Sangha","South Kolkata",22.5011,88.3472,"Theme",4.7),
            ("Chetla Agrani","South Kolkata",22.5098,88.3421,"Theme",4.8),

            # SALT LAKE
            ("FD Block Salt Lake","Salt Lake",22.5866,88.4176,"Theme",4.7),
            ("BJ Block Salt Lake","Salt Lake",22.5878,88.4155,"Theme",4.6),

            # HOWRAH
            ("Belur Math","Howrah",22.6321,88.3553,"Heritage",5.0),
            ("Liluah Sarbojanin","Howrah",22.6004,88.3308,"Theme",4.8),
            ("Howrah Maidan Sarbojanin","Howrah",22.5862,88.3433,"Theme",4.7),
            # NORTH KOLKATA
    ("Hatibagan Sarbojanin","North Kolkata",22.6029,88.3701,"Theme",4.8),
    ("Kashi Bose Lane","North Kolkata",22.5956,88.3709,"Traditional",4.7),
    ("Sovabazar Rajbari","North Kolkata",22.5969,88.3659,"Heritage",4.9),
    ("Shyambazar Friends Union","North Kolkata",22.5993,88.3732,"Theme",4.8),
    ("Paikpara Sarbojanin","North Kolkata",22.6182,88.3832,"Theme",4.7),

    # CENTRAL KOLKATA
    ("Sealdah Railway Athletic Club","Central Kolkata",22.5679,88.3728,"Theme",4.8),
    ("Lebutala Park","Central Kolkata",22.5643,88.3558,"Theme",4.7),
    ("Wellington Square","Central Kolkata",22.5567,88.3609,"Theme",4.6),
    ("Entally Sarbojanin","Central Kolkata",22.5569,88.3753,"Theme",4.7),
    ("Moulali Yubak Brinda","Central Kolkata",22.5604,88.3689,"Theme",4.8),

    # SOUTH KOLKATA
    ("Ballygunge Cultural Association","South Kolkata",22.5236,88.3662,"Theme",4.9),
    ("Hindustan Park","South Kolkata",22.5209,88.3639,"Theme",4.8),
    ("Mudiali Club","South Kolkata",22.5083,88.3519,"Traditional",4.9),
    ("Badamtala Ashar Sangha","South Kolkata",22.5114,88.3494,"Theme",4.9),
    ("66 Pally","South Kolkata",22.5139,88.3567,"Theme",4.8),
    ("Bosepukur Sitala Mandir","South Kolkata",22.5117,88.3668,"Theme",4.9),
    ("Bosepukur Talbagan","South Kolkata",22.5129,88.3685,"Theme",4.8),
    ("Jodhpur Park","South Kolkata",22.5053,88.3664,"Theme",4.7),
    ("Shiv Mandir Sarbojanin","South Kolkata",22.5038,88.3601,"Theme",4.6),
    ("Naktala Udayan Sangha","South Kolkata",22.4697,88.3713,"Theme",4.9),
    ("Ajeya Sanghati","South Kolkata",22.4651,88.3728,"Theme",4.8),
    ("Barisha Club","South Kolkata",22.4827,88.3095,"Theme",4.7),
    ("Behala Friends Club","South Kolkata",22.4923,88.3186,"Theme",4.8),
    ("Behala Notun Sangha","South Kolkata",22.4938,88.3209,"Theme",4.7),
    ("Sree Bhumi Sporting Club","North Kolkata",22.6024,88.3923,"Theme",5.0),


    # SALT LAKE / NEW TOWN
    ("AK Block Salt Lake","Salt Lake",22.5871,88.4069,"Theme",4.7),
    ("CK Block Salt Lake","Salt Lake",22.5894,88.4092,"Theme",4.6),
    ("Tank No 8 New Town","New Town",22.5815,88.4691,"Theme",4.8),
    ("NBCC Community","New Town",22.5759,88.4772,"Theme",4.7),

    # HOWRAH
    ("Ramkrishnapur Sarbojanin","Howrah",22.5937,88.3019,"Theme",4.8),
    ("Baksara Sarbojanin","Howrah",22.5708,88.2927,"Theme",4.7),
    ("Shibpur Sarbojanin","Howrah",22.5604,88.3073,"Theme",4.6),

    # SUBURBAN
    ("Baranagar Sarbojanin","Baranagar",22.6416,88.3734,"Theme",4.8),
    ("Dum Dum Park Tarun Sangha","Dum Dum",22.6139,88.4243,"Theme",4.9),
    ("Kestopur Prafulla Kanan","Kestopur",22.5957,88.4258,"Theme",4.7),
    ("Bidhannagar Sarbojanin","Bidhannagar",22.5801,88.4103,"Theme",4.6),
    ("Naihati Bandel Road","Naihati",22.9004,88.4192,"Traditional",4.7),
    # HOWRAH CITY
    ("Howrah Maidan Friends Club","Howrah",22.5869,88.3439,"Theme",4.8),
    ("Ghasbagan Sarbojanin","Howrah",22.5924,88.3447,"Theme",4.7),
    ("Salkia Friends Club","Howrah",22.6009,88.3425,"Theme",4.8),
    ("Salkia Sarbojanin","Howrah",22.6021,88.3412,"Traditional",4.7),
    ("Kadamtala Sarbojanin","Howrah",22.5953,88.3378,"Theme",4.6),

    # SHIBPUR
    ("Shibpur Tram Depot","Howrah",22.5609,88.3086,"Theme",4.8),
    ("Shibpur Buroshibtala","Howrah",22.5631,88.3064,"Traditional",4.9),
    ("Shibpur Dinobondhoo Club","Howrah",22.5627,88.3098,"Theme",4.7),
    ("Bakultala Sarbojanin","Howrah",22.5588,88.3045,"Theme",4.6),

    # BALLY
    ("Bally Sarbojanin","Howrah",22.6511,88.3402,"Traditional",4.9),
    ("Bally Ghoshpara","Howrah",22.6547,88.3371,"Theme",4.8),
    ("Bally Nischinda","Howrah",22.6429,88.3336,"Theme",4.7),
    ("Belur Pally","Howrah",22.6312,88.3538,"Theme",4.6),

    # BELUR
    ("Belur Math","Howrah",22.6321,88.3553,"Heritage",5.0),
    ("Belur Friends Club","Howrah",22.6289,88.3521,"Theme",4.8),
    ("Belur Sarbojanin","Howrah",22.6274,88.3506,"Traditional",4.7),

    # LILUAH
    ("Liluah Barowari","Howrah",22.6068,88.3267,"Traditional",4.8),
    ("Liluah Rail Colony","Howrah",22.6029,88.3289,"Theme",4.7),
    ("Liluah Young Boys","Howrah",22.6041,88.3298,"Theme",4.6),

    # BAKSARA
    ("Baksara Sarbojanin","Howrah",22.5708,88.2927,"Theme",4.8),
    ("Baksara Friends Union","Howrah",22.5689,88.2942,"Theme",4.7),

    # DOMJUR SIDE
    ("Domjur Jagadishpur","Howrah",22.6214,88.2209,"Theme",4.6),
    ("Domjur Santragachi","Howrah",22.6187,88.2351,"Theme",4.7),

    # SANTRAGACHI
    ("Santragachi Sarbojanin","Howrah",22.5911,88.2829,"Theme",4.8),
    ("Santragachi Friends Club","Howrah",22.5934,88.2847,"Theme",4.7),
    ("Santragachi Pratap Nagar","Howrah",22.5896,88.2818,"Theme",4.6),

    # ANDUL AREA
    ("Andul Sarbojanin","Andul",22.5849,88.2308,"Traditional",4.8),
    ("Andul Road Friends Club","Andul",22.5867,88.2335,"Theme",4.7),
    ("Andul Dakshinpara","Andul",22.5823,88.2289,"Theme",4.6),
    ("Andul Purba Pally","Andul",22.5881,88.2364,"Theme",4.7),
    ("Andul Paschim Pally","Andul",22.5852,88.2256,"Theme",4.6),

    # MAJHERPARA / DHULAGARH SIDE
    ("Andul Majherpara Sarbojanin","Andul",22.5794,88.2218,"Theme",4.8),
    ("Dhulgori Sarbojanin","Andul",22.5756,88.2189,"Traditional",4.7),
    ("Dhulgori Friends Club","Andul",22.5741,88.2207,"Theme",4.6),

    # NIMTALA / ANANDA NAGAR
    ("Andul Nimtala Sarbojanin","Andul",22.5902,88.2391,"Theme",4.7),
    ("Ananda Nagar Sarbojanin","Andul",22.5921,88.2416,"Traditional",4.8),

    # NEAR NH16
    ("Andul Station Road","Andul",22.5889,88.2342,"Theme",4.7),
    ("Andul Howrah Amta Road","Andul",22.5831,88.2274,"Theme",4.6),

    # JALAN COMPLEX SIDE
    ("Jalan Complex Sarbojanin","Andul",22.5874,88.2388,"Theme",4.8),
    ("Jalan Nagar Yubak Brinda","Andul",22.5896,88.2409,"Theme",4.7),

    # BIPRAPARA
    ("Andul Biprapara","Andul",22.5817,88.2236,"Traditional",4.6),
    
    # ULTADANGA / MANIKTALA
("Ultadanga Pallyshree","North Kolkata",22.5898,88.3921,"Theme",4.8),
("Maniktala Chaltabagan","North Kolkata",22.5882,88.3817,"Theme",4.9),
("Maniktala 29 Pally","North Kolkata",22.5905,88.3839,"Theme",4.8),

# SHYAMBAZAR / BAGHBAZAR SIDE
("Shyambazar Baghbazar","North Kolkata",22.6021,88.3716,"Traditional",4.7),
("Baghbazar Sarbojanin","North Kolkata",22.6031,88.3650,"Traditional",4.9),

# SEALDAH / BOWBAZAR
("Bowbazar Sarbojanin","Central Kolkata",22.5674,88.3653,"Theme",4.7),
("Subodh Mullick Square","Central Kolkata",22.5652,88.3726,"Theme",4.9),

# PARK CIRCUS / TANGRA
("Park Circus Sarbojanin","Central Kolkata",22.5459,88.3724,"Theme",4.8),
("Tangra Sarbojanin","Central Kolkata",22.5478,88.3894,"Theme",4.7),

# KASBA / GARIAHAT SIDE
("Kasba Bosepukur","South Kolkata",22.5178,88.3801,"Theme",4.9),
("Gariahat Sarbojanin","South Kolkata",22.5219,88.3649,"Theme",4.8),
("Golpark Sarbojanin","South Kolkata",22.5171,88.3657,"Theme",4.7),

# TOLLYGUNGE
("Tollygunge Agrani","South Kolkata",22.4978,88.3479,"Theme",4.9),
("Tollygunge Club","South Kolkata",22.4985,88.3458,"Heritage",4.8),

# BARUIPUR / SOUTH SUBURB
("Baruipur Sarbojanin","South Suburb",22.3569,88.4325,"Theme",4.7),
("Sonarpur Sarbojanin","South Suburb",22.4415,88.4241,"Theme",4.6),

# KHALI PALLY
("Khalipally Sarbojanin","South Suburb",22.3600,88.4249,"Theme",4.7),


# BAURIA / HOWRAH (Corrected Coordinates)

("Bauria Sarbojanin Durga Puja","Howrah",22.6058,88.2139,"Theme",4.6),
("Bauria Station Sarbojanin","Howrah",22.6074,88.2158,"Theme",4.5),
("Bauria Yuva Goshti Durga Puja","Howrah",22.6049,88.2126,"Theme",4.7),
("Bauria Kalibari Sarbojanin","Howrah",22.6037,88.2176,"Theme",4.6),
("Bauria Netaji Sangha","Howrah",22.6061,88.2119,"Theme",4.5),


# KHALI PALLY
("Khalipally Sarbojanin","Howrah",22.3600,88.4249,"Theme",4.7),
    ]
        

        for p in pandals:
            Pandal.objects.create(
                name=p[0],
                area=p[1],
                latitude=p[2],
                longitude=p[3],
                theme=p[4],
                rating=p[5]
            )

        self.stdout.write(self.style.SUCCESS("🔥 Real famous pandals loaded successfully!"))
