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
page = ['mirislom_m', 'user_name']
students = []

br.open("https://casapp.us.qwasar.io/login?service=https%3A%2F%2Fupskill.us.qwasar.io%2Fusers%2Fservice")
br.select_form(nr=0)
br.form['username'] = 'your_email'
br.form['password'] = 'your_qwasar_password'
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
                  'Season 01 Arc 01': '',
                  'Season 02 Fullstack': '',
                  'Season 01 Arc 02': '',
                  'Season 02 Software': '',
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
                        list = ['Preseason Web', 'Season 01 Arc 01', 'Season 02 Fullstack', 'Season 01 Arc 02',
                                'Season 02 Software Engineer', ]
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
# data.to_excel(f'student_{d1}.xlsx', index=False)
