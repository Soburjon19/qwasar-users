import mechanize
import json

from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib
import pandas as pd

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
from datetime import date, datetime, timedelta

today = date.today()
today_2 = datetime.now()
d1 = today.strftime("%d_%m_%Y")
d2 = today_2.strftime('%B %d, %Y %I:%M%p')
d2_f = datetime.strptime(d2, '%B %d, %Y %I:%M%p')
# print(d2_f)
page = ['daminov_s',
'isroilov_a',
'iraliyev_m',
'pardaboy_m',
'xujamura_d',
'shuhrato_m',
'asilxono_m',
'erkinov_s',
'samiyev_s',
'husanova_s',
'gasirov_y',
'odilov_a',
'atoyev_u',
'berkinov_a',
'safarov_s',
'to-lqino_a',
'bobonaza_s',
'muzaparo_a',
'xaydaral_n',
'mirg-ani_e',
'nosirov_n',
'xikmatxo_u',
'abdulla_su',
'rahmonov_a',
'ergashov_i',
'jumayev_u',
'rabbimqu_y',
'hikmatxo_s',
'toxirov_a',
'g-ulomjo_s',
'otabekov_s',
'komilov_t',
'nusratul_a',
'xaydarov_p',
'rahimov_i',
'ziyadull_u',
'aliyev_f',
'sattorov_s',
'turmatov_g',
'mirzafar_a',
'qodirov_o',
'qodirov_d',
'jo-rayev_j',
'mamirov_s',
'abdurahm_o',
'ro-zimur_d',
'tayjonov_g',
'nurtursu_m',
'tog-ayev_x',
'parpiev_s',
'matupaye_i',
'jo-rabek_a',
'xayitmat_a',
'muxammad_b',
'normato_az',
'insavali_i',
'abdullay_s',
'xalilov-_x',
'ismoilov_e',
'serikbay_b',
'razzoqov_j',
'azimov_s',
'rixsiboy_i',
'ashimov_n',
'toshtemi_m',
'turdiev_a',
'zayniddi_f',
'baratov_h',
'toychibo_a',
'qochqoro_m',
'utamurod_d',
'nazirov-_h',
'xakimov_m',
'mirzaboy_l',
'husanov_y',
'athamov_a',
'mamarakh_i',
'karimov_a',
'aralov_j',
'tangirov_d',
'xakimov_r',
'abdukamo_m',
'shermato_e',
'qaxxorov_m',
'qurbanal_r',
'ruzmetov_a',
'eranbaye_e',
'rabbimov_j',
'hayrulla_b',
'oblaqulo_l',
'aralbaev_d',
'ilesov_n',
'shonugmo_s',
'ergashe_az',
'mirhojiy_m',
'turg-uno_n',
'mehmonal_k',
'riskidin_s',
'ashirova_z',
'nomonjon_z',
'esenbaye_m',
'tlapbaye_i',
'umaraliy_s',
'abdjabar_s',
'mamatqul_a',
'mirzoahm_s',
'olimxoja_s',
'akramov_i',
'yusupov_j',
'dilmurod_b',
'aminjono_q',
'marufov_a',
'rasulov_d',
'rahmonjo_d',
'muidinov_a',
'ortiqboy_a',
'azimbaye_m',
'yo-ldosh_o',
'yuldashe_s',
'kamolidd_s',
'jalolid_xo',
'norxojay_o',
'panjiyev_s',
'abduhaki_b',
'nishanal_o',
'risaliev_e',
'oribjono_a',
'muhammad_i',
'baxriddi_h',
'umarbaye_x',
'tuychibo_a',
'abdullay_b',
'kambarov_a',
'abdugaff_f',
'rashidov_j',
'tolipov_s',
'qosimov_ab',
'yo-ldosh_m',
'nusratov_b',
'yusupov_me',
'abdusam_ab',
'valijano_a',
'anvaro_abd',
'usmanov_a',
'ergasho_ab',
'murodov_a',
'karshibo_a',
'anvarov_ak',
'mirzali_ak',
'negmurod_a',
'ni_an',
'murodal_as',
'ergashe_as',
'komiljon_a',
'safarali_a',
'mambetov_a',
'abdurax_az',
'mirmaxam_a',
'to-lqino_a-a38',
'rasulov_az',
'darxanov_b',
'boymatov_b',
'maxalbay_b',
'ibrohimo_b',
'nematov_d',
'aqlitdin_d',
'jabborov_i',
'dalimov_d',
'valiboye_d',
'abdusaid_d',
'anorboye_d',
'zoirov_f',
'eshmurod_f',
'halilov_ab',
'payzulla_h',
'murotov_j',
'bakberga_k',
'muratali_m',
'rustamo_ma',
'teshabay_m',
'fuzayliy_m',
'pirmaham_m',
'abdulaye_l',
'narzulla_m',
'tursinov_m',
'ma-rupov_m',
'qaxxor_mur',
'nosirov_m',
'mamasidi_m',
'maxkamxo_m',
'gulmurod_n',
'ismadiya_o',
'mirisman_o',
'xoshimbo_o',
'abdullay_o',
'shodiboy_o',
'burxonov_r',
'g-anixon_r',
'ruslan_k',
'pulatov_s',
'jabbaral_s',
'baxodiro_s',
'gofurov_s',
'egamberd_s',
'abdushuk_s',
'yegafaro_t',
'abdusatt_u',
'urdabaye_u',
'tursunbo_x',
'xaliljon_x',
'o-tkirov_y',
'ko-shkar_y',
'mamaniya_j',
'abdurash_z'
]
students = []

