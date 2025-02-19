import discord
from discord.ext import commands
import asyncio
import random
from io import BytesIO
import requests

intents = discord.Intents(
message_content = True,
messages = True,
reactions = True)

bot = commands.Bot(command_prefix='!', intents=intents)

quizzes= {

    'bangladesh2': [
        {'question': 'Name the district:', 'answer': 'Barguna', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/BD_Barguna_District_locator_map.svg/375px-BD_Barguna_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Barishal', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/BD_Barishal_District_locator_map.svg/375px-BD_Barishal_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Bhola', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/BD_Bhola_District_locator_map.svg/375px-BD_Bhola_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Jhalokati', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/BD_Jhalokati_District_locator_map.svg/375px-BD_Jhalokati_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Patuakhali', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/BD_Patuakhali_District_locator_map.svg/375px-BD_Patuakhali_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Pirojpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/BD_Pirojpur_District_locator_map.svg/375px-BD_Pirojpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Bandarban', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/BD_Bandarban_District_locator_map.svg/375px-BD_Bandarban_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Brahmanbaria', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/BD_Brahmanbaria_District_locator_map.svg/375px-BD_Brahmanbaria_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Chandpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/BD_Chandpur_District_locator_map.svg/375px-BD_Chandpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': ['Chattogram', 'Chittagong'], 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/BD_Chattogram_District_locator_map.svg/375px-BD_Chattogram_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': ['Cumilla', 'Comilla'], 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/BD_Cumilla_District_locator_map.svg/375px-BD_Cumilla_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Coxs Bazar', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/BD_Cox%27s_Bazar_District_locator_map.svg/375px-BD_Cox%27s_Bazar_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Feni', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/BD_Feni_District_locator_map.svg/375px-BD_Feni_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Khagrachari', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/BD_Khagrachari_District_locator_map.svg/375px-BD_Khagrachari_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Lakshmipur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/BD_Lakshmipur_District_locator_map.svg/375px-BD_Lakshmipur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Noakhali', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/BD_Noakhali_District_locator_map.svg/375px-BD_Noakhali_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Rangamati', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/BD_Rangamati_District_locator_map.svg/375px-BD_Rangamati_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Dhaka', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/BD_Dhaka_District_locator_map.svg/375px-BD_Dhaka_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Faridpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/BD_Faridpur_District_locator_map.svg/375px-BD_Faridpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Gazipur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/BD_Gazipur_District_locator_map.svg/375px-BD_Gazipur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Gopalganj', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/BD_Gopalganj_District_locator_map.svg/375px-BD_Gopalganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Kishoreganj', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/BD_Kishoreganj_District_locator_map.svg/375px-BD_Kishoreganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Madaripur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/BD_Madaripur_District_locator_map.svg/375px-BD_Madaripur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Manikganj', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/BD_Manikganj_District_locator_map.svg/375px-BD_Manikganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Munshiganj', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/BD_Munshiganj_District_locator_map.svg/375px-BD_Munshiganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Narayanganj', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/BD_Narayanganj_District_locator_map.svg/375px-BD_Narayanganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Narsingdi', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/BD_Narsingdi_District_locator_map.svg/375px-BD_Narsingdi_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Rajbari', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/BD_Rajbari_District_locator_map.svg/375px-BD_Rajbari_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Shariatpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/BD_Shariatpur_District_locator_map.svg/375px-BD_Shariatpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Tangail', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/BD_Tangail_District_locator_map.svg/375px-BD_Tangail_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Bagerhat', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/BD_Bagerhat_District_locator_map.svg/375px-BD_Bagerhat_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Chuadanga', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/BD_Chuadanga_District_locator_map.svg/375px-BD_Chuadanga_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': ['Jashore', 'Jessore'], 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/BD_Jashore_District_locator_map.svg/375px-BD_Jashore_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Jhenaidah', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/BD_Jhenaidah_District_locator_map.svg/375px-BD_Jhenaidah_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Khulna', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/BD_Khulna_District_locator_map.svg/375px-BD_Khulna_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Kushtia', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/BD_Kushtia_District_locator_map.svg/375px-BD_Kushtia_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Magura', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/BD_Magura_District_locator_map.svg/375px-BD_Magura_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Meherpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/BD_Meherpur_District_locator_map.svg/375px-BD_Meherpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Narail', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/BD_Narail_District_locator_map.svg/375px-BD_Narail_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Satkhira', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/BD_Satkhira_District_locator_map.svg/375px-BD_Satkhira_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Jamalpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/BD_Jamalpur_District_locator_map.svg/375px-BD_Jamalpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Mymensingh', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/BD_Mymensingh_District_locator_map.svg/375px-BD_Mymensingh_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Netrokona', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/BD_Netrokona_District_locator_map.svg/375px-BD_Netrokona_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Sherpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/BD_Sherpur_District_locator_map.svg/375px-BD_Sherpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Bogura', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/BD_Bogura_District_locator_map.svg/375px-BD_Bogura_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Joypurhat', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/BD_Joypurhat_District_locator_map.svg/375px-BD_Joypurhat_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Naogaon', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/BD_Naogaon_District_locator_map.svg/375px-BD_Naogaon_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Natore', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/BD_Natore_District_locator_map.svg/375px-BD_Natore_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': ['Chapai Nawabganj', 'Chapainawabganj'], 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/BD_Chapai_Nawabganj_District_locator_map.svg/375px-BD_Chapai_Nawabganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Pabna', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/BD_Pabna_District_locator_map.svg/375px-BD_Pabna_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Rajshahi', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/BD_Rajshahi_District_locator_map.svg/375px-BD_Rajshahi_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Sirajganj', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/BD_Sirajganj_District_locator_map.svg/375px-BD_Sirajganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Dinajpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/BD_Dinajpur_District_locator_map.svg/375px-BD_Dinajpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Gaibandha', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/BD_Gaibandha_District_locator_map.svg/375px-BD_Gaibandha_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Kurigram', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/BD_Kurigram_District_locator_map.svg/375px-BD_Kurigram_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Lalmonirhat', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/BD_Lalmonirhat_District_locator_map.svg/375px-BD_Lalmonirhat_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Nilphamari', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/BD_Nilphamari_District_locator_map.svg/375px-BD_Nilphamari_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Panchagarh', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/BD_Panchagarh_District_locator_map.svg/375px-BD_Panchagarh_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Rangpur', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/BD_Rangpur_District_locator_map.svg/375px-BD_Rangpur_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Thakurgaon', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/BD_Thakurgaon_District_locator_map.svg/375px-BD_Thakurgaon_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Habiganj', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/BD_Habiganj_District_locator_map.svg/375px-BD_Habiganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': ['Mouvibazar', 'Maulvibazar', 'Moulavibazar', 'Maulavibazar'], 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/BD_Moulvibazar_District_locator_map.svg/375px-BD_Moulvibazar_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Sunamganj', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/BD_Sunamganj_District_locator_map.svg/375px-BD_Sunamganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Sylhet', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/BD_Sylhet_District_locator_map.svg/375px-BD_Sylhet_District_locator_map.svg.png'}
    ],
    'bangladesh3': [
        {'question': 'Name the district:', 'answer': 'Natore', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/BD_Natore_District_locator_map.svg/375px-BD_Natore_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': ['Chapai Nawabganj', 'Chapainawabganj'], 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/BD_Chapai_Nawabganj_District_locator_map.svg/375px-BD_Chapai_Nawabganj_District_locator_map.svg.png'},
        {'question': 'Name the district:', 'answer': 'Pabna', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/BD_Pabna_District_locator_map.svg/375px-BD_Pabna_District_locator_map.svg.png'}
    ],
    'zaplates': [
        {"question": 'In which province was this plate issued?', 'answer': 'Western Cape', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/western-cape.png'},
        {'question': 'In which province was this plate issued?', 'answer': 'Kwazulu-Natal', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/kwazulu-natal.png'},
        {'question': 'In which province was this plate issued?', 'answer': 'Mpumalanga', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/mpumalanga.png'},
        {'question': 'In which province was this plate issued?', 'answer': 'Eastern Cape', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/eastern-cape.png'},
        {'question': 'In which province was this plate issued?', 'answer': 'Limpopo', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/limpopo.png'},
        {'question': 'In which province was this plate issued?', 'answer': 'Gauteng', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/gauteng.png'},
        {'question': 'In which province was this plate issued?', 'answer': 'Northern Cape', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/northern-cape.png'},
        {'question': 'In which province was this plate issued?', 'answer': 'Free State', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/free-state.png'},
        {'question': 'In which province was this plate issued?', 'answer': 'North West', 'image_url': 'https://raw.githubusercontent.com/bagaboiebailey/zaplates/main/north-west.png'}
    ],
    "esflags": [
        {"question": "Guess the autonomous community", "answer": ["Aragon", "Aragón"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_Aragon.svg.png"},
        {"question": "Guess the autonomous community", "answer": "Cantabria", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_Cantabria_(Official).svg.png"},
        {"question": "Guess the autonomous community", "answer": ["Castile-La Mancha", "Castilla-La Mancha"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_Castile-La_Mancha.svg.png"},
        {"question": "Guess the autonomous community", "answer": ["Castile and León", "Castile and Leon", "Castilla y Leon", "Castilla y León"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_Castile_and_Leon.svg.png"},
        {"question": "Guess the autonomous community", "answer": "Ceuta", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_Ceuta.svg.png"},
        {"question": "Guess the autonomous community", "answer": "La Rioja", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_La_Rioja_(with_coat_of_arms).svg.png"},
        {"question": "Guess the autonomous community", "answer": "Melilla", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_Melilla.svg.png"},
        {"question": "Guess the autonomous community", "answer": ["Navarre", "Navarra"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_Navarre.svg.png"},
        {"question": "Guess the autonomous community", "answer": ["Balearic Islands", "Illes Balears", "Islas Baleares"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_the_Balearic_Islands.svg.png"},
        {"question": "Guess the autonomous community", "answer": ["Basque Country", "Euskadi", "Pais Vasco", "País Vasco"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_the_Basque_Country.svg.png"},
        {"question": "Guess the autonomous community", "answer": ["Canary Islands", "Canarias", "Canaries"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_the_Canary_Islands.svg.png"},
        {"question": "Guess the autonomous community", "answer": "Madrid", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Flag_of_the_Community_of_Madrid.svg.png"},
        {"question": "Guess the autonomous community", "answer": "Valencia", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/Valencia.png"},
        {"question": "Guess the autonomous community", "answer": ["Andalucia", "Andalucía", "Andalusia"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/andalucia.png"},
        {"question": "Guess the autonomous community", "answer": "Asturias", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/asturias.png"},
        {"question": "Guess the autonomous community", "answer": ["Catalonia", "Catalunya", "Cataluna", "Cataluña"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/catalonia.png"},
        {"question": "Guess the autonomous community", "answer": "Extremadura", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/extremadura.png"},
        {"question": "Guess the autonomous community", "answer": "Galicia", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/galicia.png"},
        {"question": "Guess the autonomous community", "answer": "Murcia", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/esflags/main/murcia.png"}
    ], 
    "ph2": [
        {"question": "Guess the region", "answer": ["Metro Manila", "National Capital Region"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/lw0z1so9.png"},
        {"question": "Guess the region", "answer": "Cordillera", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/s6azhcu3.png"},
        {"question": "Guess the region", "answer": "Ilocos", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/4hhb9ysf.png"},
        {"question": "Guess the region", "answer": "Cagayan Valley", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/1gbbctuc.png"},
        {"question": "Guess the region", "answer": "Central Luzon", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/sv9t9gkl.png"},
        {"question": "Guess the region", "answer": "Calabarzon", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/38wsfh7e.png"},
        {"question": "Guess the region", "answer": "Mimaropa", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/u272l05y.png"},
        {"question": "Guess the region", "answer": "Bicol", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/mjm5t4nb.png"},
        {"question": "Guess the region", "answer": "Western Visayas", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/h1yllk4r.png"},
        {"question": "Guess the region", "answer": "Negros Island", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/202fucfb.png"},
        {"question": "Guess the region", "answer": "Central Visayas", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/bgzw0g39.png"},
        {"question": "Guess the region", "answer": "Eastern Visayas", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/oulw4x92.png"},
        {"question": "Guess the region", "answer": "Zamboanga Peninsula", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/mxygl9xc.png"},
        {"question": "Guess the region", "answer": "Northern Mindanao", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/ulalmu6u.png"},
        {"question": "Guess the region", "answer": "Davao", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/4qyoyf01.png"},
        {"question": "Guess the region", "answer": "Soccsksargen", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/yeedamnz.png"},
        {"question": "Guess the region", "answer": "Caraga", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/xi3jjqwz.png"},
        {"question": "Guess the region", "answer": ["Bangsamoro", "Autonomous Region in Muslim Mindanao"], "image_url": "https://raw.githubusercontent.com/bagaboiebailey/ph2/main/ukcpkcgz.png"}
    ],
    "argflags": [
        {"question": "Guess the province", "answer": "Buenos Aires", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/vQCxP30nv2.svg.png"},
        {"question": "Guess the province", "answer": "Catamarca", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/TyXVjiRl6q.svg.png"},
        {"question": "Guess the province", "answer": "Chaco", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/ZqE2bcmocY.svg.png"},
        {"question": "Guess the province", "answer": "Chubut", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/7CmNav1X8w.svg.png"},
        {"question": "Guess the province", "answer": "Cordoba", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/6tsuipoBoh.svg.png"},
        {"question": "Guess the province", "answer": "Corrientes", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/6T85v6ZdPo.svg.png"},
        {"question": "Guess the province", "answer": "Entre Rios", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/N6fplszGc7.svg.png"},
        {"question": "Guess the province", "answer": "Formosa", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/aE9JeCF0iQ.svg.png"},
        {"question": "Guess the province", "answer": "Jujuy", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/wOeiKiNLBm.svg.png"},
        {"question": "Guess the province", "answer": "La Pampa", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/w7q5O0txJy.svg.png"},
        {"question": "Guess the province", "answer": "La Rioja", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/PsZmuO7eG4.svg.png"},
        {"question": "Guess the province", "answer": "Mendoza", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/8vkJoNlPjq.svg.png"},
        {"question": "Guess the province", "answer": "Misiones", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/etrwtSeZMn.svg.png"},
        {"question": "Guess the province", "answer": "Neuquen", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/XJPkZlERRe.svg.png"},
        {"question": "Guess the province", "answer": "Rio Negro", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/FmLep9neSz.svg.png"},
        {"question": "Guess the province", "answer": "Salta", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/gMgHfJmWN1.svg.png"},
        {"question": "Guess the province", "answer": "San Juan", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/5ZY7OsX9WO.svg.png"},
        {"question": "Guess the province", "answer": "San Luis", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/XhGl2qktf6.svg.png"},
        {"question": "Guess the province", "answer": "Santa Cruz", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/pH5CHzi0UG.svg.png"},
        {"question": "Guess the province", "answer": "Santa Fe", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/VjKIZJ1GU2.svg.png"},
        {"question": "Guess the province", "answer": "Santiago del Estero", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/OMJ0C0lOId.svg.png"},
        {"question": "Guess the province", "answer": "Tierra del Fuego", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/81tFiq42jz.svg.png"},
        {"question": "Guess the province", "answer": "Tucuman", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/argflags/main/3cOG5X4Bhj.svg.png"}
    ],
    "subvocab": [
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Albanian name for Albanian first-level subdivisions?", "answer": ["qarqe", "qarqet"]},
        {"question": "[FLS] What is the local Spanish name for Argentinian first-level subdivisions?", "answer": ["provincia", "provincias"]},
        {"question": "[FLS] What is the local English name for Australian first-level subdivisions?", "answer": ["state", "states"]},
        {"question": "[FLS] What is the local German name for Austrian first-level subdivisions?", "answer": ["Land", "Länder", "Bundesland", "Bundesländer"]},
        {"question": "[FLS] What is the local Bengali name for Bangladeshi first-level subdivisions (Latin transcription)?", "answer": "bibhag"},
        {"question": "[FLS] What is the local Belarusian name for Belarusian first-level subdivisions (Latin transcription)?", "answer": ["oblasts", "oblasti"]},
        {"question": "[FLS] What is the local Dutch name for Belgian first-level subdivisions?", "answer": "gewest"},
        {"question": "[FLS] What is the local Dutch name for (Kingdom of the) Netherlands first-level subdivisions?", "answer": "landen"},
        {"question": "[FLS] What is the local Bhutanese name for Bhutan first-level subdivisions (Latin transcription)?", "answer": ["dzongkhag", "dzongkhags"]},
        {"question": "[FLS] What is the local Spanish name for Bolivian first-level subdivisions?", "answer": ["departamento", "departamentos"]},
        {"question": "[FLS] What is the local English name for Botswana first-level subdivisions?", "answer": ["district", "districts"]},
        {"question": "[FLS] What is the local Portuguese name for Brazilian first-level subdivisions?", "answer": ["estado", "estados"]},
        {"question": "[FLS] What is the local Bulgarian name for Bulgarian first-level subdivisions (Latin transcription)?", "answer": ["oblast", "oblasti"]},
        {"question": "[FLS] What is the local Khmer name for Cambodian first-level subdivisions (Latin transcription)?", "answer": ["khett", "khaet", "khet"]},
        {"question": "[FLS] What is the local English name for Canadian first-level subdivisions?", "answer": ["province", "provinces"]},
        {"question": "[FLS] What is the local German name for Switzerland first-level subdivisions?", "answer": ["Kanton", "Kantone"]},
        {"question": "[FLS] What is the local Spanish name for Chilean first-level subdivisions?", "answer": ["región", "regiones"]},
        {"question": "[FLS] What is the local Mandarin name for Chinese first-level subdivisions (Latin transcription)?", "answer": "sheng"},
        {"question": "[FLS] What is the local Spanish name for Colombian first-level subdivisions?", "answer": ["departamento", "departamentos"]},
        {"question": "[FLS] What is the local Czech name for Czechia first-level subdivisions?", "answer": ["kraj", "kraje"]},
        {"question": "[FLS] What is the local German name for German first-level subdivisions?", "answer": ["Land", "Länder", "Bundesland", "Bundesländer"]},
        {"question": "[FLS] What is the local Danish name for Denmark first-level subdivisions?", "answer": "regioner"},
        {"question": "[FLS] What is the local Spanish name for Dominican Republic first-level subdivisions?", "answer": ["provincia", "provincias"]},
        {"question": "[FLS] What is the local Spanish name for Ecuadorian first-level subdivisions?", "answer": ["provincia", "provincias"]},
        {"question": "[FLS] What is the local Spanish name for Spain first-level subdivisions?", "answer": ["comunidad autónoma", "comunidades autónomas"]},
        {"question": "[FLS] What is the local Estonian name for Estonia first-level subdivisions?", "answer": "maakond"},
        {"question": "[FLS] What is the local English name for Eswatini first-level subdivisions?", "answer": ["region", "regions"]},
        {"question": "[FLS] What is the local Finnish name for Finland first-level subdivisions?", "answer": "maakunta"},
        {"question": "[FLS] What is the local French name for French first-level subdivisions?", "answer": ["région", "régions"]},
        {"question": "[FLS] What is the local English name for Ghana first-level subdivisions?", "answer": ["region", "regions"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},
        {"question": "[FLS] What is the local Catalan name for Andorran first-level subdivisions?", "answer": ["parròquia", "parròquies"]},

        {"question": "[SLS] What is the local French name for French second-level subdivisions?", "answer": ["département", "départements"]},
        {"question": "[SLS] What is the local Spanish name for Spain second-level subdivisions?", "answer": ["provincia", "provincias"]},
        {"question": "[SLS] What is the local Dutch name for Belgian second-level subdivisions?", "answer": ["provincie", "provincies"]},
        {"question": "[SLS] What is the local German name for German second-level subdivisions?", "answer": ["Landkreis", "Kreis"]},
        {"question": "[SLS] What is the local German name for Austrian second-level subdivisions?", "answer": ["Bezirk", "Bezirke"]},
        {"question": "[SLS] What is the local Dutch name for (Kingdom of the) Netherlands second-level subdivisions (under 'the Netherlands' specifically)?", "answer": ["provincie", "provincies"]},
    ],
    "sg2": [
        {"question": "Name the planning area:", "answer": "Ang Mo Kio", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1kpqof0tb.png"},
        {"question": "Name the planning area:", "answer": "Bedok", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1ekpqof0tb.png"},
        {"question": "Name the planning area:", "answer": "Bishan", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1mmojhjft4.png"},
        {"question": "Name the planning area:", "answer": "Boon Lay", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1c867vdl28.png"},
        {"question": "Name the planning area:", "answer": "Bukit Batok", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1nbwi1kknx.png"},
        {"question": "Name the planning area:", "answer": "Bukit Merah", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1kdst2eczi.png"},
        {"question": "Name the planning area:", "answer": "Bukit Panjang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1xj145yp2y.png"},
        {"question": "Name the planning area:", "answer": "Bukit Timah", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1opikeawqd.png"},
        {"question": "Name the planning area:", "answer": "Central Area", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/16h5cvebkh.png"},
        {"question": "Name the planning area:", "answer": "Central Water Catchment", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1vvemjpi7g.png"},
        {"question": "Name the planning area:", "answer": "Changi Bay", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1i6re9rygtu.png"},
        {"question": "Name the planning area:", "answer": "Changi", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/188dpdf8fkr.png"},
        {"question": "Name the planning area:", "answer": "Choa Chu Kang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1uouddagxqa.png"},
        {"question": "Name the planning area:", "answer": "Clementi", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1li4pj8g9j.png"},
        {"question": "Name the planning area:", "answer": "Geylang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/14mhmfroi.png"},
        {"question": "Name the planning area:", "answer": "Hougang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/14i394y7l.png"},
        {"question": "Name the planning area:", "answer": "Jurong East", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/13oycnes6.png"},
        {"question": "Name the planning area:", "answer": "Jurong West", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/13hxj4esb.png"},
        {"question": "Name the planning area:", "answer": "Kallang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1qx4f3mh1.png"},
        {"question": "Name the planning area:", "answer": "Lim Chu Kang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1pq9c6bi3.png"},
        {"question": "Name the planning area:", "answer": "Mandai", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1f90b6ae6.png"},
        {"question": "Name the planning area:", "answer": "Marine Parade", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1evp3at15.png"},
        {"question": "Name the planning area:", "answer": "North-Eastern Islands", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1runltqw6.png"},
        {"question": "Name the planning area:", "answer": "Novena", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1xtsg8j0u.png"},
        {"question": "Name the planning area:", "answer": "Pasir Ris", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1kj2rjf4c.png"},
        {"question": "Name the planning area:", "answer": "Paya Lebar", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/10rtmw3ne.png"},
        {"question": "Name the planning area:", "answer": "Pioneer", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/161yhtsoa8.png"},
        {"question": "Name the planning area:", "answer": "Punggol", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/18n4wc9cx8.png"},
        {"question": "Name the planning area:", "answer": "Queenstown", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1frryoobq.png"},
        {"question": "Name the planning area:", "answer": "Seletar", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1qvsxyw62b.png"},
        {"question": "Name the planning area:", "answer": "Sembawang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1yvi9aaqkt.png"},
        {"question": "Name the planning area:", "answer": "Sengkang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/181jpm4ubv.png"},
        {"question": "Name the planning area:", "answer": "Serangoon", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/16tv803zc2.png"},
        {"question": "Name the planning area:", "answer": "Simpang", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1lja9dy2p2.png"},
        {"question": "Name the planning area:", "answer": "Southern Islands", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/107j98av60.png"},
        {"question": "Name the planning area:", "answer": "Sungei Kadut", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/112duq7f7z.png"},
        {"question": "Name the planning area:", "answer": "Tanglin", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1pugw28iqe.png"},
        {"question": "Name the planning area:", "answer": "Tengah", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1qldu93bxl.png"},
        {"question": "Name the planning area:", "answer": "Toa Payoh", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1gw83uuren.png"},
        {"question": "Name the planning area:", "answer": "Tuas", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1noro4l5b5.png"},
        {"question": "Name the planning area:", "answer": "Western Water Catchment", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1anohljuob.png"},
        {"question": "Name the planning area:", "answer": "Western Islands", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1z3gk4qdtw.png"},
        {"question": "Name the planning area:", "answer": "Woodlands", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1b0z9riaxp.png"},
        {"question": "Name the planning area:", "answer": "Yishun", "image_url": "https://raw.githubusercontent.com/bagaboiebailey/sg2/main/1bc2defgh.png"}
    ]
}

quiz_active = False
current_quiz = None
current_question = None
current_correct_answer = None
questions_to_ask = 1
correct_answers = 0

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='quiz', aliases=['q'])
async def start_quiz(ctx, quiz_name: str, num_questions: int = 1):
    global quiz_active, current_quiz, current_question, current_correct_answer, questions_to_ask, correct_answers
    
    if quiz_name.lower() in quizzes:
        current_quiz = quiz_name.lower()
        quiz_active = True
        questions_to_ask = min(max(1, num_questions), len(quizzes[current_quiz]))

        questions = quizzes[current_quiz]
        random.shuffle(questions)

        correct_answers = 0

        for question_info in questions[:questions_to_ask]:
            if not quiz_active:
                break

            current_question_info = question_info
            current_question = current_question_info['question']
            current_correct_answer = current_question_info['answer']
            image_url = current_question_info['image_url']

            image_bytes = BytesIO(requests.get(image_url).content)

            current_question_info = await ctx.send(f'{current_question}', file=discord.File(image_bytes, filename='image.png'))

            def check_answer(message):
                return message.author == ctx.author and message.channel == ctx.channel

            try:
                answer_message = await bot.wait_for('message', check=check_answer, timeout=15.0)
                user_answer = answer_message.content.lower()
     
                if isinstance(current_correct_answer, list):
                    if user_answer in map(str.lower, current_correct_answer):
                        await answer_message.add_reaction('\U00002705') 
                        await ctx.send(f'Correct!')
                        correct_answers += 1
                    else:
                        await answer_message.add_reaction('\U0000274C') 
                        await ctx.send(f'Incorrect. The correct answer is: {current_correct_answer}.')   
                else:
                    if user_answer == current_correct_answer.lower():
                        await answer_message.add_reaction('\U00002705')
                        await ctx.send(f'Correct!')
                        correct_answers += 1
                    else:
                        await answer_message.add_reaction('\U0000274C')
                        await ctx.send(f'Incorrect. The correct answer is: {current_correct_answer}.')    
            except asyncio.TimeoutError:
                await ctx.send(f"Time's up! The correct answer is: {current_correct_answer}.")

        await ctx.send(f'Quiz finished. You got {correct_answers}/{questions_to_ask} correct answers.')
        quiz_active = False
        current_quiz = None
        current_question = None
        current_correct_answer = None
    else:
        await ctx.send(f'There is no quiz by that name.')

@bot.command(name='skip')
async def skip_question(ctx):
    await ctx.send(f"Question skipped. The correct answer is: {current_correct_answer}.")

@bot.command(name='end')
async def end_quiz(ctx):
    global quiz_active
    await ctx.send(f"Quiz ended. You got {correct_answers}/{questions_to_ask} correct answers.")
    quiz_active = False

bot.run('')