br.open("https://casapp.us.qwasar.io/login?service=https%3A%2F%2Fupskill.us.qwasar.io%2Fusers%2Fservice")
br.select_form(nr=0)
br.form['username'] = 'soburjon19@icloud.com'
br.form['password'] = 'Sobur2002'
br.submit()

for i in page:
    try:
        br.open(f"https://upskill.us.qwasar.io/users/{i}")
        soup = bs(br.response().read(), 'html.parser')

        student_name = [i.text.strip() for i in soup.find_all("h1", {"class": 'text-c-yellow'})][0]
        student_qpoints = soup.find("div", id= "user_qpoints").text.strip()
        # print(student_qpoints)
        student_nik = i
        prog2 = soup.find_all("time", {"data-local": "time-ago"})
        # print(prog2)
        last_login = prog2[0].text
        last_login_f = datetime.strptime(last_login, '%B %d, %Y %I:%M%p')
        last_login_f = last_login_f + timedelta(hours=5)
        # out_time = datetime.strftime(last_login_f, "%Y-%m-%d %H:%M")
        diference = (d2_f - last_login_f)
        min = diference.seconds / 60
        hour = diference.seconds / 3600

        since_last_login = ''
        if diference.days == 0:
            if min < 60:
                if round(min) == 1:
                    since_last_login += f'{round(min)} minute ago'

                else:
                    since_last_login += f'{round(min)} minutes ago'
            else:
                if round(hour) == 1:
                    since_last_login += f'{round(hour)} hour ago'
                else:
                    since_last_login += f'{round(hour)} hours ago'
        else:
            if diference.days == 1:
                since_last_login += f'{diference.days} day ago'
            else:
                since_last_login += f'{diference.days} days ago'

        # print(since_last_login)
        # out_time = datetime.strftime(diference, "%Y-%m-%d %H:%M")
        # print(out_time)
        # print(type(out_time))

        s_data = {'nik': student_nik,
                  'name and lastname': student_name,
                  'qpoints': '',
                  'Preseason Web': '',
                  # 'Preseason Data': '',
                  'Season 01 Arc 01': '',
                  'Season 02 Fullstack': '',
                  'Season 03 Frontend': '',
                  'Season 03 Backend': '',
                  'Season 03 Fullstack Java': '',
                  'Season 03 Cloud Engineer': '',
                  # 'Season 02 Data Science': '',
                  # 'Season 03 Machine Learning': '',
                  # 'Season 01 Arc 02': '',
                  # 'Season 02 Software': '',
                  # 'Season 03 CPP': '',
                  # 'Season 03 Rust': '',
                  'Last Login': '',
                  'Days since login': ''}

        student_progresses = soup.find_all("div", {"class": 'row p-t-10 align-items-center'})
        labels = soup.find_all("label", {"class": "label bg-c-blue"})

        for student_progress in student_progresses:
            current_progress = student_progress.text.strip().split("\n")[0]
            prog = student_progress.find_all("div", {"class": "progress b-radius-1"})

            for t in prog:
                try:
                    if t['title']:
                        s_data['Last Login'] = str(last_login_f)
                        s_data['Days since login'] = since_last_login
                        s_data['qpoints'] = student_qpoints
                        list = ['Preseason Web', 'Season 03 Fullstack Java', 'Season 01 Arc 01',
                                'Season 02 Fullstack', 'Season 03 Frontend', 'Season 03 Backend', 'Season 03 Cloud Engineer']
                        if current_progress in list:
                            if current_progress == 'Season 02 Software Engineer':
                                s_data['Season 02 Software'] = t['title']
                            elif current_progress == 'Season 03 Software Engineer CPP':
                                s_data['Season 03 CPP'] = t['title']
                            elif current_progress == 'Season 03 Software Engineer Rust':
                                s_data['Season 03 Rust'] = t['title']
                            else:
                                s_data[current_progress] = t['title']





                except:
                    pass

        students.append(s_data)

    except:
        print(i)

json_list = json.dumps(students)

data = pd.read_json(json_list)

data.to_csv(f'student_{d1}.csv', index=False)
